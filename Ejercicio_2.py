'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''

def solution(inputString):
    maximo = 0
    if len(inputString) <= 1:
        return False
    for letra in inputString:
        if inputString.count(letra)%2!=0 and len(inputString)%2 == 0:
            return False
        elif inputString.count(letra)%2!=0 and len(inputString)%2 == 1:
            maximo += 1
        if maximo>1:
            return False
        inputString =  [caracter for caracter in inputString if caracter != letra]
    else:
        return True