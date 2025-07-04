# LeetCode Problem: Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        array = []  
        while current:
            array.append(current.val)
            current = current.next  

        result = [] 
        length = len(array)

        for i in range(length):
            power = length - 1 - i  
            value = array[i] * (2 ** power)
            result.append(value)

        total = 0
        for num in result:
            total += num  

        return total
