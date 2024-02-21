from serpapi import GoogleSearch
import os
import json
import scratchattach as scratch3
from dotenv import load_dotenv

load_dotenv()
scratch_token = os.getenv('SCRATCH_TOKEN')
scratch_user = os.getenv('SCRATCH_USERNAME')
scratch_project = os.getenv('SCRATCH_PROJECT')
api_key = os.getenv('API_KEY')

session = scratch3.Session(scratch_token, username=scratch_user)
conn = session.connect_cloud(scratch_project)

client = scratch3.CloudRequests(conn)


@client.request
def ping():
    return "pong"

@client.request
def searches():
    search = GoogleSearch({"api_key": api_key})
    account = search.get_account()
    return account["plan_searches_left"]

@client.event
def on_ready():
    print("Request handler is running")

@client.request
def search(question, username):
    search = GoogleSearch({"api_key": api_key})
    account = search.get_account()

    if (account["plan_searches_left"] == 0):
        return "('Max Searches Reached!')"
    params = {
        "q": question,
        "hl": "en",
        "gl": "us",
        "google_domain": "google.com",
        "api_key": api_key
    }

    print(username + " searched " + question)
    print()

    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get('organic_results', [])

    results_list = []
    for result in organic_results[:10]:
        title = result.get('title', '')
        link = result.get('link', '')
        results_list.append((title, link))

    return results_list

client.run()