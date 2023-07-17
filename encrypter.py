import os
import pyaes

## Abrir o Arquivo a ser criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remover Arquivo Original

os.remove(file_name)

## Definir a chave de encryptação

key = b'chavede16bytesse'
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar o arquivo

crypto_data = aes.encrypt(file_data)

## Salvando arquivo criptografado

new_file = file_name + ".crypto"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()	