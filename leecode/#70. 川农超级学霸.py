filename = 'C:\\Users\\Administrator\\Desktop\\70.file.txt'
data = []
with open(filename) as f:
    for i in f.readlines():
        i = i.split(' ')
        data.append(i)

epochs: int = int(data[0][0])
course_dict: dict = {}
for course_inf in data[1:]:
    course_dict[course_inf[0]] = [i.strip('\n') for i in course_inf[1:] if i.strip('\n') != 'E']

max_score: int = 0
print(course_dict)
def dfs(studied_course: set, score: int, alternative_course_list:list):
    global max_score
    for i in alternative_course_list:
        if i not in studied_course:
            if len(course_dict[i]) <= 1:
                max_score = max(max_score, score + int(course_dict[i][0]))
            else:
                studied_course.add(i)
                dfs(studied_course, score + int(course_dict[i][0]), course_dict[i][1:])



dfs(studied_course=set(), score=0, alternative_course_list=list(course_dict.keys()))
print(max_score)