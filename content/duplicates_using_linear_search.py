from mapcode.mapcode import mapcode
from linear_search import linear_search

def rho(a):
    return (a, 0)

def f(x):
    (a, i) = x
    if i < len(a) and linear_search(a[i+1:], a[i]) != i:
        return (a, i + 1)
    else:
        return (a, i)
    
def pi(x):
    (a, i) = x
    if i < len(a):
        return i  # Return the index of the first occurrence of a[i]
    else:
        return -1  # Return -1 if no duplicate is found
    
def find_duplicate(a):
    search = mapcode(rho, f, pi)
    return search(a)

# Example usage:
print(find_duplicate([1, 2, 3, 4, 5, 3]))  # Should return 2 (index of the first occurrence of duplicate 3)