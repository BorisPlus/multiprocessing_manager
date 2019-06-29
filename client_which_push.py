import random
import time
from core import QueryClient
import config

# python3 client_which_push.py

if __name__ == '__main__':
    pusher = QueryClient(config.HOST, config.PORT, config.AUTHKEY).connect()
    while True:
        data = random.random()
        print('I push data:', data)
        pusher.push_to_queue(data)
        time.sleep(3)
