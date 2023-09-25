import json 
from datetime import datetime
from tweeterpy import TweeterPy

from gspread_dataframe import set_with_dataframe


import gspread

credentials = {
    "installed": {
        "client_id": "117044127800-dg6q9197854uc0g375ul2d7569d8v9mj.apps.googleusercontent.com",
        "project_id": "docs-382418",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "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",
        "redirect_uris": ["http://localhost"],
    }
}


# twitter = TweeterPy()
# twitter.get_liked_tweets('rngland')
# twitter.get_friends('rngland', following=True)


worksheet.format(f"g2:g{len(rest_ids)}", {
  "textFormat": {
    "fontSize": 14
   }
})


with open('liked_tweets.py', 'r') as file:
    file_contents = file.read()
my_dict = {}
exec(file_contents, my_dict)


rest_ids = []
for i in range(len(my_dict['liked']['data'])):
    if 'rest_id' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        rest_ids.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['rest_id'])


created_at = []
for i in range(len(my_dict['liked']['data'])):
    if 'legacy' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        created_at.append(datetime.strptime(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['created_at'], "%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d %H:%M:%S"))


result = []

for i in range(len(my_dict['liked']['data'])): 
    if 'legacy' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result'] and \
    len(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['urls']) >= 1:
        urls = my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['urls']
        expanded_urls = [p['expanded_url'] for p in urls]
        result.append('  '.join(expanded_urls))
    else:
        result.append((' '))


profile_images = []
for i in range(len(my_dict['liked']['data'])):
    if 'core' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        profile_images.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['profile_image_url_https'])
        
len(profile_images)
profile_images[0:3]


p_img = ["=IMAGE(\"" + profile_images[i] + "\"" + ',4 ,45, 45)'  for i in range(len(profile_images))]

p_img = [image.replace("'", "") for image in p_img]

p_img[0:3]


screen_names = []
for i in range(len(my_dict['liked']['data'])):
    if 'core' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        screen_names.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['screen_name'])


name = []
for i in range(len(my_dict['liked']['data'])):
    if 'core' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        name.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['name'])
# name       


profile_url =['https://twitter.com/' + i for i in screen_names]


full_text = []
for i in range(len(my_dict['liked']['data'])):
    if 'legacy' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        full_text.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])           


tweet_url =['https://twitter.com/' + screen_names[i] + '/status/' + rest_ids[i] for i in range(len(
screen_names))]


card_title = [p['value']['string_value'] for i in binding_values for p in i if p['key'] == 'title']

card_description = [p['value']['string_value'] for i in binding_values for p in i if p['key'] == 'description']

card_thumbnail_image= [p['value']['image_value']['url'] for i in binding_values for p in i if p['key'] == 'thumbnail_image']

card_photo_image_full_size_alt_text = [p['value']['string_value'] for i in binding_values for p in i if p['key'] == 'photo_image_full_size_alt_text']


fields = [
rest_ids,
created_at,
profile_url,
p_img,
screen_names,
full_text,
tweet_url,
result,
name,
card_title,
card_description,
card_thumbnail_image,
card_photo_image_full_size_alt_text
]

# def normalize_array_length():
#     if len(rest_ids) != len(result):
#         while len(result) > len(rest_ids) and result[-1] == ' ':
#             _ = result.pop()


len(rest_ids)
len(created_at)
len(profile_url)
len(p_img)
len(screen_names)
len(full_text)
len(tweet_url)
len(result)
len(name)
len(card_title)
len(card_description)
len(card_thumbnail_image)
len(card_photo_image_full_size_alt_text)


import pandas as pd

data = {
    "rest_ids" : rest_ids, 
    "created_at" : created_at, 
    "profile_url":profile_url, 
    "p_img" : p_img,    
    "screen_names" :screen_names,
    "name" : name, 
    "full_text": full_text, 
    "expanded_urls" : result, 
    "tweet_url": tweet_url
}
df = pd.DataFrame(data)
# df.to_csv('D:/Github/TweeterPy/liked_tweets.csv')


set_with_dataframe(worksheet, df) 





gc, authorized_user = gspread.oauth_from_dict(credentials)


sh = gc.open("liked_tweets")
worksheet  = sh.get_worksheet(0)    





print(my_dict['liked']['data'][8]['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])

urls = my_dict['liked']['data'][3]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['urls']

for i in urls:
    i['expanded_url']

# [i for i in urls['expanded_url']]

screen_name = my_dict['liked']['data'][0]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['screen_name']

rest_id = my_dict['liked']['data'][0]['content']['itemContent']['tweet_results']['result']['rest_id']

'https://twitter.com/' + screen_name + '/status/' + rest_id

screen_name
rest_id

print(my_dict['liked']['data'][0]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['description'])


my_dict['liked']['data'][0]['content']['itemContent']['tweet_results']['result']['legacy']['created_at']

#  'in_reply_to_screen_name': 'ryxcommar',
# 'in_reply_to_status_id_str': '1700002950012145747',

# my_dict['liked']['data'][0]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['is_blue_verified']

my_dict['liked']['data'][3]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['profile_image_url_https']


my_dict['liked']['data'][0]['content']['itemContent']['tweet_results']['result']['card']['legacy']['binding_values'][2]['value']['string_value']



# my_dict['liked']['data'][0]['content']['itemContent']['tweet_results']['result']['card']['legacy']['binding_values']

# my_dict['liked']['data'][3]['content']['itemContent']['tweet_results']['result']['card']['legacy']['binding_values'][4]
# my_dict['liked']['data'][3]['content']['itemContent']['tweet_results']['result']['card']['legacy']['binding_values'][0]['value']['string_value']


# card  
    #   {'key': 'title',
    #        'value': {'string_value': 'My solopreneur story: zero to $45K/mo in 2 years',
    #   {'key': 'description',
    #        'value': {'string_value': 'Today is exactly 2 years since I quit my job and become a full-time indie hacker.',
        #   {'key': 'photo_image_full_size_alt_text',
        #    'value': {'string_value': 'Search over large image datasets with natural language and computer vision! - GitHub - deepfates/memery: Search over large image datasets with natural language and computer vision!',
        #      {'key': 'thumbnail_image',
        #    'value': {'image_value': {'height': 200,
        #      'width': 400,
        #      'url': 'https://pbs.twimg.com/card_img/1704513029398745088/aRyYEIOj?format=jpg&name=400x400'},
        #     'type': 'IMAGE'}},
        ##card 

