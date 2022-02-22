year = 2000
    
if (year % 100 == 0) and (year % 400 == 0):
        print("True")
elif year % 4 == 0:
        print("True")
else:
        print("False")