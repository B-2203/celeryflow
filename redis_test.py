import redis
r = redis.Redis(host='localhost', port=6379)

print(r.ping())  # Should print True if Redis is running
