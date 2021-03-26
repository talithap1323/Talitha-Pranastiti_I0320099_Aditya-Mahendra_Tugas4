# berat bagasi maksimum
berat_maks = 50*0.453592
print("Berat Maksimal Bagasi adalah", berat_maks, "kg")
print("Berat Maks <= 22.6796 kg")
print ("==============================")

# berat > 110 kg
print("a. Berat > 110 kg")
berat_a = float(input("Masukkan berat > 110 kg: "))
if berat_a <= 22.6796:
    print(berat_a, "True")
else:
    print(berat_a, "False")

print("------------------------------")
# berat = 49 kg
print("b. Berat = 49 kg")
berat_b = float(49)
berat = berat_b <= 22.6796
print(berat_b, berat)
