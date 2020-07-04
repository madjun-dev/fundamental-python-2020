"""
Tipe data dictionary sekedar menghubungkan KEY dan VALUE
KVP=Key Value Pair
"""
kamus_ind_eng= {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['istri'])
print(kamus_ind_eng['ibu'])

print('\ndata ini dikirim oleh server gojek, untuk memberikan info driver di sekitar pemakai aplkasi')
data_dari_server_gojek={
    'tanggal':'2020-07-04',
    'driver_list':[
        {'nama':'Eka','jarak':10},
        {'nama':'Dwi','jarak':50},
        {'nama':'Tri','jarak':100},
        {'nama':'Catur','jarak':1000}]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"jarak Driver terdekat {data_dari_server_gojek['driver_list'][0]['jarak']} meter")

