Panjang = 4
Lebar = 3
Tinggi = 3
LuasDinding = 2 * (Panjang * Tinggi) + 2 * (Lebar * Tinggi)
mod10 = LuasDinding % 10
Kaleng = (LuasDinding - mod10) / 10
print (LuasDinding, "Meter persegi")
print ("Sisa",mod10, "Meter persegi")
print ("Total kaleng dibutuhkan: ",Kaleng)