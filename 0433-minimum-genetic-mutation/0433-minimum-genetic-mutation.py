class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        Output: 2
        """
        
        
        queue = deque([(start, 0)])
        seen = { start }
        
        while queue:
            node, steps = queue.popleft()
            if node == end:
                return steps

            for gene in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + gene + node[i + 1:]
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)

        return -1