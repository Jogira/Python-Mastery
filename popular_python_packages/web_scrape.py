import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions", timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")
# print(questions[0].select_one(".s-link").getText())

for question in questions:
    print(question.select_one(".s-link").getText())
    print(question.select_one(".s-post-summary--stats-item").getText())
