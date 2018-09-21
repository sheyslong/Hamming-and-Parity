binary  = input()

def paridade(binary:
    count = 0
    for bit in binary:
        if bit == "1":
             count++
    return count
