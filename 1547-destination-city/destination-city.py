class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()

        for a, b in paths:
            source.add(a)

        for a, b in paths:
            if b not in source:
                return b
        