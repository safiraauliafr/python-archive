# for i in range(0,101):
#     print([i,"test","buzz","fizz","fizzbuzz"][2*(i%3==0) + (i%5==0)])

for i in range(1, 101): 
    print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i))

# that code looks more reasonable for me tho