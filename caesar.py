vowels = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
VOWELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar(Word, shift):
    word_list = list(Word)
    for i in range(len(Word)):
        for j in range(len(vowels)):
            if word_list[i] == vowels[j]:
                secondShift = int(shift % len(vowels))
                if secondShift + j >= len(vowels):
                    word_list[i] = vowels[secondShift + j - len(vowels)]
                else:
                    word_list[i] = vowels[j + secondShift]
                break
            if word_list[i] == VOWELS[j]:
                secondShift = int(shift % len(VOWELS))
                if secondShift + j >= len(VOWELS):
                    word_list[i] = VOWELS[secondShift + j - len(VOWELS)]
                else:
                    word_list[i] = VOWELS[j + secondShift]
                break
    return ''.join(word_list)

