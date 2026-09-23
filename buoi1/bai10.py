chon = input("Nhap lua chon: ")
if chon == "C":
    a = float(input("Nhap do C"))
    doi = a * 9/5 + 32
    print(doi)
else:
    b = float(input("Nhap do F"))
    doi = (b - 32) * 5/9
    print(doi)

