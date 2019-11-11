#f = open("새파일.txt", 'w')
import ecdsa
import os
#pip3 install ecdsa
ec = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) 
vk = sk.verifying_key
#keygen
#const privateKeyLocation = "wallet/" + (process.env.PRIVATE_KEY || "default");
#const privateKeyFile = privateKeyLocation + "/private_key";

privateKeyLocation = ""
privateKeyFile = privateKeyLocation+"/private_key.txt" #txt파일?

def generatePrivateKey():
    keyPair = ec.get_verifying_key()
    privatekey = vk.getPrivate()
    return str(privatekey)


def initWallet():
    f = open(privateKeyFile, 'w') #load 체크
    try:
        if not(os.path.isdir("wallet/")):
            os.makedirs(os.path.join("wallet/"))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory")
            raise
    try:
        if not(os.path.isdir(privateKeyLocation)):
            os.makedirs(os.path.join(privateKeyLocation))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory")
            raise

    newPrivateKey = generatePrivateKey()
    f.write(privateKeyFile,newPrivateKey)
    print("Create new wallet with private key to:"+privateKeyFile)


def getPrivateFromWallet():
    buffer = fs.read(privateKeyFile)
    return str(buffer)


def getPublicFromWallet():
    privateKey = getPrivateFromWallet()
    key = ec.keyFromPrivate(privateKey,"hex")
    return key.getPublic().encode("hex");
