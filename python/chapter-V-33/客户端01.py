from socket import *

cb_w = ('127.0.0.1', 8000)
bc_n = 5
js_n = 1024
khd = socket(AF_INET, SOCK_STREAM)
khd.connect(cb_w)

while True:
    data = input('请输入:').strip()

    # if data=="":
    #     print("请重新输入:")
    # else:
    khd.send(data.encode('utf-8'))
    jd = khd.recv(js_n)
    print(jd.decode('utf-8'))

fwd.close()
