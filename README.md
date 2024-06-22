# [1. 자료 구조](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L1)

## [1) 리스트 (List)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L3)
## 정의: 순서가 있는 변경 가능한 데이터 구조로, 다양한 데이터 타입을 포함할 수 있음
## 특징:
### 1. 인덱스로 접근 가능
### 2. 중복 요소 허용
### 3. 동적 배열 구조
### 4. 데이터 저장 및 순차 처리: 학생들의 성적을 저장하고 처리할 때
my_list = [1, 2, 3, 'a', 'b']
print(my_list)

##### [조회: 원하는 데이터를 인덱스를 통해 조회 가능](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L13)
##### 첫 번째 요소 조회
print(my_list[0])
##### 마지막 요소 조회
print(my_list[-1])

##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L19)
##### append(): 리스트 끝에 요소 추가
my_list.append(4)
print(my_list)
##### insert(): 특정 위치에 요소 삽입
my_list.insert(1, 'a')
print(my_list)
##### extend(): 리스트 확장
my_list.extend([5, 6])
print(my_list)

##### [수정:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L30)
##### 인덱스를 사용하여 값 수정
my_list[1] = 'b'
print(my_list)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L35)
##### remove(): 특정 값을 찾아 삭제
my_list.remove('b')
print(my_list)
##### pop(): 인덱스로 삭제하고 그 값을 반환
removed_value = my_list.pop(2)
print(removed_value)
print(my_list)
##### del: 인덱스를 사용하여 삭제
del my_list[0]
print(my_list)


## [2) 튜플 (Tuple)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L48)
## 정의: 순서가 있는 변경 불가능한 데이터 구조
## 특징:
### 1. 인덱스로 접근 가능
### 2. 중복 요소 허용
### 3. 불변성 (immutable)
### 4. 좌표 (x, y)를 저장할 때
my_tuple = (1, 2, 3, 'a', 'b')
print(my_tuple)

##### [조회: 원하는 데이터를 인덱스를 통해 조회 가능](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L58)
##### 첫 번째 요소 조회
print(my_tuple[0])
##### 마지막 요소 조회
print(my_tuple[-1])

##### [불변!: 직접적으로 요소를 추가, 수정, 삭제 할 수 없음. 튜플을 변경하려면 새로운 튜플을 생성해야 함](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L64)
my_tuple2 = (1, 2, 3)
new_tuple = my_tuple2 + (4,)
print(new_tuple)

new_tuple = (1,) + my_tuple2[1:]
print(new_tuple)

new_tuple = my_tuple2[:1] + (5,) + my_tuple2[2:]
print(new_tuple)


## [3) 사전 (Dictionary)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L76)
## 정의: 키-값 쌍으로 데이터를 저장하는 변경 가능한 데이터 구조
## 특징:
### 1. 키는 고유해야 하며, 값은 중복 가능
### 2. 키로 접근 가능
### 3. 순서가 유지됨 (파이썬 3.7 이상)
### 4. 빠른 데이터 검색: 학생ID로 성적 조회
### 5. 키-값 매핑 : JSON 데이터를 파싱하여 저장할 떄
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)

##### [조회: 원하는 데이터를 키를 통해 조회 가능](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L87)
##### 키를 사용한 조회
value_a = my_dict['a']
print(f"a키 값은 : {value_a}")
##### get() 메서드 사용
value_b = my_dict.get('b')
print(f"b키 값은 : {value_b} ")
##### 키가 존재하지 않을 때 기본 값 반환
value_d = my_dict.get('d', 'default_value')
print(f"d키 값은 : {value_d}")
##### 키 존재 여부 확인 후 값 조회
if 'c' in my_dict:
    value_c = my_dict['c']
    print(f"c키 값은 {value_c}")
else:
    print(f"c키는 딕셔너리에 값이 없습니다.")

##### 추가 및 수정:
##### 키를 사용하여 값 할당
##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L106)
my_dict['d'] = 5
print(my_dict)

##### [수정:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L110)
my_dict['b'] = 5
print(my_dict)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L114)
##### del: 키를 사용하여 삭제
del my_dict['a']
print(my_dict)
##### pop(): 키로 삭제하고 그 값을 반환
removed_value = my_dict.pop('c')
print(removed_value)
print(my_dict)
##### popitem(): 마지막 키-값 쌍을 삭제하고 반환
last_item = my_dict.popitem()
print(last_item)
print(my_dict)


