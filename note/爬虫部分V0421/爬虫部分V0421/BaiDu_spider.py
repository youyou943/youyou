import requests
from lxml import etree
import get_user_agent
import os
def get_information(url,query,i):
    user_agent = get_user_agent.get_user_agent_of_pc()
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    html = response.content.decode('utf-8')
    res = etree.HTML(html)
    li_list_1 = res.xpath(r"//h3[contains(text(), '师资力量')]/ancestor::div[1]/following-sibling::node()[position()<coun"
                          r"t(//h3[contains(text(), '师资力量')]/ancestor::div[1]/following-sibling::node())-count(//h3[co"
                          r"ntains(text(), '师资力量')]/ancestor::div[1]/following-sibling::div[@class='paraTitle_IjGV2 l"
                          r"evel-2_PLGkw MARK_MODULE'][1]/following-sibling::node())]")
    os.makedirs(f'./university_sz/{i}.{query}')
    for li in li_list_1:
        information = li.xpath('./span//text()')
        with open(f"./university_sz/{i}.{query}/introduction.txt", "a", encoding="utf-8") as file:
            file.write(f"{information}\n")
        # print(f"{information}")
    for li in li_list_1:
        information = li.xpath('.//td//span//text()')
        for td in information:
            with open(f"./university_sz/{i}.{query}/tabel.txt", "a", encoding="utf-8") as file:
                file.write(f"{td}\n")
        # print(f"{information}")
    for li in li_list_1:
        information = li.xpath('.//img/@src')
        a=0
        if information:  # 检查列表是否为空
            for a in range(0,len(information)):
                response = requests.get(information[a])
                if response.status_code == 200:
                    # 设置图片保存路径及文件名
                    file_path = f'./university_sz/{i}.{query}/image{a}.jpg'
                    # 打开一个文件以写入二进制数据
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
        #         print(f"Image saved successfully as {file_path}")
        #     else:
        #         print("Failed to retrieve the image.")
        # else:
        #     print("No image found for this element.")
    return

with open("./university_bksz_url.txt", "r") as file:
    i=0
    for line in file:
        i+=1
        url = line.strip().split()[1]
        query = line.strip().split()[0]
        get_information(url,query,i)
        print(f"{i}.{query}")

