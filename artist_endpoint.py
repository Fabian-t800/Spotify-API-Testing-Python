import requests
import json
from Test import Refresh_token


class ArtistEndpoint:

    def __init__(self, oauth, env_var_path):
        self.oauth = oauth
        self.env_var_path = env_var_path
        self.art_id_1 = ""
        self.art_id_2 = ""
        self.inv_art_id = ""
        self.art_ids = ""
        self.read_env_vars()

    # read_env_vars: populates all relevant variables for the artist endpoint, from the environment variables .json
    def read_env_vars(self):
        with open(self.env_var_path) as json_file:
            data = json.load(json_file)
            env_values = data.get("values")
            for env_value in env_values:
                if env_value["key"] == "artist_id_1":
                    self.art_id_1 = env_value["value"]
                elif env_value["key"] == "artist_id_2":
                    self.art_id_2 = env_value["value"]
                elif env_value["key"] == "incorrect_artist_id":
                    self.inv_art_id = env_value["value"]
            self.art_ids = "ids=" + str(self.art_id_1) + "," + str(self.art_id_2)

    # get_artist: gets the artist
    # documentation url: https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/
    def get_artists(self):
        url = "https://api.spotify.com/v1/artists/" + self.art_id_1

        querystring = {"": ""}

        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)

        return response, response.json()

    # gets related artists for an artist
    # documentation url: https://developer.spotify.com/documentation/web-api/reference/artists/get-related-artists/
    def get_artist_related_artists(self):
        url = "https://api.spotify.com/v1/artists/" + self.art_id_1 + "/related-artists"
        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers)
        return response, response.json()

    # gets the artist's albums
    # documentation url: https://developer.spotify.com/documentation/web-api/reference/artists/get-artists-albums/
    def get_artist_albums(self):
        url = "https://api.spotify.com/v1/artists/" + self.art_id_1 + "/albums"
        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers)
        return response, response.json()

    # gets and artist's top tracks
    # documentation url: https://developer.spotify.com/documentation/web-api/reference/artists/get-artists-top-tracks/
    def get_artists_top_tracks(self):
        url = "https://api.spotify.com/v1/artists/" + self.art_id_1 + "/top-tracks"
        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        querystring = {"country": "RO"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response, response.json()

    # get Spotify catalog information for several artists based on their Spotify IDs.
    # documentation url: https://developer.spotify.com/documentation/web-api/reference/artists/get-several-artists/
    def get_several_artists(self):
        url = "https://api.spotify.com/v1/artists?" + str(self.art_ids)
        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        querystring = {"ids": "hE8S8ohRErocpkY7uJW4a,wWVKhxIU2cEi0K81v7HvP"}

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response, response.json()


# auth_token = generates the authentication token used for OAuth 2.0
auth_token = Refresh_token.ObtainToken("C:\\Users\\fabian.tolgyi\\Desktop\\Postman_spotify_dudu\\Spotify_API"
                                       ".postman_environment_FABI.json").generate_auth_token()
# json_path = path to the environment variables file
json_path = "D:\\Spotify_repo\\Spotify_Api_Testing\\Spotify_Api_Testing\\Environment " \
            "Variables\\Spotify_API_fabian.postman_environment.json "

ae1 = ArtistEndpoint(auth_token, json_path).get_artists()
print("Get artists test case returns: \n" + str(ae1))
ae2 = ArtistEndpoint(auth_token, json_path).get_artist_albums()
print("Get artist albums test case returns: \n" + str(ae2))
ae3 = ArtistEndpoint(auth_token, json_path).get_artist_related_artists()
print("Get artists related artists test case: \n" + str(ae3))
ae4 = ArtistEndpoint(auth_token, json_path).get_artists_top_tracks()
print("Get artists top tracks related test case: \n" + str(ae4))
ae5 = ArtistEndpoint(auth_token, json_path).get_several_artists()
print("Get several artists test case returns: \n" + str(ae5))
