def my_sort(my_list):
    len1 = len(my_list)
    for i in range(0, len1-1):
        for j in range(i+1, len1):
            if my_list[i] >= my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    print(my_list)




list1 = [10,6,9,4,8,0,1,-1]
my_sort(list1)
list1.sort()
print(list1)
list1.sort(reverse = True)
print(list1)