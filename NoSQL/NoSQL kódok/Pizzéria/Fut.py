# -*- coding: windows-1250 -*-
from POsztaly import POsztaly
rf=POsztaly()

# rf.uj_pizza('songoku', 1800)
# rf.uj_pizza('hawaii', 2300)
# rf.uj_pizza('magyaros', 2800)
#
# rf.uj_feltet('songoku', 'sonka')
# rf.uj_feltet('songoku', 'gomba')
# rf.uj_feltet('songoku', 'kukorica')
#
# rf.uj_feltet('hawaii', 'ananasz')
# rf.uj_feltet('hawaii', 'sonka')
#
# rf.uj_feltet('magyaros', 'kolbasz')
# rf.uj_feltet('magyaros', 'szalonna')
# rf.uj_feltet('magyaros', 'hagyma')

rf.pizza_lista()

# mra1=rf.megrendeles('202204071430', 'Db Kassai 26 TEOKJ')
# rf.megrendeles_pizza(mra1, 'magyaros', 2)
# rf.megrendeles_pizza(mra1, 'songoku', 1)
#
# mra2=rf.megrendeles('202204071435', 'Laktanya u. 23')
# rf.megrendeles_pizza(mra2, 'hawaii', 1)
# rf.megrendeles_pizza(mra2, 'songoku', 1)

print('sutnivalo')
rf.sutnivalo_lista()

rf.sutobe('6')
rf.sutobe('7')
rf.sutobe('8')
rf.sutobe('9')


print('suto')
rf.suto_lista()

print('sutnivalo')
rf.sutnivalo_lista()


rf.kesz('6')
rf.kesz('7')
rf.kesz('8')
rf.kesz('9')

print('suto')
rf.suto_lista()

print('kesz')
rf.kesz_megrendeles_lista()

rf.kiszallit('3')


