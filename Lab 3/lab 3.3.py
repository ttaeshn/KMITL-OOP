def is_plusone_dictionary(d):
    keys = list(d.keys())
    if len(keys) < 2: return True
    
    for i in range(len(keys) - 1): 
        if keys[i] + 1 != d[keys[i]] or d[keys[i]] + 1 != keys[i + 1]: return False
    return True

print(is_plusone_dictionary({1: 2, 3: 4, 5: 6}))