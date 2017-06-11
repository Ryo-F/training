class User:
    def __init__(self, name, login_id, email, location, repos={}):
        self.name = name
        self.login_id = login_id
        self.email = email
        self.location = location
        self.repos = repos


class GitHubScraper(User):
    """docstring for GitHubScraper."""

    def __init__(self, url, user=0):
        self.url = url
        self.user = user

    def scrape_user_info(self):
        user_info = json.loads(requests.get(self.url).text)
        return user_info

    def scrape_repos(self):
        user_info = json.loads(requests.get(self.url).text)
        return json.loads(requests.get(user_info["repos_url"]).text)

    def get_user(self):
        user_info = json.loads(requests.get(self.url).text)
        self.user = User(user_info["name"],
                         user_info["login"],
                         user_info["email"],
                         user_info["location"],
                         json.loads(requests.get(user_info["repos_url"]).text))
        return self.user
