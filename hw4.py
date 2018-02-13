import requests
import json

def retrieve_github_info(userID):
    base_repo_url = 'https://api.github.com/users/' + str(userID) + '/repos' 
    repo_req = requests.get(base_repo_url, auth=('mnuzzo567','Nanoo96@SnoozeO14'))
    
    if repo_req.status_code != 200:
        print 'Error: Could Not Reach Endpoint'
    else:
        print repo_req.json()
        return repo_req


def parse_dat_json(rawRepoJSON):
    for repo in rawRepoJSON:
        for project in repo:
            print project["name"]


if __name__ == '__main__':
    temp = retrieve_github_info('mnuzzo567')
    parse_dat_json(temp)