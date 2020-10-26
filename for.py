def  sum_array(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    return sum
def sum_array_while(array):
    sum=0
    i=0
    while i <(len(array)):
        sum+=array[i]
        i+=1
    return sum
def merge_list(list1,list2):
    list_merged=[]
    min_len=min(len(list1),len(list2))
    max_len=max(len(list1),len(list2))
    for i in range(0,min_len):
            print(i)
            list_merged.append(list1[i])
            list_merged.append(list2[i])

    for i in range(min_len,max_len):
            if len(list1)<len(list2):
                list_merged.append(list2[i])
            else :
                list_merged.append(list1[i])
    return list_merged
if __name__=='__main__':
   Array1=[1,2,3,4]
   print(Array1)
   print(sum_array(Array1))
   print(sum_array_while(Array1))
   list1=['a','b','c','d','e','f','g','h']
   list2=[1,2,3,4]
   print(merge_list(list1,list2))
