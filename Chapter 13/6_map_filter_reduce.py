from functools import reduce
#map
list_map=[1,2,3,4,5,6,]
squared_l_map=lambda x:x*x
final_list=map(squared_l_map,list_map) #run this func on list
print(list(final_list)) #print output in the form of list

#filter
def finding_even(n):
    if n%2 == 0:
        return True
    return False
onlyEven = filter(finding_even,list_map)
print (list(onlyEven))

#reduce
sum_1=lambda a,b: a+b
print((reduce(sum_1,list_map)))