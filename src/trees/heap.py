class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left = None
        self.right = None
        self.parent = None


class MinHeap:
    def __init__(self):
        self.root = None
        self.size = 0
        

    # -------------------------
    # INSERT
    # -------------------------
    def insert(self, value: int) -> None:
        new_node = Node(value)
        self.size += 1

        # if heap is empty
        if self.root is None:
            self.root = new_node
            return

        # find parent
        parent = self._get_parent(self.size)

        if parent.left is None:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.parent = parent
        self.bubble_up(new_node)

    # -------------------------
    # GET MIN
    # -------------------------
    def get_min(self) -> int | None:
        return self.root.value if self.root else None

    # -------------------------
    # BUBBLE UP
    # -------------------------
    def bubble_up(self, node) -> None:
        while node.parent and node.value < node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent

    # -------------------------
    # BUBBLE DOWN
    # -------------------------
    def bubble_down(self, node: Node) -> None:
        while node:

            smallest = node

            if node.left and node.left.value < smallest.value:
                smallest = node.left

            if node.right and node.right.value < smallest.value:
                smallest = node.right

            if smallest == node:
                break

            node.value, smallest.value = smallest.value, node.value
            node = smallest

    # -------------------------
    # GET PARENT (by index path)
    # -------------------------
    def _get_parent(self, index) -> Node:
        path = bin(index)[3:]
        current = self.root

        for bit in path[:-1]:
            if bit == "0":
                current = current.left
            else:
                current = current.right

        return current

    # -------------------------
    # DELETE MIN
    # -------------------------
    def delete_min(self) -> int | None:

        if self.root is None:
            return None

        min_value = self.root.value

        if self.size == 1:
            self.root = None
            self.size = 0
            return min_value

        # find last node
        path = bin(self.size)[3:]
        current = self.root

        for bit in path:
            if bit == "0":
                current = current.left
            else:
                current = current.right

        last_node = current

        # move last value to root
        self.root.value = last_node.value

        # remove last node
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        self.size -= 1

        # fix heap
        self.bubble_down(self.root)

        return min_value

    # -------------------------
    # SEARCH (boolean)
    # -------------------------
    def search(self, node, value: int) -> bool:

        if node is None:
            return False

        if node.value == value:
            return True

        return self.search(node.left, value) or self.search(node.right, value)

    # -------------------------
    # FIND NODE (returns Node)
    # -------------------------
    def find_node(self, node: Node | None, value: int) -> Node | None:

        if node is None:
            return None

        if node.value == value:
            return node

        return (
            self.find_node(node.left, value)
            or self.find_node(node.right, value)
        )

    # -------------------------
    # DELETE VALUE
    # -------------------------
    def delete_value(self, value: int) -> bool:

        if self.root is None:
            return False

        target = self.find_node(self.root, value)

        if target is None:
            return False

        # find last node
        path = bin(self.size)[3:]
        current = self.root

        for bit in path:
            if bit == "0":
                current = current.left
            else:
                current = current.right

        last_node = current

        # replace value
        target.value = last_node.value

        # remove last node
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        self.size -= 1

        # fix heap property
        self.bubble_down(target)

        if target.parent and target.value < target.parent.value:
            self.bubble_up(target)

        return True