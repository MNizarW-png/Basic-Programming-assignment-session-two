jam = int(input("Masukkan jumlah jam kerja: "))
menit = int(input("Masukkan jumlah menit kerja: "))
upahperjam = float(input("Masukkan upah per jam (Rp): "))

totaljamdesimal = jam + (menit / 60)
totalbayaran = totaljamdesimal * upahperjam

print("Total jam: ", jam)
print("Total menit: ", menit)
print("Total waktu kerja: ", totaljamdesimal)
print("Total bayaran Anda: Rp.", totalbayaran)