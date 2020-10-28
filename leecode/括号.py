result: list = []

def generate_bracket(n, l=0, r=0, string=''):
    l == r == n and result.append(string)
    l < n and generate_bracket(n, l + 1, r, string + '(')
    r < l and generate_bracket(n, l, r + 1, string + ')')


def generate_bracket_(n, string: str = ''):
    if n:
        for op in ['(', ')']:
            generate_bracket_(n=n - 1, string=string + op)
    else:
        result.append(string)


generate_bracket_(6)
print(result)
