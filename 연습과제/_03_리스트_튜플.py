# **시퀀스 자료형의 특성에 대한 설명으로 옳지 않은 것은?**
#
# 1. 리스트는 요소를 수정하거나 삭제할 수 있다.
# 2. 튜플은 요소의 변경이 가능하다.
# 3. 문자열은 인덱스를 이용해 특정 문자를 접근할 수 있다.
# 4. 리스트는 여러 자료형의 요소를 포함할 수 있다.
# 5. 시퀀스 자료형은 인덱스를 사용하여 요소를 접근할 수 있다.
# 정답 : 2번
from os.path import split

# 다음 코드의 실행 결과를 고르세요.
#
# data = [1, 2, 3, 4, 5]
# print(data[1:4:2])
# ```
#
# 1. `[1, 3]`
# 2. `[2, 4]`
# 3. `[2, 3, 4]`
# 4. `[1, 2, 3]`
# 5. `[3, 4]`
# 정답 : 2번

# 1. `fruits`라는 리스트에 다음 요소를 저장하세요.
#     - `'apple', 'banana', 'cherry'`.
# 2. `print()`를 사용해 `fruits`의 첫 번째 요소와 세 번째 요소를 출력하세요.
fruits = ['apple', 'banana', 'cherry']
print(fruits[0:3:2])

# 1. `numbers`라는 리스트를 선언하고 숫자 `1`부터 `5`까지 저장하세요.
# 2. 이 리스트의 **길이**를 출력하세요
numbers = [1, 2, 3, 4, 5]
print(len(numbers))

# 1. `animals` 리스트에 `'cat', 'dog', 'bird'`를 저장하세요.
# 2. 이 리스트의 마지막에 `'fish'`를 추가하고, 리스트를 출력하세요.
animals = ['cat', 'dog', 'bird']
animals.append('fish')
print(animals)


# 1. `numbers` 리스트에 숫자 `3, 6, 9`를 저장하세요.
# 2. 리스트의 첫 번째 요소를 **2배**로 만들어 다시 저장하고, 리스트를 출력하세요.
numbers = [3, 6, 9]
numbers[0] = numbers[0]*2
print(numbers)

# 1. 문자열 `'Python-is-fun'`을 `'-'`를 기준으로 분리하여 리스트로 만드세요.
# 2. 결과 리스트를 출력하세요.
data = "Python-is-fun"
data_ = data.split('-')
print(data_)

# 1. `my_tuple`이라는 이름으로 숫자 `10, 20, 30`을 가진 튜플을 선언하세요.
# 2. `my_tuple`의 두 번째 요소를 출력하세요.
my_tuple = (10, 20, 30)
print(my_tuple[1])

# 1. `colors` 리스트에 `'red', 'blue', 'green'`을 저장하세요.
# 2. `'blue'`를 `'yellow'`로 변경하고 리스트를 출력하세요.
colors = ['red', 'green', 'blue']
colors[2] = 'yellow'
print(colors)

# 1. 숫자 `1`부터 `10`까지 중에서 **짝수만**을 추출해 새로운 리스트에 저장하세요.
# 2. 리스트를 출력하세요.
numbers = [ n for n in range(1,11) if n % 2 == 0 ]
print(numbers)
# -------------다시 공부하기 ----------------- 순회 및 for 반복문 ----------------------


# 1. 리스트 `words`에 `'Life', 'is', 'too', 'short'`를 저장하세요.
# 2. 리스트의 요소를 공백으로 이어붙여 문자열 `'Life is too short'`를 출력하세요.
words = ['life','is','too','short']
dara2 =" ".join(words)
print(dara2)
# -------------다시 공부하기 ---------------------------------------


# 1. 리스트 `numbers`에 숫자 `1, 2, 3, 4, 5`를 저장하세요.
# 2. 슬라이싱을 이용하여 다음을 수행하세요:
#     - 리스트의 **처음 3개의 요소**를 출력하세요.
#     - 리스트의 **마지막 2개의 요소**를 출력하세요.
#     - 리스트의 **모든 요소를 역순**으로 출력하세요.
numbers = [ 1,2,3,4,5]
print(numbers[:3])
print(numbers[3:])
print(numbers[::-1])