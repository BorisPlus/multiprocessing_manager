from core import QueryServer
import config

# python3 server.py

if __name__ == '__main__':
    QueryServer(config.HOST, config.PORT, config.AUTHKEY).serve_forever()
