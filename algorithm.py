# 1. 자료 구조

## 1) 리스트 (List)
## 정의: 순서가 있는 변경 가능한 데이터 구조로, 다양한 데이터 타입을 포함할 수 있음
## 특징:
### 1. 인덱스로 접근 가능
### 2. 중복 요소 허용
### 3. 동적 배열 구조
### 4. 데이터 저장 및 순차 처리: 학생들의 성적을 저장하고 처리할 때
my_list = [1, 2, 3, 'a', 'b']
print(my_list)

##### 조회: 원하는 데이터를 인덱스를 통해 조회 가능
##### 첫 번째 요소 조회
print(my_list[0])
##### 마지막 요소 조회
print(my_list[-1])

##### 추가:
##### append(): 리스트 끝에 요소 추가
my_list.append(4)
print(my_list)
##### insert(): 특정 위치에 요소 삽입
my_list.insert(1, 'a')
print(my_list)
##### extend(): 리스트 확장
my_list.extend([5, 6])
print(my_list)

##### 수정:
##### 인덱스를 사용하여 값 수정
my_list[1] = 'b'
print(my_list)

##### 삭제:
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


## 2) 튜플 (Tuple)
## 정의: 순서가 있는 변경 불가능한 데이터 구조
## 특징:
### 1. 인덱스로 접근 가능
### 2. 중복 요소 허용
### 3. 불변성 (immutable)
### 4. 좌표 (x, y)를 저장할 때
my_tuple = (1, 2, 3, 'a', 'b')
print(my_tuple)

##### 조회: 원하는 데이터를 인덱스를 통해 조회 가능
##### 첫 번째 요소 조회
print(my_tuple[0])
##### 마지막 요소 조회
print(my_tuple[-1])

##### 불변!: 직접적으로 요소를 추가, 수정, 삭제 할 수 없음. 튜플을 변경하려면 새로운 튜플을 생성해야 함
my_tuple2 = (1, 2, 3)
new_tuple = my_tuple2 + (4,)
print(new_tuple)

new_tuple = (1,) + my_tuple2[1:]
print(new_tuple)

new_tuple = my_tuple2[:1] + (5,) + my_tuple2[2:]
print(new_tuple)


## 3) 사전 (Dictionary)
## 정의: 키-값 쌍으로 데이터를 저장하는 변경 가능한 데이터 구조
## 특징:
### 1. 키는 고유해야 하며, 값은 중복 가능
### 2. 키로 접근 가능
### 3. 순서가 유지됨 (파이썬 3.7 이상)
### 4. 빠른 데이터 검색: 학생ID로 성적 조회
### 5. 키-값 매핑 : JSON 데이터를 파싱하여 저장할 떄
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)

##### 조회: 원하는 데이터를 키를 통해 조회 가능
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
##### 추가:
my_dict['d'] = 5
print(my_dict)

##### 수정:
my_dict['b'] = 5
print(my_dict)

##### 삭제:
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


## 4) 집합 (set)
## 정의: 순서가 없고 중복을 허용하지 않는 데이터 구조
## 특징:
### 1. 요소의 순서가 없음
### 2. 중복 요소 허용하지 않음
### 3. 수학적 집합 연산 지원 (합집합, 교집합 등)
### 4. 고유 요소 저장: 사용자ID 저장할 때 
my_set = {1, 2, 3}
print(my_set)

##### 조회: 집합은 순서가 없어 특정 인덱스로 조회 불가능하나 특정 값이 집합에 존재하는지는 확인 가능
##### 값 2가 집합에 존재하는지 확인
print(2 in my_set)
##### 값 5가 집합에 존재하는지 확인
print(5 in my_set)

##### 추가:
##### add(): 요소 추가
my_set.add(4)
print(my_set)
##### update(): 여러 요소 추가
my_set.update([5, 6])
print(my_set)

##### 삭제:
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


## 5) 덱 (Deque)
## 정의: 양쪽 끝에서 삽입과 삭제가 모두 가능한 큐
## 특징:
### 1. 빠른 양쪽 끝 삽입 및 삭제 연산
### 2. 리스트보다 효율적
### 3. 양방향 큐: 브라우저의 앞/뒤로 이동 기록을 관리할 때
### 4. 슬라이딩 윈도우: 고정 크기 윈도우를 유지하면서 데이터를 처리할 때
from collections import deque
my_deque = deque([1, 2, 3])
print(my_deque)

##### 조회: 인덱스를 통해 조회하거나, 양 끝에서 요소를 추가 및 제거할 수 있음
##### 첫 번째 요소 출력:
print(my_deque[0])
##### 마지막 요소 출력:
print(my_deque[-1])

##### 추가:
##### append(): 오른쪽 끝에 추가
my_deque.append(4)
print(my_deque)
##### appendleft(): 왼쪽 끝에 추가
my_deque.appendleft(0)
print(my_deque)

