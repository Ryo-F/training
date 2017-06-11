from bs4 import BeautifulSoup
import requests


def get_html_content(url):
    return requests.get(url).text


def get_title(url):
    html = get_html_content(url)
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.string


def get_all_links(url):
    html = get_html_content(url)
    soup = BeautifulSoup(html, "html.parser")
    return [l.get("href") for l in soup.find_all("a")]
