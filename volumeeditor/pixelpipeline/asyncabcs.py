from abc import ABCMeta, abstractmethod

def _has_attribute( cls, attr ):
    if any(attr in B.__dict__ for B in cls.__mro__):
        return True
    return False

def _has_attributes( cls, attrs ):
    if all(_has_attribute(cls, a) for a in attrs):
        return True
    return False
    

class RequestABC:
    __metaclass__ = ABCMeta

    @abstractmethod
    def wait( self ):
        ''' doc '''

    @abstractmethod
    def notify( self, callback, **kwargs ):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is RequestABC:
            if _has_attributes(C, ['wait', 'notify']):
                return True
            return False
        return NotImplemented



class ArraySourceABC:
    __metaclass__ = ABCMeta

    @abstractmethod
    def request( self, slicing ):
        pass

    @abstractmethod
    def setDirty( slicing ):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is ArraySourceABC:
            if _has_attributes(C, ['request', 'setDirty']):
                return True
            return False
        return NotImplemented


class ImageSourceABC:
    __metaclass__ = ABCMeta

    @abstractmethod
    def request( self, rect ):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is ImageSourceABC:
            if _has_attribute(C, 'request'):
                return True
            return False
        return NotImplemented