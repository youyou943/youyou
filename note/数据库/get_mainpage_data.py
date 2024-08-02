import csv,json
# data=[]
# with open('mainpage_data.csv','r', encoding='UTF-8') as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         if(row['class_rank']=='A'):
#            data.append(row)
# print(data)
#
# #将数据写入到 txt 文件中
# with open('classA.txt', 'w', encoding='UTF-8') as output_file:
#         json.dump(data, output_file, ensure_ascii=False, indent=4)


data=[]
with open('mainpage_data.csv','r', encoding='UTF-8') as file:
    reader=csv.DictReader(file)
    for row in reader:
        if(row['class_rank']=='G'):
           data.append(row)
print(data)

#将数据写入到 txt 文件中
with open('classG.txt', 'w', encoding='UTF-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)