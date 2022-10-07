from . import ffi, pango, Attribute, PangoObject


class AttrList(PangoObject):
    """
    The :class:`AttrList` represents a list of attributes(:class:`Attribute`)
    that apply to a section of text. The attributes are, in general, allowed
    to overlap in an arbitrary fashion, however, if the attributes are
    manipulated only through :func:`AttrList.change()`, the overlap between
    properties will meet stricter criteria.

    In general, you should not use a single :class:`AttrList` for more than
    one paragraph of text due to internal structures.
    """

    _INIT_METHOD = pango.pango_attr_list_new
    _GC_METHOD = pango.pango_attr_list_unref
    _COPY_METHOD = pango.pango_attr_list_copy

    def _ref(self) -> None:
        """
        Increase the reference count of the given attribute list by one.
        """
        self._pointer = pango.pango_attr_list_ref(self._pointer)

    def _unref(self) -> None:
        """
        Decrease the reference count of the given attribute list by one.
        If the result is zero, free the attribute list and the attributes
        it contains.
        """
        pango.pango_attr_list_unref(self._pointer)

    def insert(self, attr: Attribute) -> None:
        """
        Insert the given attribute into the PangoAttrList. It will be inserted
        after all other attributes with a matching ``start_index``.

        :param attr:
            The :class:`Attribute` to insert.
        :raises: AssertionError
            When ``attr`` isn't a :class:`Attribute`.
        """
        assert isinstance(attr, Attribute), "attr isn't a Attribute"
        self._ref()
        pango.pango_attr_list_insert(self._pointer, attr.pointer)

    def insert_before(self, attr: Attribute) -> None:
        """
        Insert the given attribute into the PangoAttrList. It will be inserted
        before all other attributes with a matching ``start_index``.

        :param attr:
            The :class:`Attribute` to insert.
        :raises: AssertionError
            When ``attr`` isn't a :class:`Attribute`.
        """
        assert isinstance(attr, Attribute), "attr isn't a Attribute"
        self._ref()
        pango.pango_attr_list_insert_before(self._pointer, attr.pointer)

    def change(self, attr: Attribute) -> None:
        """
        Insert the given attribute into the :class:`AttrList`. It will replace
        any attributes of the same type on that segment and be merged with any
        adjoining attributes that are identical.

        This function is slower than :py:meth:`AttrList.insert` for creating
        an attribute list in order (potentially much slower for large lists).
        However, :py:meth:`AttrList.insert` is not suitable for continually
        changing a set of attributes since it never removes or combines
        existing attributes.

        :param attr:
            The :class:`Attribute` to insert.
        :raises: AssertionError
            When ``attr`` isn't a :class:`Attribute`.
        """
        assert isinstance(attr, Attribute), "attr isn't a Attribute"
        self._ref()
        pango.pango_attr_list_change(self._pointer, attr.pointer)

    def splice(self, attr_list: "AttrList", pos: int, length: int):
        """
        This function opens up a hole in ``self``, fills it in with attributes
        from the left, and then merges other on top of the hole.
        This operation is equivalent to stretching every attribute that applies
        at position pos in list by an amount len , and then calling
        :py:meth:`AttrList.change` with a copy of each attribute in other in
        sequence (offset in position by pos ).

        This operation proves useful for, for instance, inserting a pre-edit
        string in the middle of an edit buffer.


        :param attr_list: another :class:`AttrList`
        :type attr_list: AttrList
        :param pos: the position in ``self`` at which to insert other
        :type pos: int
        :param length:
            the length of the spliced segment. (Note that this must be
            specified since the attributes in other may only be present
            at some subsection of this range)
        :type length: int
        :raises: AssertionError
            When ``attr_list`` isn't a :class:`AttrList`.
            When ``pos`` isn't a :class:`int`
            When ``length`` isn't a :class:`int`
        """
        assert isinstance(attr_list, AttrList), "attr_list isn't a AttrList"
        assert isinstance(pos, int), "pos isn't a int"
        assert isinstance(length, int), "length isn't a int"
        length = ffi.cast("gint", length)
        pos = ffi.cast("gint", pos)
        pango.pango_attr_list_splice(
            self._pointer,
            attr_list._pointer,
            pos,
            length,
        )

    # avoid _EQ_METHOD since pango_attr_list_equal is a newer method
    def __eq__(self, other) -> bool:
        if isinstance(other, PangoObject):
            if self.pointer == other.pointer:
                return True
            else:
                return bool(pango.pango_attr_list_equal(
                    self.pointer, other.pointer
                ))

        return False

    # TODO: pango_attr_list_filter ()
