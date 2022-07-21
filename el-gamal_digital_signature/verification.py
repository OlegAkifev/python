import hashlib
from modules import power_mod


# Проверка подписи у файла. Сообщение о наличии/отсутствии изменений в файле
def verification(name_of_file, public_keys_file, signature):
    numbers_public = []
    numbers_signature = []
    with open(name_of_file, 'rb') as f:
        m = hashlib.sha1()
        while True:
            data = f.read(1024)
            if not data:
                break
            m.update(data)
        hash_file = int(m.hexdigest(), 16)
    with open(public_keys_file, 'r') as public_file:
        for elem in public_file:
            numbers_public.append(int(elem))
        public_file.close()
    y, g, p = numbers_public[0], numbers_public[1], numbers_public[2]
    with open(signature, 'r') as signature_file:
        for elem in signature_file:
            numbers_signature.append(int(elem))
        signature_file.close()
    a, b = numbers_signature[0], numbers_signature[1]
    check_1 = (power_mod(y, a, p)) * (power_mod(a, b, p)) % p
    check_2 = power_mod(g, hash_file, p)
    if check_1 == check_2:
        print(f'file without changes \n {check_1} \n =\n {check_2}')
    else:
        print('file changed')


verification('document.txt', 'file_with_public_keys', 'file_with_signature')
