# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:31:52 2017

@author: Wangdi
"""


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