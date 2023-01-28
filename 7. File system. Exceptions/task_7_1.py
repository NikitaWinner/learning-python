import os


def create_folders(structure: dict):
    """Функция принимает структуру для создания иерархии папок"""
    for main_folder, sub_folders in structure.items():
        for sub_folder in sub_folders:
            os.makedirs(os.path.join(main_folder, sub_folder), exist_ok=True)


lisr_dirs = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
abs_path = os.path.abspath(__file__)  # C:\Users\Xiaomi\Desktop\GeekBrains\Python_base_1\hw_7\task_7_1.py

dict_dirs = {
    'my_project_1':[
        'settings',
        'mainapp',
        'adminapp',
        'authapp'
    ]
}

create_folders(dict_dirs)