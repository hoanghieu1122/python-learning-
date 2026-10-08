-Module là một file Python (.py) chứa các biến, hàm hoặc đoạn code có thể được sử dụng trong những file Python khác.
Module	Công dụng
math	Các phép toán toán học
random	Tạo số ngẫu nhiên
os	Thao tác với thư mục và hệ điều hành
sys	Thông tin và môi trường chạy Python
statistics	Tính toán thống kê
string	Các tập hợp ký tự
datetime	Xử lý ngày giờ
json	Xử lý dữ liệu JSON
re	Xử lý chuỗi bằng biểu thức chính quy
collections	Các kiểu cấu trúc dữ liệu bổ sung
1. OS Module – Làm việc với thư mục
import os
os.mkdir('test')       # Tạo thư mục test
print(os.getcwd())     # Xem thư mục hiện tại
os.chdir('test')       # Chuyển vào thư mục test
os.chdir('..')         # Quay lại thư mục cha
os.rmdir('test')       # Xóa thư mục test nếu rỗng
2. SYS Module – Thông tin hệ thống Python
import sys
print(sys.version)   # Phiên bản Python
print(sys.path)      # Danh sách đường dẫn tìm module
print(sys.maxsize)   # Giá trị kích thước nguyên tối đa thường dùng
3. Statistics Module – Thống kê
from statistics import mean, median, mode, stdev
ages = [20, 20, 21, 22, 25]
print(mean(ages))    # Trung bình
print(median(ages))  # Trung vị
print(mode(ages))    # Giá trị xuất hiện nhiều nhất
print(stdev(ages))   # Độ lệch chuẩn mẫu
4. Math Module – Toán học
Hàm	Ý nghĩa	Ví dụ
math.pi	Số Pi	3.14159…
math.sqrt(25)	Căn bậc hai	5.0
math.pow(2,3)	Lũy thừa	8.0
math.floor(9.8)	Làm tròn xuống	9
math.ceil(9.2)	Làm tròn lên	10
math.log10(100)	Logarit cơ số 10	2.0
5. String Module – Các ký tự
import string
print(string.ascii_letters) #abcdefghijklmnopqrstuvwxyzABCDEF
print(string.digits) #0123456789
print(string.punctuation) #!"#$%&'()*+,-./:;
6. Random Module – Tạo giá trị ngẫu nhiên
from random import random, randint
print(random())
print(randint(5, 20))