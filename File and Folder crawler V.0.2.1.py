import os, random
import time
import getpass
import webbrowser
import math

current_user = getpass.getuser()

file_path = ['C://Users/', current_user, '/music']

current_dir_path = 'current_dir.txt'

global basedir
basedir = 'C://users/'

current_dir = 'C://users'

#make program read txt to find and append directory paths -done
#append to current path with user input ie. user type ex. Games, while in desktop, it appends \games to current path -done
#Add webbrowser.open(https:webpage) function -done
#Add Calculator and unit conversion class - 1/2 done (unit conversion pending)
#Add all current functions to class. Call class subfunctions from main, by class.function -done
#Came up with folder crawler while making random file opener
#cut down the write function to one, instead of rewriting everytime
#isolate the first word of input in order to allow commands like cd music, instead of cd, then music. ala. the calculator class, with 1 + 1.
#make powershell function that opens powershell as admin


class folder_crawler():
    def quick_dir():
        current_user = getpass.getuser()
        quickdir_input01 = input('input directory: ')
        if quickdir_input01 == 'music' or quickdir_input01 == 'Music' or quickdir_input01 == 'm':
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
        elif quickdir_input01 == 'music 2' or quickdir_input01 == 'all' or quickdir_input01 == 'm2' or quickdir_input01 == 'music all' or quickdir_input01 == 'music/all':
            music2_path = [basedir, current_user, '/Music/all']
            music2_path_real = ''.join(music2_path)
            try:
                music2_path_stripped = music2_path_real.strip('"')
                current_dir = music2_path_stripped
                print_music = os.listdir(current_dir)
                print_music_2 = '\n'.join(print_music)
                print(print_music_2)
                dir_music = open(current_dir_path, 'w+')
                dir_music.write(music2_path_stripped)
                dir_music.close()
            except Exception as o:
                print(o)
        elif quickdir_input01 == 'documents' or quickdir_input01 == 'Documents' or quickdir_input01 == 'd' or quickdir_input01 == 'docs':
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
        elif quickdir_input01 == 'pictures' or quickdir_input01 == 'Pictures' or quickdir_input01 == 'pics' or quickdir_input01 == 'p':
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
        elif quickdir_input01 == 'desktop' or quickdir_input01 == 'Desktop' or quickdir_input01 == 'desk':
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
        folder_crawler.quick_dir()
    def help_list():
        print('Command List:\ncd\nopen\nrandom\ntime\ncalculator\nweb\nquit\n\ncd quick commands:\ndocuments\nmusic\ndownloads\ndesktop\npictures\n')
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
    def file_reset():
        original_path = 'C:\\Users'
        file_reset = open(current_dir_path,'w+')
        file_reset.write(original_path)
        file_reset.close()
        #file_reset() resets the directory text file
    def add_quick_directory():
        print('Not Implemented Yet.')
        #will add directory as a quick_dir command in the future. Probably will use a seperate txt file to store quick commands
    def list_dir():
        dir_file = open(current_dir_path,'r')
        dir_list_path = dir_file.read()
        dir_list = os.listdir(dir_list_path)
        dir_list_real = '\n'.join(dir_list)
        print(dir_list_real)
        dir_file.close()
        #lists files and folders in the current directory
    def webpage_open():
        webpage_input = input('Which Webpage would you like to open?: ')
        webpage_02 = [webpage_input]
        try:
            webbrowser.open(webpage_input, new=2)
        except Exception as u:
            print('error in webpage subfunction', u)
        #opens webpage in browser

#calc class is calculator. It creates a file called calculator_query.txt, to get around issues relating to function specific items (like strings)

