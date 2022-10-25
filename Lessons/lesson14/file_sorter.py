import os
import shutil

my_path = r'C:\Users\Алексей\Downloads'

extensions = {
    '.docx': 'Word',
    '.jpg': 'Pictures',
    '.xlsx': 'Excel',
    '.mp3': 'Music'
}


def sorter(main_path: str):
    os.chdir(main_path)
    content = os.listdir()
    for file in content:
        if os.path.isfile(f'{main_path}\\{file}'):
            tag = os.path.splitext(file)[1]
            try:
                os.mkdir(extensions.setdefault(tag, 'Others'))
                shutil.move(f'{main_path}\\{file}', f'{main_path}\\{extensions[tag]}')
            except OSError:
                shutil.move(f'{main_path}\\{file}', f'{main_path}\\{extensions[tag]}')


sorter(my_path)