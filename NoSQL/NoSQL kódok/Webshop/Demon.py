# -*- coding: windows-1250 -*-
import redis
from _datetime import datetime
from time import sleep
from datetime import timedelta

redis_host='172.22.223.200'
redis_port=6379
               
r=redis.Redis(host=redis_host, port=redis_port,
              decode_responses=True)

while(True):
    sleep(10)
    ido=(datetime.now()-timedelta(minutes=1)).strftime("%Y%m%d%H%M%S")
    
    for i in r.zrangebyscore('aktiv_tokenek', 0, ido, 
                             withscores=False):
        r.hdel('tokenek', i)
        r.zrem('aktiv_tokenek', i)
        
    print(r.rpop('megrendelve'))