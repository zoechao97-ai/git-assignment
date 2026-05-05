import os
import requests
from bs4 import BeautifulSoup

url = input("Enter Medium article URL: ")

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")
text = "\n".join([p.get_text(strip=True) for p in paragraphs])

folder_name = "Assignment_1"
os.makedirs(folder_name, exist_ok=True)

file_path = os.path.join(folder_name, "medium_article_text.txt")

with open(file_path, "w", encoding="utf-8") as file:
    file.write(text)

print(f"Text saved to: {file_path}")