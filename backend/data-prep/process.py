import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres://pshah:hello@localhost:5432/chaosmonkey')

df = pd.read_sql_query('select * from "Logs"',con=engine)

print(df)
