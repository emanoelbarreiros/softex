from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine('postgresql://postgres:postgres@localhost:5432/softex')
#connection = engine.connect()
#tabela_df = pd.read_sql_table('produtos', con=engine)
tabela_df = pd.read_csv("salaries.csv")
tabela_df.hist(column="salary", bins=30)
plt.show()