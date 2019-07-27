# while循环
prompt = 'input'
messages = True
while messages:
    message = input(prompt)
    if message == 'quit':
        messages = False
    else:
        print(message)
