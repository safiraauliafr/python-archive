# cari panjang string terkecil
import re

input_str = "abcbcacab"

# cari faktor terkecil dari panjang string, dimana bukan 1 dan angka itu sendiri
def getAnagramPeriod(s):

    # Remove uppercase
    s = removingUpperCaseCharacters(s)

    n = len(s)

    if n < 1:
        return "string is invalid"
    if n > pow(10,5):
        return "string is invalid"

    # get factorial by n
    factorial = getFactorial(n)

    # get minimum factorial where not 1 and not itself
    minStringLength = factorial[1]

    return minStringLength

def getFactorial(n):
    factorial = []
    for i in range(1,n+1):
        if (n % i) == 0:
            factorial.append(i)
        continue
    # sort factorial ascending
    factorial.sort()
    return factorial


def removingUpperCaseCharacters(str):
    # Create a regular expression
    regex = "[A-Z]"

    # Replace every matched pattern
    # with the target string using
    # sub() method
    return (re.sub(regex, "", str))

print(getAnagramPeriod(input_str))

# 8
# 2 x 4 = 8
# 4 x 2 = 8
# 8 x 1 = 8
# cari nilai paling kecil dari kemungkinan perkalian, dimana angka tersebut bukan angka itu sendiri dan 1
# jawaban 2,1


# 6
# 2 x 3
# 3 x 2
# 1 x 6

# 9
# 3 x 3
# 1 x 9