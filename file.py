#!-coding:utf-8-

with open('pi_digits.txt') as file_object:
    contents=file_object.readlines()
    pi_string=''
    for line in contents:
        pi_string+=line.strip()
    print(pi_string)
    print(len(pi_string))
file_path=r'C:\Users\leimaosheng1\Desktop\地址.txt'
with open(file_path.encode('utf-8')) as file_object1:
    lines=file_object1.readlines()
print(lines)
for line in lines:
    print(line.strip())
