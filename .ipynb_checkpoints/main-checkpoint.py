from fastapi import FastAPI
import json
from scraping import scrape_jobs_data

app = FastAPI()

@app.get("/jobs/{job_search}")
def get_job_data(job_search: str):
    try:
        with open('jobs_data.json', 'r') as json_file:
            jobs_data = json.load(json_file)
    except FileNotFoundError:
        jobs_data = {}
    
    if job_search not in jobs_data:
        scrape_jobs_data([job_search])
        with open('jobs_data.json', 'r') as json_file:
            jobs_data = json.load(json_file)
    
    return jobs_data.get(job_search, {})

@app.get("/jobs/")
def get_all_jobs():
    try:
        with open('jobs_data.json', 'r') as json_file:
            jobs_data = json.load(json_file)
    except FileNotFoundError:
        jobs_data = {}
    
    return jobs_data

jobs_list = ['data scientist', 'data analyst']  # List of job searches
scrape_jobs_data(jobs_list)
