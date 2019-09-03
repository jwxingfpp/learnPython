# coding: utf-8
"""
@Time    : 2019/9/2 下午6:00
@Author  : xingjiawei
尝试建立树（从上而下）
"""
PERMS = [{"text": "\u4ea7\u54c1\u4e0e\u670d\u52a1", "id": 39, "parent": 102}, {"text": "TechProvider", "id": 40, "parent": 39}, {"text": "\u67e5\u770b\u5168\u90e8\u5ba2\u6237\u7684\u8d44\u6599", "id": 73, "parent": 741}, {"text": "\u7ba1\u7406\u5168\u90e8\u5ba2\u6237\u7684\u8d44\u6599", "id": 74, "parent": 741}, {"text": "\u7ba1\u7406\u4e0e\u914d\u7f6e", "id": 76, "parent": 102}, {"text": "\u5b50\u8d26\u53f7\u7ba1\u7406", "id": 77, "parent": 76}, {"text": "\u67e5\u770b\u5b50\u8d26\u53f7", "id": 78, "parent": 77}, {"text": "\u7f16\u8f91\u89d2\u8272", "id": 80, "parent": 77}, {"text": "FaceID", "id": 86, "parent": 103}, {"text": "\u67e5\u770b\u76d1\u63a7\u62a5\u8868", "id": 88, "parent": 86}, {"text": "\u67e5\u770b\u5e94\u7528\u914d\u7f6e", "id": 89, "parent": 86}, {"text": "\u7ed1\u5b9aBundle ID", "id": 90, "parent": 86}, {"text": "\u67e5\u8be2\u6bd4\u5bf9\u7ed3\u679c", "id": 91, "parent": 86}, {"text": "TechProvider\u5185\u90e8\u63a7\u5236\u53f0", "id": 102, "parent": "#"}, {"text": "\u63a7\u5236\u53f0", "id": 103, "parent": "#"}, {"text": "\u7f16\u8f91\u5b50\u8d26\u53f7", "id": 104, "parent": 77}, {"text": "\u5b50\u8d26\u53f7\u7ba1\u7406", "id": 107, "parent": 103}, {"text": "\u7f16\u8f91\u5b50\u8d26\u53f7 ", "id": 109, "parent": 107}, {"text": "\u67e5\u770b\u5b50\u8d26\u53f7", "id": 115, "parent": 107}, {"text": "\u7f16\u8f91\u89d2\u8272", "id": 116, "parent": 107}, {"text": "\u7ba1\u7406\u81ea\u6709\u5ba2\u6237\u8d44\u6599", "id": 117, "parent": 741}, {"text": "\u67e5\u770b\u7528\u91cf\u3001\u6982\u89c8\u3001API\u76d1\u63a7\u62a5\u8868", "id": 119, "parent": 742}, {"text": "\u67e5\u770b\u7528\u91cf\u62a5\u8868", "id": 134, "parent": 86}, {"text": "\u7528\u6237\u6b21\u6570\u5305\u7ba1\u7406", "id": 530, "parent": 228}, {"text": "\u4fc3\u9500\u89c4\u5219\u7ba1\u7406", "id": 595, "parent": 228}, {"text": "\u5ba2\u6237\u63a5\u5165\u5ba1\u6279\u6743", "id": 624, "parent": 743}, {"text": "\u67e5\u770b\u6388\u6743\u6982\u89c8", "id": 625, "parent": 77}, {"text": "\u67e5\u770b\u6388\u6743\u6982\u89c8", "id": 626, "parent": 107}, {"text": "\u4fee\u6539\u5ba2\u6237\u6ce8\u518c\u90ae\u7bb1", "id": 706, "parent": 743}, {"text": "\u4ee3\u7406\u5546\u63a7\u5236\u53f0", "id": 711, "parent": "#"}, {"text": "", "id": 716, "parent": "#"}, {"text": "\u67e5\u770bAPI\u6bd4\u5bf9\u7ed3\u679c\u3001\u5ba1\u6838", "id": 717, "parent": 742}, {"text": "\u8ba1\u91cf\u8ba1\u8d39", "id": 718, "parent": 711}, {"text": "\u67e5\u770b\u5168\u90e8\u5ba2\u6237\u7684\u8ba1\u91cf\u4fe1\u606f", "id": 719, "parent": 718}, {"text": "\u5b50\u8d26\u53f7\u7ba1\u7406", "id": 720, "parent": 711}, {"text": "\u67e5\u770b\u5b50\u8d26\u53f7", "id": 721, "parent": 720}, {"text": "\u7f16\u8f91\u89d2\u8272", "id": 722, "parent": 720}, {"text": "\u7f16\u8f91\u5b50\u8d26\u53f7", "id": 723, "parent": 720}, {"text": "\u67e5\u770b\u6388\u6743\u6982\u89c8", "id": 724, "parent": 720}, {"text": "Megvii\u5185\u90e8\u63a7\u5236\u53f0", "id": 726, "parent": "#"}, {"text": "\u4ea7\u54c1\u4e0e\u670d\u52a1", "id": 728, "parent": 726}, {"text": "\u8bbe\u7f6eQPS", "id": 729, "parent": 728}, {"text": "\u7ba1\u7406\u4e0e\u914d\u7f6e", "id": 730, "parent": 726}, {"text": "\u5b50\u8d26\u53f7\u7ba1\u7406", "id": 731, "parent": 730}, {"text": "\u67e5\u770b\u5b50\u8d26\u53f7", "id": 732, "parent": 731}, {"text": "\u7f16\u8f91\u89d2\u8272", "id": 733, "parent": 731}, {"text": "\u7f16\u8f91\u5b50\u8d26\u53f7", "id": 734, "parent": 731}, {"text": "\u67e5\u770b\u6388\u6743\u6982\u89c8", "id": 735, "parent": 731}, {"text": "\u7ba1\u7406\u5168\u90e8\u5ba2\u6237\u7684\u8d44\u6599", "id": 736, "parent": 728}, {"text": "\u67e5\u770b\u5168\u90e8\u5ba2\u6237\u7684\u7528\u91cf\u4fe1\u606f", "id": 737, "parent": 728}, {"text": "\u67e5\u770b\u5168\u90e8\u5ba2\u6237\u7684\u5ba1\u6838\u3001API\u6bd4\u5bf9\u7ed3\u679c", "id": 738, "parent": 728}, {"text": "\u67e5\u770b\u5168\u90e8\u5ba2\u6237\u7684API\u76d1\u63a7\u62a5\u8868\u3001\u6982\u89c8", "id": 739, "parent": 728}, {"text": "\u5ba1\u6838\u9a8c\u8bc1\u6570\u636e", "id": 740, "parent": 86}, {"text": "\u5ba2\u6237\u8303\u56f4", "id": 741, "parent": 40}, {"text": "\u67e5\u770b\u9875\u9762\u8303\u56f4", "id": 742, "parent": 40}, {"text": "\u5176\u4ed6\u6743\u9650", "id": 743, "parent": 40}]


