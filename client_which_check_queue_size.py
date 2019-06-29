import time
from core import QueryClient
import config

# python3 client_which_check_queue_size.py

if __name__ == '__main__':
    client = QueryClient(config.HOST, config.PORT, config.AUTHKEY).connect()
    while True:
        print('So data queue size is:', client.get_queue().qsize())
        time.sleep(5)
