word = input("Please enter the word: ")

word = word.lower()
wordList = list(word.strip())
resultList = []
uzz_added = False  # Flag to indicate if "uzz" has been added

blockers = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for i in range(len(wordList)):
    if uzz_added:
        break  # Stop processing if "uzz" has already been added
    elif wordList[i] == 'a' and (i + 1 >= len(wordList) or wordList[i + 1] not in blockers):
        resultList.append("uzz")
        uzz_added = True  # Set the flag to True
    elif wordList[i] in ['e', 'i', 'o', 'u']:
        resultList.append("uzz")
        uzz_added = True  # Set the flag to True
    else:
        resultList.append(wordList[i])
    
    # This part seems to be intended to remove the last 's' if it exists
    if wordList[len(wordList) - 1] == 's':
        wordList[len(wordList) - 1] = ''

result = ''.join(resultList)
print(result)
