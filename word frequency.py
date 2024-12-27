def count_word_frequency(filename):
    word_frequency = {}
    file = open(filename, 'r')
    for line in file:
        words = line.split()
    for word in words:
        word = word.strip(",.?!")
        if word:
            word_frequency[word] = word_frequency.get(word, 0) + 1
    file.close()
print("Word Frequency:")
for word,frequency in word_frequency.items():
    print(f"{word}: {frequency}")
def main():
    filename = input("Enter the filename: ")
    count_word_frequency(filename)
if __name__ == "__main__":
    main()
