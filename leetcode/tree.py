class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lstToTreeNode(inputValues):
    if not inputValues:
        return None

    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item is not None:
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item is not None:
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


if __name__ == '__main__':

    tree = lstToTreeNode([1,2,3,4,None,5])
    print("ok")
