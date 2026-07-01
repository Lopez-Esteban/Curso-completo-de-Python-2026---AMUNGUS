
Lista_T = [1,2,3,4,5]
Lista_T2 = [6,7,8,9,10]

Lista_T3 = Lista_T + Lista_T2

print(Lista_T3[0:5])
print(Lista_T3[:5])
print(Lista_T3[5:])
print(Lista_T3[-5:])
print(Lista_T3[::2])
print(Lista_T3[::-1])

############################
print("------------------------------------------------------------")
############################

Lista_V = [84, 12, 45, 67, 23, 90, 9]

print(sorted(Lista_V))
print(sorted(Lista_V, reverse=True))

############################
print("------------------------------------------------------------")
############################

print(max(Lista_V))
print(min(Lista_V))
print(sum(Lista_V))