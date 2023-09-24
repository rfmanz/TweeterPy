import json 
from tweeterpy import TweeterPy




#twitter password  =AJ#~Z+cBUR&7r/ 





twitter = TweeterPy()


# twitter.get_liked_tweets('rngland')


# twitter.get_friends('rngland', following=True)


# with open("me.json", "w") as a:
#     json.dump(twitter.get_user_info('rngland'), a)


twitter.logged_in()


from liked_tweets import liked_tweets
liked_tweets = liked_tweets.locals()


with open('liked_tweets.py', 'r') as file:
    file_contents = file.read()


my_dict = {}
exec(file_contents, my_dict)


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from IPython.display import Markdown


len(my_dict['liked']['data'])


rest_ids = []
contains_rest_id = my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']
for i in range(len(my_dict['liked']['data'])):
    if 'rest_id' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        rest_ids.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['rest_id'])
    
rest_ids[0:10]


from datetime import datetime


created_at = []
for i in range(len(my_dict['liked']['data'])):
    if 'legacy' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        created_at.append(datetime.strptime(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['created_at'], "%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d %H:%M:%S"))
len(created_at)
created_at[0:10]


profile_images = []
for i in range(len(my_dict['liked']['data'])):
    if 'core' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        profile_images.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['profile_image_url_https'])
        
len(profile_images)
profile_images[0:10]


g_sheet_profile_images = ["=IMAGE(\"" + profile_images[i] + "\"" + ',4 ,45, 45)'  for i in range(len(profile_images))]

g_sheet_profile_images = [image.replace("'", "") for image in g_sheet_profile_images]

g_sheet_profile_images[0:10]





screen_names = []
for i in range(len(my_dict['liked']['data'])):
    if 'core' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        screen_names.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['screen_name'])
len(screen_names)
screen_names[0:10]


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


gc, authorized_user = gspread.oauth_from_dict(credentials)

sh = gc.open("liked_tweets")


get_ipython().system('pip install gspread_dataframe')


from gspread_dataframe import set_with_dataframe


worksheet  = sh.get_worksheet(0)


set_with_dataframe(worksheet, df) 


len((df.columns))


sh.add_worksheet(title='h', rows=len(df), cols=len((df.columns))).update(
    [df.columns.values.tolist()] + df.values.tolist()
)


worksheet_list = sh.worksheets()
worksheet_names = [i.title for i in worksheet_list]
worksheet_names


tweet_url =['https://twitter.com/' + screen_name[i] + '/status/' + rest_ids[i] for i in range(len(
screen_name))]


full_text = []
for i in range(len(my_dict['liked']['data'])):
    if 'legacy' in my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']:
        full_text.append(my_dict['liked']['data'][i]['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
len(full_text)
full_text[0:10]


import pandas as pd

# urls
data = {"rest_ids" : rest_ids, "created_at" : created_at,"g_sheet_profile_images" : g_sheet_profile_images ,"screen_names" :screen_names ,"full_text": full_text,"tweet_url": tweet_url}
df = pd.DataFrame(data)
# df.to_csv('D:/Github/TweeterPy/liked_tweets.csv')


df


# cards 

# each element in the list is
#  a dictionary. for each dictionary search for title, description, photo_image_full_size_alt_text, thumbnail_image and then get value, string_value and url for photo_image_full_size_alt_text

my_dict['liked']['data'][0]['content']['itemContent']['tweet_results']['result']['card']['legacy']['binding_values'][2]['value']['string_value']


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

