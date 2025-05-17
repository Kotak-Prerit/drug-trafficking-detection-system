instagram_id=17841415193421434
import requests

access_token = "EAARUtomTexEBOz6mXzmnT4N0USwIj3NONvvHXXmuwOIniFeoJktn0KIR2CLDYanQR40CfZCFG4XjpjWkqpaOkYwrn1lPRC3HcJSFpbPcVY2ag6ZB3V3gMFIZCXhXTJqihZAwQE15PBIYiwiWJR7HHugGZAaJesZBE2laKDhxrTXEh9PhZB9wkLGaj1NgljpopfX15jvSuxPVlRuPbzI7AZDZD"
hashtag = "weed"

graph_url = 'https://graph.facebook.com/v20.0/'
def get_hashtag_id(hashtag = '',instagram_account_id = '',access_token = ''):
    url = graph_url + 'ig_hashtag_search'
    param = dict()
    param['user_id'] = instagram_account_id
    param['q'] = hashtag
    param['access_token'] = access_token
    response = requests.get(url,param)
    response = response.json()
    print(response)
    hashtag_id = response['data'][0]['id']
    return hashtag_id

hashtag_id = get_hashtag_id(hashtag, instagram_id, access_token)
print("Hashtag ID:", hashtag_id)
linl="17841562732114399/top_media?fields=id,media_type,comments_count,like_count,permalink&user_id=17841415193421434&pretty=0&limit=25"
url=graph_url+linl
param = dict()
param['access_token'] = access_token
response = requests.get(url,param)
response = response.json()
print(response)