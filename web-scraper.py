import requests
from bs4 import BeautifulSoup as bs
import argparse

# Handle Arguments
parser = argparse.ArgumentParser(description='Job Search Query')
parser.add_argument('title', type=str, help='Title of Job')
parser.add_argument('where', type=str, help='Location (State or City)')

args = parser.parse_args()

# Monster.com
URL_monster = f'http://www.monster.com/jobs/search/?q={args.title}&where={args.where}'
monster_page = requests.get(URL_monster)

soup = bs(monster_page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
jobs = results.find_all('section', class_='card-content')
for job in jobs:
    title = job.find('h2', class_='title')
    company = job.find('div', class_='company')
    location = job.find('div', class_='location')
    
    if None in (title, company, location):
        continue
    link = title.find('a')['href']
    
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(f"Application Link: {link}\n")
    print()

print(URL_monster)
