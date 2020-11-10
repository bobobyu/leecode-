class Process:
    def __init__(self, index: int, max_require: dict):
        self.sequence: list = []
        self.index: int = index
        self.max_require: dict = max_require
        self.allowed_resource: dict = {i: 0 for i in max_require.keys()}
        self.need_resource: dict = {i: self.max_require[i] - self.allowed_resource[i] for i in max_require.keys()}

    def __call__(self):
        self.allowed_resource: dict = {i: 0 for i in self.max_require.keys()}
        self.need_resource: dict = self.max_require.copy()

    def _apply_resource(self, apply_inf: dict) -> None:
        for resource_name, resource_number in apply_inf.items():
            self.allowed_resource[resource_name] = min(self.max_require[resource_name],
                                                       self.allowed_resource[resource_name] + resource_number)
            self.need_resource[resource_name] = max(0, self.max_require[resource_name] - self.allowed_resource[
                resource_name])

    def _check_finished(self) -> bool:
        for resource_name, resource_number in self.max_require.items():
            if self.allowed_resource[resource_name] != resource_number:
                return False
        return True

    def _display_information(self):
        print(
            f'{self.index}\t\t{"  ".join([str(i) for i in self.max_require.values()])}\t\t{"  ".join([str(i) for i in self.allowed_resource.values()])}\t\t\t{"  ".join([str(i) for i in self.need_resource.values()])}\t')


class ResourceControlCenter:
    def __init__(self, attainable_resource: dict):
        self.attainable_resource: dict = attainable_resource
        self.max_resource: dict = attainable_resource.copy()
        self.resource_name_list: list = list(attainable_resource.keys())

    def __call__(self):
        self.attainable_resource = self.max_resource.copy()
    def _take_back_or_allocate_resource(self, resource_dict:dict, flag:bool=False):
        if flag:
            for i in self.resource_name_list:
                self.attainable_resource[i] += resource_dict[i]
        else:
            for i in self.resource_name_list:
                self.attainable_resource[i] -= resource_dict[i]


class Banker:
    def _distribute_resource(self) -> None:
        attainable_resource: dict = {}
        resource_num: int = int(input('Please input the number of resource categories:'))
        for i in range(resource_num):
            p_name: str = input(f'The name of source {i}: ')
            p_resource: int = int(input('The number of source: '))
            attainable_resource[p_name] = p_resource
        self.rcc: ResourceControlCenter = ResourceControlCenter(attainable_resource=attainable_resource)


    def _initial_process(self) -> bool:

        self.works_number: int = int(input('Please input the number of works:'))
        self.works_dict:dict = {}
        standard_list:list = list(self.rcc.max_resource.values())
        print(
            f'Please input the max resource number that each process required(it must be a {self.works_number}x{len(self.rcc.resource_name_list)} matrix.):')
        for index in range(self.works_number):
            initial_list: list = [int(i) for i in input(':').split(' ')]
            while not  all(i <= j for i, j in zip(initial_list, standard_list)):
                print('--->Resource oversubscribed please reallocate resource!!<--')
                initial_list: list = [int(i) for i in input(':').split(' ')]
            self.works_dict[index] = Process(index=index,  max_require={i: j for i, j in zip(self.rcc.resource_name_list, initial_list)})

        self.work_list = [i for i in self.works_dict.values()]

        overflow: bool = False
        print(f'Please input the allowed resource number that each process required(it must be a {self.works_number}x{len(self.rcc.resource_name_list)} matrix.):')
        for i in range(self.works_number):
            access_flag: bool = True
            distribute_list = [int(i) for i in input(':').split(' ')]
            for j, p in enumerate(self.rcc.resource_name_list):
                distribute_ = self.rcc.attainable_resource[p] - distribute_list[j]
                if distribute_ < 0 :
                    access_flag = False
                    overflow = not overflow
                    print(
                        f'!!!!---Process {self.works_dict[i].index} Oversubscribed resources!Refuse distribute resource---!!!!')
                    break
            dis_dic = {i: j for i, j in zip(self.rcc.resource_name_list, distribute_list)}
            access_flag and self.works_dict[i]._apply_resource(dis_dic) or self.rcc._take_back_or_allocate_resource(dis_dic)
        return overflow

    def __init__(self):
        self._distribute_resource()
        self._initial_process()
        self.work_list = [i for i in self.works_dict.values()]
        self.need_list: list = [list(i.need_resource.values()) for i in self.work_list]
        self.resource_list: list = list(self.rcc.attainable_resource.values())
        print(self.need_list, self.resource_list)

        while not self._check_safe():
            re_flag = input(f'Do you want to reallocate resources?(y/n)')
            if re_flag == 'y':
                self._initial_process()
            else:
                print(f'--->Exit process<---')
                return

        print(self.rcc.attainable_resource)
        print('The distribute condition of current time:')
        print(f'\nEach resource available condition:')
        [print(f'The resource:{i}, which residue resource number:{j}') for i, j in self.rcc.attainable_resource.items()]
        print(f'\nIndex\tMax\t\t\tAllocation\t\t\tNeed')
        for i in range(self.works_number):
            self.works_dict[i]._display_information()


    def _check_safe(self) -> bool:
        safe_sequence = []
        print('--->Conduct safety checks<---')

        def deep_search(work_list: list, residue_resource: dict, sol: list):
            if not safe_sequence:
                if not work_list:
                    safe_sequence.append(sol)
                for index, process in enumerate(work_list):
                    distribute_resource: list = [residue_resource[resource] - process.need_resource[resource] for
                                                 resource in self.rcc.resource_name_list]
                    if all([i >= 0 for i in distribute_resource]):
                        [residue_resource.update(
                            {resource: residue_resource[resource] + process.allowed_resource[resource]}) for resource in
                            self.rcc.resource_name_list]
                        deep_search(work_list=work_list[:index] + work_list[index + 1:],
                                    residue_resource=residue_resource, sol=sol + [process.index])

        deep_search(work_list=self.work_list[:], residue_resource=self.rcc.attainable_resource.copy(), sol=[])
        if safe_sequence:
            print('This system is secure!This secure execute sequence is:')
            [print(safe_sequence[0][i], end=' -> ') if i != len(safe_sequence[0]) - 1 else print(_) for i, _ in enumerate(safe_sequence[0])]
            return True
        else:
            print('This system is not secure! Take back all resource!')
            [i() for i in self.work_list]
            self.rcc()
            return False


res = []

x = Banker()
