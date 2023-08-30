import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


download_folder = 'subscriber_emote_images'

emote_data = []

req = requests.get("https://www.twitchmetrics.net/c/156037856-fextralife/emotes")
soup = BeautifulSoup(req.text, 'html.parser')

emote_links = soup.find_all('a', href=True)

img_count = #<起始编号>

for link in emote_links:
    emote_name_tag = link.find('samp')
    if emote_name_tag:
        emote_name = emote_name_tag.text.strip()
     

        img_tag = link.find('img', class_='img-fluid')
        if img_tag:
            img_url = urljoin("https://www.twitchmetrics.net", img_tag['src'])

            # 处理 emote 名称，将非法字符替换为下划线
            img_name = f"{img_count}.png"
            img_path = os.path.join(download_folder, img_name)

            response = requests.get(img_url)
            with open(img_path, 'wb') as f:
                f.write(response.content)

            print(f"Downloaded: {img_name}")

            emote_data.append({'Emote Name': emote_name, 'Image Path': img_path})  # 添加数据到 emote_data 列表

            img_count += 1  

text_file_path = 'subscriber_emote_data.txt'

with open(text_file_path, 'a') as text_file:
    for idx, row in enumerate(emote_data, start= #<起始编号>):
        emote_name = row['Emote Name']
        text_file.write(f"{idx}\t{emote_name}\n")

print(f"Data saved to {text_file_path}")



