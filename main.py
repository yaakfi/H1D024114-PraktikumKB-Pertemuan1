import random
from datetime import datetime

score_history = []

print("=== Game Tebak Angka ===")
nama = input("Masukkan nama kamu: ")

sekarang = datetime.now()
print("Waktu bermain:", sekarang.strftime("%d-%m-%Y %H:%M:%S"))

angka_rahasia = random.randint(1, 10)

percobaan = 0
tebakan = 0

while tebakan != angka_rahasia:
    tebakan = int(input("Tebak angka dari 1 - 10: "))
    percobaan += 1
    
    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print("Benar! Kamu menebak dalam", percobaan, "percobaan")

score_history.append((nama, percobaan))

print("\n=== Riwayat Skor ===")
for data in score_history:
    print("Nama:", data[0], "| Percobaan:", data[1])
