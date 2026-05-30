starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print(dict)
starting_dictionary["c"] = 7
final_dictionary=starting_dictionary

print(starting_dictionary)
print(final_dictionary)


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])