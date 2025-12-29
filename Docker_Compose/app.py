# ═══════════════════════════════════════════════════════════════════
# FILE: app.py (Flask App with Redis)
# ═══════════════════════════════════════════════════════════════════

from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    return cache.incr('hits')

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello Krish! I have seen {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)