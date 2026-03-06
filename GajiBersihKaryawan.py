GajiPokok = 5000000
Tunjangan = 750000
BPJS = 0.02
Pajak = 0.05
GajiPotonganBPJS = (GajiPokok + Tunjangan) * BPJS
GajiPotonganPajak = (GajiPokok + Tunjangan) * Pajak
print ("Gaji bersih: ",(GajiPokok + Tunjangan) - GajiPotonganBPJS - GajiPotonganPajak)