import random
import time
import string

nolist = ["no", "n", "nope", "nah", "ne","nay","never"]
yeslist = ["yes", "y", "yer", "yeah","yessir","ye","okay","yep","yea","ok","k","yh","sure"]


amount = int(input("How many passwords do you need?: "))
length = int(input("How long do you need your password?: "))
caps = input("Do you need the first letter to be capital?: ")
sym = input("Do you need to have a symbol?:" )

def password():
    for i in range(amount):
        if caps in yeslist and sym in yeslist:
            a = ''.join(random.choice(string.ascii_uppercase))
            b = ''.join(random.choice(string.punctuation))
            c = ''.join(random.choice(string.ascii_letters)for x in range(length))
            print("Your password is {}{}{}".format(a,b,c))

        elif caps in yeslist and sym in nolist:
            a = ''.join(random.choice(string.ascii_uppercase))
            c = ''.join(random.choice(string.ascii_letters)for x in range(length))
            print("Your password is {}{}".format(a,c))
        elif caps in nolist and sym in yeslist:

            b = ''.join(random.choice(string.punctuation))
            c = ''.join(random.choice(string.ascii_letters)for x in range(length))
            print("Your password is {}{}".format(b,c))

        elif caps in nolist and sym in nolist:
            c = ''.join(random.choice(string.ascii_letters)for x in range(length))
            print("Your password is {}".format(c))

    restart = input("Do you want to restart?: ")
    if restart in yeslist:
        password()
    else:
        exit()
password()



