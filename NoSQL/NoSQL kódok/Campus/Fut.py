# -*- coding: windows-1250 -*-
from CFOsztaly import COsztaly

rf=COsztaly()

# rf.uj_helyszin('Nagyerdo')
# rf.uj_helyszin('Viztorony')
# rf.uj_helyszin('Stadion')
# rf.uj_helyszin('DEIK sator')

rf.helyszin_lista()

#rf.uj_esemeny('Kassai', '202203171400', '202203171500', 
#              'Tankcsapda', 'Geza', '123')

# rf.uj_esemeny('Nagyerdo', '202203171400', '202203171500', 
#               'Tankcsapda', 'Geza', '123')
# rf.uj_esemeny('Nagyerdo', '202203171530', '202203171700', 
#               'Shakira', 'Anna', '124')
# rf.uj_esemeny('Nagyerdo', '202203171430', '202203171700', 
#               'HoneyBeast', 'Peti', '125')
# rf.uj_esemeny('Viztorony', '202203171430', '202203171520', 
#               'HoneyBeast', 'Peti', '125')

rf.esemeny_lista()
print()

#rf.esemeny_lista_idopont('202203171440')

# rf.uj_jegytipus('felnott', 20000, '202203140000', '202203210000')
# rf.uj_jegytipus('felnott_csutortok', 5000, '202203170000', 
#                 '202203180000')
# rf.uj_jegytipus('felnott_pentek', 5000, '202203180000', 
#                 '202203190000')
# rf.uj_jegytipus('gyerek_pentek', 2000, '202203180000', 
#                 '202203190000')
# rf.uj_jegytipus('gyerek_csutortok', 2000, '202203170000', 
#                 '202203180000')



rf.jegytipus_lista()

# rf.uj_vendeg('Anna', 'a@g.c', '20000101')
# rf.uj_vendeg('Cili', 'c@g.c', '20100101')
# rf.uj_vendeg('Bela', 'b@g.c', '20010101')
# rf.uj_vendeg('Denes', 'd@g.c', '20010101')

rf.vendeg_lista()
print()

# rf.vendeg_jegyet_vesz('c@g.c', 'gyerek_csutortok')
# rf.vendeg_jegyet_vesz('c@g.c', 'gyerek_pentek')
# rf.vendeg_jegyet_vesz('b@g.c', 'felnott_csutortok')
# rf.vendeg_jegyet_vesz('d@g.c', 'felnott')

rf.jegyvasarlasok()
print()

#rf.vendeg_idopont('202203171410')

rf.like('c@g.c', 'h_esemeny_1')
rf.like('c@g.c', 'h_esemeny_x')
rf.like('x@g.c', 'h_esemeny_1')
rf.like('c@g.c', 'h_esemeny_1')
rf.like('c@g.c', 'h_esemeny_2')
rf.like('c@g.c', 'h_esemeny_3')

rf.like('d@g.c', 'h_esemeny_2')


rf.vendeg_lajkjai('c@g.c')

rf.esemeny_lista_lajkkal()





