fruits = ("Apple", "Banana", "Orange")
vegetables = ("Carrot", "Cabbage", "Tomato")
animal_products = ("Milk", "Egg", "Meat")

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
middle = len(food_stuff_tp) // 2
print("Phần tử ở giữa:", food_stuff_tp[middle])
food_stuff_lt = food_stuff_lt[3:-3]
print("Sau khi bỏ 3 đầu và 3 cuối:", food_stuff_lt)
del food_stuff_tp
nordic_countries = (
    "Denmark",
    "Finland",
    "Iceland",
    "Norway",
    "Sweden"
)
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)