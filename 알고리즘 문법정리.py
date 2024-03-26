class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            raise IndexError("push to a full stack")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def get_size(self):
        return len(self.items)


# Stack 클래스 사용 예시
size = int(input("스택의 크기를 입력하세요: "))
stack = Stack(size)

print("스택이 비어있는가?", stack.is_empty())  # 스택이 비어있는지 확인
print("스택이 가득 찼는가?", stack.is_full())   # 스택이 가득 찼는지 확인

for i in range(size):
    stack.push(i)

print("스택이 비어있는가?", stack.is_empty())  # 스택이 비어있는지 확인
print("스택이 가득 찼는가?", stack.is_full())   # 스택이 가득 찼는지 확인

print("Pop:", stack.pop())  # 스택에서 항목 꺼내기

print("Peek:", stack.peek())  # 스택의 맨 위 항목 확인

print("스택의 크기:", stack.get_size())  # 스택의 크기 확인

# 임우재 튜터 24-03-08 특강자료 ( 스택과 자료구조에 대한 설명 )
# ----------------------------------------------------------------------------------------------------
"""Usage:

heap = []            # creates an empty heap
heappush(heap, item) # pushes a new item on the heap
item = heappop(heap) # pops the smallest item from the heap
item = heap[0]       # smallest item on the heap without popping it
heapify(x)           # transforms list into a heap, in-place, in linear time
item = heapreplace(heap, item) # pops and returns smallest item, and adds
# new item; the heap size is unchanged """


def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)

def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt
    
def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    # Transform bottom-up.  The largest index there's any point to looking at
    # is the largest with a child index in-range, so must have 2*i + 1 < n,
    # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
    # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
    # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
    for i in reversed(range(n//2)):
        _siftup(x, i)