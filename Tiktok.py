import requests
from bs4 import BeautifulSoup

def get_country(username):
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url)  soup = BeautifulSoup(response.text, 'html.parser')   bio = soup.find('div', {'class': 'tiktok-y0c9h8-ProfileHeader-module_bioContainer___15XVt'}).text
    country = None
    if"Country" in bio:
        country = bio.split("Country:")[1].split(" ")[0]    return country
