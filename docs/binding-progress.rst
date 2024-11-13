.. _binding-progress:

Binding progress
================

Below is a list of bindings that have (denoted with a ✔︎) and have not been implemented.

Basic Pango Interfaces
______________________

* pango_itemize ()
* pango_itemize_with_base_dir ()
* ✔︎ pango_item_free ()
* ✔︎ pango_item_copy ()
* pango_item_new ()
* pango_item_split ()
* pango_reorder_items ()
* ✔︎ pango_context_new ()
* pango_context_changed ()
* pango_context_get_serial ()
* pango_context_set_font_map ()
* pango_context_get_font_map ()
* ✔︎ pango_context_get_font_description ()
* ✔︎ pango_context_set_font_description ()
* pango_context_get_language ()
* pango_context_set_language ()
* pango_context_get_base_dir ()
* pango_context_set_base_dir ()
* ✔︎ pango_context_get_base_gravity ()
* ✔︎ pango_context_set_base_gravity ()
* ✔︎ pango_context_get_gravity ()
* ✔︎ pango_context_get_gravity_hint ()
* ✔︎ pango_context_set_gravity_hint ()
* pango_context_get_matrix ()
* pango_context_set_matrix ()
* ✔︎ pango_context_load_font ()
* pango_context_load_fontset ()
* pango_context_get_metrics ()
* pango_context_list_families ()
* pango_break ()
* pango_get_log_attrs ()
* pango_find_paragraph_boundary ()
* pango_default_break ()
* pango_shape ()
* pango_shape_full ()
* ✔︎ PangoContext
* ✔︎ PangoItem
* PangoAnalysis
* PANGO_ANALYSIS_FLAG_CENTERED_BASELINE
* PANGO_ANALYSIS_FLAG_IS_ELLIPSIS
* PANGO_TYPE_DIRECTION
* PangoLogAttr
* PANGO_PIXELS()
* PANGO_PIXELS_FLOOR()
* PANGO_PIXELS_CEIL()
* PANGO_UNITS_ROUND()
* ✔︎ pango_units_to_double ()
* ✔︎ pango_units_from_double ()
* PANGO_ASCENT()
* PANGO_DESCENT()
* PANGO_LBEARING()
* PANGO_RBEARING()
* pango_extents_to_pixels ()
* pango_matrix_copy ()
* pango_matrix_free ()
* pango_matrix_translate ()
* pango_matrix_scale ()
* pango_matrix_rotate ()
* pango_matrix_concat ()
* pango_matrix_transform_point ()
* pango_matrix_transform_distance ()
* pango_matrix_transform_rectangle ()
* pango_matrix_transform_pixel_rectangle ()
* pango_matrix_get_font_scale_factor ()
* pango_matrix_get_font_scale_factors ()
* PANGO_GET_UNKNOWN_GLYPH()
* pango_glyph_string_new ()
* pango_glyph_string_copy ()
* pango_glyph_string_set_size ()
* pango_glyph_string_free ()
* pango_glyph_string_extents ()
* pango_glyph_string_extents_range ()
* pango_glyph_string_get_width ()
* pango_glyph_string_index_to_x ()
* pango_glyph_string_x_to_index ()
* pango_glyph_string_get_logical_widths ()
* ✔︎ pango_glyph_item_copy ()
* ✔︎ pango_glyph_item_free ()
* ✔︎ pango_glyph_item_split ()
* pango_glyph_item_apply_attrs ()
* pango_glyph_item_letter_space ()
* ✔︎ pango_glyph_item_get_logical_widths ()
* pango_glyph_item_iter_copy ()
* pango_glyph_item_iter_free ()
* ✔︎ pango_glyph_item_iter_init_start ()
* ✔︎ pango_glyph_item_iter_init_end ()
* ✔︎ pango_glyph_item_iter_next_cluster ()
* ✔︎ pango_glyph_item_iter_prev_cluster ()
* PANGO_SCALE
* ✔︎ PangoRectangle
* PangoMatrix
* PANGO_TYPE_MATRIX
* PANGO_MATRIX_INIT
* PangoGlyph
* PANGO_GLYPH_EMPTY
* PANGO_GLYPH_INVALID_INPUT
* PANGO_GLYPH_UNKNOWN_FLAG
* PangoGlyphInfo
* PangoGlyphGeometry
* PangoGlyphUnit
* PangoGlyphVisAttr
* PangoGlyphString
* PangoGlyphItem
* PangoGlyphItemIter
* PANGO_TYPE_GLYPH_STRING
* PANGO_TYPE_GLYPH_ITEM
* PANGO_TYPE_GLYPH_ITEM_ITER
* ✔︎ pango_font_description_new ()
* ✔︎ pango_font_description_copy ()
* pango_font_description_copy_static ()
* pango_font_description_hash ()
* pango_font_description_equal ()
* ✔︎ pango_font_description_free ()
* pango_font_descriptions_free ()
* ✔︎ pango_font_description_set_family ()
* pango_font_description_set_family_static ()
* ✔︎ pango_font_description_get_family ()
* ✔︎ pango_font_description_set_style ()
* ✔︎ pango_font_description_get_style ()
* ✔︎ pango_font_description_set_variant ()
* ✔︎ pango_font_description_get_variant ()
* ✔︎ pango_font_description_set_weight ()
* ✔︎ pango_font_description_get_weight ()
* ✔︎ pango_font_description_set_stretch ()
* ✔︎ pango_font_description_get_stretch ()
* ✔︎ pango_font_description_set_size ()
* ✔︎ pango_font_description_get_size ()
* ✔︎ pango_font_description_set_absolute_size ()
* ✔︎ pango_font_description_get_size_is_absolute ()
* ✔︎ pango_font_description_set_gravity ()
* ✔︎ pango_font_description_get_gravity ()
* pango_font_description_get_set_fields ()
* pango_font_description_unset_fields ()
* pango_font_description_merge ()
* pango_font_description_merge_static ()
* pango_font_description_better_match ()
* pango_font_description_from_string ()
* pango_font_description_to_string ()
* pango_font_description_to_filename ()
* pango_font_metrics_ref ()
* pango_font_metrics_unref ()
* ✔︎ pango_font_metrics_get_ascent ()
* ✔︎ pango_font_metrics_get_descent ()
* ✔︎ pango_font_metrics_get_approximate_char_width ()
* ✔︎ pango_font_metrics_get_approximate_digit_width ()
* ✔︎ pango_font_metrics_get_underline_thickness ()
* ✔︎ pango_font_metrics_get_underline_position ()
* ✔︎ pango_font_metrics_get_strikethrough_thickness ()
* ✔︎ pango_font_metrics_get_strikethrough_position ()
* PANGO_FONT()
* PANGO_IS_FONT()
* pango_font_find_shaper ()
* pango_font_describe ()
* pango_font_describe_with_absolute_size ()
* pango_font_get_coverage ()
* pango_font_get_glyph_extents ()
* pango_font_get_metrics ()
* pango_font_get_font_map ()
* PANGO_FONT_FAMILY()
* PANGO_IS_FONT_FAMILY()
* pango_font_family_get_name ()
* pango_font_family_is_monospace ()
* pango_font_family_list_faces ()
* PANGO_FONT_FACE()
* PANGO_IS_FONT_FACE()
* pango_font_face_get_face_name ()
* pango_font_face_list_sizes ()
* pango_font_face_describe ()
* pango_font_face_is_synthesized ()
* PANGO_FONT_MAP()
* PANGO_IS_FONT_MAP()
* PANGO_FONT_MAP_CLASS()
* PANGO_IS_FONT_MAP_CLASS()
* PANGO_FONT_MAP_GET_CLASS()
* pango_font_map_create_context ()
* pango_font_map_load_font ()
* pango_font_map_load_fontset ()
* pango_font_map_list_families ()
* pango_font_map_get_shape_engine_type ()
* pango_font_map_get_serial ()
* pango_font_map_changed ()
* pango_fontset_get_font ()
* pango_fontset_get_metrics ()
* (* PangoFontsetForeachFunc) ()
* pango_fontset_foreach ()
* pango_fontset_simple_new ()
* pango_fontset_simple_append ()
* pango_fontset_simple_size ()
* PangoFontDescription
* PANGO_TYPE_FONT_DESCRIPTION
* ✔︎ PangoStyle
* PANGO_TYPE_STYLE
* ✔︎ PangoWeight
* PANGO_TYPE_WEIGHT
* ✔︎ PangoVariant
* PANGO_TYPE_VARIANT
* ✔︎ PangoStretch
* PANGO_TYPE_STRETCH
* ✔︎ PangoFontMask
* PANGO_TYPE_FONT_MASK
* ✔︎ PangoFontMetrics
* PANGO_TYPE_FONT_METRICS
* PangoFont
* PANGO_TYPE_FONT
* PangoFontFamily
* PANGO_TYPE_FONT_FAMILY
* PangoFontFace
* PANGO_TYPE_FONT_FACE
* PangoFontMap
* PANGO_TYPE_FONT_MAP
* PangoFontMapClass
* PangoFontset
* PANGO_TYPE_FONTSET
* PangoFontsetClass
* PangoFontsetSimple
* PANGO_TYPE_FONTSET_SIMPLE
* pango_parse_markup ()
* pango_markup_parser_new ()
* pango_markup_parser_finish ()
* pango_attr_type_register ()
* pango_attr_type_get_name ()
* pango_attribute_init ()
* ✔︎ pango_attribute_copy ()
* ✔︎ pango_attribute_equal ()
* ✔︎ pango_attribute_destroy ()
* pango_attr_language_new ()
* ✔︎ pango_attr_family_new ()
* ✔︎ pango_attr_style_new ()
* ✔︎ pango_attr_variant_new ()
* ✔︎ pango_attr_stretch_new ()
* ✔︎ pango_attr_weight_new ()
* ✔︎ pango_attr_size_new ()
* ✔︎ pango_attr_size_new_absolute ()
* ✔︎ pango_attr_font_desc_new ()
* ✔︎ pango_attr_foreground_new ()
* ✔︎ pango_attr_background_new ()
* ✔︎ pango_attr_strikethrough_new ()
* ✔︎ pango_attr_strikethrough_color_new ()
* ✔︎ pango_attr_underline_new ()
* ✔︎ pango_attr_underline_color_new ()
* ✔︎ pango_attr_shape_new ()
* pango_attr_shape_new_with_data ()
* (* PangoAttrDataCopyFunc) ()
* ✔︎ pango_attr_scale_new ()
* ✔︎ pango_attr_rise_new ()
* ✔︎ pango_attr_letter_spacing_new ()
* ✔︎ pango_attr_fallback_new ()
* ✔︎ pango_attr_gravity_new ()
* ✔︎ pango_attr_gravity_hint_new ()
* ✔︎ pango_attr_font_features_new ()
* ✔︎ pango_attr_foreground_alpha_new ()
* ✔︎ pango_attr_background_alpha_new ()
* ✔︎ pango_color_parse ()
* ✔︎ pango_color_copy ()
* ✔︎ pango_color_free ()
* ✔︎ pango_color_to_string ()
* ✔︎ pango_attr_list_new ()
* ✔︎ pango_attr_list_ref ()
* ✔︎ pango_attr_list_unref ()
* ✔︎ pango_attr_list_copy ()
* ✔︎ pango_attr_list_insert ()
* ✔︎ pango_attr_list_insert_before ()
* ✔︎ pango_attr_list_change ()
* ✔︎ pango_attr_list_splice ()
* pango_attr_list_filter ()
* (* PangoAttrFilterFunc) ()
* pango_attr_list_get_iterator ()
* pango_attr_iterator_copy ()
* pango_attr_iterator_next ()
* pango_attr_iterator_range ()
* pango_attr_iterator_get ()
* pango_attr_iterator_get_font ()
* pango_attr_iterator_get_attrs ()
* pango_attr_iterator_destroy ()
* PangoAttrType
* PANGO_TYPE_ATTR_TYPE
* PangoAttrClass
* PangoAttribute
* PANGO_ATTR_INDEX_FROM_TEXT_BEGINNING
* PANGO_ATTR_INDEX_TO_TEXT_END
* PangoAttrString
* PangoAttrLanguage
* PangoAttrColor
* PangoAttrInt
* PangoAttrFloat
* PangoAttrFontDesc
* PangoAttrShape
* PangoAttrSize
* PangoAttrFontFeatures
* PangoUnderline
* PANGO_TYPE_UNDERLINE
* PANGO_SCALE_XX_SMALL
* PANGO_SCALE_X_SMALL
* PANGO_SCALE_SMALL
* PANGO_SCALE_MEDIUM
* PANGO_SCALE_LARGE
* PANGO_SCALE_X_LARGE
* PANGO_SCALE_XX_LARGE
* PangoColor
* PANGO_TYPE_COLOR
* PangoAttrList
* PANGO_TYPE_ATTR_LIST
* PangoAttrIterator
* ✔ pango_tab_array_new ()
* pango_tab_array_new_with_positions ()
* ✔ pango_tab_array_copy ()
* ✔ pango_tab_array_free ()
* ✔ pango_tab_array_get_size ()
* ✔ pango_tab_array_resize ()
* ✔ pango_tab_array_set_tab ()
* pango_tab_array_get_tab ()
* ✔ pango_tab_array_get_tabs ()
* ✔ pango_tab_array_set_decimal_point ()
* ✔ pango_tab_array_get_decimal_point ()
* ✔ pango_tab_array_set_positions_in_pixels ()
* ✔ pango_tab_array_get_positions_in_pixels ()
* pango_tab_array_sort ()
* pango_tab_array_to_string ()
* ✔ PangoTabArray
* PANGO_TYPE_TAB_ARRAY
* ✔ PangoTabAlign
* PANGO_TYPE_TAB_ALIGN
* ✔︎ pango_layout_new ()
* pango_layout_copy ()
* ✔︎ pango_layout_get_context ()
* pango_layout_context_changed ()
* pango_layout_get_serial ()
* ✔︎ pango_layout_set_text ()
* ✔︎ pango_layout_get_text ()
* pango_layout_get_character_count ()
* ✔︎ pango_layout_set_markup ()
* pango_layout_set_markup_with_accel ()
* ✔︎ pango_layout_set_attributes ()
* ✔︎ pango_layout_get_attributes ()
* ✔︎ pango_layout_set_font_description ()
* ✔︎ pango_layout_get_font_description ()
* ✔︎ pango_layout_set_width ()
* ✔︎ pango_layout_get_width ()
* ✔︎ pango_layout_set_height ()
* ✔︎ pango_layout_get_height ()
* ✔︎ pango_layout_set_wrap ()
* ✔︎ pango_layout_get_wrap ()
* pango_layout_is_wrapped ()
* ✔︎ pango_layout_set_ellipsize ()
* ✔︎ pango_layout_get_ellipsize ()
* pango_layout_is_ellipsized ()
* pango_layout_set_indent ()
* pango_layout_get_indent ()
* ✔︎ pango_layout_get_spacing ()
* ✔︎ pango_layout_set_spacing ()
* pango_layout_set_justify ()
* pango_layout_get_justify ()
* pango_layout_set_auto_dir ()
* pango_layout_get_auto_dir ()
* ✔︎ pango_layout_set_alignment ()
* ✔︎ pango_layout_get_alignment ()
* ✔︎ pango_layout_set_tabs ()
* ✔︎ pango_layout_get_tabs ()
* pango_layout_set_single_paragraph_mode ()
* pango_layout_get_single_paragraph_mode ()
* pango_layout_get_unknown_glyphs_count ()
* pango_layout_get_log_attrs ()
* pango_layout_get_log_attrs_readonly ()
* pango_layout_index_to_pos ()
* pango_layout_index_to_line_x ()
* pango_layout_xy_to_index ()
* pango_layout_get_cursor_pos ()
* pango_layout_move_cursor_visually ()
* pango_layout_get_extents ()
* pango_layout_get_pixel_extents ()
* ✔︎ pango_layout_get_size ()
* pango_layout_get_pixel_size ()
* ✔︎ pango_layout_get_baseline ()
* ✔︎ pango_layout_get_line_count ()
* pango_layout_get_line ()
* pango_layout_get_line_readonly ()
* pango_layout_get_lines ()
* pango_layout_get_lines_readonly ()
* ✔︎ pango_layout_get_iter ()
* ✔︎ pango_layout_iter_copy ()
* ✔︎ pango_layout_iter_free ()
* ✔︎ pango_layout_iter_next_run ()
* ✔︎ pango_layout_iter_next_char ()
* ✔︎ pango_layout_iter_next_cluster ()
* ✔︎ pango_layout_iter_next_line ()
* ✔︎ pango_layout_iter_at_last_line ()
* ✔︎ pango_layout_iter_get_index ()
* ✔︎ pango_layout_iter_get_baseline ()
* ✔︎ pango_layout_iter_get_run ()
* pango_layout_iter_get_run_readonly ()
* pango_layout_iter_get_line ()
* pango_layout_iter_get_line_readonly ()
* pango_layout_iter_get_layout ()
* ✔︎ pango_layout_iter_get_char_extents ()
* ✔︎ pango_layout_iter_get_cluster_extents ()
* ✔︎ pango_layout_iter_get_run_extents ()
* ✔︎ pango_layout_iter_get_line_yrange ()
* ✔︎ pango_layout_iter_get_line_extents ()
* ✔︎ pango_layout_iter_get_layout_extents ()
* pango_layout_line_ref ()
* pango_layout_line_unref ()
* pango_layout_line_get_extents ()
* pango_layout_line_get_pixel_extents ()
* pango_layout_line_index_to_x ()
* pango_layout_line_x_to_index ()
* pango_layout_line_get_x_ranges ()
* PangoLayout
* PangoLayoutIter
* ✔︎ PangoWrapMode
* ✔︎ PANGO_TYPE_WRAP_MODE
* ✔︎ PangoEllipsizeMode
* PANGO_TYPE_ELLIPSIZE_MODE
* ✔︎ PangoAlignment
* PANGO_TYPE_ALIGNMENT
* PangoLayoutLine
* PangoLayoutRun
* pango_script_for_unichar ()
* pango_script_get_sample_language ()
* pango_script_iter_new ()
* pango_script_iter_get_range ()
* pango_script_iter_next ()
* pango_script_iter_free ()
* ✔︎ pango_language_from_string ()
* ✔︎ pango_language_to_string ()
* ✔︎ pango_language_matches ()
* pango_language_includes_script ()
* pango_language_get_scripts ()
* ✔︎ pango_language_get_default ()
* ✔︎ pango_language_get_preferred ()
* ✔︎ pango_language_get_sample_string ()
* PangoScript
* PANGO_TYPE_SCRIPT
* PangoScriptIter
* ✔︎ PangoLanguage
* PANGO_TYPE_LANGUAGE
* pango_unichar_direction ()
* pango_find_base_dir ()
* pango_get_mirror_char ()
* pango_bidi_type_for_unichar ()
* PangoDirection
* PangoBidiType
* PANGO_GRAVITY_IS_IMPROPER()
* PANGO_GRAVITY_IS_VERTICAL()
* pango_gravity_get_for_matrix ()
* pango_gravity_get_for_script ()
* pango_gravity_get_for_script_and_width ()
* pango_gravity_to_rotation ()
* ✔︎ PangoGravity
* ✔︎ PangoGravityHint

Low Level functionality
_______________________

* PANGO_VERSION_ENCODE()
* PANGO_VERSION_CHECK()
* ✔︎ pango_version ()
* ✔︎ pango_version_string ()
* pango_version_check ()
* PANGO_VERSION
* PANGO_VERSION_MAJOR
* PANGO_VERSION_MINOR
* PANGO_VERSION_MICRO
* PANGO_VERSION_STRING