class calc():
    def calc_startup_text():
        print('Folder crawler integrated 2 number calculator V.1\n')
        print(time.strftime('%X %x'))
        print('\n')
    def calculator_main():
        calc.calc_startup_text()
        calc_loop = True
        while calc_loop == True:
            calculator_startup = input('calculator function. Input example 1 + 1: ')
            if calculator_startup == 'quit' or calculator_startup == 'exit':
                calc_loop == False
                print('\n\nExiting Calculator.\n\n')
                return None
            elif calculator_startup != 'quit' or calculator_startup != 'exit':
                try:
                    calculator_query = open('calculator_query.txt','w+')
                    calculator_query.write(calculator_startup)
                    calculator_query.close()
                    calculator_split_query = open('calculator_query.txt','r')
                    calculator_split_list = calculator_split_query.read()
                    calculator_split_list_02 = str.split(calculator_split_list)
                    if calculator_split_list_02[1] == '+':
                        calc.addition()
                    elif calculator_split_list_02[1] == '-':
                        calc.subtraction()
                    elif calculator_split_list_02[1] == '*' or calculator_split_list_02[1] == 'x':
                        calc.multiplication()
                    elif calculator_split_list_02[1] == '/':
                        calc.division()
                    else:
                        print('invalid. valid symbols include: *  x  -  /  +\n\n')
                except Exception as o:
                    print('error in calculator main loop', o)
    def input_split():
        try:
            calculator_full_query = open('calculator_query.txt','r')
            calculator_query = calculator_full_query.read()
            calculator_full_query.close()
            split_input = str.split(calculator_query)
            write_split = open('calculator_query.txt','w+')
            write_split.write(split_input)
        except Exception as p:
            print(p)
    def addition():
        try:
            add_line = open('calculator_query.txt','r')
            add_line_02 = add_line.read()
            add_item_pre_list = str.split(add_line_02)
            add_line.close()
            add_item_01 = add_item_pre_list[0]
            add_item_02 = add_item_pre_list[-1]
            add_item_int_01 = float(add_item_01)
            add_item_int_02 = float(add_item_02)
            add_item_list = [add_item_01, add_item_02]
            equation = add_item_int_01 + add_item_int_02
            print('\nAnswer is: ', equation, '\n')
        except Exception as q:
            print('error in addition subfunction', q)
    def subtraction():
        try:
            sub_line = open('calculator_query.txt','r')
            sub_line_02 = sub_line.read()
            sub_line_list = str.split(sub_line_02)
            sub_line.close()
            sub_item_01 = sub_line_list[0]
            sub_item_02 = sub_line_list[-1]
            sub_item_int_01 = float(sub_item_01)
            sub_item_int_02 = float(sub_item_02)
            equation = sub_item_int_01 - sub_item_int_02
            print('\nAnswer is: ', equation, '\n')
        except Exception as r:
            print('error in subtraction subfunction. ', r)
    def multiplication():
        try:
            mult_line = open('calculator_query.txt','r')
            mult_line_02 = mult_line.read()
            mult_line_list = str.split(mult_line_02)
            mult_line.close()
            mult_item_01 = mult_line_list[0]
            mult_item_02 = mult_line_list[-1]
            mult_item_int_01 = float(mult_item_01)
            mult_item_int_02 = float(mult_item_02)
            equation = mult_item_int_01 * mult_item_int_02
            print('\nAnswer is: ', equation, '\n')
        except Exception as s:
            print('error in multiplication subfunction. ', s)
    def division():
        try:
            div_line = open('calculator_query.txt','r')
            div_line_02 = div_line.read()
            div_line_list = str.split(div_line_02)
            div_line.close()
            div_item_01 = div_line_list[0]
            div_item_02 = div_line_list[-1]
            div_item_int_01 = float(div_item_01)
            div_item_int_02 = float(div_item_02)
            equation = div_item_int_01 / div_item_int_02
            print('\nAnswer is: ', equation, '\n')
        except Exception as t:
            print('error in division subfunction. ', t)
    def sin():
        pass
    def cos():
        pass
class unit_conversion():
    pass
    

def main():
    main_loop_01 = True
    while main_loop_01 == True:
        new_dir = open(current_dir_path,'r')
        dir_list_path = new_dir.read()
        print(current_user, '\n\n', dir_list_path, end='')
        command_input = input(': ')
        if command_input == 'cd' or command_input == 'dir' or command_input == 'directory':
            folder_crawler.cd()
        elif command_input == 'help':
            folder_crawler.help_list()
        elif command_input == 'random' or command_input == 'Random':
            folder_crawler.random_file()
        elif command_input == 'open' or command_input == 'Open':
            folder_crawler.list_dir()
            print('Open File or Folder?', end='')
            open_question = input(': ')
            if open_question == 'file' or open_question == 'File':
                folder_crawler.open_file()
            elif open_question == 'folder' or open_question == 'Folder':
                folder_crawler.open_folder()
        elif command_input == 'time' or command_input == 'Time':
            print('\n\n')
            print(time.strftime("%X %x"))
            print('\n\n')
        elif command_input == 'calc' or command_input == 'calculator' or command_input == 'Calculator' or command_input == 'Calc':
            calc.calculator_main()
        elif command_input == 'quit' or command_input == 'exit':
            file_reset_prompt = input('\nWould you like to reset Base Directory? y/n: ')
            if file_reset_prompt == 'y':
                folder_crawler.file_reset()
                main_loop_01 = False
            else:
                main_loop_01 = False
        elif command_input == 'listdir':
            folder_crawler.list_dir()
        elif command_input == 'reset' or command_input == 'file reset' or command_input == 'filereset':
            folder_crawler.file_reset()
        elif command_input == 'web' or command_input == 'webpage' or command_input == 'https' or command_input == 'browser' or command_input == 'internet':
            folder_crawler.webpage_open()
        else:
            pass

if __name__ == '__main__':
    main()
