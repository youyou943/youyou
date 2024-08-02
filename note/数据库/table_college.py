import os
import pymysql
import pandas as pd
import chardet
# 连接到 MySQL 数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='CN',
    charset='utf8mb4'
)
cursor = conn.cursor()

# CSV 文件目录
csv_directory = r"D:\软件工程大作业\数据库\university"

# 遍历目录中的每个 CSV 文件
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        id = filename[:-4]  # 假设文件名即为学校ID
        file_path = os.path.join(csv_directory, filename)

        # 检测文件编码
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())

        # 使用检测到的编码读取文件
        df = pd.read_csv(file_path, encoding=result['encoding'])

        # 准备插入数据
        if 'twebsite' in df.columns:
            data_to_insert = [(id, row['text'], row['href'],row['twebsite']) for _, row in df.iterrows()]
        else:
            print(id,"插不了")
        # 定义插入查询
        insert_query = """
        INSERT INTO college (id, college_name, cwebsite,twebsite) 
        VALUES (%s, %s, %s,%s)
        """

        # 批量插入数据
        cursor.executemany(insert_query, data_to_insert)
        print(f"已成功将文件 {filename} 中的数据导入到 college 表中")

# 提交事务并关闭连接
conn.commit()
cursor.close()
conn.close()


# CREATE TABLE college (
#     id INT,
#     college_name VARCHAR(255),
#     cwebsite VARCHAR(255),
#     twebsite VARCHAR(255),
#     FOREIGN KEY (id) REFERENCES universities(id)
# );


# 测试了以后发现url太长了，没有存完
# 如果使用的是UTF-8编码，通常一个字符可能会占用多个字节，这可能导致实际存储的字符数超出预期。
# CREATE TABLE college (
#     id INT,
#     college_name VARCHAR(255),
#     cwebsite VARCHAR(255),
#     twebsite TEXT(255),
#     FOREIGN KEY (id) REFERENCES universities(id)
# );