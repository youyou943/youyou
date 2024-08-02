import pymysql
import csv

# 连接到 MySQL 数据库
conn = pymysql.connect(host='localhost', user='root', password='123456', database='CN')
cursor = conn.cursor()

# 读取 CSV 文件并将数据插入到数据库中
with open(r"logo3.csv", 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # 跳过 CSV 文件的标题行
    for line_num, row in enumerate(csvreader, start=1):
        print(row[0])
        cursor.execute(
            "UPDATE universities SET logo  = %s WHERE id = %s",
            (row[0], line_num)  # 使用csvreader.line_num获取行号
        )

# 提交事务并关闭连接
conn.commit()
cursor.close()
conn.close()


#ALTER TABLE universities ADD COLUMN logo VARCHAR(255);

#代码写错了一直用insert into 导致一直插在下面了
#而且这个编码格式也很奇怪，似乎要按照文件的编码格式来确定