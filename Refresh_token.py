import requests
import json


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
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        self.read_json_file()
        payload = "grant_type=refresh_token&refresh_token=" + self.refresh_token + self.callback_uri + "&client_id=" + self.client_id + "&client_secret=" + self.client_secret
        response = requests.request("POST", self.access_url, data=payload, headers=headers)
        return response.json().get("access_token")

    def read_json_file(self):

        with open(self.file_path) as json_file:
            data = json.load(json_file)
            env_values = data.get("values")
            for env_value in env_values:
                if env_value.get('key') == "client_id":
                    self.client_id = env_value.get('value')

                elif env_value.get('key') == "client_secret":
                    self.client_secret = env_value.get('value')

                elif env_value.get('key') == "refresher_token":
                    self.refresh_token = env_value.get('value')


auth_token = ObtainToken("C:\\Users\\fabian.tolgyi\\Desktop\\Postman_spotify_dudu\\Spotify_API.postman_environment_FABI.json").generate_auth_token()
print(auth_token)
