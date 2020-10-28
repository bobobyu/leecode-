def suffix_prefix_dict(string: str):
    sp_list = []
    for i in range(len(string)):
        alternative_string = string[:i + 1]
        p_string = ''
        s_string = ''
        max_length = 0
        for p, s in zip(alternative_string[:-1], alternative_string[1:][::-1]):
            p_string += p
            s_string = s + s_string
            if p_string == s_string:
                max_length=len(p_string)
        sp_list.append(max_length)
    return sp_list


def KMP(source: str, template: str):
    sp_list = suffix_prefix_dict(template)
    print(sp_list)
    source_point: int = 0
    template_point: int = 0
    template_length: int = len(template)
    source_length: int = len(source)
    while template_point < template_length  and source_point < source_length :
        print(template_point, source_point)
        if source[source_point] == template[template_point]:
            template_point += 1
        else:
            template_point = sp_list[template_point]
        source_point += 1

    if template_point == template_length - 1:
        return source_point - template_length + 1
    else:
        return -1


print(KMP(source='cabababababac', template='ababab'))
