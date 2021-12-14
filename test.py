#%%
from pyhive import hive
from sqlalchemy.engine import create_engine


engine = create_engine('hive://localhost:10000/default')
# %%

connection = engine.connect()
# %%
a = connection.execute("use lineman_beta")
# %%
a.description()
# %%
dir(a)

# %%
dir(a.keys)
# %%
a.keys()
# %%
b = connection.execute("show tables")
b.fetchall()

# %%
# %%
