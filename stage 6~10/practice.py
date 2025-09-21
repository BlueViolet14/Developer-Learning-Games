# 함수 / 모듈 / 파일 I/O / 예외

# 1. 함수
# 1) 함수의 정의와 호출
# def 함수이름(매개변수):
#     실행문1
#     실행문2
#     return 반환값
# 함수이름(인수)
# 예시
def add(a, b):
    return a + b
result = add(3, 4)
print(result)  # 7
# 2) 매개변수와 인수
# 매개변수: 함수 정의 시 함수 이름 옆에 지정하는 변수
# 인수: 함수 호출 시 함수 이름 옆에 지정하는 값
# 3) 반환값
# return 키워드를 사용하여 함수에서 값을 반환
# 반환값이 없는 경우 None을 반환
# 4) 기본 매개변수
def greet(name, message="Hello"):
    return f"{message}, {name}!"
print(greet("Alice"))          # Hello, Alice!
print(greet("Bob", "Hi"))      # Hi, Bob!
# 5) 가변 매개변수
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3))        # 6
print(sum_all(4, 5, 6, 7, 8))  # 30
# 6) 키워드 매개변수
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
introduce(name="Alice", age=30, city="New York")
# name: Alice age: 30 city: New York
# 7) 람다 함수
square = lambda x: x * x
print(square(5))  # 25
# 8) 재귀 함수
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # 120

# 2. 모듈
# 1) 모듈의 정의와 사용
# 모듈: 관련된 함수, 클래스, 변수 등을 하나의 파일로 묶은 것
# import 모듈이름
# from 모듈이름 import 함수이름
# 2) 표준 라이브러리
import math
print(math.sqrt(16))  # 4.0
import random
print(random.randint(1, 10))  # 1부터 10 사이의 랜덤한 정수
# 3) 외부 라이브러리
# pip install 라이브러리이름

# 3. 파일 I/O
# 1) 파일 열기와 닫기
# open(파일이름, 모드)
# 모드: 'r' (읽기), 'w' (쓰기), 'a' (추가), 'b' (바이너리)
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()
# 2) 파일 읽기
file = open("example.txt", "r")
content = file.read()
print(content)  # Hello, World!
file.close()
# 3) with 문을 사용한 파일 처리
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Hello, World!
# 파일이 자동으로 닫힘
# 4) 파일의 여러 줄 읽기
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
# 5) 파일에 여러 줄 쓰기
with open("example.txt", "w") as file:
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
# 6) CSV 파일 처리
import csv
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# 7) JSON 파일 처리
import json
data = {"name": "Alice", "age": 30, "city": "New York"}
with open("data.json", "w") as file:
    json.dump(data, file)
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
# 8) 바이너리 파일 처리
with open("example.bin", "wb") as file:
    file.write(b'\x00\xFF\x7A\x3C')
with open("example.bin", "rb") as file:
    content = file.read()
    print(content)  # b'\x00\xffz<'
# 9) 파일 경로 다루기
import os
file_path = os.path.join("folder", "subfolder", "file.txt")
print(file_path)  # folder/subfolder/file.txt (운영체제에 따라 다름)
# 10) 디렉토리 다루기
import os
os.makedirs("new_folder/subfolder", exist_ok=True)
print(os.listdir("new_folder"))  # ['subfolder']
os.rmdir("new_folder/subfolder")
os.rmdir("new_folder")
# 11) 파일 존재 여부 확인
import os
print(os.path.exists("example.txt"))  # True
print(os.path.isfile("example.txt"))  # True
print(os.path.isdir("example.txt"))   # False
# 12) 파일 복사와 이동
import shutil
shutil.copy("example.txt", "example_copy.txt")
shutil.move("example_copy.txt", "new_folder/example_moved.txt")
# 13) 파일 삭제
import os
os.remove("example.txt")
os.remove("new_folder/example_moved.txt")
os.rmdir("new_folder")

# 4. 예외 처리
# 1) 예외의 정의와 처리
# try:
#     실행문1
#     실행문2
# except 예외종류1:
#     예외처리1
# except 예외종류2:
#     예외처리2
# else:
#     예외가 발생하지 않았을 때 실행
# finally:
#     항상 실행
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("나눗셈 성공:", result)
finally:
    print("프로그램 종료")
