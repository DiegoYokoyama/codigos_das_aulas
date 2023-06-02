#converter list para tupla
li=[[1,2],[3],[3,4,5]]
print(type(li))
li=(tuple(li))
print(type(li))
#converter tupla para list
tu=(1,2,3,4,5,6,'a','b','c')
print(type(tu))
tu=list(tu)
print(type(tu))