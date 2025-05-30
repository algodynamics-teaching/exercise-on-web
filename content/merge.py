from mapcode.main import mapcode
from collections import deque
from functools import lru_cache
import copy

# === 1. Recursive Merge ===


def merge_recursive(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge_recursive(a[1:], b)
    else:
        return [b[0]] + merge_recursive(a, b[1:])


# === 2. Mapcode Merge ===


def rho_mapcode(inst):
    a, b = inst
    return [a, b, []]


def next_mapcode(x):
    a, b, c = x
    if not a and not b:
        return x
    if not a:
        return [[], [], list(reversed(b)) + c]
    if not b:
        return [[], [], list(reversed(a)) + c]
    if a[0] < b[0]:
        return [a[1:], b, [a[0]] + c]
    else:
        return [a, b[1:], [b[0]] + c]


def pi_mapcode(x):
    a, b, c = x
    return list(reversed(c))


def merge_mapcode(a, b):
    return mapcode(rho_mapcode, next_mapcode, pi_mapcode)((a, b))


# === 3. DP-style Merge (Fixed Point Map)


def scons(x, xs):
    if not xs:
        return [x]
    return [x] + xs


def bot():
    return None


def rho_dp(inst):
    a, b = inst
    return [[(a, b)], {}]


def next_dp(state):
    pending, fs = state
    if not pending:
        return state
    (a, b), *rest = pending
    key = (tuple(a), tuple(b))
    if key in fs:
        return [rest, fs]
    if not a:
        fs[key] = lambda x: b
        return [rest, fs]
    if not b:
        fs[key] = lambda x: a
        return [rest, fs]
    if a[0] < b[0]:
        ta = a[1:]
        updated_key = (tuple(ta), tuple(b))
        fs[key] = lambda x: scons(a[0], x[updated_key])
        return [[(ta, b)] + rest, fs]
    else:
        tb = b[1:]
        updated_key = (tuple(a), tuple(tb))
        fs[key] = lambda x: scons(b[0], x[updated_key])
        return [[(a, tb)] + rest, fs]


def pi_dp(state):
    _, fs = state
    return fs


def fixed_point(f, x0):
    x = x0
    while True:
        x1 = f(x)
        if x1 == x:
            return x
        x = x1


def apply_fs(fs):
    def apply(x):
        return {k: f(x) for k, f in fs.items()}

    return apply


def bot_hash(keys):
    return {k: bot() for k in keys}


def merge_dp(a, b):
    # Generate function set
    state = rho_dp((a, b))
    while True:
        new_state = next_dp(state)
        if new_state == state:
            break
        state = new_state
    fs = pi_dp(state)

    keys = fs.keys()
    x0 = bot_hash(keys)
    G = apply_fs(fs)
    G_star = fixed_point(G, x0)
    key = (tuple(a), tuple(b))
    return G_star[key]


# === Alias main merge ===
merge = merge_mapcode