# 2) 여러 예외 처리
try:
    num = int(input("숫자를 입력하세요: "))
    result = 10 / num
except ValueError:
    print("유효한 숫자를 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("나눗셈 성공:", result)
finally:
    print("프로그램 종료")
# 3) 예외 발생시키기
def check_positive(number):
    if number < 0:
        raise ValueError("음수는 허용되지 않습니다.")
    return number
try:
    check_positive(-5)
except ValueError as e:
    print(e)  # 음수는 허용되지 않습니다.
# 4) 사용자 정의 예외
class CustomError(Exception):
    pass
def do_something(value):
    if value < 0:
        raise CustomError("음수는 허용되지 않습니다.")
try:
    do_something(-10)
except CustomError as e:
    print(e)  # 음수는 허용되지 않습니다.
# 5) 예외 정보 얻기
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("예외 발생:", e)  # 예외 발생: division by zero
    print("예외 종류:", type(e))  # 예외 종류: <class 'ZeroDivisionError'>
    import traceback
    traceback.print_exc()
# 6) assert 문
def divide(a, b):
    assert b != 0, "0으로 나눌 수 없습니다."
    return a / b
try:
    divide(10, 0)
except AssertionError as e:
    print(e)  # 0으로 나눌 수 없습니다.
# 7) with 문과 예외 처리
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다:", e)  # 파일을 찾을 수 없습니다: [Errno 2] No such file or directory: 'non_existent_file.txt'
# 8) 예외 전환
class LowLevelError(Exception):
    pass
class HighLevelError(Exception):
    pass
def low_level_function():
    raise LowLevelError("저수준 오류 발생")
def high_level_function():
    try:
        low_level_function()
    except LowLevelError as e:
        raise HighLevelError("고수준 오류 발생") from e
try:
    high_level_function()
except HighLevelError as e:
    print(e)  # 고수준 오류 발생
    print("원인:", e.__cause__)  # 원인: 저수준 오류 발생
# 9) 예외 무시하기
try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # 예외 무시
print("프로그램 계속 실행")
# 10) 디버깅과 로깅
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("디버그 메시지")
logging.info("정보 메시지")
logging.warning("경고 메시지")
logging.error("오류 메시지")
logging.critical("치명적 메시지")
# 연습문제
# 1. 함수 연습문제
# 1) 두 수를 입력받아 더하는 함수 작성
def add(a, b):
    return a + b
print(add(3, 5))  # 8
# 2) 리스트를 입력받아 평균을 계산하는 함수 작성
def average(numbers):
    return sum(numbers) / len(numbers)
print(average([1, 2, 3, 4, 5]))  # 3.0
# 3) 문자열을 입력받아 역순으로 반환하는 함수 작성
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))  # "olleh"
# 4) 팩토리얼을 계산하는 재귀 함수 작성
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # 120
# 5) 두 수를 입력받아 최대공약수를 계산하는 함수 작성
def gdc(a, b):
    while b:
        a, b = b, a % b
    return a
print(gdc(48, 18))  # 6
# 6) 문자열을 입력받아 각 단어의 첫 글자만 대문자로 변환하는 함수 작성
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())
print(capitalize_words("hello world"))  # "Hello World"
# 7) 리스트를 입력받아 중복된 값을 제거하는 함수 작성
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
# 8) 두 문자열을 입력받아 아나그램인지 확인하는 함수 작성
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
# 9) 리스트를 입력받아 오름차순으로 정렬하는 함수 작성
def sort_list(lst):
    return sorted(lst)
