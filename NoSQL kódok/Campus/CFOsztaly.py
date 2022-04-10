# -*- coding: windows-1250 -*-
import redis

class COsztaly():
        
    def __init__(self):
        redis_host='172.22.223.200'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, 
                           port=redis_port, 
                           decode_responses=True)
        
    def uj_helyszin(self, helyszin):
        self.r.sadd('s_helyszinek',helyszin)
        
    def helyszin_lista(self):
        print(self.r.smembers('s_helyszinek'))
        
    def uj_esemeny(self, helyszin, kezdet, veg, megnevezes, 
                   felelos_nev, felelos_tel):
        if not(self.r.sismember('s_helyszinek', helyszin)):
            print('Nincs ilyen helyszin')
            return
        if kezdet>=veg:
            print('Hibas idointervallum')
            return 
        
        for i in self.r.zrange('z_esemenyek', 0,-1,
                               withscores=False):
            if helyszin==self.r.hget(i, 'helyszin'):
                if not(self.r.hget(i, 'veg')<kezdet or 
                       veg<=self.r.hget(i, 'kezdet')):
                    print('Mar vannak a szinpadon')
                    return 
        
        a=str(self.r.incr('esemeny_azon'))
        self.r.hmset('h_esemeny_'+a, 
                     {'helyszin':helyszin,
                      'kezdet':kezdet,
                      'veg':veg,
                      'megnevezes':megnevezes,
                      'felelos_nev':felelos_nev, 
                      'felelos_tel':felelos_tel})
        self.r.zadd('z_esemenyek','h_esemeny_'+a, kezdet)
        
        
    def esemeny_lista(self):
        for i in self.r.zrange('z_esemenyek',0,-1, 
                               withscores=False):
            print(i)
            print(self.r.hgetall(i))
            
    def esemeny_lista_idopont(self, idopont):
        for i in self.r.zrange('z_esemenyek',0,-1, 
                               withscores=False):
            if (self.r.hget(i,'kezdet')<=idopont
                and idopont<=self.r.hget(i,'veg')):
                print(self.r.hgetall(i))
                
    def uj_jegytipus(self, nev, ar, kezdet, veg):
        self.r.sadd('s_jegytipusok', nev)
        self.r.hmset('h_jegytipus_'+nev, 
                     {'nev':nev,
                      'ar':ar,
                      'ervenyesseg_kezdete':kezdet,
                      'ervenyesseg_vege':veg})
    
    def jegytipus_lista(self):
        for i in self.r.smembers('s_jegytipusok'):
            print(self.r.hgetall('h_jegytipus_'+i))
            
    def uj_vendeg(self, nev, email, szul_dat):
        self.r.sadd('s_vendegek', email)
        self.r.hmset('h_vendeg_'+email, 
                     {'nev':nev,
                      'email':email,
                      'szul_dat':szul_dat})
    
    def vendeg_lista(self):
        for i in self.r.smembers('s_vendegek'):
            print(self.r.hgetall('h_vendeg_'+i)) 
            
    def vendeg_jegyet_vesz(self, email, jegytipus_nev):
        if not(self.r.sismember('s_vendegek', email)):
            print('Nincs ilyen vendeg')
            return 
        if not(self.r.sismember('s_jegytipusok', jegytipus_nev)):
            print('Nincs ilyen jegytipus')
            return 
        self.r.sadd('s_vendeg_jegyei_'+email, jegytipus_nev)           
        
    def vendeg_jegyei(self, email):
        print(self.r.smembers('s_vendeg_jegyei_'+email))
        
    def jegyvasarlasok(self):
        for i in self.r.smembers('s_vendegek'):
            print(i)
            print(self.r.hget('h_vendeg_'+i, 'nev'))
            self.vendeg_jegyei(i)
            
    def vendeg_idopont(self, idopont):
        for i in self.r.smembers('s_vendegek'):
            for j in self.r.smembers('s_vendeg_jegyei_'+i):
                if (self.r.hget('h_jegytipus_'+j,'ervenyesseg_kezdete')<=idopont
                    and idopont<=self.r.hget('h_jegytipus_'+j,'ervenyesseg_vege')):
                    print(i)
                    print(self.r.hget('h_vendeg_'+i, 'nev'))
    
    def like(self, email, esemeny):
        if not(self.r.sismember('s_vendegek', email)):
            print('nincs ilyen vendeg')
            return 
        
        if self.r.zscore('z_esemenyek', esemeny)==None:
            print('nincs ilyen esemeny')
            return 
        
        if not(self.r.sismember('s_'+email+'_lajkjai', esemeny)):
            self.r.sadd('s_'+email+'_lajkjai', esemeny)
            self.r.zincrby('z_lajkok', esemeny,1)
            
    def esemeny_lista_lajkkal(self):
        print(self.r.zrevrange('z_lajkok', 0, -1, withscores=True))
        
    def vendeg_lajkjai(self, email):
        print(self.r.smembers('s_'+email+'_lajkjai'))
                
        
        
        
        
        
        
        
            
        
        
        
        
        
        
        
        