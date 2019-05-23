# 数据属性会覆盖掉具有相同名称的方法属性


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


