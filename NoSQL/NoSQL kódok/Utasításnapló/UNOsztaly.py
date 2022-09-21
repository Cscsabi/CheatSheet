# -*- coding: windows-1250 -*-
import redis
import uuid
from _datetime import datetime

class UNOsztaly():
        
    def __init__(self):
        redis_host='172.22.223.200'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, 
                           port=redis_port, 
                           decode_responses=True)
        
    def uj_felh(self, nev, jelszo):
        if self.r.hexists('felhasznalok', nev):
            print('foglalt nev')
            return 
        self.r.hset('felhasznalok', nev, jelszo)
        
    def felhasznalo_lista(self):
        print(self.r.hkeys('felhasznalok'))
        
    def elfelejtett_jelszo(self, nev):
        print(self.r.hget('felhasznalok', nev))
        
    def bejelentkezes(self, nev, jelszo):
        if self.r.hget('felhasznalok', nev)!=jelszo:
            print('hibas jelszo')
            return 
        
        tok=self.generate_token()
        
        self.r.hset('tokenek', tok, nev)
        self.kattint(tok)
        return tok
        
    def generate_token(self):
        return str(uuid.uuid4())
    
    def erv_tok(self, tok):
        return self.r.hexists('tokenek', tok)
    
    def token_lista(self):
        print(self.r.hkeys('tokenek'))
        
    def kijelentkezik(self, tok):
        self.r.hdel('tokenek', tok)
        
    def utasitas(self, tok, ut):
        felh=self.r.hget('tokenek', tok)
        if felh!=None:
            self.r.lrem(felh+'_utasitasai', ut, 5)
            self.r.lpush(felh+'_utasitasai', ut)
            self.r.ltrim(felh+'_utasitasai', 0, 4)
            self.kattint(tok)
            
    def utasitas_lista(self, tok):
        felh=self.r.hget('tokenek', tok)
        if felh!=None:
            print(self.r.lrange(felh+'_utasitasai', 0, -1))
            self.kattint(tok)
            
    def kattint(self, tok):
        if self.erv_tok(tok):
            ido=datetime.now().strftime("%Y%m%d%H%M%S") 
            self.r.zadd('aktiv_tokenek', tok, ido)
            
    def ut_ajanl(self, tok, kb):
        felh=self.r.hget('tokenek', tok)
        if felh!=None:
            for i in self.r.lrange(felh+'_utasitasai', 0, -1):
                if kb[0]==i[0]:
                    print(i)
            
            
            
        
        
        
            
        
    