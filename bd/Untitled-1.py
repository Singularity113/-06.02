import sqlite3
bd=sqlite3.connect('E:/bd/data.sqlite')
cursor = bd.cursor()
cursor.execute("SELECT * FROM product_attribute")
for i in cursor.execute("SELECT * FROM product_attribute"):
    print(i)
input()