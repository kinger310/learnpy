# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:31:52 2017

@author: Wangdi
"""


# namespace 是一个从名字到对象的映射
# 一个函数的本地命名空间在这个函数被调用时创建，并在函数返回或抛出一个不在函数内部处理的错误时被删除。
# 一个 作用域 是一个命名空间可直接访问的Python程序的文本区域。 这里的 “可直接访问” 意味着对名称的非限定引用会尝试在命名空间中查找名称。

# Python 的一个特殊之处在于 -- 如果不存在生效的 global 语句 -- 对名称的赋值总是进入最内层作用域。
# 赋值不会复制数据 --- 它们只是将名称绑定到对象。 删除也是如此

# global 语句可被用来表明特定变量生存于全局作用域并且应当在其中被重新绑定；
# nonlocal 语句表明特定变量生存于外层作用域中并且应当在其中被重新绑定。


def scope_test():
    """
    the local assignment (which is default) didn't change scope_test's binding of spam. 
    The nonlocal assignment changed scope_test‘s binding of spam,
    and the global assignment changed the module-level binding.
    """

    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