## [4) 집합 (set)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L128)
## 정의: 순서가 없고 중복을 허용하지 않는 데이터 구조
## 특징:
### 1. 요소의 순서가 없음
### 2. 중복 요소 허용하지 않음
### 3. 수학적 집합 연산 지원 (합집합, 교집합 등)
### 4. 고유 요소 저장: 사용자ID 저장할 때 
my_set = {1, 2, 3}
print(my_set)

##### [조회: 집합은 순서가 없어 특정 인덱스로 조회 불가능하나 특정 값이 집합에 존재하는지는 확인 가능](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L138)
##### 값 2가 집합에 존재하는지 확인
print(2 in my_set)
##### 값 5가 집합에 존재하는지 확인
print(5 in my_set)

##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L144)
##### add(): 요소 추가
my_set.add(4)
print(my_set)
##### update(): 여러 요소 추가
my_set.update([5, 6])
print(my_set)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L152)
##### remove(): 특정 요소 삭제 (없으면 오류 발생)
my_set.remove(2)
print(my_set)
##### discard(): 특정 요소 삭제 (없어도 오류 발생 안함)
my_set.discard(3)
print(my_set)
##### pop(): 임의의 요소 삭제하고 반환
removed_value_set = my_set.pop()
print(removed_value_set)
print(my_set)
##### clear(): 모든 요소 삭제
my_set.clear()
print(my_set)


## [5) 덱 (Deque)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L168)
## 정의: 양쪽 끝에서 삽입과 삭제가 모두 가능한 큐
## 특징:
### 1. 빠른 양쪽 끝 삽입 및 삭제 연산
### 2. 리스트보다 효율적
### 3. 양방향 큐: 브라우저의 앞/뒤로 이동 기록을 관리할 때
### 4. 슬라이딩 윈도우: 고정 크기 윈도우를 유지하면서 데이터를 처리할 때
from collections import deque
my_deque = deque([1, 2, 3])
print(my_deque)

##### [조회: 인덱스를 통해 조회하거나, 양 끝에서 요소를 추가 및 제거할 수 있음](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L179)
##### 첫 번째 요소 출력:
print(my_deque[0])
##### 마지막 요소 출력:
print(my_deque[-1])

##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L185)
##### append(): 오른쪽 끝에 추가
my_deque.append(4)
print(my_deque)
##### appendleft(): 왼쪽 끝에 추가
my_deque.appendleft(0)
print(my_deque)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L193)
##### pop(): 오른쪽 끝에서 삭제하고 반환
right_removed = my_deque.pop()
print(right_removed)
print(my_deque)
##### popleft(): 왼쪽 끝에서 삭제하고 반환
left_removed = my_deque.popleft()
print(left_removed)
print(my_deque)


## [6) 힙 (Heap)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L204)
## 정의: 완전 이진 트리 기반의 우선순위 큐를 구현하는 데이터 구조
## 특징:
### 1. 최소 힙(min-heap)과 최대 힙(max-heap) 존재
### 2. 항상 최소값 또는 최대값을 빠르게 찾을 수 있음
### 3. 정렬 알고리즘 구현시
### 4. 우선 순위가 높은 작업을 처리할 때
import heapq
min_heap = [3, 1, 4, 1, 5, 9]
hhmin_heap = heapq.heapify(min_heap)
print(min_heap)
print(hhmin_heap)

##### [조회: 힙에서 최소값 또는 최대값을 조회할 수 있음](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L217)
##### 최소값 조회
print(min_heap[0])
##### 3번째로 작은 요소 출력
k = 3
kth_smallest = heapq.nsmallest(k, min_heap)[-1]
print(kth_smallest)
##### 최대값 조회
max_value = max(min_heap)
print(max_value)

##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L228)
##### heappush(): 힙에 요소 추가
heapq.heappush(min_heap, 2)
print(min_heap)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L233)
##### heappop(): 최소값 삭제하고 반환
min_value = heapq.heappop(min_heap)
print(min_value)
print(min_heap)


## [7) 스택 (Stack)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L240)
## 정의: 후입선출(LIFO) 원칙을 따르는 데이터 구조
## 특징:
### 1. 마지막에 추가된 요소가 가장 먼저 제거됨
### 2. 리스트로 구현 가능
### 3. 재귀적 알고리즘 구현: 깊이 우선 탐색(DFS)에서 호출 스택을 사용할 때
### 4. 구문분석: 컴파일러가 코드의 구문을 분석할 때
### 5. 간단한 메모리 관리: 함수 호출의 지역 변수를 관리할 때
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

##### [조회: 원하는 데이터를 인덱스를 통해 조회](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L254)
print(stack[-1])

