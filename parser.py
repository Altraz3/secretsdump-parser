
with open(r'c:\Net\Вспомогательное\PYTHON\Projects\hashess.txt', 'r') as file:
        lines = file.readlines() 

with open(r'c:\Net\Вспомогательное\PYTHON\Projects\ntlmhashess.txt', 'w') as file:     
   for line in lines:
     parts = line.strip().split(":")
     print(f'{parts[0]} : {parts[3]}')
     file.write((f'{parts[0]} : {parts[3]}\n'))