##### 삭제:
##### pop(): 오른쪽 끝에서 삭제하고 반환
right_removed = my_deque.pop()
print(right_removed)
print(my_deque)
##### popleft(): 왼쪽 끝에서 삭제하고 반환
left_removed = my_deque.popleft()
print(left_removed)
print(my_deque)


## 6) 힙 (Heap)
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

##### 조회: 힙에서 최소값 또는 최대값을 조회할 수 있음
##### 최소값 조회
print(min_heap[0])
##### 3번째로 작은 요소 출력
k = 3
kth_smallest = heapq.nsmallest(k, min_heap)[-1]
print(kth_smallest)
##### 최대값 조회
max_value = max(min_heap)
print(max_value)

##### 추가:
##### heappush(): 힙에 요소 추가
heapq.heappush(min_heap, 2)
print(min_heap)

##### 삭제:
##### heappop(): 최소값 삭제하고 반환
min_value = heapq.heappop(min_heap)
print(min_value)
print(min_heap)


## 7) 스택 (Stack)
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

##### 조회: 원하는 데이터를 인덱스를 통해 조회
print(stack[-1])

##### 추가: 
##### append(): 요소 추가
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

##### 삭제:
##### pop(): 마지막 요소 삭제하고 반환
top_value = stack.pop()
print(top_value)
print(stack)


## 8) 큐 (Queue)
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

##### 조회: 원하는 데이터를 인덱스를 통해 조회
##### 첫 번째 요소 조회
print(queue[0])

##### 추가:
##### append(): 오른쪽 끝에 요소 추가
queue.append(7)
print(queue)

##### 삭제:
##### popleft(): 왼쪽 끝에 요소 삭제하고 반환
front_value = queue.popleft()
print(front_value)
print(queue)


## 9) 기본적인 트리 (Tree)
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

##### 조회: 트리에서 원하는 데이터를 조회하려면 노드를 통해 접근 필요
##### 루트 노드의 값 조회
print(root.value)
##### 루트의 왼쪽 자식 노드의 값 조회
print(root.left.value)

##### 추가 및 수정:
##### 노드를 생성하여 트리에 연결하거나 노드 값을 변경
##### 추가:
root.left.left = Node(7)
print(root.left.left.value)

##### 수정:
root.right.value = 5
print(root.right.value)

##### 삭제:
##### 노드를 제거하고, 그 자식을 부모 노드에 연결
root.left = None
print(root.left)


## 10) 그래프 (Graph)
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

##### 조회: 그래프에서 원하는 데이터를 조회하려면 노드(정점)를 통해 접근해야 함
##### 노드 'A'의 인접 노드 조회
print(graph['A'])
##### 노드 'C'의 인접 노드 조회
print(graph['C'])

##### 추가 및 수정:
##### 노드 또는 간선을 그래프에 추가하거나 노드 값을 변경
##### 추가:
graph['G'] = ['A']
graph['A'].append('G')
print(graph)

##### 수정:
graph['A'] = ['B', 'C']
print(graph)

##### 삭제:
##### 노드 또는 간선을 그래프에서 제거
del graph['G']
graph['A'].remove('G')
print(graph)


## 11) 기본적인 링크드 리스트 (Linked List)
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

##### 조회: 데이터를 조회하려면 노드를 통해 순차적으로 접근 해야함
##### 첫 번째 노드의 값 조회
print(head.value)
##### 두 번째 노드의 값 조회
print(head.next.value)
##### 세 번째 노드의 값 조회
print(head.next.next.value)

##### 추가:
##### 새 노드를 생성하여 기존 노드에 연결
new_node = ListNode(7)
new_node.next = head.next.next
head.next.next = new_node
print(head.next.next.value)

##### 수정:
##### 노드의 값을 변경
head.next.value = 5
print(head.next.value)

##### 삭제:
##### 노드를 제거하고, 그 다음 노드를 이전 노드에 연결
head.next = head.next.next
print(head.next.value)


# 2. 노드(Node)와 엣지(Edge)

## 1) 노드(Node)
### 정의: 노드는 그래프에서 객체 또는 개체를 나타내는 기본 단위
### 예시: 소셜 네트워크에서 그래프에서 노드는 사용자 하나하나를 나타냄
######## 사용자 A, B, C가 있으면 A, B, C 각각이 노드가 됨

## 2) 엣지(Edge)
### 정의: 엣지는 두 노드를 연결하는 선 또는 간선
######## 엣지는 노드 간의 관계를 나타냄
######## 엣지에는 방향이 있을 수도 있고 없을 수도 있음
### 예시: 소셜 네트워크 그래프에서 엣지는 사용자 간의 친구 관계를 나타냄
######## 사용자 A와 B가 친구라면, A와 B를 연결하는 엣지가 존재

