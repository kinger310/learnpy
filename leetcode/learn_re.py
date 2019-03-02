import pandas as pd
import re


doc = '''
count_pre_all_suc == 0 and (count_83_ing + count_98_ing < 1)
count_pre_all_suc == 0 and (count_83_ing + count_98_ing >= 1)
count_pre_all_suc > 0 and  count_pre_all_suc == count_pre_ccd_suc
count_pre_all_suc > 0 and count_pre_dae_suc == 0 and listtype_suc_valid_first_excl_ccd == 21
count_pre_all_suc > 0 and count_pre_dae_suc == 0 and listtype_suc_valid_first_excl_ccd == 100 and sublisttype_suc_valid_first_excl_ccd == 0
count_pre_all_suc > 0 and count_pre_dae_suc == 0 and listtype_suc_valid_first_excl_ccd == 99
count_pre_all_suc > 0 and count_pre_dae_suc == 0 and listtype_suc_valid_first_excl_ccd == 82
count_pre_dae_suc == 0 and (listtype_suc_valid_first_excl_ccd not in [21, 82, 99, 100, 97, 98, 106] or (listtype_suc_valid_first_excl_ccd in [98] and sublisttype_suc_valid_first_excl_ccd not in [60001]))
count_pre_all_suc > 0 and count_pre_dae_suc > 0 and auditingdate_suc_dae_app_first < auditingdate_suc_dae_m_first
count_pre_all_suc > 0 and count_pre_dae_suc > 0 and auditingdate_suc_dae_app_first > auditingdate_suc_dae_m_first
count_pre_all_suc > 0 and count_pre_dae_suc == 0 and listtype_suc_valid_first_excl_ccd in [98] and sublisttype_suc_valid_first_excl_ccd in [60001]
count_pre_all_suc > 0 and count_pre_dae_suc == 0 and listtype_suc_valid_first_excl_ccd in [97]
'''


def is_valid(x):
    if x in ['==', '<', '<=', '>', '>=', '+', 'in', 'not in', '']:
        return False
    try:
        int(x)
    except:
        return True
    return False

#
# df1 = pd.read_excel(r"C:\Users\wangdi03\Desktop\wangdi\19.02\pata-ding-go\dingconf.xlsx")
#
# grouped = df1.groupby(["bizid"])
# result_lst = []
# for bizid, df in grouped:
#     print(bizid)
#     if bizid == 1014:
#         print("ok")
#
#     var_lst = set()
#     for row in df.itertuples():
#         doc = row.condition
#         if pd.isna(doc):
#             break
#         group = re.findall(r"(\w*) (==|<|<=|>|>=|\+|in|not in) (\w*)", doc)
#         for x in group:
#             for e in x:
#                 if is_valid(e):
#                     var_lst.add(e)
#     result_lst.append({"bizid": bizid, "variables": ",".join(var_lst)})
#
# df_biz = pd.DataFrame(result_lst)
# df_biz.to_csv(r"C:\Users\wangdi03\Desktop\wangdi\19.02\pata-ding-go\dingbizvar.csv")


group = re.findall(r"(\w*) (==|<|<=|>|>=|\+|in|not in) (\w*)", doc)
for x in group:
    print(x)


