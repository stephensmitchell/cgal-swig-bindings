# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""SWIG wrapper for the CGAL Intersecting Sequences of dD Iso-oriented Boxes package provided under the GPL-3.0+ license"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _CGAL_Box_intersection_d
else:
    import _CGAL_Box_intersection_d

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import CGAL.CGAL_Kernel
class Pair_of_int(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _CGAL_Box_intersection_d.Pair_of_int_swiginit(self, _CGAL_Box_intersection_d.new_Pair_of_int(*args))
    first = property(_CGAL_Box_intersection_d.Pair_of_int_first_get, _CGAL_Box_intersection_d.Pair_of_int_first_set)
    second = property(_CGAL_Box_intersection_d.Pair_of_int_second_get, _CGAL_Box_intersection_d.Pair_of_int_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _CGAL_Box_intersection_d.delete_Pair_of_int

# Register Pair_of_int in _CGAL_Box_intersection_d:
_CGAL_Box_intersection_d.Pair_of_int_swigregister(Pair_of_int)

class Ids_iterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _CGAL_Box_intersection_d.Ids_iterator_swiginit(self, _CGAL_Box_intersection_d.new_Ids_iterator())

    def __iter__(self):
        return _CGAL_Box_intersection_d.Ids_iterator___iter__(self)

    def __next__(self):
        return _CGAL_Box_intersection_d.Ids_iterator___next__(self)

    def next(self, *args):
        return _CGAL_Box_intersection_d.Ids_iterator_next(self, *args)

    def deepcopy(self, *args):
        return _CGAL_Box_intersection_d.Ids_iterator_deepcopy(self, *args)

    def hasNext(self):
        return _CGAL_Box_intersection_d.Ids_iterator_hasNext(self)

    def __eq__(self, p):
        return _CGAL_Box_intersection_d.Ids_iterator___eq__(self, p)

    def __ne__(self, p):
        return _CGAL_Box_intersection_d.Ids_iterator___ne__(self, p)
    __swig_destroy__ = _CGAL_Box_intersection_d.delete_Ids_iterator

# Register Ids_iterator in _CGAL_Box_intersection_d:
_CGAL_Box_intersection_d.Ids_iterator_swigregister(Ids_iterator)

class Box_for_segment_polyline_2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, s, polyline_id, id):
        _CGAL_Box_intersection_d.Box_for_segment_polyline_2_swiginit(self, _CGAL_Box_intersection_d.new_Box_for_segment_polyline_2(s, polyline_id, id))
    __swig_destroy__ = _CGAL_Box_intersection_d.delete_Box_for_segment_polyline_2

# Register Box_for_segment_polyline_2 in _CGAL_Box_intersection_d:
_CGAL_Box_intersection_d.Box_for_segment_polyline_2_swigregister(Box_for_segment_polyline_2)

class Box_with_id_2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, bbox, id):
        _CGAL_Box_intersection_d.Box_with_id_2_swiginit(self, _CGAL_Box_intersection_d.new_Box_with_id_2(bbox, id))
    __swig_destroy__ = _CGAL_Box_intersection_d.delete_Box_with_id_2

# Register Box_with_id_2 in _CGAL_Box_intersection_d:
_CGAL_Box_intersection_d.Box_with_id_2_swigregister(Box_with_id_2)

class Box_with_id_3(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, bbox, id):
        _CGAL_Box_intersection_d.Box_with_id_3_swiginit(self, _CGAL_Box_intersection_d.new_Box_with_id_3(bbox, id))
    __swig_destroy__ = _CGAL_Box_intersection_d.delete_Box_with_id_3

# Register Box_with_id_3 in _CGAL_Box_intersection_d:
_CGAL_Box_intersection_d.Box_with_id_3_swigregister(Box_with_id_3)

COMPLETE = _CGAL_Box_intersection_d.COMPLETE
BIPARTITE = _CGAL_Box_intersection_d.BIPARTITE
HALF_OPEN = _CGAL_Box_intersection_d.HALF_OPEN
CLOSED = _CGAL_Box_intersection_d.CLOSED
class Collect_ids_callback_2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def ids(self):
        return _CGAL_Box_intersection_d.Collect_ids_callback_2_ids(self)

    def __init__(self):
        _CGAL_Box_intersection_d.Collect_ids_callback_2_swiginit(self, _CGAL_Box_intersection_d.new_Collect_ids_callback_2())
    __swig_destroy__ = _CGAL_Box_intersection_d.delete_Collect_ids_callback_2

# Register Collect_ids_callback_2 in _CGAL_Box_intersection_d:
_CGAL_Box_intersection_d.Collect_ids_callback_2_swigregister(Collect_ids_callback_2)

class Collect_ids_callback_3(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def ids(self):
        return _CGAL_Box_intersection_d.Collect_ids_callback_3_ids(self)

    def __init__(self):
        _CGAL_Box_intersection_d.Collect_ids_callback_3_swiginit(self, _CGAL_Box_intersection_d.new_Collect_ids_callback_3())
    __swig_destroy__ = _CGAL_Box_intersection_d.delete_Collect_ids_callback_3

# Register Collect_ids_callback_3 in _CGAL_Box_intersection_d:
_CGAL_Box_intersection_d.Collect_ids_callback_3_swigregister(Collect_ids_callback_3)


def box_intersection_d(*args):
    return _CGAL_Box_intersection_d.box_intersection_d(*args)

def box_intersection_all_pairs_d(*args):
    return _CGAL_Box_intersection_d.box_intersection_all_pairs_d(*args)

def box_self_intersection_d(*args):
    return _CGAL_Box_intersection_d.box_self_intersection_d(*args)

def box_self_intersection_all_pairs_d(*args):
    return _CGAL_Box_intersection_d.box_self_intersection_all_pairs_d(*args)


