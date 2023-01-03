# генеруємо список від 0 до 100 і на його основі створюємо новий список із числами, що кратні 3
lst = [i for i in range(100)]
print(lst)
lst2 = [i for i in lst if i % 3 == 0]
print(lst2)
