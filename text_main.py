# -*- coding: utf-8 -*-

#------------------------
#  Required in python2.7
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
#------------------------

import konlpy
import nltk

import text_io
import text_show
import text_filter
File_Path = "./listen_data/"  # 119 text space
xlsx_Path = "./"   # xlsx_Path


def checkTextdata(start,end):
    cnt_rescue = cnt_fire = cnt_accident = cnt_etc = 0
    for i in range(start,end):
        print ('*********', i, '*********')
        c_name, t_name = text_io.read_xfile(i)                         #read a file name from xlsx

        #print(c_name, t_name)

        caller_data = text_io.read_text(File_Path + c_name, i, c_name) #read a text file
        taker_data = text_io.read_text(File_Path + t_name, i, t_name)  #read a text file

        if caller_data is 0 or taker_data is 0:                        #the xlsx space is empty
            continue
        caller_msg = text_filter.combine(caller_data, 'caller')        #combine the data
        taker_msg = text_filter.combine(taker_data, 'taker')           #combine the data
        msg_list = sorted(caller_msg + taker_msg)                      #sort the data by time
        #text_show.org(msg_list)
        #print '+++++filtered++++'

        msg_size, filtered_msg = text_filter.newlist(msg_list)         #filter the data
        msg_size = text_show.filtered(i, msg_size, filtered_msg)       #show filtered data
        text_io.write_text(msg_size, filtered_msg, i, start)

        #------------------------
        c_data = caller_data['TEXT']

        sentences = text_filter.filter_out(c_data)

        situation_data = text_io.read_situation(xlsx_Path + "wisenut/" + c_name, i, c_name)  # read a text file
        if situation_data != 0:
            situation_data = situation_data['SITUATION']
            fire = situation_data['fire']
            accident = situation_data['accident']
            rescue = situation_data['rescue']
            etc = situation_data['etc']

            if fire != 0:
                situation = u'화재'
                cnt_fire += 1
            elif accident != 0:
                situation = u'구급'
                cnt_accident += 1
            elif rescue != 0:
                situation = u'구조'
                cnt_rescue += 1
            else:
                situation = u'기타'
                cnt_etc += 1
            sentences = sentences + '\n' + situation + '\n' + '==='

        #print(caller_data['TEXT'])
        #print(caller_msg)
        #print(taker_msg)

        #text_show.org(msg_list)

        #print('+++++filtered++++')
        #print(filtered_msg)

        text_io.write_sentences(sentences, i, start)
        #-------------------------


        print("cnt_rescue, cnt_fire, cnt_accident, cnt_etc = ", cnt_rescue, cnt_fire, cnt_accident, cnt_etc)
        print ('*********************')


def fixTextdata(start,end):
    for i in range(start,end):
        print ('*********', i, '*********')
        c_name, t_name = text_io.read_xfile(i)                         #read a file name from xlsx

        lines = text_io.read_situation_corection(xlsx_Path + "wisenut/" + c_name, i, c_name)  # read a text file
        text_io.write_situation_corection(xlsx_Path + "wisenut/" + c_name, lines)  # write a text file

        lines = text_io.read_truelevel_corection(xlsx_Path + "wisenut/" + c_name, i, c_name)  # read a text file
        text_io.write_truelevel_corection(xlsx_Path + "wisenut/" + c_name, lines)  # write a text file


if __name__ == "__main__":
    #checkTextdata(2,10323) #start 2, end 10323

    #checkTextdata(2,4) #start 2, end 5
    checkTextdata(2,10323) #start 2, end 10323

    #fixTextdata(18,101) #start 2, end 5
    #fixTextdata(101,10323) #start 2, end 5

    '''
    refer
        num 9 : sentence 3 -> 0
        
    exp    
    # line52 :: 2574 ??
    # line33:: 6060 '\' character! edited -> 20150925_052234_00000430_012.TEXT (~맞으시죠\)
    '''
