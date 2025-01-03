import secrets # números aleatórios mais seguros que o random.
import string # manipulação de caracteres.
scaracters=(string.punctuation) # Caracteres especiais
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result=[]

def password():
    for number in range(5):
        number=secrets.choice(scaracters)
        result.append(number)
        number=secrets.randbelow(11)
        result.append(number)
        number=secrets.choice(letters)
        result.append(number)
    print("by:")
    print(" __     ______           __ __               __ ")
    print("|  |--.|      |.--.--.--|  |__|.-----.-----.|__|")
    print("|     ||  --  ||  |  |  _  |  ||     |     ||  |")
    print("|__|__||______||_____|_____|__||__|__|__|__||__|")
    print("Your password as: ")
    for results in result:
        print(results, end = "") # end = "" Remove quebra de linha automática.
    print("") # Linha vazia
password()

while True:
    result.clear()
    choice = input("Generate another password (s/n)?  ")
    if choice == "s" or choice == "S":
        password()
    elif choice == "n" or choice == "N":
        break
    else:
        print("Invalid option... ")