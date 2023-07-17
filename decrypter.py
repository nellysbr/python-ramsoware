import os
import pyaes

## Abrir o Arquivo criptografado

file_name = 'teste.txt.crypto'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de decryptação

key = b'chavede16bytesse'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)


## remover arquivo criptografado

os.remove(file_name)

## criando um novo arquivo criptografado

new_file = "teste.txt"
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()