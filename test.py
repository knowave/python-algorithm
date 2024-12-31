# 학생의 이름과 키가 서로 매핑이 되어 있음.

student_names = ["영희", "철수", "딩코", "코딩",]
student_heights = [166, 198, 188, 100]

# 학생의 키가 180 이상인 index를 반환.
def get_180_over_indexes(heights):
    result = []

    for i in range(len(heights)):
        height = heights[i]

        if height > 180:
            result.append(i)

    return result

# 키가 180 초과인 학생의 indexes를 반환.
over_indexes = get_180_over_indexes(student_heights)

# 키가 180 초과인 학생을 print를 이용해서 출력.
for i in over_indexes:
    print(student_names[i])