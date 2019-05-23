# __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
#
# __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
#
# __init__有一个参数self，就是这个__new__返回的实例
# ---------------------
# 作者：一如故往
# 来源：CSDN
# 原文：https://blog.csdn.net/qq_37616069/article/details/79476249
# 版权声明：本文为博主原创文章，转载请附上博文链接！

class BBB:
    def __new__(cls, *args, **kwargs):
        kwargs.pop("bbb", None)
        print(id(kwargs))
        print(kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(id(kwargs))
        print(kwargs)

class CCC(BBB):
    pass


class  User:
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)

    def __init__(self,name):
        self.name=name
        print("init")

user=User("a")

CCC(aaa=12,bbb=34)