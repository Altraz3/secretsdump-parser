
with open(r'c:\Net\Вспомогательное\PYTHON\Projects\hashess.txt', 'r') as file:
        lines = file.readlines() 

with open(r'c:\Net\Вспомогательное\PYTHON\Projects\ntlmhashess.txt', 'w') as file:     
   for line in lines:
     parts = line.strip().split(":")
     print(f'{parts[0]} : {parts[3]}')
     file.write((f'{parts[0]} : {parts[3]}\n'))

    
# (r'c:\Net\Вспомогательное\PYTHON\Projects\hashess.txt', 'r') - путь к файлу(r-чтение, w - запись, a - добавление )
# readlines - возвращает список строк
# for line in lines - для каждой строки из списка строк
# parts - переменная для списка
# strip() - удаляет добавляемое "readlines" в конце каждой строки значение \n
# split() - после деления строка превращается в список
# file.write - 
