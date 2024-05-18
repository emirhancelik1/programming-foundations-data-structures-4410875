# Linear Search

my_list = [8, 5, 0, 3, 9, 7]
ITEM = 7

def search(item, listy):
  for i in range(len(listy)):
    if item == my_list[i]:
      return True
  return False

print(search(ITEM,my_list))

ITEM_INDEX = my_list.index(ITEM)
print(ITEM_INDEX)