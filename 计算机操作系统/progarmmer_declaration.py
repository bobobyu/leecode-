'programmer:BoYu-Du by:2020/11/17 summary:This program is used to simulate continuous storage allocation management.'

import time
def writer_log(**kwargs):
    def inner(obj):
        return obj
    print(f'''
    Programmer :\t{kwargs.get('writer', 'BoYu-Du')}
    Running on :\t{time.asctime( time.localtime(time.time()) )}
    Summary :\t\tThis program is used to simulate {kwargs['summary']}.
    ''')
    return inner


