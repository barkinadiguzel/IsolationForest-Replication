from ..math.score import c_n

def path_length(x, node, current_height=0):
    if node.size is not None:
        if node.size <= 1:
            return current_height
        else:
            return current_height + c_n(node.size)
    if x[node.split_attr] < node.split_value:
        return path_length(x, node.left, current_height + 1)
    else:
        return path_length(x, node.right, current_height + 1)
