from requests import get
from time import sleep

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    response = get("https://api.github.com/users/osam7a/repos?sort=updated&direction=desc")
    repos = response.json()
    repos = [repo for repo in repos if repo["full_name"] not in ("osam7a/osam7a", "osam7a/alhennawi.tech") and not repo['archived'] and not repo['fork']][:8]
    for repo in repos:
        repo['source'] = repo['html_url']
        repo['image'] = f"https://opengraph.githubassets.com/1/{repo['full_name']}"
        sleep(0.1)

    return render(request, "index.html", {"projects": repos})