## 3) 그래프 예시
### 노드: A, B, C, D, E
### 엣지: (A-B), (A-C), (B-D), (C-D), (C-E)


# 3. append와 add, insert 차이

## 메서드 데이터 구조와 동작 방식에 차이가 있음

## 1) 'append'
## 사용대상: list
## 동작: list 끝에 새로운 요소를 추가
## 특징:
### 1. list의 순서를 유지하며, 요소가 추가된 순서대로 저장
### 2. 중복된 요소 허용
my_list_append = [1, 2, 3]
my_list_append.append(4)
print(my_list_append)
## 출력 : [1, 2, 3, 4]


## 2) 'add'
## 사용대상: 집합(set)
## 동작: 집합에 새로운 요소를 추가
## 특징:
### 1. 집합은 순서를 유지하지 않으며, 요소가 임의의 순서로 저장됨
### 2. 중복된 요소를 허용하지 않고 이미 존재하는 요소를 추가하려고 하면, 아무런 변화가 없음
my_set_add = {1, 2, 3}
my_set_add.add(4)
print(my_set_add) # 출력: {1, 2, 3, 4}


## 3) 'insert'
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


# 4. 알고리즘

## 1) BFS (Breadth-First Search) 너비 탐색
### 사용 자료구조:
### 큐(Queue): BFS는 너비 우선 탐색을 위해 큐를 사용
############# 큐에 현재 노드를 넣고, 이웃 노드를 탐색하면서 큐에 추가하는 방식
### 집합(Set): 방문한 노드를 추적하기 위해 사용
############# 이미 방문한 노드를 저장하여 중복 탐색을 방지
### 딕셔너리(Dictionary): 그래프를 표현하기 위해 사용
####################### 각 노드로 키로, 이웃 노드 리스트는 값으로 저장
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

## 2) DFS (Depth-First Search) 깊이 탐색
### 사용 자료구조:
### 스택(Stack): DFS는 깊이 우선 탐색을 위해 스택을 사용
############### 재귀적으로 호출할 때 시스템을 스택을 사용하거나, 명시적으로 스택을 사용할 수 있음
### 집합(Set): 방문한 노드를 추적하기 위해 사용
### 딕셔너리(Dictionary): 그래프를 표현하기 위해 사용
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

## 3) 브루트 포스 (Brute Force)
### 사용 자료구조:
### 리스트(List): 가능한 모든 경우의 수를 저장하고, 반복문을 통해 순차적으로 탐색할 때 사용
### 튜플(Tuple): 불변 데이터를 저장할 떄 사용
from itertools import permutations

def brute_force(arr):
    for perm in permutations(arr):
        print(perm)

## 4) 동적 프로그래밍 (Dynamic Programming, DP)
### 사용 자료구조:
### 리스트(List): 부분 문제의 해를 저장하여 중복 계산을 피하기 위해 사용
### 딕셔너리(Dictionary): 메모이제이션을 위해 사용
def fibonacci(n):
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

## 5) 정렬 알고리즘
### 사용 자료구조:
### 리스트(List): 대부분의 정렬 알고리즘은 리스틀 사용하여 데이터를 저장하고 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1]. arr[j]

## 6) 이진 탐색 (Binary Search)
### 사용 자료구조:
### 리스트(List): 정렬된 리스트에서 이진 탐색 수행
def binary_search(arr, target):
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

## 7) 그래프 알고리즘
### 사용 자료구조:
### 딕셔너리(Dictionary): 그래프를 표현하기 위해 사용
### 리스트(List): 인접 리스트 표현을 위해 사용
### 집합(Set): 방문한 노드를 추적하기 위해 사용
### 큐(Queue): BFS와 같은 알고리즘에서 사용
### 스택(Stack): DFS와 같은 알고리즘에서 사용
### 덱(Deque): 양방향 탐색을 효율적으로 수행할 때 사용
##### 예시: 다익스트라 알고리즘
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

## 8) 다익스트라 알고리즘(Dijkstra's Algorithm)
### 정의: 다익스트라 알고리즘은 가중치가 있는 그래프에서 주어진 시작 노드로부터 다른 모드 노드까지의 최단 경로를 찾는 알고리즘
### 사용 자료구조:
### 우선순위 큐(Priority Queue): 최소 힙(min-heap)을 사용하여 가장 작은 가중치를 가진 노드를 효율적으로 추출
### 딕셔너리(Dictionary): 그래프 표현 및 각 노드까지의 최단 거리를 저장
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

