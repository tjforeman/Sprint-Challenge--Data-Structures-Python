import time
from binary_search_tree import BinarySearchTree 
from doubly_linked_list import DoublyLinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = DoublyLinkedList()
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

tree = BinarySearchTree(' ')

for names in names_1:
    tree.insert(names)

for names in names_2:
    if tree.contains(names):
        duplicates.add_to_tail(names)

end_time = time.time()
print (f"{duplicates.length} {duplicates.display()}\n\n\n\n")
print (f"runtime: {end_time - start_time} seconds")


