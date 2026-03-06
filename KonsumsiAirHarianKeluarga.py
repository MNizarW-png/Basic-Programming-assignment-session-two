JumlahOrang = float(input("Masukan jumlah orang: "))
KebutuhanHarian = JumlahOrang * 2.5
KebutuhanMingguan = KebutuhanHarian * 7
mod19 = KebutuhanMingguan % 19
Galon = (KebutuhanMingguan - mod19) / 19
Biaya = Galon * 19000
print ("Kebutuhan air per minggu: ", KebutuhanMingguan)
print ("Galon yang dibutuhkan: ", Galon)
print ("Total biaya: ", Biaya)