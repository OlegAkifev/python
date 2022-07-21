import hashlib
from modules import find_inverse_elem, power_mod


# Цифровая подпись файла
def digital_signature(name_of_file, private_key_file, public_keys_file, session_key_file, signature):
    with open(name_of_file, 'rb') as f:
        m = hashlib.sha1()
        while True:
            data = f.read(1024)
            if not data:
                break
            m.update(data)
        hash_file = int(m.hexdigest(), 16)
    with open(private_key_file, 'r') as private_file:
        for elem in private_file:
            x_from_file = int(elem)
        private_file.close()
    numbers_public = []
    with open(public_keys_file, 'r') as public_file:
        for elem in public_file:
            numbers_public.append(int(elem))
        public_file.close()
    y, g, p = numbers_public[0], numbers_public[1], numbers_public[2]
    with open(session_key_file, 'r') as session_file:
        for elem in session_file:
            k_from_file = int(elem)
        session_file.close()
    a = power_mod(g, k_from_file, p)
    b = ((hash_file - x_from_file * a) * find_inverse_elem(k_from_file, p - 1)) % (p - 1)
    with open(signature, 'w') as signature:
        signature.write(str(a) + '\n')
        signature.write(str(b))
        signature.close()
    print(f'Файл подписан. Подпись \n a = {a}\n b = {b}')
    return signature


digital_signature('document.txt', 'file_with_private_key', 'file_with_public_keys', 'file_with_session_key',
                  'file_with_signature')
