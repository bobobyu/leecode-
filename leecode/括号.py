result: list = []

def generate_bracket(n, l=0, r=0, string=''):
    l == r == n and result.append(string)
    l < n and generate_bracket(n, l + 1, r, string + '(')
    r < l and generate_bracket(n, l, r + 1, string + ')')


generate_bracket(6)
print(result)
