# 이진 탐색트리 구현
# 전역변수 선언
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']


class TreeNode:
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None

if __name__ == '__main__':
    node = TreeNode()
    node.data = nameAry[0] # 블랙핑크
    root = node 
    memory.append(node)

    for name in nameAry[1:]:
        node = TreeNode()
        node.data = name

        current = root

        while True:
            if name < current.data: # 부모노드 왼쪽으로
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else: # 부모노드 오른쪽
                if current.right == None:
                    current.right = node
                    break
                current = current.right

        memory.append(node)

    print('이진 탐색트리 구성 완료')

    print(root.data)
    print('｜     ＼')
    print(root.left.data, root.right.data)
    print('｜     ＼     ＼')
    print(root.left.left.data, root.left.right.data, root.right.right.data)

    search = input('찾을 걸그룹을 입력하세요.')
    current = root
    while True:
        if search == current.data:
            print(search, '찾았습니다.')
            break
        elif search < current.data: # 왼 쪽으로
            if current.left == None:
                print(search, '검색 결과 없음.')
                break
            else:
                current = current.left
        else: # 오른쪽 노드로
            if current.right == None:
                print(search, '못 찾았습니다.')
                break
            else:
                current = current.right