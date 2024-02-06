'''Ejercicio_1.pyYou are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.

'''
inputArray= [-1000, 0, -2, 0]
def solution(inputArray):
    pasos = 0
    for elemento in range(len(inputArray)-1):
        while inputArray[elemento] >= inputArray[elemento+1]:
            necesario = inputArray[elemento] - inputArray[elemento+1] + 1
            pasos += necesario
            inputArray[elemento+1] +=  necesario
    return pasos

solution(inputArray)