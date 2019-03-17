import os
import re
import sys


def read_pango_file(pango_git_dir: str, file: str) -> str:
    filename = os.path.join(pango_git_dir, 'pango', file)
    return open(filename, encoding='utf-8').read()


def remove_hard_to_regex_phrases(source: str) -> str:
    # This phrase appears in pango-direction.h and messes up our regex later on.
    # We avoid this simply by removing the slash in the text.
    source = re.sub('and/or', 'and-or', source)

    # This phrase appears in pango-types.h and messes up our regex later on.
    # We avoid this simply by removing the slash in the text.
    source = re.sub('ascent/descent/lbearing/rbearing', 'a-d-lb-rb', source)

    # This phrase appears in pango-types.h and messes up our regex later on.
    # We avoid this simply by removing the slash in the text.
    source = re.sub(r'<firstterm>.*</firstterm>', '', source)

    # This phrase appears in pango-types.h and messes up our regex later on.
    # We avoid this simply by removing the slash in the text.
    source = re.sub('pango/pango-', 'pango-pango-', source)

    return source


def extract_typedefs_opaque(source: str) -> str:
    typedefs_unknown = ''
    matches = re.finditer(r'typedef \.\.\. [^;]*;\n', source, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        typedefs_unknown += match.group()
    return typedefs_unknown


def extract_typedefs_enum(source: str) -> str:
    typedefs_enum = ''
    matches = re.finditer(r'typedef enum [^;]*;\n', source, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        typedefs_enum += match.group()
    return typedefs_enum


def extract_typedefs_other(source: str) -> str:
    typedefs_other = ''
    matches = re.finditer(r'typedef (?!enum)[A-Za-z0-9]* [^;]*;\n', source, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        typedefs_other += match.group()
    return typedefs_other


def replace_compiler_computed_values(source: str) -> str:
    # Some header files contain values are meant to be computed by the compiler.
    for i in range(0, 8):
        source = re.sub('1 << %d' % i, str(1 << i), source)
    return source


def remove_typedefs(source: str) -> str:
    return re.sub(r'typedef (\.\.\.|enum|[A-Za-z0-9]*) [^;]*;\n', '', source)


def remove_private_structs_and_typedefs(source: str) -> str:
    source = re.sub(
        r'typedef struct _Pango([A-Za-z0-9_]*) ',
        'typedef ... ',
        source
    )
    source = re.sub(
        r'struct _Pango([A-Za-z0-9_]*)\s*{[^}]*};',
        '\n',
        source
    )
    return source


def remove_availability_flags(source: str) -> str:
    patterns = [
        r'PANGO_AVAILABLE_IN_(ALL|[0-9_]*)\n',
        r'PANGO_DEPRECATED\n',
        r'PANGO_DEPRECATED_IN_[0-9_]*\n',
        r'PANGO_DEPRECATED_FOR\(g_unichar_get_mirror_char\)\n',
    ]
    for pattern in patterns:
        source = re.sub(pattern, '', source)
    return source


def remove_glib_compiler_flags(source: str) -> str:
    return re.sub(r'(G_GNUC_CONST|G_GNUC_PURE)', '', source)


def remove_multiple_blank_lines(text: str) -> str:
    return re.sub(r'^(?:[\t ]*(?:\r?\n|\r))+', '', text, 0, re.MULTILINE)


def remove_multiple_spaces(text: str) -> str:
    return re.sub(r'[\t ]{2,}', ' ', text, 0, re.MULTILINE)


def get_struct_for_opaque_typedef(
        opaque_typedef_name: str,
        pango_git_dir: str,
        header_file: str,
        private_struct_name: str
) -> str:
    header_source = read_pango_file(pango_git_dir, header_file)
    regex = r"struct %s\s*{[^}]*};" % private_struct_name
    matches = re.search(regex, header_source)
    private_struct_definition = matches.group()
    public_struct_definition = re.sub(r"%s" % private_struct_name, '', private_struct_definition)
    public_struct_definition = re.sub(r"struct ", 'typedef struct', public_struct_definition)
    public_struct_definition = re.sub(r"};", '} %s;' % opaque_typedef_name, public_struct_definition)

    return public_struct_definition + '\n'


def remove_opaque_typedef(cdefs: str, opaque_typedef_name: str):
    return re.sub(r"typedef \.\.\. %s;" % opaque_typedef_name, '', cdefs)


def read_pango_header(pango_git_dir, header_file):
    source = read_pango_file(pango_git_dir, header_file)

    source = remove_hard_to_regex_phrases(source)
    source = replace_compiler_computed_values(source)

    # This phrase appears in pango-layout.h and CFFI complains. I honestly have
    # not clue why. Making the type "unknown" resolves this.
    source = re.sub(
        'typedef PangoGlyphItem PangoLayoutRun;',
        'typedef ... PangoLayoutRun;',
        source
    )

    source = re.sub(
        '/\\*.*?\\*/'
        '|G_(BEGIN|END)_DECLS'
        '|pango_public '
        r'|^\s*#.*?[^\\]\n',
        '',
        source,
        flags=re.DOTALL | re.MULTILINE)

    source = remove_private_structs_and_typedefs(source)
    source = remove_availability_flags(source)
    source = remove_glib_compiler_flags(source)

    typedefs_opaque = extract_typedefs_opaque(source)
    typedefs_enum = extract_typedefs_enum(source)
    typedefs_other = extract_typedefs_other(source)

    source = remove_typedefs(source)

    return source, typedefs_opaque, typedefs_enum, typedefs_other


def generate(pango_git_dir):
    # Remove comments, preprocessor instructions and macros.
    header_files = [
        'pango-attributes.h',
        'pango-bidi-type.h',
        'pango-break.h',
        'pango-context.h',
        'pango-coverage.h',
        'pango-direction.h',
        'pango-engine.h',
        'pango-font.h',
        'pango-fontmap.h',
        'pango-fontset.h',
        'pango-glyph.h',
        'pango-glyph-item.h',
        'pango-gravity.h',
        'pango-item.h',
        'pango-layout.h',
        'pango-language.h',
        'pango-matrix.h',
        'pango-renderer.h',
        'pango-script.h',
        'pango-tabs.h',
        'pango-types.h',
        'pango-utils.h',
        'pango-version-macros.h'
    ]
    source = ''
    typedefs_opaque = ''
    typedefs_struct = ''
    typedefs_enum = ''
    typedefs_other = ''
    for header_file in header_files:
        (
            file_source,
            file_typedefs_opaque,
            file_typedefs_enum,
            file_typedefs_other
        ) = read_pango_header(pango_git_dir, header_file)
        source += file_source
        typedefs_opaque += file_typedefs_opaque
        typedefs_enum += file_typedefs_enum
        typedefs_other += file_typedefs_other

    # Extract opaque typedefs and insert them into a string containing all the
    # structs. Then remove the opaque typedefs that have been extracted
    typedefs_struct += get_struct_for_opaque_typedef(
        'PangoRectangle',
        pango_git_dir,
        'pango-types.h',
        '_PangoRectangle'
    )
    typedefs_opaque = remove_opaque_typedef(typedefs_opaque, 'PangoRectangle')

    typedefs_struct += get_struct_for_opaque_typedef(
        'PangoItem',
        pango_git_dir,
        'pango-item.h',
        '_PangoItem'
    )
    typedefs_opaque = remove_opaque_typedef(typedefs_opaque, 'PangoItem')

    typedefs_struct += get_struct_for_opaque_typedef(
        'PangoGlyphItem',
        pango_git_dir,
        'pango-glyph-item.h',
        '_PangoGlyphItem'
    )
    typedefs_opaque = remove_opaque_typedef(typedefs_opaque, 'PangoGlyphItem')

    typedefs_struct += get_struct_for_opaque_typedef(
        'PangoGlyphItemIter',
        pango_git_dir,
        'pango-glyph-item.h',
        '_PangoGlyphItemIter'
    )
    typedefs_opaque = remove_opaque_typedef(
        typedefs_opaque,
        'PangoGlyphItemIter'
    )

    # Remove and replace the aliased opaque typedefs
    typedefs_struct += 'typedef PangoGlyphItem PangoLayoutRun;\n'
    typedefs_opaque = remove_opaque_typedef(typedefs_opaque, 'PangoLayoutRun')

    cdefs = typedefs_opaque +\
        typedefs_struct +\
        typedefs_enum +\
        typedefs_other +\
        source

    # Replace function parameter arguments with non-consts
    # Todo: Is this really needed?
    cdefs = re.sub(r'const PangoRectangle', 'PangoRectangle', cdefs)
    cdefs = re.sub(r'const PangoGlyphItem', 'PangoGlyphItem', cdefs)
    cdefs = re.sub(r'const PangoItem', 'PangoItem', cdefs)

    # Convert PangoAnalysis (util we make PangoAnalysis non-opaque)
    cdefs = re.sub(r'PangoAnalysis analysis;', 'void * analysis;', cdefs)

    cdefs = remove_multiple_blank_lines(cdefs)
    cdefs = remove_multiple_spaces(cdefs)
    print(cdefs)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        generate(sys.argv[1])
    else:
        print('Usage: %s path/to/pango_source.git' % sys.argv[0])
