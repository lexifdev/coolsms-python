import hashlib
import hmac
import secrets
import requests
from datetime import datetime


class Sender(object):
    def __init__(self, key, secret):
        self._key = key
        self._secret = secret

    def _auth_params(self):
        ts = int(datetime.now().timestamp())
        salt = secrets.token_hex(8)
        key = self._secret.encode('utf8')
        msg = '{}{}'.format(ts, salt).encode('utf8')
        sign = hmac.new(key, msg, hashlib.md5)
        return {
            'api_key': self._key,
            'timestamp': ts,
            'salt': salt,
            'signature': sign.hexdigest(),
        }

    def send(self, sender, receiver, text):
        if len(text.encode('euc-kr')) > 80:
            msg_type = 'LMS'
        else:
            msg_type = 'SMS'
        params = self._auth_params()
        params.update({
            'from': sender,
            'to': receiver,
            'text': text,
            'type': msg_type,
        })
        response = requests.post('https://api.coolsms.co.kr/sms/2/send', data=params)
        return response.json()
