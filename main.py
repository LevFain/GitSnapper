import json, requests, os, logging, datetime

if __name__ == '__main__':
    #GitPython
    try:
        from git import Repo
    except:
        os.system('pip install gitpython -q -q -q')

    #logging and datetime config
    logging.basicConfig(level="DEBUG",
                                format="[%(asctime)s] [%(levelname)s] %(message)s",
                                datefmt='%d/%m/%Y %H:%M:%S')
    now = datetime.datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    # setup owner name , access_token, and headers 
    owner=input('Owner name: ')
    access_token='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' 
    headers = {'Authorization':"Token "+access_token}

    repos=[]
    try:
    # to find all the repos' names from each page
        url=f"https://api.github.com/users/{owner}/repos" 
        repo=requests.get(url,headers=headers).json()
        repos.append(repo)
    except:
        repos.append(None)

    #write the data to a json file
    for name in repos:
        for repo in name:
            try:
                repoName = repo['name']
                with open(f'{repoName}.json', 'w') as file:
                    write= json.dumps(repo, indent=2)
                    file.writelines(write)
                    logging.info(f'All Data on the repositories are in the {repoName}.json file')
            except:
                pass

    #get repos name
    all_repo_names=[]
    for page in repos:
        for repo in page:
            try:
                all_repo_names.append(repo['full_name'].split("/")[1])
            except:
                pass

    #get links name
    all_repo_links=[]
    for link in repos:
        for repo in page:
            try:
                all_repo_links.append(repo['clone_url'])
            except:
                pass

    #clone git
    def cloneGit():
        dir = os.path.abspath('')
        for dirs, folders, files in os.walk(dir):
            if len(folders) == 0:
                for i in range(len(all_repo_names)):
                    os.makedirs(f'{all_repo_names[i]}')
                    path = dir+f'/{all_repo_names[i]}'
                    logging.info('Cloning Git ' +f'{all_repo_names[i]}')
                    Repo.clone_from(all_repo_links[i], path)

    logging.info(f'This Git has {len(all_repo_names)} repositories')
    for i in all_repo_names:
        logging.info(i)

    ans = input(f'[{current_time}]' + ' [INFO] Do you want to clone them? ')
    if ans.lower() == 'yes':
        cloneGit()
    else:
        logging.info('All Data on the repositories are in the Data.json file')