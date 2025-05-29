from mapcode.mapcode import mapcode

def rho(x):
    (arr, k) = x
    return (arr, k, 0)

def f(x):
    (arr, k, i) = x
    if i < len(arr) and arr[i] != k:
        return (arr, k, i + 1)
    else:
        return (arr, k, i)
    
def pi(x):
    (arr, k, i) = x
    if i < len(arr):
        return i  # Return the index of the first occurrence of k
    else:
        return -1  # Return -1 if k is not found

def linear_search(arr, k):
    search = mapcode(rho, f, pi)
    x = (arr, k)
    return search(x)

# Example usage:
linear_search([1, 2, 3, 4, 5], 3)  # Should return 2 (index of the first occurrence of 3)
linear_search([1, 2, 3, 4, 5], 6)  # Should return -1 (6 is not in the list)
