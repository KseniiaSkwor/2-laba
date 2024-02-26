import random

a = ["красный", "синий", "желтый"]
color1 = random.choice(a)
color2 = random.choice(a)

print(color1, color2)
if (color1 == "красный" and color2 == "синий") or (color2 == "красный" and color1 == "синий"):
    print("фиолетовый")
elif (color1 == "красный" and color2 == "желтый") or (color2 == "красный" and color1 == "желтый"):
    print("ораньжевый")
elif (color1 == "синий" and color2 == "желтый") or (color2 == "синий" and color1 == "желтый"):
    print("зеленый")
else:
    print("Не смешается")
    ""