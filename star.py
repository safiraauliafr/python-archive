# Membuat bintang
# *
# **
# ***



# array[0] = 0
# array[1] = 1
# array[2] = 2

# pake print
# 1
# 1
# 2

# Expected Result:
# 1
# 12
# 123

# inisialisasi panjang baris yang diinginkan
lengthRow = 4
# iterasi pertama untuk menentukan banyaknya baris
for row in range(lengthRow):
    row += 1
    # inisialisasi variable cetak agar menghindari break dari fungsi print()
    cetak = ""
    # inisialisasi panjang kolom yang akan di cetak
    lengthCol = row+1
    for col in range(1,lengthCol):
        # penambahan nilai kolom yang akan dicetak
        cetak += repr(col)

    # penambahan flag(tanda) sebelum variable dicetak
    cetak += repr("cetak")

    # cetak hasil yang diinginkan
    print(cetak)
