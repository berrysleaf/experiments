import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
rdcli = redis.Redis(connection_pool=pool)


