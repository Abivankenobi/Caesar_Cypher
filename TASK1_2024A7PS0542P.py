#code for 1 shift: IDK if there is a use for it,but it is motivation for what comes afterwords, it is trivial to see if the sentence is meaningful or not
""""
ques=input()
out=""
for i in ques:
    if i.isalpha()==True:
        if i!='A' and i!='Z':
            out1=chr(ord(i)-1)
        else:
            if i=='a':
                out1='z'
            else:
                out1='Z'
        out = out + out1
    else:
        out=out+str(i)
print("OUTPUT AFTER SHIFT=1 is",out)

"""
#in 1 shift reading the output is trivial, but for a shift k, I have 2 ideas, the first one involves nltk, a library containing corpus of words and the other one involves using some API to search from an online database of words, of course the second idea is better, but IDK API as of now, so here you go with nltk
#As per my tests, it gets buggy and does some mistakes after first few letters, eg-THe output for test case is "Will do this messagge?"- clearly the code has some errors, but I can improve it in further versions
def FuncToSayEtTuBrute():
    import nltk#please use pip install nltk or if you are in pycharm like me, set it from the environment
    from nltk.corpus import words
    nltk.download("words")#This is the only thing that uses internet
    wl=set(words.words())
#This is a highly suboptimal solution, I can optimise it if given more time, and of course,more programming skills
    def decryptor(p,k):
        out=list(p)
        for iterator in range(k):
            for i in  range(len(out)):
                if out[i].isalpha() == True:
                    if out[i] != 'A' and out[i] != 'a':
                        out1 = chr(ord(out[i]) - 1)
                    else:
                        if out[i] == 'a':
                            out1 = 'z'
                        else:
                            out1 = 'Z'
                    out[i]=out1
                else:
                    continue
        return "".join((out))#I am aware of the horrendous time complexity of func, and will probably implement it with a dictionary in furhter versions or maybe with a maths based formula to directly compute without doing the intermediates

    def purify(w2):#I use it to remove special characters like , ' " but IDK if it makes much difference
        w2=w2.strip()
        w2_="".join(iter1 for iter1 in w2 if iter1.isalpha())
        return w2_

    def valid(p):
        w1=p.split()
        countValidWords=0
        for iter in w1:
            if purify(iter) in wl:
                countValidWords+=1
        return countValidWords

    str1=input()
    maxcount=0
    maxshift=-1
    for i in range(26):
        num=valid(decryptor(str1,i))
        if num>=maxcount:#I do this under assumption that we can have only 1 meaningful sentence here, because if there are more, code goes for the farther one and one sentence is ignored
            maxcount=num
            maxshift=i
    print(maxshift)
    print(decryptor(str1,maxshift))

FuncToSayEtTuBrute()#Line 69,The last line, and the line which does the function cal
