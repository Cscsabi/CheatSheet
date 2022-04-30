# -*- coding: windows-1250 -*-
import redis


class Osztaly():
        
    def __init__(self):
        redis_host='172.22.230.160'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, port=redis_port, 
                           decode_responses=True)
        
    def uj_dolg(self, email, nev):
        if self.r.hexists('dolgozok', email):
            print('mar van ilyen')
            return
        
        self.r.hset('dolgozok',email, nev)
        
    def dolgozo_nev(self, email):
        print(self.r.hget('dolgozok',email))
        
    def dolgozok_email(self, nev):
        for i in self.r.hkeys('dolgozok'):
            if self.r.hget('dolgozok', i)==nev:
                print(i)
                
    def uj_feladat(self, kiiro_email,leiras, prioritas):
        fa=str(self.r.incr('f_azon'))
        
        if not(self.r.hexists('dolgozok',kiiro_email)):
            print('nincs ilyen dolgozo')
            return 
        
        
        self.r.hmset('feladat_'+fa,
                     {'kiiro_email': kiiro_email,
                      'leiras':leiras})
        self.r.zadd('feladatok', fa, prioritas)
        return fa
    
    def feladathoz_dolgozo_rendel(self, f_azon, email):
        if not(self.r.hexists('dolgozok',email)):
            print('nincs ilyen dolgozo')
            return 
        
        if self.r.zscore('feladatok', f_azon)==None:
            print('nincs ilyen feladat')
            return 
        
        #if self.r.exists('feladat_'+f_azon)
        
        self.r.sadd('feladat_munkavegzoi_'+f_azon,email)
        
    def feladat_lehetseges_munkavegzoi(self, f_azon):
        for i in self.r.smembers('feladat_munkavegzoi_'+f_azon):
            print(i)
            print(self.r.hget('dolgozok', i))
            
    def feladat_prioritas(self):
        print(self.r.zrange('feladatok', 0, -1, withscores=True))
        
    def feladat_leiras(self, f_azon):
        print(self.r.hget('feladat_'+f_azon,'leiras'))
        
    def munkavegzes(self,email, f_azon):
        if not(self.r.sismember('feladat_munkavegzoi_'+f_azon, email)):
            print('nincs a dolgozo a lehetseges munkavegzok kozott')
            return
        
        self.r.zincrby('elvegzett_munka', email, 1)
        self.r.delete('feladat_munkavegzoi_'+f_azon)
        self.r.delete('feladat_'+f_azon)
        self.r.zrem('feladatok', f_azon)
        
    def dolgozok_elvegzett_lista(self):
        for i in self.r.zrevrange('elvegzett_munka', 0, -1, 
                                  withscores=False):
            print(i)
            print(self.r.zscore('elvegzett_munka', i))
            print(self.r.hget('dolgozok',i))
            
    def dolgozo_lista(self):
        print(self.r.hgetall('dolgozok'))
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        