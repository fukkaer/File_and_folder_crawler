import os, random
import time
import getpass
import webbrowser
import math

current_user = getpass.getuser()

file_path = ['C://Users/', current_user, '/music']

current_dir_path = 'current_dir.txt'
open_file_txt = 'open_file.txt'

global basedir
basedir = 'C://users/'

current_dir = 'C://users'

#make program read txt to find and append directory paths -done
#append to current path with user input ie. user type ex. Games, while in desktop, it appends \games to current path -done
#Add webbrowser.open(https:webpage) function -done
#Add Calculator and unit conversion class -done
#Add all current functions to class. Call class subfunctions from main, by class.function -done
#Came up with folder crawler while making random file opener
#cut down the write function to one, instead of rewriting everytime
#isolate the first word of input in order to allow commands like cd music, instead of cd, then music. ala. the calculator class, with 1 + 1. -done
#make powershell function that opens powershell as admin -abandoned for now
#use str.split to split main input into list, in order to isolate first word, like cd. -done
#write errors to a text file
#V.0.3 


class folder_crawler():
    def quick_dir():
        current_user = getpass.getuser()
        quickdir_file = open(current_dir_path,'r')
        quickdir_string = quickdir_file.read()
        quickdir_input01 = quickdir_string
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
        elif quickdir_input01 == 'all' or quickdir_input01 == 'm2' or quickdir_input01 == 'music/all':
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
        print('Command List:\ncd\nopen\nrandom\ntime\ncalculator\nconverter\nweb\ncoin\nquit\n\ncd quick commands:\ndocuments\nmusic\ndownloads\ndesktop\npictures\nm2 (music/all)\n')
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
        print('\n\nOpen file function\n')
        dir_file = open(current_dir_path,'r')
        dir_list_path = dir_file.read()
        dir_file.close()
        open_file_command_text = open(open_file_txt,'r')
        open_file_command = str(open_file_command_text)
        open_file_command_text.close()
        #print(dir_list_path, end='')
        #open_file_command = input(': ')
        open_file_command_stripped = open_file_command.strip('"')
        dir_list = [dir_list_path, '/', open_file_command_stripped]
        #dir_file.close()
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
    def random_loop():
        random_loop_01 = True
        while random_loop_01 == True:
            try:
                random_input = input('Open random File? y/n: ')
                if random_input == 'y' or random_input == 'Y' or random_input == 'yes' or random_input == 'Yes' or random_input == 'YES':
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
                        except Exception as ab:
                            print('Error in random_loop subfunction. ', ab)
                    except Exception as ac:
                        print('Error in random_loop subfunction. ac. ', ac)
                elif random_input == 'n' or random_input == 'N' or random_input == 'no' or random_input == 'No' or random_input == 'NO' or random_input == 'quit' or random_input == 'exit' or random_input == 'return':
                    random_loop_01 = False
                    print('\n\nExiting Random Loop Function\n\n')
                    return None
            except Exception as ad:
                print('Error in random_loop subfunction. ad. ', ad)

#calc class is calculator. It creates a file called calculator_query.txt, to get around issues relating to function specific items (like strings)

class calc():
    def calc_startup_text():
        print('Folder crawler integrated 2 number calculator V.2\n')
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
    def floor_tile():
        print('\n\nRoom floor tile cost calculator per m/ft squared\n\n')
        floor_01 = float(input('Input the cost per sq m/ft: '))
        floor_02 = float(input('Input the length of the room: '))
        floor_03 = float(input('Input the width of the room: '))
        floor_result = floor_01 * floor_02 * floor_03
        print('\n\nThe total estimated cost of the room = ', floor_result)

