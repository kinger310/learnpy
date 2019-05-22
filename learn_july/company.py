# .Python类设计
# 设计一个公司类，完成以下要求，并实例化不同对象进行验证
#
# 类变量
#
# 类下公司的总个数，类下实例的名称列表
# 类方法
#
# 返回公司类共有多少个公司实例
# 返回公司类的公司实例有名称列表
# 实例变量
#
# 公司名，简介，利润，销售额，总成本，雇员姓名
# 实例方法：
#
# 招聘人才（每招一个人会有成本产生，影响该实例雇员列表，人数，总成本）
# 解雇人员（每解雇一个人会有成本产生，影响该实例雇员列表，人数 ，总成本）
# 公司广告推广(影响该实例总成本)
# 交社保(按公司雇员总人数计算，影响该实例总成本)
# 交税(按公司雇员总人数计算，影响该实例总成本)
# 销售（按销售件数价格计算销售额，利润按销售额利润率进行计算利润。）
# 获取公司雇员列表
# 获取公司净利润

class Company(object):

    company_cnt = 0
    company_lst = []

    def __new__(cls, *args, **kwargs):
        cls.company_cnt += 1
        return super(Company, cls).__new__(cls)

    @classmethod
    def get_company_count(cls):
        print(cls.company_cnt)

    @classmethod
    def get_company_list(cls):
        print(cls.company_lst)

    def __init__(self, name, profit, income, cost, employee, headcount):
        self.name = name
        Company.company_lst.append(name)
        self.profit = profit
        self.income = income
        self.cost = cost
        self.employee = employee
        self.headcount = headcount

    def hire(self, person, salary):
        self.headcount += 1
        self.cost += salary
        self.employee.append(person)

    def fire(self, person, compensatory):
        self.headcount -= 1
        self.cost += compensatory
        self.employee.remove(person)

    def ad(self, fee):
        self.cost += fee

    def insure(self, fee_per_person):
        self.cost += fee_per_person * self.headcount

    def tax(self, tax_per_person):
        self.cost += tax_per_person * self.headcount

    def sale(self, quantity, price):
        self.income += quantity* price

    def get_employee(self):
        print(self.employee)

    def get_profit(self):
        self.profit += self.income - self.cost
        print(self.profit)

a = Company("aaa", 0, 0, 0, [], 0)
a.hire("alice", 100000)
a.hire("bob", 150000)
a.ad(10000)
a.insure(1000)
a.tax(500)
a.sale(10000, 100)
a.fire("bob", 10000)
a.get_employee()
a.get_profit()

a.get_company_count()
a.get_company_list()


b = Company("bbb", 0, 0, 0, [], 0)
b.hire("tom", 100000)
b.hire("eric", 150000)
b.ad(10000)
b.insure(1000)
b.tax(500)
b.sale(10000, 50)
b.fire("tom", 10000)
b.get_employee()
b.get_profit()

b.get_company_count()
b.get_company_list()
