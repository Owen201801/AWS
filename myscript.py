import  pymysql.cursors


connection = pymysql.connect()


cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS persons (id int, name VARCHAR(30), ocupation VARCHAR(40))")


cursor.execute("select id,name,ocupation  from persons;")

for x in cursor.fetchall():
    print(x)

cursor.execute ("INSERT INTO persons (id,name,ocupation) VALUES (234, 'Felipe', 'Student')")

connection.commit()

