Thêm mục vào danh sách
lst = list()
lst.append(item)
Chèn các mục vào danh sách
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
Xóa các mục khỏi danh sách
# syntax
lst = ['item1', 'item2']
lst.remove(item)
Xóa các mục bằng Pop
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
Xóa các mục bằng lệnh Del
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
Xóa các mục trong danh sách
# syntax
lst = ['item1', 'item2']
lst.clear()
Sao chép danh sách
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
Tham gia danh sách
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2) # ['item1', 'item2', 'item3', 'item4', 'item5']
Đếm số mục trong danh sách
# syntax
lst = ['item1', 'item2']
lst.count(item)
Tìm chỉ mục của một mặt hàng
# syntax
lst = ['item1', 'item2']
lst.index(item)
Đảo ngược danh sách
lst = ['item1', 'item2']
lst.reverse()
Sắp xếp các mục trong danh sách
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending