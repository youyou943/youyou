import pymysql
import csv

# 连接到 MySQL 数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', database='CN')
cursor = conn.cursor()

# 读取 CSV 文件并将数据插入到数据库中
with open(r"university_info(3).csv", 'r', encoding='gb2312') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # 跳过 CSV 文件的标题行

    for row in csvreader:
        # # 将空值转换为 None
        # row = [None if value == '' else value for value in row]
        # # 尝试将排名列的值转换为整数类型，如果无法转换则跳过该行
        # try:
        #     row[3] = int(row[3])
        # except ValueError:
        #     continue


        cursor.execute(
            "INSERT INTO universities (chinese_name, english_name, province, ranking, address,website_uni,website_inner) VALUES (%s, %s, %s, %s, %s,%s,%s)",
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

# 提交事务并关闭连接
conn.commit()
cursor.close()
conn.close()
