#memanggil file gempa dan import semua method/fungsi
from Gempa import *

#membuat objek gempa dengan argumen
Gempa1 = Gempa('Banten', 1.2)
Gempa2 = Gempa('Palu', 6.1)
Gempa3 = Gempa('Cianjur', 5.6)
Gempa4 = Gempa('Jayapura', 3.3)
Gempa5 = Gempa('Garut', 4.0)




#informasi gempa
print('## Info Gempa Geulis ##')
print()
Gempa1.dampak()

print('## Info Gempa Geulis ##')
print()
Gempa2.dampak()

print('## Info Gempa Geulis ##')
print()
Gempa3.dampak()

print('## Info Gempa Geulis ##')
print()
Gempa4.dampak()

print('## Info Gempa Geulis ##')
print()
Gempa5.dampak()