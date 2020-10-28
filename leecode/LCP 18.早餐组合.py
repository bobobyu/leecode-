class Solution:
    def breakfastNumber(self, staple: list, drinks: list, x: int) -> int:
        pro_staple = sorted([i for i in staple if i < x])
        pro_drinks = sorted([i for i in drinks if i < x])
        s_drink = len(pro_drinks)
        s_staple = len(pro_staple)
        count_ = 0
        step = 0
        print(pro_staple, pro_drinks)
        if pro_drinks and pro_staple:
            for i in range(s_drink - 1, -1, -1):
                while step < s_staple and pro_drinks[i] + pro_staple[step] <= x:
                    step += 1
                if step == s_staple:
                    count_ += (i + 1) * step
                    return count_
                count_ += step
                step -= 1
                step = max(0, step)
                print(step)
            return count_
        return 0


s = Solution()
print(s.breakfastNumber([7, 3, 4, 3, 9, 9, 10, 8, 8, 3],
                        [1],
                        5
                        ))