##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L257) 
##### append(): 요소 추가
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L264)
##### pop(): 마지막 요소 삭제하고 반환
top_value = stack.pop()
print(top_value)
print(stack)


## [8) 큐 (Queue)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L271)
## 정의: 선입선출(FIFO) 원칙을 따르는 데이터 구조
## 특징:
### 1. 먼저 추가된 요소가 먼저 제거됨
### 2. deque로 구현 가능
### 3. 작업대기열: 프린터 작업 대기열을 관리할 때
### 4. 이벤트 처리: 이벤트 드리븐 프로그래밍에서 이벤트를 처리할 때
### 5. 데이터 스트리밍: 실시간 데이터 스트리밍 처리시
from collections import deque
queue = deque([1, 2, 3])
print(queue)
queue.append(5)
print(queue)
queue.popleft()
print(queue.popleft())
print(queue)

##### [조회: 원하는 데이터를 인덱스를 통해 조회](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L288)
##### 첫 번째 요소 조회
print(queue[0])

##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L292)
##### append(): 오른쪽 끝에 요소 추가
queue.append(7)
print(queue)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L297)
##### popleft(): 왼쪽 끝에 요소 삭제하고 반환
front_value = queue.popleft()
print(front_value)
print(queue)


## [9) 기본적인 트리 (Tree)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L304)
## 정의: 계층적 구조를 나타내는 비선형 데이터 구조
## 특징:
### 1. 노드와 엣지로 구성
### 2. 루트 노드에서 시작하여 자식 노드로 확장
### 3. 계층적 데이터 저장: 파일 시스템 디렉터리 구조
### 4. 빠른 검색 및 정렬: 이진 탐색 트리(BST)를 사용하여 데이터베이스 인덱스 구현
### 5. 구조적 데이터 표현: XML/HTML 문서의 구조를 나타낼 때
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
print(Node)
print(root)
root.left = Node(2)
print(root.left)
root.right = Node(3)
print(root.right)
root.left.left = Node(5)
print(root.left.left)

##### [조회: 트리에서 원하는 데이터를 조회하려면 노드를 통해 접근 필요](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L328)
##### 루트 노드의 값 조회
print(root.value)
##### 루트의 왼쪽 자식 노드의 값 조회
print(root.left.value)

##### 추가 및 수정:
##### 노드를 생성하여 트리에 연결하거나 노드 값을 변경
##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L336)
root.left.left = Node(7)
print(root.left.left.value)

##### [수정:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L340)
root.right.value = 5
print(root.right.value)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L344)
##### 노드를 제거하고, 그 자식을 부모 노드에 연결
root.left = None
print(root.left)


## [10) 그래프 (Graph)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L350)
## 정의: 노드(정점)와 노드를 연결하는 엣지(간선)로 구성된 데이터 구조
## 특징:
### 1. 방향 그래프 (Directed Graph)와 무뱡항 그래프(Undirected Graph) 존재
### 2. 연결성, 경로 탐색 등에 사용
### 3. 네트워크 모델링: 소셜 네트워크, 통신 네트워크
### 4. 경로 탐색: 지도 애플리케이션에서 최단 경로 탐색
### 5. 의존성 그래프: 프로젝트 관리에서 작업의 의존성 표현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}
print(graph)

##### [조회: 그래프에서 원하는 데이터를 조회하려면 노드(정점)를 통해 접근해야 함](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L368)
##### 노드 'A'의 인접 노드 조회
print(graph['A'])
##### 노드 'C'의 인접 노드 조회
print(graph['C'])

##### 추가 및 수정:
##### 노드 또는 간선을 그래프에 추가하거나 노드 값을 변경
##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L376)
graph['G'] = ['A']
graph['A'].append('G')
print(graph)

##### [수정:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L381)
graph['A'] = ['B', 'C']
print(graph)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L385)
##### 노드 또는 간선을 그래프에서 제거
del graph['G']
graph['A'].remove('G')
print(graph)


## [11) 기본적인 링크드 리스트 (Linked List)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L392)
## 정의: 각 노드가 데이터와 다음 노드를 가리키는 포인터를 포함하는 데이터 구조
## 특징:
### 1. 순차 접근만 가능
### 2. 동적 크기 조절 가능
### 3. 동적 메모리 할당: 크기가 변동되는 데이터를 다룰 때
### 4. 효율적인 삽입/삭제: 중간에 데이터 삽입/삭제가 빈번할 때
### 5. 구현의 기초: 다른 복잡한 자료구조(스택, 큐 등)의 기초로 사용
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

