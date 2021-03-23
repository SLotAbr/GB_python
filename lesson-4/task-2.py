origin = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [origin[i] for i in range(1,len(origin)) if origin[i] > origin[i-1]]
print(new_list)
