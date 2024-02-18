
sentence = "Python is easy and Python is powerful"

# Remove all duplicate words from the sentence
unique_words = ' '.join(sorted(set(sentence.split()), key=sentence.split().index))

# Display the result
print("Original Sentence:", sentence)
print("Sentence after removing duplicate words:", unique_words)
