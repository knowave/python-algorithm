# 내 답안
def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x" "y", "z"]

    max_number = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        number = 0

        for char in string:
            if char == alphabet:
                number += 1

            if number > max_number:
                max_alphabet = alphabet
                max_number = number

    return max_alphabet

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

# 답안
def find_max_occurred_alphabet1(string):
    max_occurred = 0
    max_alphabet_index = 0

    alphabet_occurrence_array = find_alphabet_occurrence_array(string)

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurred:
            max_occurred = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))


def find_alphabet_occurrence_array(string):
    alphabet_occurred_array = [0] * 26

    for char in string:
        # char가 alphabet 즉, 문자인지 확인.
        if not char.isalpha():
            continue

        # 문자의 index를 아스키 코드를 이용해서 index 값을 가져옴.
        arr_index = ord(char) - ord('a')

        # 가져온 index를 이용해서 alphabet_occurred_array의 배열에 index를 +1
        alphabet_occurred_array[arr_index] += 1

    return alphabet_occurred_array

result = find_max_occurred_alphabet1
print("[답안] 정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("[답안] 정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("[답안] 정답 = b 현재 풀이 값 =", result("best of best youtube"))