class unit_conversion():
    def unit_converter_startup_print():
        print('\nFolder Crawler Integrated Unit Converter V.1')
    def unit_converter():
        unit_conversion.unit_converter_startup_print()
        converter_loop = True
        while converter_loop == True:
            print('(1)Length\n(2)Weight\n(3)Temperature\n(4)exit\n\n')
            converter_input = input('Which measurement type would you like to convert?: ')
            if converter_input == 'length' or converter_input == 'l' or converter_input == 'Length' or converter_input == '1':
                try:
                    length_converter_loop = True
                    while length_converter_loop == True:
                        print('(1)Meters\n(2)Feet\n(3)Return\n')
                        length_input_01 = input('Select which unit to convert from: ')
                        if length_input_01 == '1' or length_input_01 == 'meter' or length_input_01 == 'meters' or length_input_01 == 'Meters' or length_input_01 == 'Meter' or length_input_01 == 'm':
                            length_input_meter = float(input('How many meters to convert to feet?: '))
                            length_meter_to_foot_answer = length_input_meter / 3.281
                            print('\n\n', length_input_meter, ' meters, is: ', length_meter_to_foot_answer,' feet\n\n')
                        elif length_input_01 == '2' or length_input_01 == 'f' or length_input_01 == 'feet' or length_input_01 == 'Feet' or length_input_01 == 'foot' or length_input_01 == 'Foot' or length_input_01 == 'ft':
                            length_input_foot = float(input('How many feet to convert to meters?: '))
                            length_foot_to_meter = length_input_foot * 3.281
                            print('\n\n', length_input_foot, ' feet, is: ', length_foot_to_meter, ' meters\n\n')
                        elif length_input_01 == 'return' or length_input_01 == 'quit' or length_input_01 == 'exit' or length_input_01 == '3':
                            length_converter_loop = False
                            break
                        else:
                            pass
                except Exception as y:
                    print('Error in length module. ', y)
            elif converter_input == 'Weight' or converter_input == 'weight' or converter_input == 'w' or converter_input == '2':
                try:
                    weight_converter_loop = True
                    while weight_converter_loop == True:
                        print('(1)Kilograms\n(2)Pounds\n(3)Return\n\n')
                        weight_input_01 = input('Select which unit to convert from: ')
                        if weight_input_01 == '1' or weight_input_01 == 'k' or weight_input_01 == 'kg' or weight_input_01 == 'KG' or weight_input_01 == 'Kg' or weight_input_01 == 'kilos' or weight_input_01 == 'Kilograms' or weight_input_01 == 'kilograms':
                            weight_input_kilo = float(input('How many Kg to convert to lbs?: '))
                            kilo_to_pound_answer = weight_input_kilo * 2.205
                            print('\n\n', weight_input_kilo, 'Kg, is: ', kilo_to_pound_answer, ' lbs\n\n')
                        elif weight_input_01 == 'lbs' or weight_input_01 == 'Pounds' or weight_input_01 == '2' or weight_input_01 == 'l' or weight_input_01 == 'p' or weight_input_01 == 'pounds' or weight_input_01 == 'pound' or weight_input_01 == 'Lbs' or weight_input_01 == 'Pound':
                            weight_input_pounds = float(input('How many lbs to convert to Kg?: '))
                            pound_to_kilo_answer = weight_input_pounds / 2.205
                            print('\n\n', weight_input_pounds, ' lbs, is: ', pound_to_kilo_answer, ' Kg\n\n') 
                        elif weight_input_01 == 'return' or weight_input_01 == 'quit' or weight_input_01 == 'exit' or weight_input_01 == '3':
                            weight_converter_loop == False
                            break
                        else:
                            pass
                except Exception as z:
                    print('Error in weight conversion module. ', z)
            elif converter_input == '3' or converter_input == 'temp' or converter_input == 'temperature' or converter_input == 't' or converter_input == 'Temperature' or converter_input == 'Temp':
                try:
                    temperature_converter_loop = True
                    while temperature_converter_loop == True:
                        print('(1)Celsius\n(2)Fahrenheit\n(3)Kelvin\n(4)Return\n\n')
                        temp_input_01 = input('Select which unit to convert from: ')
                        if temp_input_01 == '1' or temp_input_01 == 'celsius' or temp_input_01 == 'c' or temp_input_01 == 'Celsius' or temp_input_01 == 'celcius' or temp_input_01 == 'C' or temp_input_01 == 'Celcius':
                            temp_input_celsius = float(input('Input amount of Celsius to convert: '))
                            print('\n(1)Fahrenheit\n(2)Kelvin\n')
                            temp_input_question = input('Select unit to convert to: ')
                            if temp_input_question == '1' or temp_input_question == 'F' or temp_input_question == 'f' or temp_input_question == 'Fahrenheit' or temp_input_question == 'fahrenheit' or temp_input_question == 'farenheit':
                                c_to_f_01 = temp_input_celsius * 9
                                c_to_f_02 = c_to_f_01 / 5
                                c_to_f_03 = c_to_f_02 + 32
                                print('\n\n', temp_input_celsius, ' °C, is: ', c_to_f_03, ' °F\n\n')
                            elif temp_input_question == 'FREEDOM':
                                c_to_F_01 = temp_input_celsius * 9
                                c_to_F_02 = c_to_F_01 / 5
                                c_to_F_03 = c_to_F_02 + 32
                                print('\n\n', temp_input_celsius, ' °C, is: ', c_to_F_03, ' ° OF FREEDOM\n\n')
                                #print same as fahrenheit but FREEDOMS instead of fahrenheit
                            elif temp_input_question == 'Kelvin' or temp_input_question == 'K' or temp_input_question == 'k' or temp_input_question == 'kelvin' or temp_input_question == '2':
                                num_273 = float(273.15)
                                c_to_k_01 = temp_input_celsius + num_273
                                print('\n\n', temp_input_celsius, ' °C, is: ', c_to_k_01, ' Kelvin. \n\n')
                        elif temp_input_01 == '2' or temp_input_01 == 'f' or temp_input_01 == 'F' or temp_input_01 == 'fahrenheit' or temp_input_01 == 'Fahrenheit' or temp_input_01 == 'Farenheit' or temp_input_01 == 'farenheit':
                            farenheit_input = float(input('Input amount of Fahrenheit to convert: '))
                            print('\n(1)Celsius\n(2)Kelvin\n')
                            temp_input_question_02 = input('Select unit to convert to: ')
                            if temp_input_question_02 == 'c' or temp_input_question_02 == 'C' or temp_input_question_02 == 'celsius' or temp_input_question_02 == 'Celsius' or temp_input_question_02 == '1':
                                f_to_c_01 = farenheit_input - 32
                                f_to_c_02 = f_to_c_01 * 5
                                f_to_c_03 = f_to_c_02 / 9
                                print('\n\n', farenheit_input, ' °F, is: ', f_to_c_03, ' °C.\n\n')
                            elif temp_input_question_02 == 'k' or temp_input_question_02 == 'K' or temp_input_question_02 == 'Kelvin' or temp_input_question_02 == 'kelvin' or temp_input_question_02 == '2':
                                num_459 = float(459.67)
                                f_to_k_01 = farenheit_input + num_459
                                f_to_k_02 = f_to_k_01 * 5
                                f_to_k_03 = f_to_k_02 / 9
                                print('\n\n', farenheit_input, ' °F, is: ', f_to_k_03, ' Kelvin.\n\n')
                        elif temp_input_01 == '3' or temp_input_01 == 'k' or temp_input_01 == 'K' or temp_input_01 == 'kelvin' or temp_input_01 == 'Kelvin':
                            kelvin_input = float(input('Input amount of Kelvin to convert: '))
                            print('\n(1)Celsius\n(2)Fahrenheit\n')
                            temp_input_question_03 = input('Select unit to convert to: ')
                            if temp_input_question_03 == '1' or temp_input_question_03 == 'c' or temp_input_question_03 == 'C' or temp_input_question_03 == 'celsius' or temp_input_question_03 == 'Celsius':
                                num_k_to_c = float(273.15)
                                k_to_c_01 = kelvin_input - num_k_to_c
                                print('\n\n', kelvin_input, ' Kelvin, is: ', k_to_c_01, ' °C.\n\n')
                            elif temp_input_question_03 == '2' or temp_input_question_03 == 'f' or temp_input_question_03 == 'F' or temp_input_question_03 == 'fahrenheit' or temp_input_question_03 == 'farenheit' or temp_input_question_03 == 'Fahrenheit' or temp_input_question_03 == 'Farenheit':
                                num_k_to_f = float(459.67)
                                k_to_f_01 = kelvin_input * 9
                                k_to_f_02 = k_to_f_01 / 5
                                k_to_f_03 = k_to_f_02 - num_k_to_f
                                print('\n\n', kelvin_input, ' Kelvin, is: ', k_to_f_03, ' °F.\n\n')
                        elif temp_input_01 == '4' or temp_input_01 == 'quit' or temp_input_01 == 'exit' or temp_input_01 == 'return':
                            temperature_converter_loop = False
                            break
                except Exception as ae:
                    print('Error in temperature conversion unit. ae', ae)
            elif converter_input == 'quit' or converter_input == 'exit' or converter_input == 'return' or converter_input == '4':
                converter_loop = False
                return None
            else:
                pass

