def cut_cross_array(prices_list: list, low: int, middle: int, high: int):
    left_max = -float('inf')
    _sum: int = 0
    left_mark_: int = 0
    if middle != low:
        for i in range(middle, low - 1, -1):
            _sum += prices_list[i]
            if _sum > left_max:
                left_mark_ = i
                left_max = _sum
    else:
        left_max = prices_list[low]
        left_mark_ = low
    if middle + 1 != high:
        right_max = -float('inf')
        _sum: int = 0
        right_mark_: int = 0
        for i in range(middle + 1, high):
            _sum += prices_list[i]
            if _sum > right_max:
                right_mark_ = i
                right_max = _sum
    else:
        right_max = prices_list[high]
        right_mark_ = high
    return left_mark_, right_mark_, right_max + left_max


def max_subset(prices: list, low: int, high: int):
    if low == high:
        return low, high, prices[low]
    middle = int((low + high) / 2)
    left_low, left_high, _left_max = max_subset(low=low,
                                                high=middle,
                                                prices=prices)
    right_low, right_high, _right_max = max_subset(low=middle + 1,
                                                   high=high,
                                                   prices=prices)
    left_mark_, right_mark_, right_and_left_max = cut_cross_array(prices_list=prices,
                                                                  low=low,
                                                                  middle=middle,
                                                                  high=high)
    if _left_max >= _right_max and _left_max >= right_and_left_max:
        return left_low, left_high, _left_max

    elif _right_max >= _left_max and _right_max >= right_and_left_max:
        return right_low, right_high, _right_max
    else:
        return left_mark_, right_mark_, right_and_left_max


a = [0, -6, 4, -2, 3, -2]
print(max_subset(a, 0, 2))



