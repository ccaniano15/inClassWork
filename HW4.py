##############################################################
# Protected Division
#
# Math tells us that dividing any number by zero is
# impossible. When we try to do this in Python we get
# a ZeroDivisionError.
#
# Let's suppose that we need to define a new behavior
# for dividing by zero that does not throw an error. We
# can write a new function to do this.
#
# Let's call our function protected_dividion(n, d) and
# write it so that it takes 2 arguments.
#
# The first argument should be the numerator.
# The second argument should be the denominator.
#
# If the denominator is zero, the function should return zero.
# If the denominator is any number other than zero, it should return
# the numerator divided by the denominator.
# 

### START YOUR CODE ###
def protected_dividsion(n, d):
    if d == 0:
        return 0
    else:
        x = n/d
        return x

### END YOUR CODE ###

### BELOW IS TESTING CODE. DO NOT MODIFY ###
print("Testing protected_dividsion()")
print("Test: 10 / 2", end = "\t")
assert(protected_dividsion(10, 2) == 5.0)
print("PASSED")
print("Test: 0 / 10", end = "\t")
assert(protected_dividsion(0, 10) == 0.0)
print("PASSED")
print("Test: 3 / 0", end = "\t")
assert(protected_dividsion(3, 0) == 0.0)
print("PASSED")
print("Test: 7 / 2", end = "\t")
assert(protected_dividsion(7, 2) == 3.5)
print("PASSED")
print()
### ABOVE IS TESTING CODE. DO NOT MODIFY ###




##############################################################
# Word Count
# 
# This sentence has 5 words.
#
# Notice that the above sentence has 4 space characters. In fact,
# if we denote the number of space characters as s, we can say
# that every string has s + 1 words in it.
#
# We can write a function that will take a string as input, count
# the number of spaces, add 1, and return the resulting number.
#
# Let's call our function word_count()

### START YOUR CODE ###
words = 0
def word_count(sentence):
    s = 0
    global words
    x = len(sentence)
    i = 0
    while i <= x - 1:
        if sentence[i] == " ":
            s = s + 1
        i = i + 1
    words = s + 1
        
sentence = input("Type a sentence!")
word_count(sentence)
words = str(words)

print("there are " + words + " words!")

### END YOUR CODE ###

### BELOW IS TESTING CODE. DO NOT MODIFY ###
print("Testing protected_dividsion()")
print("Test: 'Hello world'", end = "\t\t")
assert(word_count('Hello world') == 2)
print("PASSED")
print("Test: 'The quick brown fox'", end = "\t")
assert(word_count('The quick brown fox') == 4)
print("PASSED")

print()
### ABOVE IS TESTING CODE. DO NOT MODIFY ###
