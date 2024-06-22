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


## 2) 튜플 (Tuple)
## 정의: 순서가 있는 변경 불가능한 데이터 구조
## 특징:
### 1. 인덱스로 접근 가능
### 2. 중복 요소 허용
### 3. 불변성 (immutable)
### 4. 좌표 (x, y)를 저장할 때
my_tuple = (1, 2, 3, 'a', 'b')
print(my_tuple)


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


## 4) 집합 (set)
## 정의: 순서가 없고 중복을 허용하지 않는 데이터 구조
## 특징:
### 1. 요소의 순서가 없음
### 2. 중복 요소 허용하지 않음
### 3. 수학적 집합 연산 지원 (합집합, 교집합 등)
### 4. 고유 요소 저장: 사용자ID 저장할 때 
my_set = {1, 2, 3}
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

## 리스트의 처음에 요소 삽입
my_list_insert.insert(0, 'a')
print(my_list_insert)

## 리스트의 중간에 요소 삽입
my_list_insert.insert(2, 'b')
print(my_list_insert)

## 리스트의 끝에 요소 삽입
my_list_insert.insert(10, 'c')
print(my_list_insert)

## 음수 인덱스를 사용하여 요소 삽입
my_list_insert.insert(-1, 'd')
print(my_list_insert)