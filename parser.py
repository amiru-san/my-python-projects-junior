import requests

link = "https://acm.timus.ru/"

result = requests.get(link).text

with open("test.html", "w", encoding="utf-8") as file:
    file.write(result)