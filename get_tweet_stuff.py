#!/usr/bin/env python
# coding: utf-8

# !pip install tweeterpy
# !pip install gspread_dataframe 


get_ipython().system('jupyter nbconvert --to script "D:/Github/TweeterPy/get_tweet_stuff.ipynb" --no-prompt')


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from IPython.display import Markdown


import json 
from datetime import datetime
import pandas as pd
# from tweeterpy import TweeterPy
#twitter password  =AJ#~Z+cBUR&7r/ 


# from gspread_dataframe import set_with_dataframe


# import gspread

# credentials = {
#     "installed": {
#         "client_id": "117044127800-dg6q9197854uc0g375ul2d7569d8v9mj.apps.googleusercontent.com",
#         "project_id": "docs-382418",
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_secret": "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",
#         "redirect_uris": ["http://localhost"],
#     }
# }


# gc, authorized_user = gspread.oauth_from_dict(credentials)


# twitter = TweeterPy()
# twitter.get_liked_tweets('rngland')
# twitter.get_friends('rngland', following=True)


with open('liked_tweets.py', 'r') as file:
    file_contents = file.read()
my_dict = {}
exec(file_contents, my_dict)


rest_ids = []
created_at = []
profile_images = []
screen_names = []
name = []
full_text = []
expanded_urls = []
binding_values = []


for i in range(len(my_dict['liked']['data'])):
    
    # rest_id
    if 'rest_id' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        rest_ids.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['rest_id'])
    
    # legacy
    # created_at
    if 'legacy' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        created_at.append(datetime.strptime(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['created_at'], "%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d %H:%M:%S")) 
        full_text.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']) 
    # expanded_urls 
        if len(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['urls']) >= 1:
            _1 = my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['urls']        
            _2 = [p['expanded_url'] for p in _1]
            expanded_urls.append('  '.join(_2))
        else:
            expanded_urls.append(' ')
        
    # core
    # profile_images    
    if 'core' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        profile_images.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['profile_image_url_https']) 
    # screen_names
        screen_names.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['screen_name'])
    # name   
        name.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['name'])
    # binding_values
        if 'card' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
            binding_values.append((my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['card']['legacy']['binding_values'],my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['rest_id']))  

    

p_img = ["=IMAGE(\"" + profile_images[i] + "\"" + ',4 ,45, 45)'  for i in range(len(profile_images))]

p_img = [image.replace("'", "") for image in p_img]

profile_url =['https://twitter.com/' + i for i in screen_names]

tweet_url =['https://twitter.com/' + screen_names[i] + '/status/' + rest_ids[i] for i in range(len(
screen_names))]


field_names = [
"rest_ids",
"created_at",
"profile_url",
"p_img",
"screen_names",
"name",
"full_text",
"expanded_urls",
"tweet_url",
# "card_title",
# "card_description",
# "card_thumbnail_image",
# "card_photo_image_full_size_alt_text"
]


data_dict = {field: eval(field) for field in field_names}
df = pd.DataFrame(data_dict)


card_title = [(p['value']['string_value'],i[1]) for i in binding_values for p in i[0] if p['key'] =='title']

card_description = [(p['value']['string_value'],i[1]) for i in binding_values for p in i[0] if p['key'] =='description']

card_thumbnail_image = [(p['value']['image_value']['url'],i[1]) for i in binding_values for p in i[0] if p['key'] =='thumbnail_image']

card_photo_image_full_size_alt_text = [(p['value']['string_value'],i[1]) for i in binding_values for p in i[0] if p['key'] =='photo_image_full_size_alt_text']

card_list = ["card_title", "card_description", "card_thumbnail_image", "card_photo_image_full_size_alt_text"]
card_dict = {card_type: eval(card_type) for card_type in card_list}


df.rest_ids = df.rest_ids.astype('int64')
dataframes = [pd.DataFrame(v, columns=[f"{k}", 'id']) for k, v in card_dict.items()]
dataframes = [df.astype({'id': 'int64'}) for df in dataframes]
dataframes = [df.set_index("id") for df in dataframes]
final_df = reduce(lambda x, y: pd.merge(x, y, left_on='rest_ids', how='left', right_index=True), dataframes, df)


[f"{i} :  {len(eval(i))}" for i in field_names]

final_df



# sh = gc.open("liked_tweets")

# worksheet  = sh.get_worksheet(0)    

# worksheet.format(f"g2:g{len(rest_ids)}", {
#   "textFormat": {
#     "fontSize": 14
#    }
# })
# set_with_dataframe(worksheet, df) 





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

