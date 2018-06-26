#%%
from collections import abc

class FrozenJSON:
    
    def __init__(self, mapping):
        self.__data = dict(mapping)
    
    def __getattribute__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])
    
    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

#%%
fed = FrozenJSON(feed)
fed.Schedule.keys()