import requests
import pandas as pd

def get_data(userid, option):
    url = "http://3rdreadapi.ppdapi.com/queryData"

    payload = {"appid": 11050001,"userid": userid, "options": option}
    headers = {
    'Content-Type': "application/json",
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    resp = response.json()
    return resp["data"][option]

def main():
    df_userid = pd.read_csv("/home/pld_wangdi03/tanzhi.csv")
    userids = df_userid.sort_values(by=["userid"])["userid"]
    options = ["tz_creditinfo_eventsums"]
    for option in options:
        data_lst = []
        for userid in userids[:10]:
            data = get_data(userid, option)
            df = pd.DataFrame(data)
            data_lst.append(df)
        
        df_result = pd.concat(data_lst)
        df_result.to_csv(option + ".csv", index=False)
    

