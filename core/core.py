from multiprocessing.managers import BaseManager
from multiprocessing import Queue


class Manager:
    _manager = None

    def __init__(self, host, port, authkey):
        self._manager = BaseManager(address=(host, port), authkey=authkey)

    def register(self, *args, **kwargs):
        self._manager.register(*args, **kwargs)


class QueryServer(Manager):
    __queue = Queue()

    def __init__(self, host, port, authkey):
        super().__init__(host, port, authkey)
        self.register('get_queue', callable=lambda: self.__queue)
        self.register('push_to_queue', callable=self.push_to_queue)

    def push_to_queue(self, o):
        print('New data push:', o)
        self.__queue.put(o)

    def serve_forever(self):
        self._manager.get_server().serve_forever()
        return self


class QueryClient(Manager):
    def __init__(self, host, port, authkey):
        super().__init__(host, port, authkey)
        self.register('get_queue')
        self.register('push_to_queue')

    def push_to_queue(self, *args, **kwargs):
        self._manager.push_to_queue(*args, **kwargs)

    def get_queue(self, *args, **kwargs):
        return self._manager.get_queue(*args, **kwargs)

    def connect(self):
        self._manager.connect()
        return self
