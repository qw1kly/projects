import redis
from config.redis.redis_config import redis_helper

rd_connection = redis.StrictRedis(
    host=redis_helper.HOST,
    port=redis_helper.PORT,
    password=redis_helper.PASSWORD,
    decode_responses=redis_helper.DECODE
)