class games():
    def coin_flip():
        landed = ''
        coin_loop = True
        while coin_loop == True:
            try:
                flip_input = input('Flip Coin? y/n: ')
                if flip_input == 'y'  or flip_input == 'yes' or flip_input == 'Yes' or flip_input == 'again':
                    landed = random.randint(1,2)
                    if landed == 1:
                        print('Coin landed on tails.\n\n')
                    elif landed == 2:
                        print('Coin landed on tails.\n\n')
                elif flip_input == 'n' or flip_input == 'no' or flip_input == 'return' or flip_input == 'quit' or flip_input == 'exit':
                    coin_loop = False
                    return None
            except Exception as af:
                print('Error in coin_flip module. af. ', af)
    def scissor_paper_rock():
        #Add this later
        pass

#make a loop for celsius, so that you can redo unit conversion choice to, ex. kelvin, when you accidentally chose Fahrenheit
#move open file and folder commands back to original functions, but keep new changes to them   

def main():
    main_loop_01 = True
    while main_loop_01 == True:
        new_dir = open(current_dir_path,'r')
        dir_list_path = new_dir.read()
        print(current_user, '\n\n', dir_list_path, end='')
        command_input_01 = input(': ')
        command_input_list = str.split(command_input_01)
        command_input = command_input_list[0]
        try:
            command_input_second_word = command_input_list[1]
            command_input_second_string = str(command_input_second_word)
            if command_input == 'cd' or command_input == 'dir' or command_input == 'directory':
                dir_write = open(current_dir_path,'w+')
                dir_write.write(command_input_second_string)
                dir_write.close()
                folder_crawler.cd()
            elif command_input == 'open' or command_input == 'Open':
                folder_crawler.list_dir()
                if command_input_second_string == 'file' or command_input_second_string == 'File':
                    open_file_command = open('open_file.txt','w+')
                    try:
                        open_file_third_word = command_input_list[2]
                        open_file_third_string = str(open_file_third_word)
                        open_file_third_stripped = open_file_third_string.strip('"')
                        #print('\n\nOpen file function\n')
                        dir_file = open(current_dir_path,'r')
                        dir_list_path = dir_file.read()
                        dir_file.close()
                        dir_list = [dir_list_path, '/', open_file_third_stripped]
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
                        #print('success')
                    except Exception as af:
                        print('Error in open file on main function. af. ', af)
                elif command_input_second_word == 'folder' or command_input_second_word == 'Folder':
                    current_dir = open(current_dir_path,'r')
                    current_dir_string = current_dir.read()
                    current_dir_stripped = current_dir_string.strip('"')
                    current_dir.close()
                    rewrite_dir = open(current_dir_path,'w+')
                    try:
                        command_input_third_word = command_input_list[2]
                        command_input_third_string = str(command_input_third_word)
                        command_input_third_stripped = command_input_third_string.strip('"')
                        open_dir_list = [current_dir_stripped, '/', command_input_third_stripped]
                        open_dir_actual = ''.join(open_dir_list)
                        rewrite_dir.write(open_dir_actual)
                        rewrite_dir.close()
                        folder_crawler.list_dir()
                    except Exception as x:
                        print('open folder command requires a folder to open.', x)
                        rewrite_dir.close()
            elif command_input == 'random' or command_input == 'Random':
                folder_crawler.list_dir()
                if command_input_second_word == 'loop' or  command_input_second_word == 'Loop':
                    folder_crawler.random_loop()
        except Exception as v:
            # print('No Second Word', v) used for error checking the functions that have a second word, like open folder or open file
            if command_input == 'help':
                folder_crawler.help_list()
            elif command_input == 'random' or command_input == 'Random':
                folder_crawler.random_file()
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
            elif command_input == 'converter' or command_input == 'unit' or command_input == 'uc' or command_input == 'convert':
                unit_conversion.unit_converter()
            elif command_input == 'coin' or command_input == 'flip' or command_input == 'toss':
                games.coin_flip()
            elif command_input == 'floor' or command_input == 'tile_calc' or command_input == 'floor_tile' or command_input == 'floor_calc':
                calc.floor_tile()
            else:
                pass

if __name__ == '__main__':
    main()
