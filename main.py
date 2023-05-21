from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "USE YOUR OWN EMAIL"
MY_PASSWORD = "USE YOUR OWN PASSWORD"

session = requests.Session()
response = session.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_tags = soup.select('span.titleline')
article_titles = [tag.getText() for tag in article_tags]
article_links = [tag.find("a")["href"] for tag in article_tags]

article_upvotes = [int(tag.find(class_="score").contents[0].split()[0]) if tag.find(class_="score") else 0
                   for tag in soup.select('td.subtext')]

top_articles_titles = []
top_articles_links = []
for _, index in enumerate(sorted(range(len(article_upvotes)), key=article_upvotes.__getitem__, reverse=True)[:3]):
    top_articles_titles.append(article_titles[index])
    top_articles_links.append(article_links[index])

subject = "Top3NewsAlert"
message = f"1. {top_articles_titles[0]}:\t    {top_articles_links[0]}\n" \
          f"2. {top_articles_titles[1]}:\t    {top_articles_links[1]}\n" \
          f"3. {top_articles_titles[2]}:\t    {top_articles_links[2]}"

msg = MIMEText(message, 'plain', 'utf-8')
msg['Subject'] = subject
msg['From'] = MY_EMAIL
msg['To'] = "USE ANOTHER EMAIL"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.send_message(msg)


####################################### Initial CODE #######################################
# from bs4 import BeautifulSoup
# import requests
# import smtplib
#
#MY_EMAIL = "USE YOUR OWN EMAIL"
#MY_PASSWORD = "USE YOUR OWN PASSWORD"
#
# response = requests.get("https://news.ycombinator.com/")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, 'html.parser')
#
# article_titles = []
# article_links = []
# for article_tag in soup.find_all(name="span", class_="titleline"):
#     article_titles.append(article_tag.getText())
#     article_links.append(article_tag.find("a")["href"])
#
# article_upvotes = []
# for article in soup.find_all(name="td", class_="subtext"):
#     if article.span.find(class_="score") is None:
#         article_upvotes.append(0)
#     else:
#         article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))
#
# top_articles_titles = []
# top_articles_links = []
# for i in range(3):
#     max_points_index = article_upvotes.index(max(article_upvotes))
#     top_articles_links.append(article_links[max_points_index])
#     top_articles_titles.append(article_titles[max_points_index])
#     article_upvotes.remove(article_upvotes[max_points_index])
#     article_links.remove(article_links[max_points_index])
#     article_titles.remove(article_titles[max_points_index])
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="USE ANOTHER EMAIL",
#         msg=f"Subject:HackerNews\n\n"
#             f"1. {top_articles_titles[0]}:\t    {top_articles_links[0]}\n"
#             f"2. {top_articles_titles[1]}:\t    {top_articles_links[1]}\n"
#             f"3. {top_articles_titles[2]}:\t    {top_articles_links[2]}"
#     )
