text = input("Enter a sentence: ").lower()
counts = {}
for word in text.split():
    word = word.strip(".,!?;:\"'()[]{}")
    if word: counts[word] = counts.get(word, 0) + 1
for word, count in counts.items(): print(word, ":", count)
