total_hari = int(input("Masukkan jumlah hari: "))

tahun = total_hari // 365
sisa_hari = total_hari % 365

bulan = sisa_hari // 30
hari = sisa_hari % 30

print("Hasil konversi:")
print("Tahun :", tahun)
print("Bulan :", bulan)
print("Hari  :", hari)