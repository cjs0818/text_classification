from termcolor import colored
import text_io

def filtered(i, num, msg):
    if num%2 is 1:
        num=num-1
    if num is 0:
        err_msg = 'Error, Exception! Few sentences'
        print(err_msg)
        text_io.write_data(i, err_msg)
    for i in range(num):
        if msg[i][0] is 'taker':
            print ('[', colored(msg[i][0], 'red'), '\t]', msg[i][1])
        else:
            print ('[', colored(msg[i][0], 'blue'), '\t]',msg[i][1])
    return num
def org(msg):
    for i in range(len(msg)):
        time = round(msg[i][0],3)
        if msg[i][2] is 'taker':
            print ('[',colored(msg[i][2],'red'),'\t]', \
                '[', time,'\t]',msg[i][1])
        else :
            print ('[',colored(msg[i][2],'blue'),'\t]',\
                '[', time,'\t]',msg[i][1])
