class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        first = event1 if event1[0] < event2[0] else event2
        second = event2 if first == event1 else event1
        if second[0] <= first[1]:
            return True
        else:
            return False