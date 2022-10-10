# Írj egy remove_all(item) függvényt, ami
# a paraméterként átadott elem összes előfordulását törli
    # Addig hívjunk remove-ot, amíg az elem benne van a listában

# def remove_all(items, item_to_remove):
    # while item_to_remove in items:
        # items.remove(item_to_remove)

# def remove_all(items, item_to_remove):
    ## result = items.copy()
    # result = items[:] # létrehoz egy új listát az elemekkel
    # while item_to_remove in result:
    #    result.remove(item_to_remove)
    #return result

def remove_all(items, item_to_remove):
    """
        This function removes all occurances if the item from the items list.
        First parameter is the list.
        Second parameter is the item to remove.
    """    
    result = []
    for item in items:
        if item != item_to_remove:
            result.append(item)
    return result

# Programozási tételek

# Összegzés
# Írj egy sum(numbers) függvényt, ami a paraméterként
    # átadott listában lévő egész számokat összegzi
def sum_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

# Számlálás
# Írj egy count_positive_numbers(numbers) függvényt, mely megszámolja,
    # hogy hány pozitív szám van a listában
def count_positive_numbers(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

# Szélsőérték keresés
# Eldöntés

# Még két nagyon elterjedt algoritmus
# Szűrés
# Transzformáció

if __name__ == "__main__":
    numbers = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    removed = remove_all(numbers, 2)
    print(numbers)
    print(removed)
