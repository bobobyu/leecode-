def wrapper(fun):
    def inner(*args):
        print('''
        programmer: BoYu-Du
        by:2020/11/17
        summary:This program is used to simulate continuous storage allocation management.
        ''')
        fun(args)
    inner()

