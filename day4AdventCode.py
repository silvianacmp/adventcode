import hashlib

number = 0
while True:
    h = hashlib.md5()
    h.update("iwrupvqb" + str(number))
    hashed = h.hexdigest()
    print hashed
    if hashed[0:6] == "000000":
        break
    number += 1

print number

