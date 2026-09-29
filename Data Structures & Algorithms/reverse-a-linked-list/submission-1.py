# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next        # ✓ 把右边那个人记住
            curr.next = prev       # ✓ 改牵左边
            prev = curr
            curr = nxt        # ← 自己往前走一步,走到刚才存的那个人
        return prev



        