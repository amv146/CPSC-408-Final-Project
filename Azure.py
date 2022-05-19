import mysql
from mysql import connector as connector


db = connector.connect(host='chapman-univ.mysql.database.azure.com', 
  user='adminroot',
  password='Chapman408!', 
  database='scooby_doo',
  client_flags= [connector.ClientFlag.SSL]
)

print(db)