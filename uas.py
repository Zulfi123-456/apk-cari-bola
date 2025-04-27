import random

pesan_selamat_datang = "SELAMAT DATANG DI GAME TEBAK BOLA"
bola_posisi = random.randint(1, 4)

print("======================================")
print(f"=={pesan_selamat_datang}==")
print("======================================")

nama_user = input("masukan nama kamu : ")

print(f'''
Halo {nama_user} coba perhatikan kolom dibawah ini!
(_) (_) (_) (_)
''')

pilihan_user = int(input("Menurut kamu dikolom nomor berapa bola berada? [1 / 2 / 3 / 4] "))

print(f"pilihan kamu adalah kolom nomor {pilihan_user}")

if pilihan_user == bola_posisi:
    print(f"SELAMAT {nama_user} KAMU MENANG POSISI BOLA ADA DI KOLOM NOMOR {bola_posisi} dan PILIHAN MU ADALAH KOLOM NOMOR {pilihan_user}")
else :
    print(f"KAMU KALAH BOLA BUKAN BERADA DI KOLOM NOMOR {pilihan_user}, TAPI ADA DI KOLOM NOMOR {bola_posisi} SEDANGKAN PILIHAN KAMU ADALAH KOLOM NOMOR {pilihan_user}. SEMOGA BERUNTUNG DIKESEMPATAN SELANJUTNYA. TERIMA KASIH")