import re

# at least 2 vowels
expr1 = re.compile('.*[aeiou].*[aeiou].*[aeiou].*')

# at least 2 identical consecutive letters
expr2 = re.compile('.*(\\w)\\1.*')

# does not contain ab, cd, pq, xy
expr3 = re.compile('.*(:?ab|cd|pq|xy).*')

nice_words = 0

# contains pair of repeating letters, without overlapping
expr4 = re.compile('.*(\\w\\w).*\\1.*')

# contains repeating letter with exactly one ch between the repetitions
expr5 = re.compile('.*(\\w).{1}\\1.*')


nice_words = 0
# part 1
# reads line by line until encounters the word end
while True:
    word = raw_input()
    if word == "end":
        break
    if expr1.match(word) is not None and expr2.match(word) is not None and expr3.match(word) is None:
        nice_words += 1

print nice_words

nice_words = 0
# part 2
# reads line by line until encounters the word end
while True:
    word = raw_input()
    if word == "end":
        break
    if expr4.match(word) is not None and expr5.match(word) is not None:
        nice_words += 1

print nice_words



