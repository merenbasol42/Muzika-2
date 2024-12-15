from .simple import MTSimple

'''one field "data"'''

class Int(MTSimple[int]): pass
class Float(MTSimple[float]): pass
class String(MTSimple[str]): pass
class Bool(MTSimple[bool]): pass

class List(MTSimple[list]): pass
class ListInt(MTSimple[list[int]]): pass
class ListFloat(MTSimple[list[float]]): pass
class ListString(MTSimple[list[str]]): pass
