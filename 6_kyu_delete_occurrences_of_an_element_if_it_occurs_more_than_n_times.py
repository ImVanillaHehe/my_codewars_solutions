def delete_nth(order,max_e):
    res = []
    occurrences = {}
    for n in order:
        count = occurrences.setdefault(n, 0)
        if count >= max_e:
            continue
        res.append(n)
        occurrences[n] += 1
    return res
