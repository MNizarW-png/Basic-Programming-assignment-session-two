HargaPerLiter = 13000
JarakPerjalanan = 180
mod40 = JarakPerjalanan % 40
liter40 = (JarakPerjalanan - mod40) / 40
print (mod40,"(0.5)")
print (liter40, "Liter bensin")
print ("Total biaya bensin + 20km: ",HargaPerLiter * liter40 + (13000 * 0.5))