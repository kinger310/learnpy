#!/usr/bin/env python
# coding=utf-8

"""
常用计算日期相关的函数

目前包括：
1.计算之后多少天日期
2.计算相隔多少天
"""
from datetime import datetime, timedelta
from dateutil.parser import parse


def add_days(date, add_days, format="%Y-%m-%d %H:%M:%S", need_str=False):
    """
    计算加上天数后的日期
    :param date: 传入指定日期，str or datetime.datetime
    :param add_days:需加上的天数，可为正为负，int
    :return:默认为datetime.datetime对象，need_str=True时为str
    """
    if isinstance(date, str):
        date = datetime.strptime(date, format)

    if not isinstance(date, datetime):
        raise Exception('传入的date格式不正确！要么是datetime.datetime要么是str')

    need_date = date + timedelta(days=add_days)

    if need_str:
        need_date = str(need_date)
    return need_date


def date_diff(date1, date2=None, need_delta=False, format="%Y-%m-%d %H:%M:%S"):
    """
    两个日期相隔多少天，如果只传入一个时间则默认是与当前时间对比
    date1,date2输入格式应为datetime或str类型， 其中str可接受dateutil.parser能解析的时间格式.若不能解析,则返回-1.
    Reference: https://dateutil.readthedocs.io/en/stable/parser.html
    例：2008-10-03和2008-10-01是相隔两天
    注：普通的datetime格式并没有days这一属性，只有day属性；
        days是timedelta格式特有的。

    :param need_delta:需要直接传出timedelta对象的话设为True

    """
    success, date1 = convert_date(date1)
    if not success:
        return -1

    if date2 is None:
        date2 = datetime.now()
    else:
        success, date2 = convert_date(date2)
        if not success:
            return -1

    delta = date2 - date1

    if need_delta:
        return delta
    return abs(delta.days)



def convert_date(date):
    '''判断是否能转为一个有效的日期字符串'''
    try:
        if isinstance(date, datetime):
            pass
        else:
            date = parse(date)
        return True, date
    except:
        return False, -1


if __name__ == '__main__':
    date1 = '2016-12-22 10:49:57'
    date2 = '2016-1-22 10:49:57'

    days = add_days(date1, 2)
    print('days:', days)
