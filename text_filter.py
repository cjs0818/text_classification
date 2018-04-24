import konlpy
import nltk

#word_filter_out = ['네 ', '예 ', '네.', '예.', '네네', ' 예예', ' 네네', '여기 ', '저기 ', '여기요 ', '저기요 ', '그 ', '어 ', '저 ', '거 ', '막 ']
word_filter_out = ['네 ', '예 ', '네.', '예.', '네네', ' 예예', ' 네네', '여기 ', '저기 ', '여기요 ', '저기요 ', '그 ', '막 ', '좀 ', '어 ', '저 ', '뭐 ', '하나 쫌 ', '거 ']


def combine(idata,whoami):
    idata=idata['TEXT']
    odata = [0] * len(idata)
    odata1 = [0] * len(idata)
    odata2 = [0] * len(idata)
    for i in range(0,len(idata),1):
        odata1[i] = idata[i]['start']
        odata2[i] = idata[i]['text']
        odata[i] = odata1[i], odata2[i],whoami
    return odata

def overlap(i, msg):
    j=0
    txt= msg[i][1]
    for _ in range(len(msg)-i):
        j = j + 1
        if i+j is len(msg):
            return j, txt
        if msg[i+j][2] is msg[i][2]:
            txt = txt + ' ' + msg[i+j][1]
        else :
            return j, txt

    return 0,None

def newlist(msg):
    i=0  # remove This is 119
    j=0
    k=0
    flag_xy=0

    omsg=[0]*len(msg)
    for _ in range(len(msg)*2):

        if i is len(msg):
            return k, omsg

        time = round(msg[i][0], 2)
        if flag_xy is 0:
            if msg[i][2] is 'caller':
                flag_xy=1
            else :
                i=i+1
        elif msg[i][2] is 'taker':
            j, txt = overlap(i, msg)
            omsg[k] = msg[i][2], txt
            k=k+1
        elif msg[i][2] is 'caller':
            j, txt = overlap(i, msg)
            omsg[k] = msg[i][2], txt
            k=k+1
        else :
            return 0, msg
        i = i + j
    return k, omsg


def filter_out(c_data):

    sentences = ''
    for data in c_data:
        data = data['text']


        # ---------------------------------
        # Extract noun phrases only "NP"
        words = konlpy.tag.Twitter().pos(data)

        # Define a chunk grammar, or chunking rules, then chunk
        grammar = """
        NP: {<N.*>*<Suffix>?}   # Noun phrase
        VP: {<V.*>*}            # Verb phrase
        AP: {<A.*>*}            # Adjective phrase
        """

        parser = nltk.RegexpParser(grammar)
        chunks = parser.parse(words)

        extract = ''
        for subtree in chunks.subtrees():
            if subtree.label() == 'NP':
                for e in list(subtree):
                    extract = extract + e[0] + ' '
                # print(' '.join((e[0] for e in list(subtree))))
                # print(subtree.pprint())

        #  Extract only 'Noun' type
        extract = ''
        for word in words:
            if word[1] == 'Noun':
                extract = extract + word[0] + ' '

        print (words)
        # print (sentences)
        # sentences = sentences + data + '. '
        # ---------------------------------

        #extract = data

        print(extract)

        # Remove unnecessary words such as ' 네', ' 예예', ...
        for x in word_filter_out:
            extract = extract.replace(x, '')
            #sentences = sentences.strip(x)


        #sentences = sentences + extract + '. '
        sentences = sentences + extract

    print('---- Result ---')
    print(sentences)

    return sentences