class TreeNode():
    def __init__(self, name, id, pid):
        self.name = name
        self.id = id
        self.pid = pid
        self.children = []


def read_perm(perm):
    if perm['parent'] == '#':
        node = TreeNode(perm['text'], perm['id'], None)
    else:
        node = TreeNode(perm['text'], perm['id'], perm['parent'])
    return node


def get_nodes():
    node_list = []
    root_node = []
    for perm in PERMS:
        node = read_perm(perm)
        if node.pid is None:
            root_node.append(node)
        else:
            node_list.append(node)
    return root_node, node_list


def build_tree(root, node_list):
    for node in node_list:
        if node.pid == root.id:
            root.children.append(node)
            node_list.remove(node)
            build_tree(node, node_list)
    return root


def read_tree(root):
    if not root.children:
        return [root.name]
    perms = [item.name for item in root.children]
    perm_ins = [item for item in root.children]
    for perm in perm_ins:
        texts = read_tree(perm)
        perms.extend(texts)
    return perms


def up_travel(node, perm_list):
    for perm in perm_list:
        if perm.id == node.pid:
            p_node = read_perm(perm)
            p_node.children.append(node)
            perm_list.remove(perm)
            up_travel(p_node, perm_list)
    return node

if __name__ == '__main__':
    roots, nodes = get_nodes()
    for root in roots:
        build_tree(root, nodes)
        perms = read_tree(root)
        print perms