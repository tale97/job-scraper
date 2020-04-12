import requests
from bs4 import BeautifulSoup as bs
import argparse

# Handle Arguments
parser = argparse.ArgumentParser(description='Job Search Query')
parser.add_argument('title', type=str, help='Title of Job')
parser.add_argument('where', type=str, help='Location (State or City)')

args = parser.parse_args()

# Monster.com
monster_url = f'http://www.monster.com/jobs/search/?q={args.title}&where={args.where}'
monster_page = requests.get(monster_url)

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


# Indeed.com
indeed_URL = f'http://www.indeed.com/jobs?q={args.title}&l={args.where}'
indeed_page = requests.get(indeed_URL)

indeed_soup = bs(indeed_page.content, 'html.parser')
indeed_results = indeed_soup.find('td', id='resultsCol')
#print(indeed_results)
#indeed_jobs = indeed_results.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')
indeed_jobs = indeed_results.find_all('div', class_='jobsearch-SerpJobCard')

for indeed_job in indeed_jobs:
    indeed_title = indeed_job.find('div', class_='title')
    indeed_company = indeed_job.find('span', class_='company')
    indeed_location = indeed_job.find('div', class_='location')
    indeed_link = indeed_title.find('a')['href']

    if None in (indeed_title, indeed_location, indeed_company):
        continue

    print(indeed_title.text.strip())
    print(indeed_company.text.strip())
    print(indeed_location.text.strip())
    print(f"Application Link: indeed.com{indeed_link}") 
    print()
