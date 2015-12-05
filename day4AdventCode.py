import hashlib

number = 0
while True:
    h = hashlib.md5()
    h.update("iwrupvqb" + str(number))
    hashed = h.hexdigest()
    print hashed
    # for part 1, with 5 zeroes, must change index to 5
    # and string to contain 5 zeroes
    if hashed[0:6] == "000000":
        break
    number += 1

print number

