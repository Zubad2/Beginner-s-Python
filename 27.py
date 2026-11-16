# 27. Ask the user for a word and a number, then print the word that many times.
word = input("Enter a word: ")
times = int(input("How many times should it be printed? "))
for _ in range(times):
    print(word)
