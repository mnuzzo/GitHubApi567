import requests
import json

def retrieve_github_info(userID):
    base_url = 'https://api.github.com/users/' + str(userID) + '/repos' 
    req = requests.get(base_url)
    print req.json()

if __name__ == '__main__':
    retrieve_github_info('mnuzzo567')