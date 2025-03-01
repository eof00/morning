from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
# start_date = os.environ['START_DATE']
city = os.environ['CITY']
# birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


def get_weather():
 url = "https://api.seniverse.com/v3/weather/daily.json?key=SIjoFrxMZmH7ilWpq&location="+ city+"&language=zh-Hans&unit=c&start=-1&days=1"
#   https://api.seniverse.com/v3/weather/daily.json?key=SIjoFrxMZmH7ilWpq&location=  CITY  &language=zh-Hans&unit=c&start=-1&days=1

  res = requests.get(url)
  data = res.json()["results"]

  weather = data[0]['now']
  return weather['text_day'], math.floor(weather['high'])

# def get_count():
#   delta = today - datetime.strptime(start_date, "%Y-%m-%d")
#   return delta.days

# def get_birthday():
#   next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
#   if next < datetime.now():
#     next = next.replace(year=next.year + 1)
#   return (next - today).days

# def get_words():
#   words = requests.get("https://api.shadiao.pro/chp")
#   if words.status_code != 200:
#     return get_words()
#   return words.json()['data']['text']

# def get_random_color():
#   return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature = get_weather()
data = {"weather":{"value":wea},"temperature":{"value":temperature}, "color":get_random_color()}
# "love_days":{"value":get_count()},"birthday_left":{"value":get_birthday()},"words":{"value":get_words(),
res = wm.send_template(user_id, template_id, data)
print(res)
