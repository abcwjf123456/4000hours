import socket

pheno = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pheno.connect(("127.0.0.1", 8000))  # 连接
pheno.send('gg'.encode('utf-8'))  # 发送
data = pheno.recv(1024)  # 接收
print(data)
pheno.close()
