import requests
import csv

def fetch_university_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error fetching data:", e)
        return None

def extract_university_info(data):
    if data and 'data' in data:
        rankings = data['data']['rankings']
        for ranking in rankings:
            yield [
                ranking.get('univNameCn', ''),
                ranking.get('univNameEn', ''),
                ranking.get('province', ''),
                ranking.get('score', ''),
                ranking.get('ranking', '')
            ]
            if ranking.get('univNameCn') == '浙江工商大学':
                break

def save_to_csv(university_info):
    if university_info:
        with open("university_info.csv", "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["学校名称(中文)", "学校名称(英文)", "省份", "综合评分", "排名"])
            writer.writerows(university_info)

def main():
    api_url = 'https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=10&year=2023'
    university_data = fetch_university_data(api_url)
    if university_data:
        university_info = list(extract_university_info(university_data))
        save_to_csv(university_info)
        print("University information saved to university_info.csv")
    else:
        print("Failed to fetch university data.")

if __name__ == "__main__":
    main()