## 9) 플로이드-워셜 알고리즘 (Floyd-Warshall Algorithm)
### 정의: 모든 노드 쌍 간의 최단 경로를 찾는 알고리즘으로, 그래프의 모든 쌍에 대해 최단 경로를 계산
### 사용 자료구조:
### 2차원 리스트 (2D List): 최단 경로 정보를 저장하기 위해 사용
def floyd_warshall(graph):
    num_vertices = len(graph)
    distance = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            distance[i][j] = graph[i][j]

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

## 10) 크루스칼 알고리즘 (Kruskal's Algorithm)
### 정의: 최소 스패닝 트리를 찾는 알고리즘으로, 그래프의 모든 노드를 연결하면서 최소의 비용을 찾음
### 사용 자료구조:
### 리스트(List): 간선들을 저장하여 정렬
### 유니온 파인드(Union-Find): 서로소 집합 자료구조로 사이클을 감지하고 집합을 합침
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

def kruskal(graph):
    mst = []
    edges = sorted(graph['edges'], key=lambda edge: edge[2])
    uf = UnionFind(graph['num_vertices'])

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))

    return mst

## 11) 벨만-포드 알고리즘 (Bellman-Ford Algorithm)
### 정의: 주어진 시작 노드에서 다른 모든 노드까지의 최단 경로를 찾는 알고리즘으로, 가중치가 음수인 간선도 처리할 수 있음
### 사용 자료구조:
### 리스트(List): 각 노드까지의 최단 거리를 저장
### 리스트(List): 그래프의 간선 목록을 저장
def bellman_ford(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    
    for u in graph:
        for v, weight in graph[u].items():
            if distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distance

## 12) 위상 정렬 (Topological Sort)
### 정의: 방향 그래프의 노드를 순서대로 정렬하는 알고리즘으로, 선행 조건이 있는 작업의 순서를 정할 때 유용
### 사용 자료구조:
### 스택(Stack): 정렬된 노드를 저장
### 딕셔너리(Dictionary): 그래프의 인접 리스트 표현과 각 노드의 진입 차수를 저장
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]

## 13) 합병 정렬 (Merge Sort)
### 정의: 비교 기반의 정렬 알고리즘으로, 분할 정복 기법을 사용하여 리스트를 정렬
### 사용 자료구조:
### 리스트(List): 정렬할 데이터를 저장
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

## 14) 퀵 정렬 (Quick Sort)
### 정의: 비교 기반의 정렬 알고리즘으로, 분할 정복 기법을 사용하여 리스트를 정렬
######## 피벗을 선택하여 리스트를 분할하고 재귀적으로 정렬
### 사용 자료구조:
### 리스트(List): 정렬할 데이터를 저장
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

## 15) 캐쉬 (Cache)
### 정의: 자주 사용되는 데이터를 임시로 저장하여 접근 시간을 줄이는 데 사용
### 사용 자료구조:
### 딕셔너리(Dictionary): 키-값 쌍으로 데이터 저장
### 덱(Deque): 최근에 사용된 데이터를 추적하여 캐시 교체 정책을 구현할 때 사용
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)



# 5. requests 라이브러리의 다양한 HTTP 메서드

## 1) get(): 데이터를 가져오는 것
## 2) post(): 데이터를 제출하는 것
## 3) put(): 데이터를 업데이트하는 것
## 4) delete(): 데이터를 삭제하는 것
## 5) head(): 헤더 정보를 가져오는 것
## 6) options(): 지원하는 메서드를 확인하는 것 
## 7) patch(): 데이터를 부분적으로 수정하는 것
## 8) request(): 원하는 메서드를 사용하는 것  

### 1) requests.get()
### HTTP 요청을 보낼 때 사용
import requests
response = requests.get('https://api.example.com/data')

### 2) requests.post()
### 서버에 데이터를 제출하기 위해 사용
response1 = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(response.text)

### 3) requests.put()
### 서버에 데이터를 업데이트하기 위해 사용
response2 = requests.put('https://httpbin.org/put', data={'key': 'value'})
print(response1.text)

### 4) requests.delete()
### 서버에서 리소스를 삭제하기 위해 사용
response3 = requests.delete('https://httpbin.org/delete')
print(response2.text)

### 5) requests.head()
### 서버에서 헤더 정보를 가져오기 위해 사용
response4 = requests.head('https://httpbin.org/get')
print(response4.headers)

### 6) requests.options()
### 서버에서 지원하는 HTTP 메서드를 확인하기 위해 사용
response5 = requests.options('https://httpbin.org/get')
print(response5.headers)

### 7) requests.patch()
### 서버에서 리소스의 일부를 수정하기 위해 사용
response6 = requests.patch('https://httpbin.org/patch', data={'key': 'value'})
print(response6.text)

### 8) requests.request()
### 원하는 HTTP 메서드를 사용하여 요청을 보낼 수 있는 범용 메서드
response7 = requests.request('GET', 'https://httpbin.org/get')
print(response7.text)