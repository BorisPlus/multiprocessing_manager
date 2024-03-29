# Query (Server, Client)

Simple example of sharing data between different processes by Python3 `multiprocessing`.

## Example

### Dispatcher (as server side)

Run server in terminal one:
```bash
python3 server.py
```

### Pusher (as first client side)

In terminal two run client, which push data to server queue:

```bash
python3 client_which_push.py
```

... you will see push process

```text
I push data: 0.197624408290772
I push data: 0.31292526915403995
I push data: 0.5516818968831353
```
... and you can check it in server (first) terminal

```text
New data push: 0.197624408290772
New data push: 0.31292526915403995
New data push: 0.5516818968831353
New data push: 0.4272762838375863
New data push: 0.7469592286185259
New data push: 0.9823676133264508
```

### Checker (as second client side)

In terminal three run client, which check size of server queue:

```bash
python3 client_which_check_queue_size.py
```

... you will see check process

```text
So data queue size is: 29
So data queue size is: 31
So data queue size is: 32
```

## Regards

Python3 https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager

## What is an idea

I wanna push task to queue server and run this tasks at some poll with various dynamic business logic.