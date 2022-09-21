# -*- coding: windows-1250 -*-
from UNOsztaly import UNOsztaly


rf=UNOsztaly()

# rf.uj_felh('anna', 'anna')
# rf.uj_felh('anna', 'geza')
# rf.uj_felh('bela', 'bela')
# rf.uj_felh('cili', 'cili')

rf.felhasznalo_lista()

tok_a1=rf.bejelentkezes('anna', 'anna')
tok_a2=rf.bejelentkezes('anna', 'anna')
# rf.bejelentkezes('anna', 'geza')
# rf.bejelentkezes('gabor', 'geza')
#tok_b=rf.bejelentkezes('bela', 'bela')

rf.token_lista()
#print(rf.erv_tok(tok_b))
#print(rf.erv_tok('abc'))

rf.utasitas(tok_a1, 'alma')
rf.utasitas(tok_a2, 'dio')
rf.utasitas(tok_a1, 'elefant')
rf.utasitas(tok_a2, 'alma')
rf.utasitas(tok_a2, 'eper')
rf.utasitas(tok_a1, 'elefant')
rf.utasitas(tok_a1, 'alma')
rf.utasitas(tok_a1, 'dio')
rf.utasitas(tok_a1, 'elefant')
rf.utasitas(tok_a1, 'malna')

rf.utasitas_lista(tok_a1)

rf.ut_ajanl(tok_a1, 'e')

#
# rf.utasitas(tok_b, 'delfin')
# rf.utasitas(tok_b, 'balna')
# rf.utasitas(tok_b, 'bigyo')
# rf.utasitas(tok_b, 'banan')
# rf.utasitas(tok_b, 'alma')
# rf.utasitas(tok_b, 'eper')

# rf.utasitas_lista(tok_a1)
# rf.utasitas_lista(tok_a2)
# rf.utasitas_lista(tok_b)
#
#
# rf.kijelentkezik(tok_b)
# rf.kijelentkezik(tok_a1)
# rf.kijelentkezik(tok_a2)

rf.token_lista()


