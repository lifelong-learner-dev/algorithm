# append와 add 차이
# 메서드 데이터 구조와 동작 방식에 차이가 있음

# 'append'
# 사용대상: list
# 동작: list 끝에 새로운 요소를 추가
# 특징:
## 1. list의 순서를 유지하며, 요소가 추가된 순서대로 저장
## 2. 중복된 요소 허용

my_list_append = [1, 2, 3]
my_list_append.append(4)
print(my_list_append)
# 출력 : [1, 2, 3, 4]


# 'add'
# 사용대상: 집합(set)
# 동작: 집합에 새로운 요소를 추가
# 특징:
## 1. 집합은 순서를 유지하지 않으며, 요소가 임의의 순서로 저장됨
## 2. 중복된 요소를 허용하지 않고 이미 존재하는 요소를 추가하려고 하면, 아무런 변화가 없음

my_set_add = {1, 2, 3}
my_set_add.add(4)
print(my_set_add) # 출력: {1, 2, 3, 4}


# 'insert'
# 사용대상: list
# 동작: insert(삽입할 위치를 나타내는 인덱스, 삽입할 요소)
# 특징:
## 1. 특정 위치에 삽입 : 리스트의 특정 인덱스에 요소를 삽입할 수 있음
## 2. 기존 요소의 이동 : 삽입된 요소의 위치 이후의 모든 요소는 한 칸씩 뒤로 이동
## 3. 음수 인덱스 허용 : 음수 인덱스를 사용할 수 있음, 음수 인덱스는 리스트의 끝에서 요소를 삽입하는 위치를 결정
## 4. 인덱스 범위 : 인덱스가 리스트의 길이를 초과하면 리스트의 끝에 요소를 추가
## 5. 시간 복잡도 : 'insert()' 메서드는 평균적으로 O(n)의 시간 복잡도를 가지며, 이는 리스트의 크기가 커질수록 삽입 연산의 비용이 증가함을 의미
################ 요소를 삽입할 때 이후의 모든 요소를 이동해야 함

my_list_insert = [1, 2, 3]

# 리스트의 처음에 요소 삽입
my_list_insert.insert(0, 'a')
print(my_list_insert)

# 리스트의 중간에 요소 삽입
my_list_insert.insert(2, 'b')
print(my_list_insert)

# 리스트의 끝에 요소 삽입
my_list_insert.insert(10, 'c')
print(my_list_insert)

# 음수 인덱스를 사용하여 요소 삽입
my_list_insert.insert(-1, 'd')
print(my_list_insert)