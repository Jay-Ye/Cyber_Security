import rsa
pubkey, privkey = rsa.newkeys(1024) #生成公钥和私钥

pub = pubkey.save_pkcs1()
pri = privkey.save_pkcs1('PEM') #将生成的公钥和私钥进行转换，以便存储

with open("pubkey.pem", mode='wb') as f, open('privkey.pem', mode='wb') as fl:
    f.write(pub)
    fl.write(pri)  #将公钥和私钥分别储存

with open("pubkey.pem", mode='rb') as f, open('privkey.pem', mode='rb') as fl:
    pub = f.read()
    pri = fl.read() #从文件中取出密钥
    pubkey = rsa.PublicKey.load_pkcs1(pub)  
    privkey = rsa.PrivateKey.load_pkcs1(pri)   #转换为原始形态

message = 'Hello world!'
info = rsa.encrypt(message.encode('utf-8'), pubkey) #使用公钥加密内容
msg = rsa.decrypt(info, privkey)  # 使用私钥解密
print(info)
print(msg.decode('utf-8'))