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