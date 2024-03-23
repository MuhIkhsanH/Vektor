import numpy as np

# Fungsi untuk menghitung posisi baru objek setelah bergerak dengan kecepatan tertentu
def pergerakan_objek(posisi_awal, kecepatan, waktu):
    posisi_baru = posisi_awal + kecepatan * waktu
    return posisi_baru

# Posisi awal objek
posisi_awal = np.array([0, 0])

# Kecepatan objek (vektor)
kecepatan = np.array([2, 5])

# Waktu bergerak (misalnya dalam detik)
waktu = 10

# Hitung posisi baru objek setelah bergerak
posisi_baru = pergerakan_objek(posisi_awal, kecepatan, waktu)

# Print posisi baru objek
print("Posisi baru objek:", posisi_baru)

