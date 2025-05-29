from mapcode.mapcode import mapcode
from linear_search import linear_search

def rho_2d(x):
    (a, k) = x
    return (a, k, 0, 0)

def f_2d(x):
    (a, k, i, j) = x
    if i < len(a) and linear_search(a[i], k) != -1:
        return (a, k, i, linear_search(a[i], k))
    if i < len(a):
        return (a, k, i + 1, -1)
    else:
        return (a, k, i, -1)
    
def pi_2d(x):
    (a, k, i, j) = x
    if i < len(a) and j != -1:
        return (i, j)  # Return the indices of the first occurrence of k
    else:
        return "Absent"  # Return (-1, -1) if k is not found
    
def linear_search_2d(a, k):
    search = mapcode(rho_2d, f_2d, pi_2d)
    x = (a, k)
    return search(x)

# Example usage:
print(linear_search_2d([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))  # Should return (1, 1)
print(linear_search_2d([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10))  # Should return (-1, -1)