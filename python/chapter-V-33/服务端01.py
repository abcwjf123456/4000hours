from socket import *

ip_w = ('127.0.0.1', 8000)
bc_n = 5
js_n = 1024
fwd = socket(AF_INET, SOCK_STREAM)
fwd.setsockopt(SOCK_STREAM, SO_REUSEADDR, 1) #
fwd.bind(ip_w)
fwd.listen(bc_n)
print('服务端运行了')
while True:
    cnnn, iddr = fwd.accept()
    print(cnnn)
    print(iddr)

    while True:
        try:
            msg = cnnn.recv(js_n)
            print('服务端接收的信息为:', msg.decode('utf-8'))
            cnnn.send('服务端接收了信息'.encode('utf-8'))
        except Exception:
            break

    cnnn.close()
fwd.close()
