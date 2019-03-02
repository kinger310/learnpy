
from copy import deepcopy
import traceback
from abc import ABC, abstractmethod
import asyncio
from hashlib import sha1
import time


import weakref

# class Singleton(type):
#     def __init__(self, *args, **kwargs):
#         self.__instance = None
#         super().__init__(*args, **kwargs)
#
#     def __call__(self, *args, **kwargs):
#         if self.__instance is None:
#             self.__instance = super().__call__(*args, **kwargs)
#             return self.__instance
#         else:
#             return self.__instance


class GeneralException(Exception):
    _error_message = None

    def __init__(self, need_format=True, **kwargs):
        if need_format:
            self.error_message = self._error_message.format(**kwargs)
        else:
            self.error_message = self._error_message
        super().__init__(self.error_message)


class CacheException(GeneralException):
    def __init__(self, error_message):
        self._error_message = error_message
        super().__init__(need_format=False)


app_requests = {}


def _make_cache_key(kw):
    key = ""
    if kw:
        for item in sorted(kw.items()):
            key += str(item)
    return sha1(key.encode("utf-8")).hexdigest()


# class DataSource(metaclass=Singleton):
class DataSource(ABC):

    cache = None
    lock = None
    error_message = None
    total_time = 0

    # cpu_time = 0

    def __new__(cls, *args, sid=None, **kw):
        assert not args, "DataSource only accepts named arguments"

        if sid is None:
            return super().__new__(cls)
        cache_key = _make_cache_key(kw)
        cls_id = id(cls)
        if cls_id not in app_requests[sid]:
            app_requests[sid][cls_id] = {}
        if cache_key not in app_requests[sid][cls_id]:
            app_requests[sid][cls_id][cache_key] = super().__new__(cls)
        return app_requests[sid][cls_id][cache_key]

    def __init__(self, sid=None, **kw):
        print("init", DataSource.__name__)
        self.sid = sid
        self.kw = kw

    @abstractmethod
    async def compute(self, **kw):
        pass

    async def get_dep_result(self, klass, **kw):
        ob = klass(sid=self.sid, **kw)
        result = await ob.get_result()
        # self.cpu_time += ob.cpu_time
        return result

    async def _compute(self):
        self.lock = asyncio.Event()
        start = time.time()
        task = asyncio.ensure_future(self.compute(**self.kw))
        try:
            self.cache = await task
        except GeneralException as ex:
            self.error_message = ex.error_message
            raise
        except Exception as ex:
            error = traceback.format_exc()
            self.error_message = error
            raise
        finally:
            self.total_time = int((time.time() - start) * 1000)
            # self.cpu_time += task.cpu_time
            self.lock.set()

    async def get_result(self):
        if self.lock is not None:
            await self.lock.wait()
            if self.error_message is not None:
                raise CacheException(self.error_message)
        else:
            await self._compute()
        return deepcopy(self.cache)


class MyInterface(DataSource):
    async def compute(self, userid):
        await asyncio.sleep(3)
        return int(userid + 1)


class AAA(DataSource):

    async def compute(self, user_info, variable_name):
        res = await self.get_dep_result(MyInterface, userid=user_info["userid"])
        return res


async def main():
    app_requests["100"] = {}

    s = AAA(
        user_info={"userid": 715},
        variable_name="bbb", sid="100"
    )
    t = AAA(
        user_info={"userid": 715},   # this spends 3s
        # user_info={"userid": 716},   # this spends 6s
        variable_name="bbb", sid="100"
    )
    print(s is t)
    print("-"*40)

    res1 = await s.get_result()
    res2 = await t.get_result()

    return res1, res2


if __name__ == '__main__':
    a = time.time()
    loop = asyncio.get_event_loop()
    r = loop.run_until_complete(main())
    print(r)
    print(time.time() - a)


