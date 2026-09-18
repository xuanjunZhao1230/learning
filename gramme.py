class Node:
    """缓存中的一个节点"""

    def __init__(self, key=0, value=0):
        # 缓存的键
        self.key = key

        # 缓存的值
        self.value = value

        # 当前节点被使用的次数
        # 新节点第一次放入缓存时，频率为 1
        self.freq = 1

        # 双向链表中的前一个节点
        self.prev = None

        # 双向链表中的后一个节点
        self.next = None


class DoublyLinkedList:
    """
    双向链表。

    同一个链表中的所有节点，使用次数 freq 相同。

    链表左边：
        最久没有被使用的节点

    链表右边：
        最近刚使用过的节点
    """

    def __init__(self):
        # 虚拟头节点
        self.head = Node()

        # 虚拟尾节点
        self.tail = Node()

        # 初始状态：
        # head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

        # 记录真实节点数量
        self.size = 0

    def append(self, node):
        """
        把节点添加到链表尾部。

        尾部表示：
        最近刚刚被使用过。
        """

        # 原来尾节点前面的节点
        previous_node = self.tail.prev

        # previous_node <-> node
        previous_node.next = node
        node.prev = previous_node

        # node <-> tail
        node.next = self.tail
        self.tail.prev = node

        self.size += 1

    def remove(self, node):
        """从链表中删除指定节点"""

        previous_node = node.prev
        next_node = node.next

        # 跳过 node：
        # previous_node <-> next_node
        previous_node.next = next_node
        next_node.prev = previous_node

        # 断开 node 原来的连接
        node.prev = None
        node.next = None

        self.size -= 1

    def pop_left(self):
        """
        删除并返回最左边的真实节点。

        最左边的节点就是：
        在相同使用次数中，最久没有使用的节点。
        """

        # 链表为空
        if self.size == 0:
            return None

        # head 后面的第一个真实节点
        node = self.head.next

        self.remove(node)

        return node

    def is_empty(self):
        """判断链表是否为空"""

        return self.size == 0


class LFUCache:
    """
    LFU 缓存：

    LFU = Least Frequently Used
    优先删除使用次数最少的元素。

    如果使用次数相同：
    删除其中最久没有使用的元素。
    """

    def __init__(self, capacity: int):
        # 缓存的最大容量
        self.capacity = capacity

        # key -> Node
        #
        # 通过 key 快速找到节点
        self.key_to_node = {}

        # freq -> DoublyLinkedList
        #
        # 每一种使用次数，对应一条双向链表
        #
        # 例如：
        # 1 -> 所有使用次数为 1 的节点
        # 2 -> 所有使用次数为 2 的节点
        self.freq_to_list = {}

        # 当前缓存中最小的使用次数
        #
        # 删除元素时，直接找到：
        # freq_to_list[min_freq]
        self.min_freq = 0

    def get(self, key: int) -> int:
        """
        根据 key 获取 value。

        key 不存在：
            返回 -1

        key 存在：
            返回 value
            并且该节点使用次数加 1
        """

        # key 不在缓存中
        if key not in self.key_to_node:
            return -1

        # 找到对应节点
        node = self.key_to_node[key]

        # 节点被访问了一次，更新使用次数
        self._increase_frequency(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        """
        添加或更新缓存数据。
        """

        # 容量为 0，无法保存任何数据
        if self.capacity == 0:
            return

        # 情况一：key 已经存在
        if key in self.key_to_node:
            node = self.key_to_node[key]

            # 更新 value
            node.value = value

            # put 已存在的 key，也算使用了一次
            self._increase_frequency(node)

            return

        # 情况二：key 不存在，需要创建新节点

        # 如果缓存已经满了，需要先删除一个节点
        if len(self.key_to_node) >= self.capacity:
            # 使用次数最少的节点都在：
            # freq_to_list[min_freq]
            min_freq_list = self.freq_to_list[self.min_freq]

            # 相同使用次数中，
            # 删除最久没有被使用的节点
            removed_node = min_freq_list.pop_left()

            # 从 key 字典中删除
            del self.key_to_node[removed_node.key]

        # 创建新节点
        new_node = Node(key, value)

        # 保存到 key -> node 字典
        self.key_to_node[key] = new_node

        # 新节点的使用次数为 1
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()

        # 新节点放入使用次数为 1 的链表尾部
        self.freq_to_list[1].append(new_node)

        # 新节点的频率是 1，
        # 所以当前最小频率一定变成 1
        self.min_freq = 1

    def _increase_frequency(self, node):
        """
        节点被访问后，将使用次数加 1。

        例如：
        节点原来在 freq=1 的链表中，
        访问后移动到 freq=2 的链表中。
        """

        # 保存旧频率
        old_freq = node.freq

        # 找到旧频率对应的链表
        old_list = self.freq_to_list[old_freq]

        # 从旧链表删除该节点
        old_list.remove(node)

        # 如果满足：
        # 1. 该节点原来的频率正好是最小频率
        # 2. 删除后旧链表为空
        #
        # 那么最小频率要加 1
        if old_freq == self.min_freq and old_list.is_empty():
            self.min_freq += 1

        # 节点使用次数加 1
        node.freq += 1

        # 新频率对应的链表还不存在
        if node.freq not in self.freq_to_list:
            self.freq_to_list[node.freq] = DoublyLinkedList()

        # 把节点添加到新频率链表尾部
        #
        # 尾部表示该节点是最近刚刚使用的
        self.freq_to_list[node.freq].append(node)

    def print_cache(self):
        """
        仅用于学习和观察缓存状态。

        正式提交 LeetCode 时可以删除。
        """

        print(f"当前最小使用次数：{self.min_freq}")

        for freq in sorted(self.freq_to_list):
            linked_list = self.freq_to_list[freq]

            if linked_list.is_empty():
                continue

            current = linked_list.head.next
            values = []

            while current != linked_list.tail:
                values.append(
                    f"key={current.key}, "
                    f"value={current.value}, "
                    f"freq={current.freq}"
                )
                current = current.next

            print(f"频率 {freq}：", " <-> ".join(values))

        print("-" * 60)