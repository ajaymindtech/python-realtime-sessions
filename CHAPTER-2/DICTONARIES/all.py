# 1. Storing employee information
employee = { "name": "Ajay", "age": 30,"department": "IT","salary": 120000}
print("Employee info:", employee)

# 2. Counting word frequency in a sentence
sentence = "apple banana apple orange banana apple"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequency:", word_count)

# 3. Using OrderedDict to maintain insertion order
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['a'] = 1
print("OrderedDict:", ordered_dict)