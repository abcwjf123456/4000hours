try:
    assert 1 == 2  # 断言
except Exception as e:
    print(e)
    print("cxc")
else:
    print("gg")
finally:
    print("f")
