from Osztaly import Osztaly
rf=Osztaly()

# rf.uj_dolg('a@g.c', 'anna')
# rf.uj_dolg('a@g.c', 'anna')
# rf.uj_dolg('b@g.c', 'bela')
# rf.uj_dolg('c@g.c', 'cili')
# rf.uj_dolg('d@g.c', 'denes')
# rf.uj_dolg('e@g.c', 'elek')
# rf.uj_dolg('f@g.c', 'elek')
# rf.uj_dolg('g@g.c', 'anna')

rf.dolgozo_lista()

#rf.dolgozo_nev('b@g.c')

#rf.dolgozok_email('elek')

fa1=rf.uj_feladat('c@g.c', 'takaritas', 3)
fa2=rf.uj_feladat('c@g.c', 'fozes', 5)
fa3=rf.uj_feladat('d@g.c', 'levinni a szemetet', 4)

rf.feladat_prioritas()

rf.feladathoz_dolgozo_rendel(fa1, 'a@g.c')
rf.feladathoz_dolgozo_rendel(fa1, 'b@g.c')
rf.feladathoz_dolgozo_rendel(fa1, 'd@g.c')

rf.feladathoz_dolgozo_rendel(fa2, 'd@g.c')
rf.feladathoz_dolgozo_rendel(fa2, 'e@g.c')

rf.feladathoz_dolgozo_rendel(fa3, 'e@g.c')
rf.feladathoz_dolgozo_rendel(fa3, 'g@g.c')

rf.feladathoz_dolgozo_rendel('-1', 'g@g.c')
rf.feladathoz_dolgozo_rendel(fa3, 'w@g.c')

rf.feladat_lehetseges_munkavegzoi(fa1)
print('**')
rf.feladat_lehetseges_munkavegzoi('-1')
print('**')

rf.feladat_leiras(fa1)
rf.feladat_leiras('-1')

rf.munkavegzes('e@g.c', fa1)
rf.munkavegzes('a@g.c', fa1)
rf.munkavegzes('a@g.c', '-1')
rf.munkavegzes('e@g.c', fa2)
rf.munkavegzes('e@g.c', fa3)

rf.feladat_prioritas()
print('**')
rf.dolgozok_elvegzett_lista()





















