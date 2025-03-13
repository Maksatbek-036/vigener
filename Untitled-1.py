
alpha=[]
for i in range(1072,1104):
    alpha.append(chr(i))

def create_vigenere_table(alpha):
  vigenere_table = []
  for i in range(32):
    vigenere_table.append(alpha[i:] + alpha[:i])
  return vigenere_table

def print_vigenere_table(vigenere_table):
  for i in range(len(vigenere_table)):
     print("\t|",end=" ")
     for j in range(len(vigenere_table[i])):
            print(vigenere_table[i][j],end=" ") 
     print(f"|{i}")
 
def crypto_vigenere(word,key,table):
    crypto_word=""
    for i in range(len(word)):
        for j in range(len(alpha)):
            if word[i]==alpha[j]:
                crypto_word+=table[j][key]
    return crypto_word
def decrypto_vigenere(word,key,table):
    crypto_word=""
    for i in range(len(word)):
        for j in range(len(alpha)):
            if word[i]==table[j][key]:
                crypto_word+=alpha[j]
    return crypto_word
    

def app_process():
    table=create_vigenere_table(alpha)
    while True:
        print("""Правила ввода:
          1) Вводить только слова на русском языке
          2) Вводить только целые числа для ключа от 0 до 31
  Хотите посмотреть таблицу Виженера? (да/нет)""")
        answer=input()
        if answer=="да":
            table=create_vigenere_table(alpha)
            print_vigenere_table(table)
        print("Введите слово для шифрования:")
        word=input()
        print("Введите номер ключа:")
        key=int(input())
        if key>31 or key<0:
            print("Неверный ключ")
            break
        print(f"Зашифрованное слово:{crypto_vigenere(word,key,table)}")
        print(f"Расшифрованное слово:{decrypto_vigenere(crypto_vigenere(word,key,table),key,table)}")
        print("Хотите продолжить?")
        answer=input()
        if answer=="нет":
            break
        else:
            continue

    
  

if __name__ == "__main__":
   
    app_process()




