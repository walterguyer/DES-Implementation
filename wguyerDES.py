#Permuted Choice 1
PC_1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
#Shift Sequence
SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
#Permuted Choice 2
PC_2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

def permutedChoice1(key64):
    key56 = ""
    for i in PC_1:
        key56 += key64[i-1]
    return key56

def permutedChoice2(key56):
    key48 = ""
    for i in PC_2:
        key48 += key56[i-1]
    return key48

def shiftBits(i,key):
    shiftedKey = key[SHIFTS[i]:] + key[:SHIFTS[i]]
    return shiftedKey

def createKeys(key64):
    #list of subkeys
    keys = []
    #Perform Permuted Choice 1
    key56 = permutedChoice1(key64)
    print("The key after permuted choice 1 is: \n" + key56 + "\n")
    #Split bits
    c = key56[:28]
    d = key56[28:]
    #16 rounds of keys
    for i in range(16):
        #Shift bits
        Cn = shiftBits(i,c)
        Dn = shiftBits(i,d)
        #Permuted Choice 2
        keys.append(permutedChoice2(Cn + Dn))
        c = Cn
        d = Dn
    return keys

key64 = input("Please input key: ")
print("The input key is : \n" + key64 +"\n")
subKeys = createKeys(key64)
for i in range(16):
    print("Subkey number " + str(i+1) + " is: \n" + subKeys[i] + "\n")
