import json
import hashlib
import hmac


req_url = '/api/search/searchcount'
req_data = {
    'count': True,
    'filter': "{\"i\":[\"A\"],\"r\":[{\"pr\":\"GD\"},{\"pr\":\"CQ\"}]}"
}

win_tid = '8b4ebc1e4a1b8c21235f34bf9db8f1a8'


def seeds_generator(s):
  seeds = {
    "0": "W",
    "1": "l",
    "2": "k",
    "3": "B",
    "4": "Q",
    "5": "g",
    "6": "f",
    "7": "i",
    "8": "i",
    "9": "r",
    "10": "v",
    "11": "6",
    "12": "A",
    "13": "K",
    "14": "N",
    "15": "k",
    "16": "4",
    "17": "L",
    "18": "1",
    "19": "8"
  }
  seeds_n = 20

  if not s:
    s = "/"
  s = s.lower()
  s = s + s

  res = ''
  for i in s:
      res += seeds[str(ord(i) % seeds_n)]
  return res


def a_default(url:str='/', data:object={}):
  url = url.lower()
  dataJson = json.dumps(data, ensure_ascii=False, separators=(',', ':')).lower()

  hash = hmac.new(
    bytes(seeds_generator(url), encoding='utf-8'),
    bytes(url+dataJson, encoding='utf-8'),
    hashlib.sha512
  ).hexdigest()
  return hash.lower()[8:28]

def r_default(url:str='/', data:object={}, tid:str=''):
  url = url.lower()
  dataJson = json.dumps(data, ensure_ascii=False, separators=(',', ':')).lower()

  payload = url+'pathString'+dataJson+tid
  key = seeds_generator(url)

  hash = hmac.new(
    bytes(key, encoding='utf-8'),
    bytes(payload, encoding='utf-8'),
    hashlib.sha512
  ).hexdigest()
  return hash.lower()

print('key: ' + a_default(req_url, req_data))
print('val: ' + r_default(req_url, req_data, win_tid))
