import os
import mysql.connector

# 连接到MySQL数据库
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="CN"
)
cursor = conn.cursor()

# 获取静态文件夹的绝对路径
static_folder_path = os.path.abspath('D:\PycharmProjects\FlaskDemo\static')

# 查询数据库中的所有路径
cursor.execute("SELECT logo FROM universities")
rows = cursor.fetchall()

# 更新数据库中的路径为相对路径
for row in rows:
    absolute_path = row[0]
    # 将反斜杠改为斜杠
    relative_path = absolute_path.replace("\\", "/")
    # 更新数据库中的路径
    cursor.execute("UPDATE universities SET logo = %s WHERE logo = %s", (relative_path, absolute_path))

# 提交更改
conn.commit()

# 关闭连接
conn.close()


#在渲染图片的时候发现路径不对，需要进行路径处理，把绝对路径转为相对于静态文件的相对路径才能渲染出来，或者就是把资源上传到服务器，但是我不会