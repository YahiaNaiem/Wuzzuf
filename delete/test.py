# import json

# def get_job_data():
#     try:
#         with open('jobs_data.json', 'r') as json_file:
#             jobs_data = json.load(json_file)
#     except FileNotFoundError:
#         jobs_data = {}
    
#     # if job_search not in jobs_data:
#     #     scrape_jobs_data([job_search])
#     #     with open('jobs_data.json', 'r') as json_file:
#     #         jobs_data = json.load(json_file)
    
#     return jobs_data.get("data-scientist", {})

# #print(get_job_data())
# print("*" * 100)
# with open('jobs_data.json', 'r') as json_file:
#             jobs_data = json.load(json_file)
#             print(jobs_data.get("data-analyst"))

print("-".join("driver".split()))