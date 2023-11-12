
from counting_sort import CountingSort
class StringManipulation():

    def __init__(self) -> None:
        pass

    
    def numVowels(self, input : str):

        if input is None:
            return 0

        vowels = {"a", "e", "i", "o", "u"}
        count = 0

        for s in input:
            if s.lower() in vowels:
                count += 1

        return count


    def reverse(self, string : str):
        return string[::-1]

    def reverseWords(self, string: str):
        string_array = string.split()
        string_array.reverse()
        return ' '.join(string_array)

    def isRotated(self, string1: str, string2: str):
        num_rotations = len(string1)

        for i in range(num_rotations):
            char = string1[0]
            string1 = string1[1:] + char

            if string1 == string2:
                return True

        return False


def removeDuplicates(string:str):
    chars = set()
    output_list = []
    for i in range(len(string)):
        if string[i] not in chars:
            chars.add(string[i])
            output_list.append(string[i])
    
    return ''.join(output_list)



def mostRepeatedChar(string : str):
    chars = {}

    for char in string:
        if char in chars:
            chars[char] += 1

        else:
            chars[char] = 0

    return max(chars)

def sentenceCapitalization(string : str):
    words = string.split()
    result = []

    for i in range(len(words)):

        result.append(words[i][0].upper() + words[i][1:].lower())

        # if i == 0 or (words[i - 1][-1] in {'.', '!', '?'}):
        #     word = words[i][0].upper() + words[i][1:].lower()

        # else:
        #     word = words[i].lower()

        #result.append(word)

    return ' '.join(result)


def isAnagram(string1 : str, string2: str):
    chars = {}
    
    for c in string1: 
        if c in chars:
            continue

        chars[c] = string1.count(c)

    for s in string2:
        if s not in chars or (string2.count(s) != chars[c]):
            return False

    return True


def isAnagramSort(string1 : str, string2: str):
    sorter = CountingSort()

    array1 = [ord(s) for s in string1]
    array2 = [ord(s1) for s1 in string2]

    return sorter.sort(array1) == sorter.sort(array2)



def isPalindrome(string1: str):

    return string1 == string1[::-1]


def isPalindromePoint(string1: str):

    start = 0
    end = len(string1) - 1

    while start < end:
        if string1[start] != string1[end]:
            return False

        start += 1
        end -= 1

    return True










        




    
    

def main():

    strings = StringManipulation()
    print(strings.numVowels("hEllo, world"))
    print(strings.reverse("hello"))
    print(strings.reverseWords("the sky is blue"))
    print(strings.isRotated('ABCD', 'DBAC'))
    print(removeDuplicates("hellooooo"))
    print(mostRepeatedChar("heloooooooooooo"))
    print(sentenceCapitalization('i am here!!! yay'))
    print(isAnagram("abcd", "acdbf"))
    print(isAnagramSort("abcd", "acdbf"))
    print(isPalindromePoint("abdbae"))


if __name__ == "__main__":
    main()