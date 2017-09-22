# coding=utf8
from __future__ import print_function, absolute_import, division

import gremlinrestclient

import logging
import os
import pandas as pd
import yaml
import json

import itertools
from multiprocessing.dummy import Pool as ThreadPool

pd.options.mode.chained_assignment = None

import anti_fraud.run_pdl_xinke_anti_fraud_model as run_af_model
# import random

root_dir = os.path.split(os.path.realpath(__file__))[0]
host = yaml.load(open(os.path.join(root_dir, 'conf/af1_titan.yml')))
var = yaml.load(open(os.path.join(root_dir, 'conf/af1_var.yml')))
calset = yaml.load(open(os.path.join(root_dir, 'conf/limei_var.yml')))

# COUNT = 0

def __af_gremlin(url, userid, relfunc):
    # global COUNT
    # COUNT += 1
    # print('NO.', COUNT)
    # print(url, userid, relfunc)
    conf = calset[relfunc]
    client = gremlinrestclient.GremlinRestClient(url)
    result = dict()
    result_dict = dict()
    try:
        resp = client.execute('%s(userid)' % relfunc, bindings={"userid": userid}, query_timeout=30)
        for res in resp.data:
            dem = res['key']
            if dem not in conf:
                continue
            for measure in res['value'].keys():
                if measure == 'other' and dem not in ['curr_max_overdue_repay', 'curr_max_overdue_withdraw',
                                                      'max_overdue_repay', 'max_overdue_withdraw']:
                    continue
                if measure in conf[dem] or 'top' in conf[dem]:
                    key = '@'.join([relfunc, dem, 'top' if measure == 'other' else measure])
                    result[key] = res['value'][measure]
    except Exception as e:
        pass
    result_dict[userid] = result
    return result_dict


def get_response_params_with_field_name(e_s):
    return __af_gremlin(*e_s)

# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
def get_anti_fraud(df_input):
    df_result = pd.DataFrame()
    if len(df_input) > 0:
        logging.info("=" * 5 + " 正式进入Ant Fraud计算模块！ " + "=" * 5)
        ip = host['ip']
        port = host['port']
        # dem = var['dem']
        # measure = var['measure']
        # dm = list(itertools.product(dem, measure))
        # tmap = var['relation']
        fmap = var['relfunc']
        ffmap = {k: v for k, v in fmap.items() if v in calset.keys()}

        logging.info("=" * 5 + " Ant Fruad初始化完毕 " + 5 * "=")

        df_input['ip'] = pd.Series(ip * len(df_input))
        df_input['url'] = df_input.apply(lambda x: 'http://%s:%s' % (x['ip'], port), axis=1)
        df_input = df_input[df_input['typeid'].isin(ffmap.keys())]
        df_input['relfunc'] = df_input.apply(lambda x: fmap[x['typeid']], axis=1)

        para_lst = itertools.izip(list(df_input['url']),
                                   list(df_input['userid']),
                                   list(df_input['relfunc']))
        pool10 = ThreadPool(10)
        raw_output_lst = pool10.map(get_response_params_with_field_name, para_lst)
        pool10.close()
        pool10.join()
        result_dict = {k: dict() for k in df_input['userid'].unique()}
        for userid_dict in raw_output_lst:
            if len(userid_dict):
                userid = list(userid_dict.keys())[0]
                result_dict[userid].update(userid_dict[userid])
        df_result = pd.read_json(json.dumps(result_dict), orient='index', convert_axes = False).reset_index()
        df_result.rename(columns={'index': 'userid'}, inplace=True)
        if len(df_result.columns) < 303:
            df_result = pd.DataFrame()
        # df_result.to_csv('df_anti_fraud.csv', index=False)
        logging.info("=" * 5 + " Ant Fruad运行完毕 " + 5 * "=")
        logging.info("=" * 5 + " 反欺诈变量数据传输完毕！ 小哥我干完活去休息啦！ " + 5 * "=")
    return df_result


def prepare_data(df_userid):
    userids = list(df_userid['userid'].unique())
    # 切量测试：1%
    N = 100
    # n = random.randint(0, N)
    userid_cut = [x for x in userids if x % N == 64]
    type_id = list(range(2000, 2072, 1))
    user_list = list()
    for i in userid_cut:
        user_list += [i] * len(type_id)
    df_input = pd.DataFrame(
        data={"userid": user_list, "typeid": type_id * len(userid_cut)}
    )
    return df_input


if __name__ == "__main__":
    df_user = pd.read_csv('pdl_model_test_userid1.csv', encoding='gb2312')
    # userid = [30722935, 321321]
    userid = list(df_user['userid'])
    type_id = list(range(2000, 2072, 1))
    user_list = list()
    for i in userid:
        user_list += [i] * len(type_id)
    df = pd.DataFrame(
        data={"userid": user_list, "typeid": type_id * len(userid)}
    )
    import time
    a = time.time()
    df_res = get_anti_fraud(df)
    print(time.time() - a, 's')
    df_res.to_csv('pdl_model_var_input.csv', index=False)
    df_pdl_anti_fraud_score = run_af_model.model_main(df_res)
    df_pdl_anti_fraud_score.to_csv('pdl_anti_fraud_score.csv', index=False)

