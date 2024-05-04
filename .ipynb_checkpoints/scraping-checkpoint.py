import json
import requests
from bs4 import BeautifulSoup

def scrape_jobs_data(jobs_list):
    all_jobs_data = {}
    for job_search in jobs_list:
        response = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={job_search}&start=0")
        soup = BeautifulSoup(response.text, "html.parser")  
        num_of_jobs_text = soup.find("strong").get_text()
        Num_of_Jobs = int(num_of_jobs_text.replace(',', ''))
        jops_counter = 1
        page_number = 0
        skills_count = {}
        while jops_counter <= Num_of_Jobs: 
            response = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={job_search}&start={page_number}")
            soup = BeautifulSoup(response.text, "html.parser")
            page_jobs = soup.find_all("div", attrs={"class": "css-1gatmva e1v1l3u10"})
        
            for job in page_jobs: 
                jops_counter += 1
                skills_tags = job.find("div", attrs={"class": "css-y4udm8"}).find_all("div", attrs={})[1].find_all("a", attrs={"class": "css-5x9pm1"})[0:4]
                try:
                    skills_text = [skill.get_text().lstrip(' · ') for skill in skills_tags]
                except:
                    continue
        
                for skill in skills_text:
                    skills_count[skill.lower()] = skills_count.get(skill.lower(), 0) + 1
        
            page_number += 1
            print(f"{jops_counter - 1} jobs were scraped")
            print(f"{page_number} pages were scraped")
        
        sorted_skills = dict(sorted(skills_count.items(), key = lambda item: item[1], reverse = True))
        reduced_dict = {key: value for key, value in sorted_skills.items() if value > 4}
        all_jobs_data[job_search] = reduced_dict
        
    with open('jobs_data.json', 'w') as json_file:
        json.dump(all_jobs_data, json_file, indent=4)
