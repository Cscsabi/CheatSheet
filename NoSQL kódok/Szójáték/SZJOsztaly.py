# -*- coding: windows-1250 -*-
import redis

class SZJOsztaly():
        
    def __init__(self):
        redis_host='172.22.223.200'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, 
                           port=redis_port, 
                           decode_responses=True)
        
    def get_alma(self):
        print(self.r.get('alma'))
        
    def uj_jatek(self, betu):
        for i in self.r.zrange('zutrang',0,-1, 
                               withscores=False):
            self.r.delete('s_'+i)
        
        self.r.delete('zutrang')
        self.r.setex('jatek',betu[0],60)
        
    def bekuld(self, jatekos, szo):
        if not(self.r.exists('jatek')):
            print('lejart')
            return
        if self.r.get('jatek')!=szo[0]:
            print('hibas kezdobetu')
            return 
        if self.r.sismember('s_'+jatekos, szo):
            print('mar volt')
            return 
        
        self.r.sadd('s_'+jatekos, szo)
        self.r.zincrby('zutrang', jatekos, 1)
        self.r.zincrby('zosszrang', jatekos, 1)
        
    def utolso_rangsor(self):
        print(self.r.zrevrange('zutrang',0,-1
                               , withscores=True))
        
    def ossz_rangsor(self):
        print(self.r.zrevrange('zosszrang',0,-1
                               , withscores=True))
        
        
        
            
        
        