'programmer:BoYu-Du by:2020/11/17 summary:This program is used to simulate continuous storage allocation management.'


def writer_log(**kwargs):
    def inner(obj):
        return obj
    print(f'''
    Programmer: {kwargs['writer']}
    By:{kwargs['by']}
    Summary:This program is used to simulate {kwargs['summary']}.
    ''')
    return inner