head = ListNode(1)
print(ListNode)
print(head)
head.next = ListNode(2)
print(head.next)
head.next.next = ListNode(3)
print(head.next.next)

##### [조회: 데이터를 조회하려면 노드를 통해 순차적으로 접근 해야함](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L413)
##### 첫 번째 노드의 값 조회
print(head.value)
##### 두 번째 노드의 값 조회
print(head.next.value)
##### 세 번째 노드의 값 조회
print(head.next.next.value)

##### [추가:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L421)
##### 새 노드를 생성하여 기존 노드에 연결
new_node = ListNode(7)
new_node.next = head.next.next
head.next.next = new_node
print(head.next.next.value)

##### [수정:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L428)
##### 노드의 값을 변경
head.next.value = 5
print(head.next.value)

##### [삭제:](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L433)
##### 노드를 제거하고, 그 다음 노드를 이전 노드에 연결
head.next = head.next.next
print(head.next.value)


# [2. 노드(Node)와 엣지(Edge)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L439)

## [1) 노드(Node)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L441)
### 정의: 노드는 그래프에서 객체 또는 개체를 나타내는 기본 단위
### 예시: 소셜 네트워크에서 그래프에서 노드는 사용자 하나하나를 나타냄
######## 사용자 A, B, C가 있으면 A, B, C 각각이 노드가 됨

## [2) 엣지(Edge)](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L446)
### 정의: 엣지는 두 노드를 연결하는 선 또는 간선
######## 엣지는 노드 간의 관계를 나타냄
######## 엣지에는 방향이 있을 수도 있고 없을 수도 있음
### 예시: 소셜 네트워크 그래프에서 엣지는 사용자 간의 친구 관계를 나타냄
######## 사용자 A와 B가 친구라면, A와 B를 연결하는 엣지가 존재

## [3) 그래프 예시](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L453)
### 노드: A, B, C, D, E
### 엣지: (A-B), (A-C), (B-D), (C-D), (C-E)


# [3. append와 add, insert 차이](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L458)

## 메서드 데이터 구조와 동작 방식에 차이가 있음

## [1) 'append'](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L462)
## 사용대상: list
## 동작: list 끝에 새로운 요소를 추가
## 특징:
### 1. list의 순서를 유지하며, 요소가 추가된 순서대로 저장
### 2. 중복된 요소 허용
my_list_append = [1, 2, 3]
my_list_append.append(4)
print(my_list_append)
## 출력 : [1, 2, 3, 4]


## [2) 'add'](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L474)
## 사용대상: 집합(set)
## 동작: 집합에 새로운 요소를 추가
## 특징:
### 1. 집합은 순서를 유지하지 않으며, 요소가 임의의 순서로 저장됨
### 2. 중복된 요소를 허용하지 않고 이미 존재하는 요소를 추가하려고 하면, 아무런 변화가 없음
my_set_add = {1, 2, 3}
my_set_add.add(4)
print(my_set_add) # 출력: {1, 2, 3, 4}


## [3) 'insert'](https://github.com/lifelong-learner-dev/algorithm/blob/main/algorithm.py#L485)
## 사용대상: list
## 동작: insert(삽입할 위치를 나타내는 인덱스, 삽입할 요소)
## 특징:
### 1. 특정 위치에 삽입 : 리스트의 특정 인덱스에 요소를 삽입할 수 있음
### 2. 기존 요소의 이동 : 삽입된 요소의 위치 이후의 모든 요소는 한 칸씩 뒤로 이동
### 3. 음수 인덱스 허용 : 음수 인덱스를 사용할 수 있음, 음수 인덱스는 리스트의 끝에서 요소를 삽입하는 위치를 결정
### 4. 인덱스 범위 : 인덱스가 리스트의 길이를 초과하면 리스트의 끝에 요소를 추가
### 5. 시간 복잡도 : 'insert()' 메서드는 평균적으로 O(n)의 시간 복잡도를 가지며, 이는 리스트의 크기가 커질수록 삽입 연산의 비용이 증가함을 의미
################# 요소를 삽입할 때 이후의 모든 요소를 이동해야 함
my_list_insert = [1, 2, 3]

##### 리스트의 처음에 요소 삽입
my_list_insert.insert(0, 'a')
print(my_list_insert)

##### 리스트의 중간에 요소 삽입
my_list_insert.insert(2, 'b')
print(my_list_insert)

##### 리스트의 끝에 요소 삽입
my_list_insert.insert(10, 'c')
print(my_list_insert)

##### 음수 인덱스를 사용하여 요소 삽입
my_list_insert.insert(-1, 'd')
print(my_list_insert)