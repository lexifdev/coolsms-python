import time
import hashlib
import hmac
import uuid
import requests


class Sender(object):
    _host = 'api.coolsms.co.kr'
    _version = '1'

    def __init__(self, key, secret):
        self._key = key
        self._secret = secret
        self._base_url = 'https://{host}/{version}/'.format(
            host=self._host,
            version=self._version
        )

    def _auth_info(self):
        timestamp = int(time.time())
        salt = str(uuid.uuid4())
        data = str(timestamp) + salt
        hash = hmac.new(self._secret, data, hashlib.md5)

        return timestamp, salt, hash.hexdigest()

    def send(self, sender, receiver, text):
        timestamp, salt, signature = self._auth_info()

        params = {
            'api_key': self._key,
            'timestamp': timestamp,
            'salt': salt,
            'signature': signature,

            'from': sender,
            'to': receiver,
            'text': text,
        }
        url = self._base_url + 'send'

        response = requests.post(url, data=params)

        return response.json()
