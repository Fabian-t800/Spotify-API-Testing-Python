import requests
def refreshed_token():
    url = "https://accounts.spotify.com/api/token"
    payload = "grant_type=refresh_token&refresh_token=AQC89kf_wxVAPheAVkoC-IXKosUJXvWZIgo23j7FFxWGgx5xgpnZfvwGlpJzjqho_TJKthKJgoOr2lSBEmf8OK0TRluuHdz5DjHX96aNAzs_1qRqYaftTeK1rAE4jQvUUfiZWQ&redirect_uri=https%3A%2F%2Fwww.getpostman.com%2Foauth2%2Fcallback&client_id=c8798a52d0cf490798e54b8790c431ba&client_secret=76fb7d7181124a4dbd619358f2659e7f"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'client_id': "",
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "0e942aa7-0f9d-4027-ad47-631a78ef0893,3543a2f1-988b-40ab-98a3-91205e301789",
        'Host': "accounts.spotify.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "573",
        'Cookie': "sp_t=ad1e04fa9c94f76b1b317f2050dbd925; sp_ab=%7B%222019_04_premium_menu%22%3A%22control%22%7D; spot=%7B%22t%22%3A1569849997%2C%22m%22%3A%22ro%22%2C%22p%22%3Anull%7D; _ga=GA1.2.1513823203.1569924574; sp_dc=AQAWeicDgkKjH4uouYETzSZIWtKjBY66wJbX709vr5iflVyCSpR1eqgoO5qgHcEl9FnJS0Ucd2ZFhrMLevdJZ4_weh7AhD1KN_rzc9Bzs9o; sp_key=6e4f97ba-f34e-4bc3-8407-30c9def5d58a; __Host-device_id=AQCjcK85msK6zgR-MIzzM2MBD4ax9vpdwTqH9OXOpQbcd99F0yJKe2mwPWLkdvOJ2d19fRjOZHNPJYrS9j3UNB4UWhKsEY6RvMY; inapptestgroup=; sp_ac=AQAESWw-JtpfIZ1JrRRbhGDYIgY2AgxJJkY0D1Oet39nyPAgga4m9OtYvYzwzdluXqnnhbaNzPXBYspzrCjBRmujFCzHmHQf3BJU4iCNqyH3arOeWXN_XK46XsGtAIvEzDP2l7BeWCNnbmCeS-DHFhZPPk2uDUpYiLtH2eBQgwZzHXkrrbkRDpJd0ccrYaWCxU84jCai2CI7nBhfLiKef2lAjQ6N3k79tyVB",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    response = response.json()
    auth_token = response.get("access_token")
    return auth_token



