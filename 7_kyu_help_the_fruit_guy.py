def remove_rotten(bag_of_fruits):
    not_rotten = []
    try:
        for fruit in bag_of_fruits:
            a = fruit.lower()
            not_rotten.append(a.replace('rotten', ''))
        return not_rotten
    except:
        return []


print(remove_rotten(["apple","rottenBanana","apple"]))



