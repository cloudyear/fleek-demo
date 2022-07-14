class Node(object):
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


def condense(head: Node) -> Node:
    nodeSet = set()
    pre = dummy = Node(0)
    dummy.next = head
    pre = dummy
    while head != None:
        if head.data in nodeSet:
            pre.next = head.next
        else:
            nodeSet.add(head.data)
            pre = head
        head = pre.next
    return dummy.next


def printAll(head: Node):
    while head != None:
        print(head.data)
        head = head.next


if __name__ == "__main__":
    node1 = Node(3)
    node2 = Node(4)
    node3 = Node(3)
    node4 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    printAll(node1)
    print("========")
    newNode = condense(node1)
    printAll(newNode)
