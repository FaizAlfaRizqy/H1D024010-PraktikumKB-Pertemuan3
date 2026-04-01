# Nama : M. Umar Faiz Alfa Rizqy
# NIM : H1D024010
# Shift baru : E
# Shift lama : H

# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# variabel input
terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'terjual')           #range terjual = 0–40 unit
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')  #range permintaan = 0–100 %
harga = ctrl.Antecedent(np.arange(0, 100001, 1), 'harga')  #range harga = 0–100000  

# variabel output
profit = ctrl.Antecedent(np.arange(0, 4000001, 1), 'profit')    #range profit = 0–4000000
setok = ctrl.Consequent(np.arange(0, 1001, 1), 'setok')    #range setok = 0–100

# Suhu: dingin, normal, panas
terjual['rendah'] = fuzz.trimf(terjual.universe, [0, 0, 40 ]) #grafik terjual rendah = bentuk grafik trapesium, dengan titik-titik (0,0), (0,1), (40,1), (40,0)
terjual['sedang'] = fuzz.trimf(terjual.universe, [30, 50, 70]) #grafik terjual sedang = bentuk grafik segitiga, dengan titik-titik (30,0), (50,1), (70,0)
terjual['tinggi'] = fuzz.trimf(terjual.universe, [60, 100, 100]) #grafik terjual tinggi = bentuk grafik trapesium, dengan titik-titik (60,0), (80,1), (100,1), (100,0)

# Suhu: dingin, normal, panas
permintaan['rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100]) #grafik permintaan rendah = bentuk grafik trapesium, dengan titik-titik (0,0), (0,1), (100,1), (100,0)
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250]) #grafik permintaan sedang = bentuk grafik segitiga, dengan titik-titik (50,0), (150,1), (250,0)
permintaan['tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300]) #grafik permintaan tinggi = bentuk grafik trapesium, dengan titik-titik (200,0), (250,1), (300,1), (300,0)

# Suhu: dingin, normal, panas
harga['murah'] = fuzz.trimf(harga.universe, [0, 0, 40000]) #grafik harga rendah = bentuk grafik trapesium, dengan titik-titik (0,0), (0,1), (40000,1), (40000,0)
harga['sedang'] = fuzz.trimf(harga.universe, [30000, 50000, 80000]) #grafik harga sedang = bentuk grafik segitiga, dengan titik-titik (30000,0), (50000,1), (70000,0)
harga['mahal'] = fuzz.trimf(harga.universe, [60000, 100000, 100000]) #grafik harga tinggi = bentuk grafik trapesium, dengan titik-titik (6000₀,₀), (8₀₀₀₀,₁), (1₀₀₀₀₀,₁), (1₀₀₀₀₀,₀)

profit['rendah'] = fuzz.trimf(profit.universe, [0, 0, 1000000]) 
profit['sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 2500000]) #grafik profit sedang = bentuk grafik segitiga, dengan titik-titik (1000000,0), (2000000,1), (2500000,0)
profit['tinggi'] = fuzz.trapmf(profit.universe, [1500000, 2500000, 4000000, 4000000]) #grafik profit tinggi = bentuk grafik trapesium, dengan titik-titik (1500000,0), (2500000,1), (4000000,1), (4000000,0)

# Suhu: dingin, normal, panas
setok['sedang'] = fuzz.trimf(setok.universe, [100, 500, 900]) #grafik setok sedang = bentuk grafik trapesium, dengan titik-titik (0,0), (0,1), (40000,1), (40000,0)
setok['banyak'] = fuzz.trimf(setok.universe, [600, 1000, 1000]) #grafik setok banyak = bentuk grafik segitiga, dengan titik-titik (30000,0), (50000,1), (70000,0)

# Aturan Fuzzy
# 1) JJika Barang Terjual tinggi dan Permintaan tinggi dan Harga per Item murah dan Profit tinggi maka Stok Makanan banyak
aturan1 = ctrl.Rule(terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], setok['banyak'])
# 2) Jika Barang Terjual tinggi dan Permintaan tinggi dan Harga per Item murah dan Profit sedang maka Stok Makanan sedang
aturan2 = ctrl.Rule(terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], setok['sedang'])
# 3) Jika Barang Terjual tinggi dan Permintaan sedang dan Harga per Item murah dan Profit sedang maka Stok Makanan sedang
aturan3 = ctrl.Rule(terjual['tinggi'] & permintaan['sedang'] & harga['murah'] & profit['sedang'], setok['sedang'])
# 4) Jika Barang Terjual sedang dan Permintaan tinggi dan Harga per Item murah dan Profit sedang maka Stok Makanan sedang
aturan4 = ctrl.Rule(terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], setok['sedang'])
# 5) Jika Barang Terjual sedang dan Permintaan tinggi dan Harga per Item murah dan Profit tinggi maka Stok Makanan banyak
aturan5 = ctrl.Rule(terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], setok['banyak'])
# 6) Jika Barang Terjual rendah dan Permintaan rendah dan Harga per Item sedang dan Profit sedang maka Stok Makanan sedang
aturan6 = ctrl.Rule(terjual['rendah'] & permintaan['rendah'] & harga['sedang'] & profit['sedang'], setok['sedang'])


kipas_ctrl = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6]) #membuat mesin inferensi dengan memasukkan aturan-aturan yang telah dibuat
kipas_sim = ctrl.ControlSystemSimulation(kipas_ctrl) #membuat simulasi dengan memasukkan mesin inferensi yang telah dibuat

kipas_sim.input['terjual'] = 80        # input suhu (derajat Celcius)
kipas_sim.input['permintaan'] = 255  # input kelembapan (persen)
kipas_sim.input['harga'] = 25000  # input harga per item (rupiah)
kipas_sim.input['profit'] = 3500000  # input profit (rupiah)

kipas_sim.compute() #menghitung output

print("Kecepatan kipas =", kipas_sim.output['setok']) #menampilkan output kecepatan kipas
setok.view(sim=kipas_sim) #menampilkan grafik kecepatan kipas dengan input yang telah diberikan

input("Tekan ENTER untuk keluar...") #exit program setelah menampilkan hasil dan grafik