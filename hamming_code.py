def creatingList(binary):
    binary = binary.replace("0","0 ")
    binary = binary.replace("1","1 ")
    return binary.split()

def xor(bit_1, bit_2):
    bit_1 = int(bit_1)
    bit_2 = int(bit_2)
    if(not(bit_1) and bit_2) or (bit_1 and not(bit_2)):
        return 1
    else:
        return 0
def xorFive(bin1, bin2, bin3, bin4, bin5):
    return xor(xor(xor(xor(bin1, bin2), bin3), bin4), bin5)

def xorFour(bin1, bin2, bin3, bin4):
    return xor(xor(xor(bin1, bin2), bin3), bin4)

def detectionErr(binary):
    x1 = xorFive(binary[2], binary[4], binary[6], binary[8], binary[10])
    x2 = xorFive(binary[2], binary[5], binary[6], binary[9], binary[10])
    x4 = xorFour(binary[4], binary[5], binary[6], binary[11])
    x8 = xorFour(binary[8], binary[9], binary[10], binary[11])
    if(str(x1) == binary[0] and str(x2) == binary[1] and str(x4) == binary[3] and str(x8) == binary[7]):
        return False
    else:
        return True

def parity(binary):
    count = 0
    for bit in binary:
        if bit == '1':
             count+=1
    if((count%2) == 0):
        return 0
    else:
        return 1

def correctionErr(binary):
    Parity_1 = [binary[0], binary[2], binary[4], binary[6], binary[8], binary[10]]
    Parity_2 = [binary[1], binary[2], binary[5], binary[6], binary[9], binary[10]]
    Parity_3 = [binary[3], binary[4], binary[5], binary[6], binary[11]]
    Parity_4 = [binary[7], binary[8], binary[9], binary[10], binary[11]]

    parity_1 = parity(Parity_1)
    parity_2 = parity(Parity_2)
    parity_3 = parity(Parity_3)
    parity_4 = parity(Parity_4)

    index = parity_1 + parity_2 * 2 + parity_3 * 4 + parity_4 * 8
    if binary[index - 1] == '1' or binary[index - 1] == 1:
        binary[index - 1] = 0
    else:
        binary[index - 1] = 1

    return binary
    
def mainDetection(binary):
    binary = creatingList(binary)
    if detectionErr(binary):
        return("Erro Detectado")
    return("Ok")

def creatingString(binary):
    string = ''
    for bit in binary:
        string = string + str(bit)
    return string

def mainCorrection(binary):
    binary = creatingList(binary)
    if detectionErr(binary):
        return creatingString(correctionErr(binary))
    return creatingString(binary)

def TestDetection():
    binary_receiver_ok = ['101011111011', '001111001111', '100110111101', '111011101111', '111011101111']
    binary_receiver_err = ['100011111011', '001111001110', '100110110101', '111011101011', '111011101110']

    for i in range(5):
        print("\n" + binary_receiver_ok[i] +
              ": \n" + mainDetection(binary_receiver_ok[i]))
        print("\n" + binary_receiver_err[i] +
              ": \n" + mainDetection(binary_receiver_err[i]))

    return 1


def TestCorrection():
    binary_receiver_ok = ['101011111011', '001111001111', '100110111101', '111011101111', '111011101111']
    binary_receiver_err = ['100011111011', '001111001110', '100110110101', '111011101011', '111011101110']

    for i in range(5):
        print("Binario Certo: " + binary_receiver_ok[i] +
              "\nBinario Errado: " + binary_receiver_err[i] +
              "\nBinario Corrigido: " + mainCorrection(binary_receiver_err[i]))

    return 1
print("##########################Teste de detecção de erro################################################\n")
TestDetection()

print("\n#########################Teste de correção de erro###################################################\n")
TestCorrection()




  
