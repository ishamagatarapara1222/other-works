#3.1.5 Find the position of the word "AI" in the sentence:
'''
"Machine Learning and AI are trending".

Replace "AI" with "Artificial Intelligence".
Count how many times the word "data" appears in "data data mining and big data".
'''

sentence = "Machine Learning and AI are trending"

position = sentence.find("AI")
print("Position of AI:", position)

new_sentence = sentence.replace("AI", "Artificial Intelligence")
print("After replace:", new_sentence)

text = "data data mining and big data"
count = text.count("data")

print("Data count:", count)
