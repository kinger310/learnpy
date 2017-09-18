import pandas as pd
from sqlalchemy import create_engine
import json
import sys
if sys.platform == 'win32':
    path = r'C:\Users\wangdi03\Downloads\history.db'
else:
    path = './history.db'

engine = create_engine('sqlite:///' + path)

df = pd.read_sql_query(
    """
    select * from usermmvs
    """,
    engine
)

for var in df['variablejson']:
    dic = json.loads(var)
    print dic['userid'], dic['pc_credit_edu']


print('ok')
