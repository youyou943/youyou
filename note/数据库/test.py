# import csv
#
# # 打开CSV文件
# with open('ranking.csv', 'r') as file:
#     # 读取CSV数据
#     reader = csv.reader(file)
#     next(reader)  # 跳过 CSV 文件的标题行
#     # 创建一个新的CSV文件来存储处理后的数据
#     with open('rank.csv', 'w', newline='') as processed_file:
#         # 写入处理后的数据到新的CSV文件
#         writer = csv.writer(processed_file)
#
#         for row in reader:
#             new_row = row[0][:1]
#             writer.writerow(new_row)
# import pandas as pd
#
# # 读取xls文件
# xls_file = pd.read_excel("logo.xls")
#
# # 将数据写入csv文件
# xls_file.to_csv("logo3.csv", index=False)
# import pandas as pd
#
# # 读取xls文件
# xls_file = pd.read_excel("mainpage_data.xls")
#
# # 将数据写入csv文件
# xls_file.to_csv("mainpage_data.csv", index=False)

# 这个错误是由于代码中使用os.listdir()函数列出的文件名只包含文件名，
# 而不包含完整的路径。因此，当使用pd.read_csv()函数时，
# 它会尝试在当前工作目录下寻找文件，而不是在指定的目录中查找
# import pandas as pd
# import os
# # CSV 文件目录
# csv_directory = r"D:\软件工程大作业\数据库\university"
#
# # 遍历目录中的每个 CSV 文件
# for filename in os.listdir(csv_directory):
#     #打开文件并读取数据
#     data=pd.read_csv(filename)
#     #获取列名列表
#     columns=data.columns.tolist()
#     #找到需要更改的列名索引
#     column_index=columns.index('师资')
#     #将列名改成新的列名
#     new_column_name='twebsite'
#     columns[column_index]=new_column_name
#     #保存文件
#     data.columns=columns
#     data.to_csv(filename,index=False)

import pandas as pd
import os

# # CSV 文件目录
# csv_directory = r"D:\软件工程大作业\数据库\university"
# i=0
# # 遍历目录中的每个 CSV 文件
# for filename in os.listdir(csv_directory):
#     file_path = os.path.join(csv_directory, filename)  # 获取完整的文件路径
#     # 打开文件并读取数据
#     data = pd.read_csv(file_path,encoding='UTF-8')
#     # 获取列名列表
#     columns = data.columns.tolist()
#     i=i+1
#     print(i)
#     print(columns)
#
#     # 找到需要更改的列名索引
#     column_index = columns.index('师资')
#     # 将列名改成新的列名
#     new_column_name = 'twebsite'
#     columns[column_index] = new_column_name
#     # 保存文件
#     data.columns = columns
#     data.to_csv(file_path, index=False)  # 保存文件时使用完整的文件路径

csv_directory = r"D:\软件工程大作业\数据库\university"
import chardet
for filename in os.listdir(csv_directory):
    file_path = os.path.join(csv_directory, filename)
    # 检测文件编码
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())

    # 使用检测到的编码读取文件
    df = pd.read_csv(file_path, encoding=result['encoding'])
    print(result['encoding'])