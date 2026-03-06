tagihan = float(input("Masukkan total tagihan: "))
orang = int(input("Masukkan jumlah orang: "))
        
pajak = tagihan * 0.10
totalakhir = tagihan + pajak
perorang = totalakhir / orang

print("-" * 35)
print("Total Tagihan       : Rp.", tagihan)
print("Pajak (10%)         : Rp.", pajak)
print("Total Keseluruhan   : Rp.", totalakhir)
print("Masing-masing bayar : Rp.", perorang)
print("-" * 35)