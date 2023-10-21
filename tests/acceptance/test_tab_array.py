import pangocffi
from pangocffi import Layout, TabArray, TabAlign
from tests.context_creator import ContextCreator


def test_tab_array_decimal_places():
    """
    In this test, we're aligning a list of labels and numbers.

    The list of numbers is deliberately ugly, as ideally all numbers would be
    given the same number of decimal places. But this test confirms that the
    numbers are aligned at the comma.
    """

    width = 100
    height = 100
    # CFFIs and Contexts
    context_creator = ContextCreator.create_pdf(
        'tests/acceptance/output/tab-array-decimal-places.pdf', width, height
    )
    pangocairo = context_creator.pangocairo
    cairo_context = context_creator.cairo_context

    lines = [
        ['Berlin', 891.3],
        ['Hamburg', 755.2],
        ['München', 310.7],
        ['Stuttgart', 207.33],
        ['Düsseldorf', 217.41],
        ['Bremen', 326.7],
        ['Dresden', 328.8],
        ['Hannover', 204.007],
        ['Wiesbaden', 203.9],
        ['Kiel', 118.6],
        ['Magdeburg', 201.012],
        ['Mainz', 97.7],
        ['Erfurt', 269.2],
    ]

    text = '\t<span font_weight="bold">Name</span>' \
           '\t<span font_weight="bold"> Fläche (km²)</span>\n'
    for line in lines:
        text += "\t" + line[0]
        text += "\t" + '{:.4f}'.format(line[1]).replace('.', ',').rstrip('0')
        text += '\n'

    # Using pangocairocffi, this would be `pangocairocffi.create_layout()` with
    # a cairocffi context object.
    layout = Layout.from_pointer(
        pangocairo.pango_cairo_create_layout(cairo_context)
    )

    mm_to_inches = 72 / 25.4

    layout.width = pangocffi.units_from_double(width * mm_to_inches)
    layout.apply_markup(text)

    # With this configuration, the tabs will align the text at 30mm and 70mm
    # intervals. In more simple terms: The first items that are tabbed should
    # appear right-aligned at the 30mm position, and all ',' (which will
    # be part of a number) should appear at the 70mm position.
    tabarray = TabArray()
    tabarray.tabs = [
        (TabAlign.RIGHT, pangocffi.units_from_double(30 * mm_to_inches)),
        (TabAlign.DECIMAL, pangocffi.units_from_double(45 * mm_to_inches))
    ]
    decimal_point = [None, ',']
    tabarray.decimal_point = decimal_point

    layout.tabs = tabarray

    # Using pangocairocffi, this would be `pangocairocffi.show_layout(layout)`
    pangocairo.pango_cairo_show_layout(cairo_context, layout.pointer)

    context_creator.close()
