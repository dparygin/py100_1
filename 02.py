
# Домашнее задание
#
#     Разбить список длиной N на подсписки длиной k.
#     Например список [1, 2, 3, 4, 5, 6, 7, 8] k = 3: [[1, 2, 3], [4, 5, 6], [7, 8]]

def splitlist(list, k):
    retlist = []
    for cuter in range(0,len(list),k):
        retlist.append(list[cuter:cuter+k])
    return retlist

l = list(range(9))
print(splitlist(l, 3))

#     Сделать список скользящего среднего для окна длиной k.
#     Например список [1, 2, 3, 4, 5] k = 2: [1.5, 2.5, 3.5, 4.5]
def win(list, k):
    retlist = []
    for r in range(1,(len(list)-1)):
        retlist.append((list[r] + list[r+1])/k)
    return retlist

l = list(range(6))
print(win(l, 2))


#     Дан одномерный массив числовых значений, насчитывающий N элементов.
#     Выполнить перемещение элементов массива по кругу вправо, т. е. A[1] → A[2];
#     A[2] → A[3]; ... A[n] → A[1]. (Использовать слайсирование нельзя, а именно A = A[1:] + A[0])

def simpl_slays(l): # Так нельзя?
    l.append(l[0])
    l.pop(0)
    print(l)



A = [5, 15, 91, 6, 8]
simpl_slays(A)



print('========================')

#     Дан одномерный массив числовых значений, насчитывающий N элементов.
#     Поменять местами первую и вторую половины массива.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l)

s = len(l) // 2
nl = []
for i in range(0, s):
    if len(l) % 2 == True:  #Если четное
        nl = l[len(l)-s:len(l)] + l[0:s]
    else: #нечетный вариант с разделителем
        nl = l[len(l)-s:len(l)] + l[s:s+1] + l[0:s]
print('вариант 1')
print(nl)
print('========================')

l2 = l.copy()
print('вариант 2')
l2.reverse() # Формально заданию соответствует :)
print(l2)



