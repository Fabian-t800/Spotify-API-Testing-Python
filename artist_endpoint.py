import requests
import pprint
from Test import Refresh_token


class ArtistEndpoint:

    def __init__(self, oauth, artist_id):
        self.oauth = oauth
        self.artist_id = artist_id

    def get_artists(self):
        url = "https://api.spotify.com/v1/artists/" + self.artist_id

        querystring = {"": ""}

        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)

        return response, response.json()

    def get_artist_related_artists(self):
        url = "https://api.spotify.com/v1/artists/" + self.artist_id + "/related-artists"
        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers)
        return response, response.json()

    def get_artist_albums(self):
        url = "https://api.spotify.com/v1/artists/" + self.artist_id + "/albums"
        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers)
        return response, response.json()

    def get_artists_top_tracks(self):
        url = "https://api.spotify.com/v1/artists/" + self.artist_id + "/top-tracks"
        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        querystring = {"country": "RO"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response, response.json()

    def get_several_artists(self, artist_ids):
        url = "https://api.spotify.com/v1/artists/" + self.artist_id + "/albums"
        headers = {
            'Authorization': 'Bearer ' + self.oauth,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        querystring = {"ids": artist_ids}

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response, response.json()

#    def validation_get_artist(self, response_code = "Empty Response", response_body= "Empty response body"):
 #       response_code = self.get_artists()[0]
  #      response_body = self.get_artists()[1]
   #     print(response_code)

pp = pprint.PrettyPrinter(indent=4)
art_id = "6V3F8MZrOKdT9fU686ybE9"
artist_ids = ["6V3F8MZrOKdT9fU686ybE9", "11TplWqOPQBTmg2eiSLt1m", "3TOqt5oJwL9BE2NG9MEwDa"]
ae1 = ArtistEndpoint(Refresh_token.refreshed_token(), art_id).get_artists()
ae2 = ArtistEndpoint(Refresh_token.refreshed_token(), art_id).get_artist_related_artists()
ae3 = ArtistEndpoint(Refresh_token.refreshed_token(), art_id).get_artist_albums()
ae4 = ArtistEndpoint(Refresh_token.refreshed_token(), art_id).get_artists_top_tracks()
ae5 = ArtistEndpoint(Refresh_token.refreshed_token(), art_id).get_several_artists(artist_ids)


print(ae1)
