class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        perform = {"++X": 1, "X++": 1, "X--": -1, "--X": -1}
        X = 0
        for oper in operations:
            X += perform[oper]
        return X