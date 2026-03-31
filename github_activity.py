import sys
import urllib
from urllib.request import urlopen
import json



if len(sys.argv) < 2:
    print("Please provide a username")
    sys.exit()

username = sys.argv[1]
url = f"https://api.github.com/users/{username}/events"
try:
    with urlopen(url) as response:
        html_content_bytes = response.read()

        html_content_string = html_content_bytes.decode('utf-8')

        events = json.loads(html_content_string)
        for event in events:
            event_type = event["type"]
            repo_name = event["repo"]["name"]

            if event_type == "PushEvent":
                print(f"Pushed commits to {repo_name}")
            elif event_type == "IssueCommentEvent":
                print(f"Commented on an issue in {repo_name}")
            elif event_type == "PullRequestEvent":
                print(f"Opened a pull request in {repo_name}")
            elif event_type == "IssuesEvent":
                print(f"Issue in {repo_name}")
            else:
                print(f"{event_type} in {repo_name}")



except urllib.error.HTTPError as e:
    if e.code == 404:
        print(f"User '{username}' not found. Please check the username.")
    else:
        print(f"An error occured: {e}")
except Exception as e:
    print(f"An error occured: {e}")


