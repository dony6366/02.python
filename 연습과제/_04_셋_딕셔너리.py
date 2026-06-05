# **셋(Set)의 특징**에 대한 설명 중 옳지 않은 것은 무엇인가요?
#
# 1. 셋은 중복된 요소를 허용하지 않는다.
# 2. 셋은 순서가 없는 자료형이다.
# 3. 셋은 인덱스를 사용해 요소에 접근할 수 있다.
# 4. 셋은 다양한 자료형을 요소로 가질 수 있다.
# 5. `add()` 메서드를 사용하여 새로운 요소를 추가할 수 있다.
# 정답 : 3번


# 다음 코드의 실행 결과를 고르세요.
#
# info = {'name': 'Kim', 'age': 30, 'city': 'Seoul'}
# print(info.get('country', 'Unknown'))
#
# 1. `'Kim'`
# 2. `30`
# 3. `'Seoul'`
# 4. `'Unknown'`
# 5. `None`
#정답 : 4번



# 1. `fruits`라는 셋을 선언하고 `'apple', 'banana', 'cherry'`를 추가하세요.
# 2. `print()`를 사용하여 `fruits`를 출력하세요.
fluits = {'apple', 'banana', 'cherry'}
print(fluits)

# 1. `animals`라는 셋에 `'cat', 'dog', 'bird', 'fish'`를 저장하세요.
# 2. `'bird'`를 제거한 후, `print()`를 사용해 남은 요소를 출력하세요.

animals = {'dog', 'cat', 'bird', 'fish'}
animals.remove('bird')
print(animals)

# 1. `set1`에 `{1, 2, 3}`을 저장하고, `set2`에 `{3, 4, 5}`를 저장하세요.
# 2. `set1`과 `set2`의 **합집합**을 구해서 출력하세요.
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))

# 1. `student`라는 이름의 딕셔너리를 선언하고 다음 키-값 쌍을 추가하세요:
#     - `'name'`: `'John'`
#     - `'age'`: `20`
#     - `'major'`: `'Computer Science'`
# 2. `'age'`의 값을 출력하세요.

student = {'name': 'John', 'age':'20', 'major':'Computer Science'}
print(student.get('age'))


# 1. `scores`라는 딕셔너리에 `'math': 80, 'english': 90`을 저장하세요.
# 2. `'math'`의 값을 `95`로 변경하고 딕셔너리를 출력하세요.
score = {'math': 80, 'english': 90}
score['math'] = 95
print(score)


# 1. `colors1`에 `'red', 'blue', 'green'`을 저장하세요.
# 2. `colors2`에 `'blue', 'yellow', 'pink'`를 저장하세요.
# 3. 두 셋의 **교집합**을 구하여 출력하세요.
color1 = {'red', 'green', 'blue'}
color2 = {'yellow','pink', 'blue'}
print(color1.intersection(color2))



# 1. `info` 딕셔너리에 `'name': 'Alice', 'age': 25, 'city': 'Seoul'`을 저장하세요.
# 2. `keys()` 메서드를 사용해 딕셔너리의 모든 키를 출력하세요.
# 3. `values()` 메서드를 사용해 딕셔너리의 모든 값을 출력하세요.
info = {'name': 'Alice', 'age':'25', 'city':'Seoul'}
print(info.keys())
print(info.values())


# 1. `students` 딕셔너리에 `'student1': 85, 'student2': 90, 'student3': 95`를 저장하세요.
# 2. `pop()` 메서드를 사용해 `'student2'`의 값을 제거하고, 제거된 값을 출력하세요.
student = {'student1':85, 'student2':90, 'student3':95}
print(student.pop('student2'))

# 1. 두 셋 `A = {1, 2, 3, 4}`와 `B = {3, 4, 5, 6}`가 있습니다.
# 2. `A`와 `B`의 **대칭 차집합**을 구하세요.
# 3. 결과를 `print()`를 사용해 출력하세요.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.symmetric_difference(B))