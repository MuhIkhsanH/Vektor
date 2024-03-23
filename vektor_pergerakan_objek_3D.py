import numpy as np


def pergerakan_objek(posisi_awal, kecepatan, waktu):
    posisi_baru = posisi_awal + kecepatan * waktu
    return posisi_baru

# Posisi awal objek
posisi_awal = np.array([0, 0, 0])

kecepatan = np.array([2, 5, 3])  

waktu = 1

# Hitung posisi baru objek setelah bergerak
posisi_baru = pergerakan_objek(posisi_awal, kecepatan, waktu)

print("Posisi baru objek:", posisi_baru)

