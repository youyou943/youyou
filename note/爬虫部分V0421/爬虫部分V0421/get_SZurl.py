import pandas as pd
import requests
from bs4 import BeautifulSoup
import get_user_agent
from urllib.parse import quote

user_agent = get_user_agent.get_user_agent_of_pc()
headers = {'User-Agent': user_agent}

def get_first_link(query):
    try:
        # https: // www.baidu.com / s?wd = % E5 % 8C % 97 % E4 % BA % AC % E5 % A4 % A7 % E5 % AD % A6
        # https: // www.baidu.com / s?wd = % E6 % B8 % 85 % E5 % 8D % 8E % E5 % A4 % A7 % E5 % AD % A6
        url_encoded_text = quote(query)
        # url = f"https://www.baidu.com/s?wd={url_encoded_text}"
        url = f"https://baike.baidu.com/item/{url_encoded_text}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        print(url)
        with open("./university_bksz_url.txt","a") as file:
            file.write(f"{query} {url}\n")
    except Exception as e:
        print("Error:", e)
        return None

def main():
    df = pd.read_csv("./university_info.csv")
    university_names = df["学校名称(中文)"].tolist()
    for name in university_names:
        query = "+".join(name.split())
        get_first_link(query)

if __name__ == "__main__":
    main()



