import os, random
import time
import getpass
import webbrowser

current_user = getpass.getuser()

file_path = ['C://Users/', current_user, '/music']

current_dir_path = 'current_dir.txt'

global basedir
basedir = 'C://users/'

current_dir = 'C://users'

#make program read txt to find and append directory paths
#append to current path with user input ie. user type ex. Games, while in desktop, it appends \games to current path


def quick_dir():
    current_user = getpass.getuser()
    quickdir_input01 = input('input directory: ')
    if quickdir_input01 == 'music' or quickdir_input01 == 'Music':
        music_path = [basedir, current_user, '/Music']
        music_path_real = ''.join(music_path)
        try:
            music_path_stripped = music_path_real.strip('"')
            current_dir = music_path_stripped
            print_music = os.listdir(current_dir)
            print_music_2 = '\n'.join(print_music)
            print(print_music_2)
            dir_music = open(current_dir_path, 'w+')
            dir_music.write(music_path_stripped)
            dir_music.close()
        except Exception as a:
            print(a)
    elif quickdir_input01 == 'documents' or quickdir_input01 == 'Documents':
        document_path = [basedir, current_user, '/Documents']
        doc_path_real = ''.join(document_path)
        try:
            doc_path_stripped = doc_path_real.strip('"')
            current_dir = doc_path_stripped
            dir_docs = open(current_dir_path,'w+')
            dir_docs.write(doc_path_stripped)
            dir_docs.close()
        except Exception as b:
            print(b)
    elif quickdir_input01 == 'pictures' or quickdir_input01 == 'Pictures':
        pictures_path = [basedir, current_user, '/Pictures']
        pic_path_real = ''.join(pictures_path)
        try:
            pic_path_stripped = pic_path_real.strip('"')
            current_dir = pic_path_stripped
            print_list_pics = os.listdir(current_dir)
            print_list_pics_02 = '\n'.join(print_list_pics)
            print(print_list_pics_02)
            dir_pics = open(current_dir_path,'w+')
            dir_pics.write(pic_path_stripped)
            dir_pics.close()
        except Exception as c:
            print(c)
    elif quickdir_input01 == 'desktop' or quickdir_input01 == 'Desktop':
        desktop_path = [basedir, current_user, '/Desktop']
        desk_path_real = ''.join(desktop_path)
        try:
            desk_path_stripped = desk_path_real.strip('"')
            current_path = desk_path_stripped
            dir_desk = open(current_dir_path,'w+')
            dir_desk.write(desk_path_stripped)
            dir_desk.close()
        except Exception as d:
            print(d)
    elif quickdir_input01 == 'downloads' or quickdir_input01 == 'download' or quickdir_input01 == 'Download' or quickdir_input01 == 'Downloads':
        download_path = [basedir, current_user, '/Downloads']
        download_path_real = ''.join(download_path)
        try:
            stripped_download = download_path_real.strip('"')
            dir_download = open(current_dir_path,'w+')
            dir_download.write(stripped_download)
            dir_download.close()
        except Exception as e:
            print(e)
    else:
        new_path = quickdir_input01
        try:
            stripped_path = new_path.strip('"')
            current_dir = stripped_path
            dir_custom = open(current_dir_path,'w+')
            dir_custom.write(stripped_path)
            dir_custom.close()
            print_new_dir = os.listdir(current_dir)
            print_new_dir_real = '\n'.join(print_new_dir)
            print(print_new_dir_real)
        except Exception as f:
            print(f)
def cd():
    quick_dir()
def help_list():
    print('Command List:\ncd\nopen\nrandom\ntime\ncalculator\nquit\n\ncd quick commands:\ndocuments\nmusic\ndownloads\ndesktop\npictures\n')
def random_file():
    try:
        file_01 = open(current_dir_path,'r')
        file_02 = file_01.read()
        file_03 = ''.join(file_02)
        file_01.close()
        try:
            file_stripped = file_03.strip('"')
            try:
                file = random.choice([x for x in os.listdir(file_stripped) if os.path.isfile(os.path.join(file_stripped, x))])
                print('Opening Random File {}...'.format(file))
                os.startfile(os.path.join(file_stripped, file))
            except Exception as k:
                print(k)
        except Exception as l:
            print(l)
    except Exception as m:
        print(m)
    # call command is random
def open_folder():
    dir_file = open(current_dir_path,'r')
    dir_list_path = dir_file.read()
    print(dir_list_path, end='')
    open_folder_command = input(': ')
    open_folder_command_stripped = open_folder_command.strip('"')
    dir_list = [dir_list_path, '/', open_folder_command_stripped]
    dir_file.close()
    try:
        real_dir = ''.join(dir_list)
        stripped_real_dir_folder = real_dir.strip('"')
        dir_new_path = open(current_dir_path,'w+')
        dir_new_write =  dir_new_path.write(stripped_real_dir_folder)
        print_list = os.listdir(stripped_real_dir_folder)
        print_list_02 = '\n'.join(print_list)
        print(print_list_02)
        dir_new_path.close()
    except Exception as n:
        print(n)
def open_file():
    dir_file = open(current_dir_path,'r')
    dir_list_path = dir_file.read()
    print(dir_list_path, end='')
    open_file_command = input(': ')
    open_file_command_stripped = open_file_command.strip('"')
    dir_list = [dir_list_path, '/', open_file_command_stripped]
    dir_file.close()
    try:
        real_dir = ''.join(dir_list)
        try:
            try:
                stripped_real_dir = real_dir.strip('"')
                os.startfile(stripped_real_dir)
            except Exception as i:
                print(i)
        except Exception as j:
            print(j)
    except Exception as g:
        print(g)

def add_quick_directory():
    print('Not Implemented Yet.')
    #adds directory as a quick_dir command
def calc():
    print('\n\nNot implemented at this time.\n\n')
def list_dir():
    dir_file = open(current_dir_path,'r')
    dir_list_path = dir_file.read()
    dir_list = os.listdir(dir_list_path)
    dir_list_real = '\n'.join(dir_list)
    print(dir_list_real)
    dir_file.close()
    #lists files and folders in directory

def main():
    main_loop_01 = True
    while main_loop_01 == True:
        print(current_user, '\n\n', current_dir, end='')
        command_input = input(': ')
        if command_input == 'cd' or command_input == 'dir' or command_input == 'directory':
            cd()
        elif command_input == 'help':
            help_list()
        elif command_input == 'random' or command_input == 'Random':
            random_file()
        elif command_input == 'open' or command_input == 'Open':
            list_dir()
            print('Open File or Folder?', end='')
            open_question = input(': ')
            if open_question == 'file' or open_question == 'File':
                open_file()
            elif open_question == 'folder' or open_question == 'Folder':
                open_folder()
        elif command_input == 'time' or command_input == 'Time':
            print('\n\n')
            print(time.strftime("%X %x"))
            print('\n\n')
        elif command_input == 'calc' or command_input == 'calculator' or command_input == 'Calculator' or command_input == 'Calc':
            pass
        elif command_input == 'quit' or command_input == 'exit':
            main_loop_01 = False
        elif command_input == 'listdir':
            list_dir()
        else:
            pass

if __name__ == '__main__':
    main()
