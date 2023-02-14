# 단순 연결 리스트 구현
class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

# 전역변수 만들기
memory = [] # lists
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

def printNodes(start):
    current = start
    if current == None:
        return

    print(current.data, end= ' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end=' -> ')

# 노드추가
def insertNode(findData, insertData):
    global memory, pre, current, head

    if head.data == findData: # 첫노드 앞
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head # current 제일 앞으로 당김
    while current.link == None: # 중간노드 삽입
        pre = current
        current = current.link
        
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # current.link == None 까지 옴
    node = Node()
    node.data = insertData
    current.link = node
    return

# 노드 삭제
def deleteNode(deleteData):
    global memory, pre, current, head

    if head.data == deleteData: # 첫번째 노드 삭제
        current = head
        head = head.link # 두번째 노드로 변경
        del(current)
        return

    current = head
    while current.link != None: # 첫번째 이외 노드 삭제
        pre = current # 모두 첫번째 노드를 가리킴
        current - current.link
        if current.data == deleteData:
            pre.link = current.link # current 가리키는 노드를 pre가 가리키도록 함
            del(current) # 메모리에서 삭제
            return

# 노드 검색
def findNode(findData):
    global memory, pre, current, head

    current = head # 첫번째 노드
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link # 다음노드로 넘어감
        if current.data == findData:
            return current

    return Node() # 빈노드 전환

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0] # 다현을 말함
    head = node
    memory.append(node)

    for data in dataArray[1:]: # 두번째 노드 이후 4번 반복
        pre =node
        node = Node()
        node.data = data # 정연, 쓰위, 사나, 지효 순으로 들어감
        pre.link = node
        memory.append(node)

    printNodes(head)

    insertNode('재남', '문별') # 다현을 화사로 노드 변경
    printNodes(head)

    insertNode('사나', '솔라') # 사나를 솔라로 노드 변경
    printNodes(head)

    insertNode('다현', '화사')
    printNodes(head)

    print('노드 삭제 --------')

    deleteNode('화사')
    printNodes(head)

    deleteNode('지효')
    printNodes(head)

    deleteNode('재남') # 데이터 삭제
    printNodes(head)

    print('노드 검색 -------')
    
    result = findNode('정연')
    print(result.data)

    result = findNode('재남')
    print(result.data)