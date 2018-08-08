import re
def add_define():
    new_list=''
    for line in open('1.txt'):
        string=line
    print(string)
    string2=re.findall(r'\[\s(.*)\s\]',string)
    string3=re.split(r',\s|;\s',string2[0])
    print(string3)
    word=['INV_A','INV_B','INV_C','INV_D','INV_E','INV_F','INV_G','INV_H']
    f = open('2.txt', 'w')
    for i in range(len(string3)-1):
        new_list+=('#define '+word[i]+' '+string3[i]+'\n')
    f.write(new_list)
add_define()
