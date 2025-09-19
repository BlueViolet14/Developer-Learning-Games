numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers = list(set(numbers))              # 중복 제거
numbers.sort()                             # 리스트를 오름차순으로 정렬
print(numbers)                             # 정렬된 리스트 출력

fruits = {"사과": 3, "바나나": 2, "체리": 5}

for key, value in fruits.items():
    print(key, value)

nums = [1, 2, 3, 4, 5]

squared = [x**2 for x in nums]
print(squared)