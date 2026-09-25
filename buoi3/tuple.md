Tuple là một tập hợp các kiểu dữ liệu khác nhau, được sắp xếp và không thể thay đổi (bất biến). Tuple được viết bằng dấu ngoặc tròn, (). Sau khi một tuple được tạo, chúng ta không thể thay đổi giá trị của nó. Chúng ta không thể sử dụng các phương thức add, insert, remove trên một tuple vì nó không thể sửa đổi (mutable). Không giống như list, tuple có ít phương thức hơn. Các phương thức liên quan đến tuple:
tuple(): để tạo một tuple rỗng
count(): để đếm số lượng của một mục cụ thể trong một bộ dữ liệu.
index(): tìm chỉ mục của một mục cụ thể trong một bộ dữ liệu.
+toán tử: dùng để kết hợp hai hoặc nhiều bộ dữ liệu và tạo một bộ dữ liệu mới.
Chuyển đổi Tuple thành List
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
