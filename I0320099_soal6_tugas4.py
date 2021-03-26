x = 4
y = 11
print("Nilai:", x, ",  Binary: ", format(x, '08b'))
print("Nilai:", y, ", Binary: ", format(y, '08b'))

print("\n======OR======")
a = x|y
print(x, "|", y)
print("Nilai:", a, ", Binary: ", format(a, '08b'))

print("\n======RIGHT SHIFT======")
b = x>>y
print(x, ">>", y)
print("Nilai:", b, ",  Binary: ", format(b, '08b'))

print("\n======XOR======")
c = x^y
print(x, "^", y)
print("Nilai:", c, ", Binary: ", format(c, '08b'))

print("\n======NOT======")
d = ~x
print("~", x)
print("Nilai:", d, ", Binary: ", format(d, '08b'))

print("\n======AND======")
e = y&x
print(y, "&", x)
print("Nilai:", e, ",  Binary: ", format(e, '08b'))
