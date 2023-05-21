# Top 3 News Alert

This project fetches the top 3 articles from the Hacker News website and sends them via email as an alert. Stay updated with the latest trending news and never miss out on the most popular articles.

## Prerequisites

- Python 3.x
- `beautifulsoup4` library (for web scraping)
- `requests` library (for making HTTP requests)
- `smtplib` library (for sending emails)
- `email` library (for email composition)

## Installation

1. Clone the repository:

```shell
git clone https://github.com/BloodShoT14/top-3-news-alert.git
```

2. Navigate to the project directory:

```shell
cd top-3-news-alert
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```

## Configuration

1. Open the `main.py` file.

2. Update the following variables with your own Gmail account credentials:

```python
MY_EMAIL = "your-email@gmail.com"
MY_PASSWORD = "your-password"
```

3. Replace the recipient email address with the desired email address to receive the top articles:

```python
msg['To'] = "recipient-email@example.com"
```

## Usage

Run the script using the following command:

```shell
python main.py
```

The script will automatically fetch the top 3 articles from Hacker News and send them as an email alert to the specified recipient.

## Customization

You can customize the project to suit your needs:

- Modify the number of top articles to retrieve by changing the range in the `for` loop:
  ```python
  for _, index in enumerate(sorted(range(len(article_upvotes)), key=article_upvotes.__getitem__, reverse=True)[:3]):
  ```

- Customize the email subject and message in the `msg` object:
  ```python
  subject = "Top 3 News Alert"
  message = f"1. {top_articles_titles[0]}:\t    {top_articles_links[0]}\n" \
            f"2. {top_articles_titles[1]}:\t    {top_articles_links[1]}\n" \
            f"3. {top_articles_titles[2]}:\t    {top_articles_links[2]}"
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project uses the Hacker News website (https://news.ycombinator.com/) as the data source.
- The project utilizes the `beautifulsoup4` library for web scraping and extracting article information.
- Special thanks to the creators and contributors of the open-source libraries used in this project.

Feel free to modify and customize the `README.md` file according to your project's specific needs and requirements. Include any additional sections or information that you think would be beneficial for users.