from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x:(x[0],-x[1]))
        scores = defaultdict(list)
        for item in items:
            student = item[0]
            score = item[1]
            scores[student].append(score)
        solution = []
        for student in scores:
            total = 0
            k = 5
            while k > 0:
                total += scores[student][k - 1]
                k -= 1
            solution.append([student, total // 5])
        return solution