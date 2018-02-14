import requests
import json

def retrieve_github_info(userID):
    base_repo_url = 'https://api.github.com/users/' + str(userID) + '/repos' 
    repo_req = requests.get(base_repo_url, auth=('mnuzzo567','Nanoo96@SnoozeO14'))
    
    if repo_req.status_code != 200:
        print 'Error: Could Not Reach Endpoint'
        return 'Error'
    else:
        return repo_req.json()

def retrieve_github_commit_info(project, userID):
    base_commit_url = 'https://api.github.com/repos/' + str(userID) + '/' + str(project) + '/commits'
    commit_req = requests.get(base_commit_url, auth=('mnuzzo567','Nanoo96@SnoozeO14'))

    if commit_req.status_code != 200:
        print 'Error: Could Not Reach Endpoint'
        return 'Error'
    else:
        return len(commit_req.json())

def parse_dat_json(rawRepoJSON, userID):
    i = 0
    j = 0
    projects = []
    commits = []
    
    while i < len(rawRepoJSON):
        projects.append(rawRepoJSON[i]["name"])
        i += 1
    
    while j < len(projects):
        commits.append(retrieve_github_commit_info(projects[j], userID))
        j += 1

    print 'User: ' + str(userID)
    for repo in projects:
        print 'Repo: ' + str(repo) + '  Number of commits: ' + str(commits[projects.index(repo)])


if __name__ == '__main__':
    temp = retrieve_github_info('mnuzzo567')
    parse_dat_json(temp, 'mnuzzo567')