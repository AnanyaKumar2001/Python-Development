# ****************----------------------- Web Scraping

import requests
from bs4 import BeautifulSoup


url = "https://stackoverflow.com/questions"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
# print(questions)
# print(type(questions))
# print(questions[0].attrs)
# print(questions[0].get("id", 0))
# print(questions[0].select_one(".question-hyperlink"))
# print(questions[0].select_one(".question-hyperlink").getText())

for question in questions:
    print(question.select_one('.question-hyperlink').getText())
    print(question.select_one(".vote-count-post ").getText())
