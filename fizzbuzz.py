# for i in range(0,101):
#     print([i,"test","buzz","fizz","fizzbuzz"][2*(i%3==0) + (i%5==0)])
# array itu memiliki index, index bisa berupa angka atau huruf
# jika array memiliki index dengan angka itu dinamakan array numeric ex: def array[0] = "Safira"
# jika array memiliki index string maka dinamakan array assosiatif ex: def array["nama"] = "Safira"
# array = 0123456789 10

# array[0] = 1
# array[1] = 2
# array[2] = 3

for i in range(1, 10):
    print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i))


# that code looks more reasonable for me tho
# print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i))
# kelipatan 3 itu fizz
# syarat jika suatu bilangan dibagi 3 itu habis maka dia kelipatan 3, jika dia kelipatan 3 maka dia fizz
# kelipatan 5 itu buzz
# syarat jika suatu bilangan dibagi 5 itu habis maka dia kelipatan 5, jika dia kelipatan 5 maka dia buz