# -*- coding:utf-8 -*-
import redis
import json
# import os
# path = os.path.split(os.path.realpath(__file__))[0]
# path2 = os.path.dirname(os.path.abspath(__file__))
# print(path)
# print(path2)

def main():
    port = [6379, 6380, 6381]
    result_list = []
    for i in range(len(port)):
        # conn = redis.Connection()
        pool = redis.ConnectionPool(max_connections=10, host='192.168.211.20', port=port[i])
        r = redis.Redis(connection_pool=pool)
        try:
            result = r.hgetall('pata-flow-result:1xxxxxx')
            result_list.append(method_name(result))
        except Exception as e:
            pass
            # print('cant find 1xx!')
        try:
            result = r.hgetall('pata-flow-result:1yyyyyy')
            result_list.append(method_name(result))
        except Exception as e:
            pass
            # print('cant find 1yy!')

    print(result_list)


def method_name(result):
    res = json.loads(str(result[b'result:-1']))
    want = (res['userid'], res['app_list_score_ppx'], res['pdl_max_default_days'], res['pc_credit_edu'])
    return want


if __name__ == '__main__':
    main()

