import pandas as pd 
from sqlalchemy.engine import URL
import sqlalchemy as db
from sqlalchemy import create_engine

url_object = URL.create(
    "mysql+mysqlconnector",
    username="root",
    password="ehsan",
    host="localhost",    
    database="coffeeshopdata",
)
# user = "user_group4"
# db = "group4"
# password = "5)kUA%nuwVZ9&rCV"
# engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{db}")
engine = db.create_engine(url_object)
conn = engine.connect()

d = pd.DataFrame(engine.execute(
"""
SELECT * FROM address Inner join coffeeshop on address.CoffeID = coffeeshop.Id 
Inner join featuers on featuers.CoffeID = coffeeshop.Id 
Inner join points on points.CoffeID = coffeeshop.Id 
""").fetchall())
d=d.drop([d.columns[4],d.columns[10],d.columns[21]],axis=1) # drop columns of Id of Coffee shops sleeted in Inner join
id = d.index
d.insert(0,"Id",id)
d.to_csv("dash_data.csv",index=False)
