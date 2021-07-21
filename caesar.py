vowels = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
VOWELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar(Word, sdvig):
    word_list = list(Word)
    for i in range(len(Word)):
        for j in range(len(vowels)):
            if word_list[i] == vowels[j]:
                secondSdvig = int(sdvig % len(vowels))
                if secondSdvig + j >= len(vowels):
                    word_list[i] = vowels[secondSdvig + j - len(vowels)]
                else:
                    word_list[i] = vowels[j + secondSdvig]
                break
            if word_list[i] == VOWELS[j]:
                secondSdvig = int(sdvig % len(VOWELS))
                if secondSdvig + j >= len(VOWELS):
                    word_list[i] = VOWELS[secondSdvig + j - len(VOWELS)]
                else:
                    word_list[i] = VOWELS[j + secondSdvig]
                break
    return ''.join(word_list)
