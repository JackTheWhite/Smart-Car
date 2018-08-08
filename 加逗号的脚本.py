import re
def add_coma():
    lines_list=[]
    lines=''
    for line in open('col1.txt'):
        lines+=line
    lines_list=re.split(r'\s',lines)
##    print(lines_list[0])
    lines=''
    for i in range(len(lines_list)):
        if i !=(len(lines_list)-1):
            lines=lines+lines_list[i]+','
        else:
            lines+=lines_list[i]
        
    f = open('invcol4.1.txt', 'w')
    f.write(lines)
add_coma()
    
