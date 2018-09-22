def creatingList(binary):
    binary = binary.replace("0","0 ")
    binary = binary.replace("1","1 ")
    return binary.split()

def verifyBinary(binary):
    for bit in binary:
        if(bit != '0' and bit != '1'):
            return True
    
    return False

def paridade(binary):
    count = 0
    for bit in binary:
        if bit == '1':
             count+=1
    if((count%2) == 0):
        return '0'
    else:
        return '1' 

def removeParity(binary):
    del binary[0]
    return binary
    
def main(binary_receiver):
    binary_receiver = creatingList(binary_receiver)
    parity_receiver = binary_receiver[0]
    new_binary_receiver = removeParity(binary_receiver)
    new_parity_receiver = paridade(new_binary_receiver)

    if(new_parity_receiver == parity_receiver):
        return "Nenhum erro detectado"
    else:
        return "Erro detectado"

def Test():
    #Test One
    binary_receiver_ok = ['101101011', '00101101', '00000', '1011111', '11111111']
    binary_receiver_err = ['101101001', '00101111', '100000', '1011110', '01111111']

    for i in range(5):
        print("\n" + binary_receiver_ok[i] + ": \n" + main(binary_receiver_ok[i]))
        print("\n" + binary_receiver_err[i] + ": \n" + main(binary_receiver_err[i]))

    return 1    
    
Test()











