from os import system, environ

def auth():
    print('Authenticating to GitHub.')
    try:
        system(f"echo {environ.get('GH_PAT')} | gh auth login --git-protocol https --hostname GitHub.com --with-token || exit 1")
    except:
        print("Failure authenticating to GitHub.")
