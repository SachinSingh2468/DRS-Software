# normal syntax

# list = []
# for  i in range(100):
#     if i%5 == 0:
#         list.append(i)
# print(list)        

# list comprehension

# l = [i for i in range(100) if i%7 == 0]
# print(l)

# dict commprehension
print("\n")

# dict = {i: f"item{i}" for i in range(100) if i%7 == 0}
# dict = {value: key for key, value in dict.items()}
# print(dict)

print("\n")

# set comprehension

s = (set for set in ['set1', 'set2', 'set3', 'set2', 'set1'])

print(type(s))
print(s.__next__())
print(s.__next__())
print(s.__next__())