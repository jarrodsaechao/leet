# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []

        # grab the head of each linked list
        for i,head in enumerate(lists):
            if head:
                heapq.heappush(heap,(head.val,i,head))



        temp = ListNode()
        curr = temp


        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            # Check if extracted node has a next node
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))


        return temp.next