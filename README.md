
# coolsms-python
~Simple python library for korean SMS service provider CoolSMS(coolsms.co.kr)~

Not maintain anymore. Use official SDK instead. https://www.coolsms.co.kr/Python_SDK_Start_here


## Installation
```
pip install coolsms
```

## Basic Usage
```
from coolsms import Sender

# API key and secret from http://coolsms.co.kr/service_setup
API_KEY = 'N012340123401234'
API_SECRET = '01234012340123401234'
   
sender = Sender(API_KEY, API_SECRET)
sender.send(
    '01012341234',  # from
    '01043214321',  # to
    'Test Message'
)
```
