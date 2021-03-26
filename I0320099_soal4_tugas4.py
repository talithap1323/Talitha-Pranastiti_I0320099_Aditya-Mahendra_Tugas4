print("PENDAFTARAN KURSUS ONLINE")
print("==========================")
print("Syarat:"
      "\n minimal 21 tahun"
      "\n lulus ujian kualifikasi \n")

umur = float(input("Berapa usia kamu? "))
bolehumur = umur >= 21

print("## isi 1 jika ya, isi 0 jika tidak ##")
ujian = int(input("Apakah Anda sudah lulus ujian kualifikasi (Y(1) / T(0))? "))
bolehujian = ujian == True

print("--------------------------")
hasil = bolehumur and bolehujian

if hasil == True:
    print("Anda dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")

