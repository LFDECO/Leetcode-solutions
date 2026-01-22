class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = list(zip(names, heights))
        pairs.sort(key=lambda x: x[1], reverse=True)

        result = []
        for name, height in pairs:
            result.append(name)

        return result
