# first install mysql-connector-python
import mysql.connector
db = mysql.connector.connect(host ="localhost" ,user ="root" ,password ="admin")
print(db)

