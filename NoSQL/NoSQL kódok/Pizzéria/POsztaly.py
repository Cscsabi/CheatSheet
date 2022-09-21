# -*- coding: windows-1250 -*-
import redis

class POsztaly():
        
    def __init__(self):
        redis_host='172.22.223.200'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, 
                           port=redis_port, 
                           decode_responses=True)
    
    #1, 3        
    def uj_pizza(self, nev, ar):
        self.r.hset('pizzak', nev, ar)
        
    def uj_feltet(self, pizza, feltet):
        if not(self.r.hexists('pizzak', pizza)):
            print('nincs ilyen pizza')
            return 
        
        self.r.sadd('feltet_'+pizza, feltet)
        
    def pizza_lista(self):
        #for i in self.r.hgetall('pizzak')
        for i in self.r.hkeys('pizzak'):
            print(i)
            print(self.r.hget('pizzak', i))
            print(self.r.smembers('feltet_'+i))
            
    def megrendeles(self, ido, cim):
        mra=str(self.r.incr('mra'))
        
        self.r.hmset('mr_'+mra,
                     {'ido':ido,
                      'cim':cim})
        self.r.sadd('megrendelesek', mra)
        return mra
        
    def megrendeles_pizza(self, mra, pizza, db):
        if not(self.r.sismember('megrendelesek', mra)):
            print('nincs ilyen megrendeles')
            return 
        
        for i in range(db):
            mrr=str(self.r.incr('mrr'))
            self.r.hmset('mrr_'+mrr,
                         {'mra':mra,
                          'pizza':pizza})
            
            self.r.sadd('mrreszletek_'+mra, mrr)
            
            self.r.rpush('sutnivalo', mrr)
    
    def sutnivalo_lista(self):
        for i in self.r.lrange('sutnivalo', 0, -1):
            print('mrr:'+i)
            print(self.r.hget('mrr_'+i, 'mra'))
            pizza=self.r.hget('mrr_'+i, 'pizza')
            print(pizza)
            print(self.r.smembers('feltet_'+pizza))
            
    def sutobe(self, mrr):
        if self.r.lrem('sutnivalo', mrr)==0:
            print('nincs mrr')
            return 
        self.r.rpush('suto', mrr)
        
    def suto_lista(self):
        for i in self.r.lrange('suto', 0, -1):
            print('mrr:'+i)
            print(self.r.hget('mrr_'+i, 'mra'))
            print(self.r.hget('mrr_'+i, 'pizza'))
            
    def kesz(self, mrr):
        if self.r.lrem('suto', mrr)==0:
            print('nincs mrr')
            return 
        self.r.rpush('kesz_pizzak', mrr)
        
        mra=self.r.hget('mrr_'+mrr, 'mra')
        
        kesz=True
        for i in self.r.lrange('sutnivalo', 0,-1):
            if mra==self.r.hget('mrr_'+i, 'mra'):
                kesz=False
                break
            
        for i in self.r.lrange('suto', 0,-1):
            if mra==self.r.hget('mrr_'+i, 'mra'):
                kesz=False
                break
            
        if kesz:
            self.r.rpush('kesz_megrendeles', mra)
            for i in self.r.smembers('mrreszletek_'+mra):
                self.r.lrem('kesz_pizzak', i)
                
    def kesz_megrendeles_lista(self):
        for i in self.r.lrange('kesz_megrendeles', 0, -1):
            print(i)
            print(self.r.hget('mr_'+i, 'cim'))
            for j in self.r.smembers('mrreszletek_'+i):
                print(self.r.hget('mrr_'+j, 'pizza'))
                
    def kiszallit(self, mra):
        if self.r.lrem('kesz_megrendeles', mra)==0:
            print('nincs ilyen mra')
            return
        
        for i in self.r.smembers('mrreszletek_'+mra):
            self.r.delete('mrr_'+i)
            
        self.r.delete('mrreszletek_'+mra)
        self.r.srem('megrendelesek', mra)
        self.r.delete('mr_'+mra)
    
        
        
        
        
        
        
        
        
            
            
            
    
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
        
        
        
        
        
        
            
    
    
    
    
    
        
        
        
        
        
        
