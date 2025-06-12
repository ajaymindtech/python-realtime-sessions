from collections import defaultdict
word_count = defaultdict(int)
print("before word cout:",word_count) 
words = ["apple", "banana", "apple"]
for word in words:
    word_count[word] += 1
print("after word cout:",word_count)