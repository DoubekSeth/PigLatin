ay = "ay"
word = input('What do you want to translate: ')
word = str.lower(word)
newWord = ''
startWord = 0
endWord = 0
Sentence = []
newSentence = ''
for var in range(len(word)):
    letterList = [word[var]]
    spacePlace = letterList.count(' ')
    if spacePlace == 0:
        endWord += 1
    else:
        Sentence.append(word[startWord:endWord])
        startWord = endWord + 1
        endWord += 1
Sentence.append(word[startWord:endWord])
for var in range(len(Sentence)):
    newWord = str(Sentence[var])
    endingVowel = newWord[0]
    beginning = newWord[:3]
    ending = 0
    beginningNumber = []
    if 'a' in endingVowel:
        newSentence = newSentence + ' ' + newWord + "way"
    elif 'e' in endingVowel:
        newSentence = newSentence + ' ' + newWord + "way"
    elif 'i' in endingVowel:
        newSentence = newSentence + ' ' + newWord + "way"
    elif 'o' in endingVowel:
        newSentence = newSentence + ' ' + newWord + "way"
    elif 'u' in endingVowel:
        newSentence = newSentence + ' ' + newWord + "way"
    elif 'y' in endingVowel:
        newSentence = newSentence + ' ' + newWord + "way"
    else:
        for var in range(len(beginning)):
            endingVowel = word[var]
            beginningList = [beginning[var]]
            aPlace = beginningList.count('a')
            ePlace = beginningList.count('e')
            iPlace = beginningList.count('i')
            oPlace = beginningList.count('o')
            uPlace = beginningList.count('u')
            yPlace = beginningList.count('y')
            vowelCount = aPlace + ePlace + iPlace + oPlace + uPlace + yPlace
            if vowelCount == 1:
                beginningNumber.append('0')
            else:
                beginningNumber.append('1')
        if(beginningNumber == ['1','1','0']):
            ending = 2
            endingLetter = newWord[:2]
            newSentence = newSentence + ' '+ newWord[ending:] + endingLetter + ay
        elif(beginningNumber == ['1', '1', '1']):
            ending = 3
            endingLetter = newWord[:3]
            newSentence = newSentence + ' ' + newWord[ending:] + endingLetter + ay
        else:
            ending = 1
            endingLetter = newWord[0]
            newSentence = newSentence + ' ' + newWord[ending:] + endingLetter + ay
print(newSentence[1:])
