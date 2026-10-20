class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()        # 一棵空树，只有根

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()       # ① 这条路没有，造一个新节点
            cur = cur.children[c]                       # ② 往下走一格
        cur.endOfWord = True                 # ③ 走完了，打开开关

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False                  # ④ 路断了
            cur = cur.children[c]
        return cur.endOfWord                          # ⑤ 路通了，但还要看什么？

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True                          # ⑥ 和⑤只差这一行