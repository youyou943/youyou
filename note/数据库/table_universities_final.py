import pymysql
import csv
# 连接到 MySQL 数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', database='CN')
cursor = conn.cursor()

# 读取 CSV 文件并将数据插入到数据库中
with open(r"rank.csv", 'r', encoding='gb2312') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # 跳过 CSV 文件的标题行

    for line_num, row in enumerate(csvreader, start=1):
        # # 将空值转换为 None
        # row = [None if value == '' else value for value in row]

        # # 尝试将排名列的值转换为整数类型，如果无法转换则设为 None
        # try:
        #     row[3] = int(row[3])
        # except ValueError:
        #     row[3] = None
        # school_name = row[0]
        # classification_ranking = row[8]

        cursor.execute(
            "UPDATE universities SET class  = %s WHERE id = %s",
            (row[0], line_num)  # 使用csvreader.line_num获取行号
        )

# 提交事务并关闭连接
conn.commit()
cursor.close()
conn.close()


#添加分类排名：
#ALTER TABLE universities ADD COLUMN class VARCHAR(255);
