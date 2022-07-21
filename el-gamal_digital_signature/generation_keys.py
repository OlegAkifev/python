from Cryptodome.Util import number
from modules import gcd, power_mod


# Генерируем p
def gen_p():
    p = number.getPrime(512)
    return p


# Генерируем g
def gen_g(p):
    while True:
        g = number.getPrime(512)
        if 1 < g < p:
            return g


# Генерируем закрытый ключ x
def gen_x(p):
    while True:
        x = number.getPrime(512)
        if 1 < x < (p - 1):
            return x


# Вычисляем y
def calculate_y(g, x, p):
    y = power_mod(g, x, p)
    return y


# Генерируем ессионный ключ k
def gen_k(p):
    while True:
        k = number.getPrime(512)
        if gcd(k, p - 1) == 1 and 1 < k < (p - 1):
            return k


# Создание файла с открытыми ключами (y, g, p)
def create_file_with_public_keys(y, g, p):
    public_keys = [y, g, p]
    with open('file_with_public_keys', 'w') as file_with_public_keys:
        for key in public_keys:
            file_with_public_keys.writelines(str(key) + '\n')
        file_with_public_keys.close()


# Создание файла с закрытым ключом x
def create_file_with_private_key(x):
    with open('file_with_private_key', 'w') as file_with_private_key:
        file_with_private_key.write(str(x))
        file_with_private_key.close()
    return file_with_private_key


# Создание файла с сессионным ключом k
def create_file_with_session_key(k):
    with open('file_with_session_key', 'w') as file_with_session_key:
        file_with_session_key.write(str(k))
        file_with_session_key.close()
    return file_with_session_key


def generation_keys():
    p = gen_p()
    g = gen_g(p)
    x = gen_x(p)
    y = calculate_y(g, x, p)
    k = gen_k(p)
    create_file_with_private_key(x)
    create_file_with_public_keys(y, g, p)
    create_file_with_session_key(k)
    print(f'p = {p} ')
    print(f'g = {g} ')
    print(f'x = {x} ')
    print(f'y = {y} ')
    print(f'k = {k} ')


generation_keys()
