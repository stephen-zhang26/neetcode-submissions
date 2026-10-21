class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        # 一棵空树，只有根

        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()       # ① 这条路没有，造一个新节点
            cur = cur.children[c]                       # ② 往下走一格
        cur.endOfWord = True       
        

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():     # ① 遍历所有子节点
                        if dfs(i+1, child):              # ② 从下一个字符接着匹配
                            return True
                    return False                           # ③ 所有分支都试过了，都不通

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]                            # ④ 和昨天一样，往下走

            return cur.endOfWord                                   # ⑤ 和昨天 search 最后一行一样

        return dfs(0, self.root)                            # 从第 0 个字符、从根开始
        
