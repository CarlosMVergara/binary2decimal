dec = 0
numero_binario = 0
numero_decimal = 0
print("Dame un número para transformar a binario o decimal: ")
dec = int(input())

# Binario a decimal

def bin2dec(binario):
    dec = int(str(binario), 2)
    return dec

# Decimal a binario
def dec2bin(decimal):
    bina = ""
    bin(dec)
    bina = int(bin(decimal)[2:])
    return bina

numero_decimal = dec2bin(dec)
numero_binario = bin2dec(numero_decimal)
print("Numero binario: {}" .format(numero_binario))
print("Numero decimal: {}" .format(numero_decimal))