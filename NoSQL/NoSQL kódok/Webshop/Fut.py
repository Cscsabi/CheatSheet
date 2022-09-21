# -*- coding: windows-1250 -*-
from Osztaly import Osztaly


rf=Osztaly()

# rf.uj_felh('anna', 'ja', 'a@g.c', 'Anna C', 2000)
# rf.uj_felh('anna', 'ja2', 'a@g.c', 'Anna C2', 2000)
# rf.uj_felh('bela', 'jb', 'b@g.c', 'Bela B', 2000)
# rf.uj_felh('cili', 'jc', 'c@g.c', 'Cili F', 2000)
# rf.uj_felh('denes', 'jd', 'd@g.c', 'Denes D', 2000)
# rf.uj_felh('elek', 'je', 'e@g.c', 'Elek M', 2000)
#
# rf.felh_lista()
# print()
#
# rf.fel_torol_nev('elek')
# rf.felh_torol_email('d@g.c')
rf.felh_lista()

# rf.elfelejtett_jelszo('anna')

tok_a=rf.bejelentkezik('anna', 'ja')
# #tok_a2=rf.bejelentkezik('anna', 'ja2')
tok_a3=rf.bejelentkezik('anna', 'ja')
tok_b=rf.bejelentkezik('bela','jb')
tok_c=rf.bejelentkezik('cili','jc')


rf.tok_lista()

#print(rf.erv_tok(tok_a))

# rf.uj_cikk('alma')
# rf.uj_cikk('twix')
# rf.uj_cikk('kenyer')
# rf.uj_cikk('tv')
# rf.uj_cikk('eger')
# rf.uj_cikk('kortele')

rf.cikk_lista()


rf.kosarba_tesz(tok_a, 'alma', 10)
rf.kosarba_tesz(tok_a, 'alma', -2)
rf.kosarba_tesz(tok_a, 'twix', 5)
rf.kosarba_tesz(tok_a3, 'tv', 5)

rf.kosar_lista(tok_a)

rf.kosarba_tesz(tok_a3, 'tv', 0)

rf.kosar_lista(tok_a)

rf.kosarba_tesz(tok_c, 'alma', 10)
rf.kosarba_tesz(tok_c, 'kenyer', 2)
rf.kosarba_tesz(tok_c, 'eger', 5)
rf.kosarba_tesz(tok_c, 'tv', 5)

rf.kosar_lista(tok_c)

#rf.fel_torol_nev('bela')
rf.megrendel(tok_a, 'Db', '123')
rf.megrendel(tok_c, 'Bp', '124')