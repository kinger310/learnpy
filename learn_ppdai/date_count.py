from datetime import datetime, timedelta
from dateutil.parser import parse

def date_diff(date1, date2=None, need_delta=False, format="%Y-%m-%d %H:%M:%S"):
    """
    两个日期相隔多少天，如果只传入一个时间则默认是与当前时间对比
    date1,date2输入格式为datetime或str类型， # 其中str可接受许多时间格式
    例：2008-10-03和2008-10-01是相隔两天
    注：普通的datetime格式并没有days这一属性，只有day属性；
        days是timedelta格式特有的。

    :param need_delta:需要直接传出timedelta对象的话设为True

    """
    if is_valid_date(date1):
        date1 = convert_date(date1)
    else:
        return -1

    if date2 is None:
        date2 = datetime.now()
    elif is_valid_date(date2):
        date2 = convert_date(date2)
    else:
        return -1

    delta = date2 - date1

    if need_delta:
        return delta
    return abs(delta.days)


def convert_date(date1=None):
    if isinstance(date1, str) and is_valid_date(date1):
        date = parse(date1)
    elif isinstance(date1, datetime):
        date = date1
        # raise Exception('传入的date格式不正确！要么是datetime要么是str')
    return date

def is_valid_date(date1):
    '''判断是否是一个有效的日期字符串'''
    try:
        if isinstance(date1, datetime):
            pass
        else:
            parse(date1)
        return True
    except:
        return False


if __name__ == '__main__':
    date1 = '2016-12-22 10:49:57'
    date2 = '2016-1-22 10:49:57'

    days = date_diff('2016-1-12 00:00:00', '2016.5.12')
    print('days:', days)