import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买手机
phone.bind(("127.0.0.1", 8000))  # 绑定手机卡需要传元组
phone.listen(5)  # 开机
cnv, sjk = phone.accept()  # 等电话 收到两个值一个ip地址  一个手机号
mag = cnv.recv(1024)  # 接消息
cnv.send("hello".encode('utf-8'))  # 发消息但要转换成二进制
print(mag)
cnv.close()
phone.close()
