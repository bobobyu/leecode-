from typing import *
from File_System_Control import *
import tkinter as tk


class GUI:
    def __init__(self):
        self.system: FileSystem = FileSystem()

    def map_function(self):
        map_function: Dict[Callable] = {i: j for i, j in
                                        zip(('初始化系统', '创建新文件', '复制文件', '打开文件', '删除文件', '打开文件目录', '展示磁盘信息'),
                                            self.system.program_dict.values())}

        map_function[self.selection_boxes.get(self.selection_boxes.curselection())]()

    def initial(self):
        system_window = tk.Tk()
        system_window.title('File System Control GUI')
        system_window.geometry('500x500')

        # 定义头交互窗口
        interaction_window = tk.Label(system_window,
                                      text='文件管理系统启动成功，\n请选择以下功能:(！初次使用请先进行初始化！)',
                                      bg='yellow',
                                      font=('Arial', 9),
                                      width=50,
                                      height=12)

        # 定义确认按钮
        affirm_button: tk.Button = tk.Button(system_window,
                                             text='启动你选择的功能',
                                             width=13,
                                             height=1,
                                             command=self.map_function)
        # 定义选择框
        system_function = tk.Variable()
        system_function.set(('初始化系统', '创建新文件', '复制文件', '打开文件', '删除文件', '打开文件目录', '展示磁盘信息'))
        self.selection_boxes = tk.Listbox(system_window, listvariable=system_function)

        # 此处控制布局
        interaction_window.pack()
        affirm_button.pack()
        self.selection_boxes.pack()

        # 循环窗口
        system_window.mainloop()


g = GUI()
g.initial()
