# 내 방식
def find_max_num(arr):
    answer = 0

    for value in arr:
        if answer < value:
            answer = value

    return answer

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

# 답안
def find_max_num1(array):
    max_number = array[0]

    for number in array:
        if max_number < number:
            max_number = number

    return max_number

print("[답안] 정답 = 6 / 현재 풀이 값 = ", find_max_num1([3, 5, 6, 1, 2, 4]))
print("[답안] 정답 = 6 / 현재 풀이 값 = ", find_max_num1([6, 6, 6]))
print("[답안] 정답 = 6 / 현재 풀이 값 = ", find_max_num1([6, 9, 2, 7, 1888]))