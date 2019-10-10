import requests


class ObtainToken:
    access_url = "https://accounts.spotify.com/api/token"
    callback_uri = "&redirect_uri=https%3A%2F%2Fwww.getpostman.com%2Foauth2%2Fcallback"

    def __init__(self, file_path):
        self.file_path = file_path
        self.client_id = ""
        self.client_secret = ""
        self.refresh_token = ""

    def generate_auth_token(self):
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'client_id': "",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "accounts.spotify.com",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "573",
            'Cookie': "sp_t=ad1e04fa9c94f76b1b317f2050dbd925; sp_ab=%7B%222019_04_premium_menu%22%3A%22control%22%7D; spot=%7B%22t%22%3A1569849997%2C%22m%22%3A%22ro%22%2C%22p%22%3Anull%7D; _ga=GA1.2.1513823203.1569924574; sp_dc=AQAWeicDgkKjH4uouYETzSZIWtKjBY66wJbX709vr5iflVyCSpR1eqgoO5qgHcEl9FnJS0Ucd2ZFhrMLevdJZ4_weh7AhD1KN_rzc9Bzs9o; sp_key=6e4f97ba-f34e-4bc3-8407-30c9def5d58a; __Host-device_id=AQCjcK85msK6zgR-MIzzM2MBD4ax9vpdwTqH9OXOpQbcd99F0yJKe2mwPWLkdvOJ2d19fRjOZHNPJYrS9j3UNB4UWhKsEY6RvMY; inapptestgroup=; sp_ac=AQAESWw-JtpfIZ1JrRRbhGDYIgY2AgxJJkY0D1Oet39nyPAgga4m9OtYvYzwzdluXqnnhbaNzPXBYspzrCjBRmujFCzHmHQf3BJU4iCNqyH3arOeWXN_XK46XsGtAIvEzDP2l7BeWCNnbmCeS-DHFhZPPk2uDUpYiLtH2eBQgwZzHXkrrbkRDpJd0ccrYaWCxU84jCai2CI7nBhfLiKef2lAjQ6N3k79tyVB",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        self.read_json_file()
        payload = "grant_type=refresh_token&refresh_token=" + self.refresh_token + self.callback_uri + "&client_id=" + self.client_id + "&client_secret=" + self.client_secret
        response = requests.request("POST", self.access_url, data=payload, headers=headers)
        return response.json().get("access_token")

    def read_json_file(self):
        import json

        with open(self.file_path) as json_file:
            data = json.load(json_file)
            env_values = data.get("values")
            for i in range(0, len(env_values)):
                if env_values[i].get('key') == "client_id":
                    self.client_id = env_values[i].get('value')

                elif env_values[i].get('key') == "client_secret":
                    self.client_secret = env_values[i].get('value')

                elif env_values[i].get('key') == "refresher_token":
                    self.refresh_token = env_values[i].get('value')

q = ObtainToken("C:\\Users\\fabian.tolgyi\\Desktop\\Postman_spotify_dudu\\Spotify_API.postman_environment_FABI.json")
print(q.generate_auth_token())