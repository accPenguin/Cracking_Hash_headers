import json
import hashlib
import hmac


req_url = '/api/search/searchcount'
req_data = {
    'count': True,
    'filter': "{\"i\":[\"A\"],\"r\":[{\"pr\":\"GD\"},{\"pr\":\"CQ\"}]}"
}