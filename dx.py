import pymysql

# 连接mysql数据库
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="zzmzxj294482972",
    database="testdb",
    charset="utf8mb4"
)

cursor = conn.cursor()

# 查询
cursor.execute("select * from student;")
res = cursor.fetchall()
print([head[0] for head in cursor.description])
for line in res:
    print(line)

cursor.close()
conn.close()


