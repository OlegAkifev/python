def egcd(c, d):
    if c == 0:
        return d, 0, 1
    else:
        g, x, y = egcd(d % c, c)
        return g, y - (d // c) * x, x


# Ищем обратный элемент в кольце по модулю
def find_inverse_elem(k, p):
    g, x, _ = egcd(k, p)
    if g == 1:
        return x % p


# НОД
def gcd(p, k):
    if p < k:
        return gcd(k, p)
    elif p % k == 0:
        return k
    else:
        return gcd(k, p % k)


# Возведение в степень по модулю
def power_mod(b, e, m):
    x = 1
    while e > 0:
        if e % 2:
            b, e, x = (b * b) % m, e // 2, (b * x) % m
        else:
            b, e, x = (b * b) % m, e // 2, x

    return x

