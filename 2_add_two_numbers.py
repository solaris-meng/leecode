
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def pp(self):
        msg = ''
        cur = self
        while cur:
            msg += ' %d ' % cur.val
            cur = cur.next
        print(msg)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = l3_head = ListNode(-1)
        over = 0
        while l1 or l2:
            l1_v = l1.val if l1 else 0
            l2_v = l2.val if l2 else 0

            s = l1_v + l2_v + over
            over = 0
            if s > 9:
                s = 0
                over = 1

            l3.next = ListNode(s)
            l3 = l3.next

            l1 = l1.next
            l2 = l2.next

        return l3_head.next

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)
d.next = e
e.next = f

a.pp()
d.pp()

s = Solution()
rv = s.addTwoNumbers(a, d)
rv.pp()

