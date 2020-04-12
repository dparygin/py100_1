# Домашнее задание
print('==========================================================================')
print('  Написать функцию, которая будет принимать строку и печатать её по диагонали.')
print('==========================================================================')
def distr(str_):
    wigh = len(str_)
    leng = len(str_)
    prob = -1
    n = 1
    for char in str_:
        prob += 1
        print((' ' * prob + char) * 4)
    return (' ')
print(distr('Диагонали на выбор'))

print('==========================================================================')
print('  Составить функцию, формирующую строку, состоящую из любого заданного количества любых одинаковых символов.')
print('==========================================================================')
def printsim(sim, len_):
    numsim = 1  # Общая длинна строки
    mylist = []
    count_ = 0
    for i in range(0, len_):
        for s in sim:
            count_ += 1
            mylist.append(s)
            if count_ == len_:
                str_ = ''.join(mylist)
                return str_

print(printsim('kjhqwdqldkwj', 114))


print('==========================================================================')
print('   Написать функцию, которая принимает список слов и длину слова.')
print('   Заменить последние три символа слов, имеющих выбранную длину на символ "$"')
print('==========================================================================')

def tsenzor(mylist, dlsl):
    newlist = []
    dlsl = int(dlsl)
    for inslovo in mylist:
        if len(inslovo) != dlsl:
            newlist.append(inslovo)
        elif len(inslovo) == dlsl:
            slovo = list(inslovo)
            slovo[-1] = '$'
            slovo[-2] = '$'
            slovo[-3] = '$'
            mod_slovo = ''.join(slovo)
            newlist.append(mod_slovo)
    return newlist


l1 = ['lrgkjelkHrg', 'lkjgfleYgj', 'dfg', 'vnvnv', 'jgheld', 'hjviu', 'hibub']
print(tsenzor(l1, 5))

print('==========================================================================')
print(' Написать функцию, которая принимает строку слов, разделенных пробелами')
print(' (пробелов между словами может быть несколько). ')
print(' Найти самое длинное слово и вывернуть его.')
print(' В случае, когда самых длинных слов может быть несколько, вернуть их списком.')
print('==========================================================================')

def lstslov(strslov):
    nlistslov = []
    listslov = strslov.split()
    for word in listslov:
        tmplist = [len(word), word]
        nlistslov.append(tmplist)
        nlistslov.sort(reverse=True)
    numz = nlistslov[0][0]
    finallist = []
    finallist.append(str(nlistslov[0][1])[::-1])
    for num, wordz in nlistslov[1:]:
        if numz == num:
            wordz = wordz[::-1]
            finallist.append(wordz)
    return finallist
print(lstslov('0jbkjbkjbjhvghvjhjbk111uj1   bjhbjhkb iuh lknlknlknkjbkj  lklk  lkjkl lkjlkjllcfgcf 0jbkjbkjbjhvghvjhjbkjbkuj1       0bgdlbTgfnbjubylmiubhtfbo1'))

print('==========================================================================')
print('Написать функцию, которая принимает текст. Напечатать все различные слова.')
def words(text):
    dict = {}
    slovar = []
    for w in text.split():
        if dict.get(w)==None:
            dict[w] = 0
    for key in dict.keys():
        slovar.append(key)
    return slovar

print(words("fff uuu 777r fjdfvdfvdfv\s.v fff ee uuu"))
