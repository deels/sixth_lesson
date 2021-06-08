# TODO: Task 1
#  Make a program that has some sentence (a string) on input and returns a dict containing all unique
#  words as keys and the number of occurrences as values.

text = input('Input text: ').lower()
count = dict()
words = str.split(text)

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