print(sort_list([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # [1, 1, 2, 3, 4, 5, 5, 6, 9]
# 10) 문자열을 입력받아 회문인지 확인하는 함수 작성
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))  # False
# 2. 모듈 연습문제
# 1) math 모듈을 사용하여 삼각함수 계산
import math

def calculate_trigonometry(angle):
    radian = math.radians(angle)
    return {
        "sin": math.sin(radian),
        "cos": math.cos(radian),
        "tan": math.tan(radian)
    }

print(calculate_trigonometry(30))  # { 'sin': 0.49999999999999994, 'cos': 0.8660254037844387, 'tan': 0.5773502691896257 }
print(calculate_trigonometry(45))  # { 'sin': 0.7071067811865475, 'cos': 0.7071067811865476, 'tan': 0.9999999999999999 }
print(calculate_trigonometry(60))  # { 'sin': 0.8660254037844387, 'cos': 0.49999999999999994, 'tan': 1.7320508075688767 }

# 2) random 모듈을 사용하여 로또 번호 생성
import random

def generate_lotto_numbers():
    return random.sample(range(1, 46), 6)

print(generate_lotto_numbers())  # 예: [5, 12, 23, 34, 41, 45]
print(generate_lotto_numbers())  # 예: [3, 15, 22,
print(generate_lotto_numbers())  # 예: [1, 8, 19, 27, 33, 44] 36]
# 3) datetime 모듈을 사용하여 현재 날짜와 시간 출력
import datetime

def print_current_datetime():
    now = datetime.datetime.now()
    print("현재 날짜와 시간:", now)

print_current_datetime()  # 예: 현재 날짜와 시간: 2023-10-05 14:30:00.123456
# 4) os 모듈을 사용하여 현재 작업 디렉토리 출력
import os

def print_current_working_directory():
    cwd = os.getcwd()
    print("현재 작업 디렉토리:", cwd)

print_current_working_directory()  # 예: 현재 작업 디렉토리: /home/user/project
# 5) sys 모듈을 사용하여 명령줄 인수 출력
import sys

def print_command_line_arguments():
    args = sys.argv[1:]
    print("명령줄 인수:", args)

print_command_line_arguments()  # 예: 명령줄 인수: ['arg1', 'arg2']
# 6) json 모듈을 사용하여 딕셔너리를 JSON 문자열로
import json

def convert_dict_to_json(data):
    return json.dumps(data)

print(convert_dict_to_json({"name": "Alice", "age": 30}))  # 예: {"name": "Alice", "age": 30}
# 7) csv 모듈을 사용하여 CSV 파일 읽기
import csv

def read_csv_file(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print("행:", row)
# 예: read_csv_file("data.csv")
# 8) re 모듈을 사용하여 이메일 주소 추출
import re

def extract_email_addresses(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

print(extract_email_addresses("문의는 support@example.com 또는 sales@example.com으로 해주세요."))  # 예: ['support@example.com', 'sales@example.com']
# 9) urllib 모듈을 사용하여 웹 페이지 내용 가져오기
import urllib.request

def fetch_webpage(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

print(fetch_webpage("http://example.com"))  # 예: <html>...</html>
# 10) collections 모듈을 사용하여 리스트에서 가장 빈번한 요소 찾기
from collections import Counter

def find_most_frequent_element(lst):
    if not lst:
        return None
    counter = Counter(lst)
    return counter.most_common(1)[0]

print(find_most_frequent_element([1, 2, 2, 3, 4, 4, 5]))  # 예: (2, 2)
print(find_most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))  # 예: ('apple', 3)
# 3. 파일 I/O 연습문제
# 1) 텍스트 파일에 문자열 쓰기
def write_to_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
write_to_file("output.txt", "Hello, World!")
# 2) 텍스트 파일에서 문자열 읽기
def read_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
print(read_from_file("output.txt"))  # 예: Hello, World!
# 3) CSV 파일에 데이터 쓰기
import csv

def write_to_csv(file_name, data):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

write_to_csv("data.csv", [["이름", "나이"], ["Alice", 30], ["Bob", 25]])
# 4) CSV 파일에서 데이터 읽기
import csv

def read_from_csv(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print("행:", row)
read_from_csv("data.csv")
# 5) JSON 파일에 데이터 쓰기
import json

def write_to_json(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file)

write_to_json("data.json", {"이름": "Alice", "나이": 30})
# 6) JSON 파일에서 데이터 읽기
import json

def read_from_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

print(read_from_json("data.json"))  # 예: {"이름": "Alice", "나이": 30}
# 7) 바이너리 파일에 데이터 쓰기
def write_to_binary_file(file_name, data):
    with open(file_name, 'wb') as file:
        file.write(data)
write_to_binary_file("example.bin", b'\x00\xFF\x7A\x3C')
# 8) 바이너리 파일에서 데이터 읽기
def read_from_binary_file(file_name):
    with open(file_name, 'rb') as file:
        return file.read()
print(read_from_binary_file("example.bin"))  # 예: b'\x00\xFF\x7A\x3C'
# 9) 파일 존재 여부 확인
import os

def check_file_exists(file_name):
    return os.path.exists(file_name)

print(check_file_exists("output.txt"))  # 예: True
print(check_file_exists("non_existent.txt"))  # 예: False
# 10) 디렉토리 생성 및 삭제
import os

def create_directory(dir_name):
    os.makedirs(dir_name, exist_ok=True)

def delete_directory(dir_name):
    os.rmdir(dir_name)
create_directory("new_folder/subfolder")
print(os.listdir("new_folder"))  # 예: ['subfolder']
delete_directory("new_folder/subfolder")
delete_directory("new_folder")
# 4. 예외 처리 연습문제
# 1) 0으로 나누기 예외 처리
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."

print(divide_numbers(10, 2))  # 예: 5.0
print(divide_numbers(10, 0))  # 예: 0으로 나눌 수 없습니다.
# 2) 파일 열기 예외 처리
def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "파일을 찾을 수 없습니다."

print(read_file("output.txt"))  # 예: Hello, World!
print(read_file("non_existent.txt"))  # 예: 파일을 찾을 수 없습니다.
# 3) 리스트 인덱스 예외 처리
def get_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "인덱스가 리스트 범위를 벗어났습니다."

print(get_list_element([1, 2, 3], 1))  # 예: 2
print(get_list_element([1, 2, 3], 5))  # 예: 인덱스가 리스트 범위를 벗어났습니다.
# 4) 사용자 정의 예외 처리
class NegativeNumberError(Exception):
    pass

def sqrt(x):
    if x < 0:
        raise NegativeNumberError("음수의 제곱근은 정의되지 않습니다.")
    return x ** 0.5

try:
    print(sqrt(4))  # 예: 2.0
    print(sqrt(-1))  # 예: 음수의 제곱근은 정의되지 않습니다.
except NegativeNumberError as e:
    print(e)
# 5) 여러 예외 처리
def process_input(value):
    try:
        num = int(value)
        return 10 / num
    except ValueError:
        return "유효한 숫자를 입력하세요."
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
print(process_input("5"))    # 예: 2.0
print(process_input("abc"))  # 예: 유효한 숫자를 입력하세요.
print(process_input("0"))    # 예: 0으로 나눌 수 없습니다.
# 6) finally 블록 사용
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    finally:
        print("연산 완료")
print(safe_divide(10, 2))  # 예: 5.0 연산 완료
print(safe_divide(10, 0))  # 예: 0으로 나눌 수 없습니다. 연산 완료
# 7) assert 문 사용
def test_divide_numbers():
    assert divide_numbers(10, 2) == 5.0
    assert divide_numbers(10, 0) == "0으로 나눌 수 없습니다."
test_divide_numbers()
print("모든 테스트 통과")  # 예: 모든 테스트 통과
# 8) 예외 전환
class LowLevelError(Exception):
    pass

class HighLevelError(Exception):
    pass

def process_data(data):
    if data < 0:
        raise LowLevelError("음수는 처리할 수 없습니다.")
    elif data > 100:
        raise HighLevelError("100을 초과하는 값은 처리할 수 없습니다.")
    return data * 2

try:
    print(process_data(50))   # 예: 100
    print(process_data(-10))  # 예: 음수는 처리할 수 없습니다.
    print(process_data(150))  # 예: 100을 초과하는 값은 처리할 수 없습니다.
except LowLevelError as e:
    print(e)
except HighLevelError as e:
    print(e)
# 9) 예외 무시하기
def ignore_exceptions(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception:
        pass
print(ignore_exceptions(divide_numbers, 10, 0))  # 예: None
print("프로그램 계속 실행")  # 예: 프로그램 계속 실행
# 10) 로깅 사용
import logging

logging.basicConfig(level=logging.INFO)

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("0으로 나눌 수 없습니다.")
        return None
print(divide_numbers(10, 2))  # 예: 5.0
print(divide_numbers(10, 0))  # 예: None (로그에 오류 메시지 출력)
# 0으로 나눌 수 없습니다.
# 연습문제 끝