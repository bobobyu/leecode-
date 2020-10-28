class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        result: list = []
        candidates.sort()
        check_layer_valid: list = [[] for _ in range(target // candidates[0])]

        def recursion(sol: list, layer: int = 0, target: int = target):

            if target >= 0:
                for j, i in enumerate(candidates):
                    val = i
                    if not sol:
                        layer = j
                    print(val, sol, target, check_layer_valid)
                    if val not in [j for j in i for i in check_layer_valid]:
                        if val == target:
                            [check_layer_valid[layer].append(j) for j in set(sol + [val])]
                            result.append(sol + [val])
                        # check_layer_valid[layer].append(val)
                        recursion(sol=sol + [val], layer=layer, target=target - val)

        recursion(sol=[], target=target)
        return result


s = Solution()
print(s.combinationSum([2, 3, 5], 8))
