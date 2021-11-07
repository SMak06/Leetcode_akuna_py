# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # def flatten_list(n):
        #     for nested_int in nested_list:
        #         if nested_int.isInteger():
        #             yeild (nested_int.getInteger())
        #         else:
        #             yeild from flatten_list(nested_int.getList()):
        
        def flatten(n):
            res = []
            for i in n:
                if i.isInteger():
                    res.append(i.getInteger())
                else:
                    res.extend(flatten(i.getList()))
            return res
        self.deq = deque(flatten(nestedList))
    
    def next(self) -> int:
        return self.deq.popleft()
        
    
    def hasNext(self) -> bool:
        return self.deq

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())