class Node(object):
    """节点"""

    def Node(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self._head = None

    def is_empty(self):
        """链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        pass

    def travel(self):
        """遍历整个链表"""
        pass

    def add(self):
        """链表头部添加元素"""
        pass

    def append(self):
        """链表尾部添加元素"""
        pass

    def insert(self):
        """指定位置添加元素"""
        pass

    def remove(self):
        """删除节点"""
        pass

    def search(self):
        """查找节点是否存在"""


sing_obj = SingleLinkList()
sing_obj.travel()
