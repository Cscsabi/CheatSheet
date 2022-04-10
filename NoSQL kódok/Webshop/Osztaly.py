# -*- coding: windows-1250 -*-
import redis
import uuid
from _datetime import datetime

class Osztaly():
        
    def __init__(self):
        redis_host='172.22.223.200'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, 
                           port=redis_port, 
                           decode_responses=True)
        
    def uj_felh(self, user, jelszo, email, nev, szul_dat):
        if self.r.sismember('felhasznalok', user):
            print('mar regisztralt')
            return
                
        self.r.hmset('felh_'+user, 
                     {'user':user, 
                      'jelszo':jelszo, 
                      'email':email, 
                      'nev':nev, 
                      'szul_dat':szul_dat})
        self.r.sadd('felhasznalok', user)
        
    def generate_token(self):
        return str(uuid.uuid4())
    
    def bejelentkezik(self, user, jelszo):
        if jelszo!=self.r.hget('felh_'+user, 'jelszo'):
            print('hibas jelszo')
            return 
        
        tok=self.generate_token()
        self.r.hset('tokenek', tok, user)
        self.kattint(tok)
        return tok
    
    def felh_torol_email(self, email):
        for i in self.r.smembers('felhasznalok'):
            if self.r.hget('felh_'+i, 'email')==email:
                self.r.delete('felh_'+i)
                self.r.delete('kosar_'+i)
                self.r.srem('felhasznalok', i)
                
    def fel_torol_nev(self, nev):
        self.r.delete('felh_'+nev)
        self.r.delete('kosar_'+nev)
        self.r.srem('felhasznalok', nev)
        
    def elfelejtett_jelszo(self, user):
        print(self.r.hget('felh_'+user,'jelszo'))
        
    def felh_lista(self):
        for i in self.r.smembers('felhasznalok'):
            print(self.r.hgetall('felh_'+i))
        
    def erv_tok(self, tok):
        return self.r.hexists('tokenek', tok)
    
    def tok_lista(self):
        print(self.r.hkeys('tokenek'))
        
    def kattint(self, tok):
        if self.erv_tok(tok):
            ido=datetime.now().strftime("%Y%m%d%H%M%S") 
            self.r.zadd('aktiv_tokenek', tok, ido)  
            
    def uj_cikk(self, cikk):
        self.r.sadd('cikkek', cikk)
        
    def cikk_lista(self):
        print(self.r.smembers('cikkek')) 
        
    def kosarba_tesz(self, tok, cikk, db):
        felh=self.r.hget('tokenek', tok)
        if felh==None:
            print('nincs bejelentkezve')
            return
        
        if not(self.r.sismember('cikkek', cikk)):
             print('nincs ilyen cikk')
             return 
         
        if db<0:
            print('ejnye')
            return
        if db==0:
            self.r.hdel('kosar_'+felh, cikk)
        else:
            self.r.hset('kosar_'+felh, cikk, db)
            
        self.kattint(tok)
        
    def kosar_lista(self, tok):
        felh=self.r.hget('tokenek', tok)
        if felh!=None:
            print(self.r.hgetall('kosar_'+felh))
            
    def megrendel(self, tok, cim, tel):
        felh=self.r.hget('tokenek', tok)
        if felh==None:
            print('nincs bejelentkezve')
            return 
        if not(self.r.exists('kosar_'+felh)):
            print('nincs kosar')
            return
       
        nev=self.r.hget('felh_'+felh, 'nev')
        js="{nev:"+nev+", cim:"+cim+", tel:"+tel+", cikkek:["
        for i in self.r.hkeys('kosar_'+felh):
            db=self.r.hget('kosar_'+felh, i)
            js=js+i+":"+db+","
        js=js[:-1]
        js=js+"]}"
        
        self.r.lpush('megrendelve', js)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        