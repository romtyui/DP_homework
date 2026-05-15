# 挑戰 1：簡易登入系統

users = {}

while True:
    choice = input("請選擇操作選項（a 註冊, b 登入, c 退出）? ")

    # 註冊
    if choice == "a":
        account = input("請輸入帳號：")
        password = input("請輸入密碼：")

        if account in users:
            print("帳號已存在，請重新輸入!")
        else:
            users[account] = password
            print("註冊成功!")

    # 登入
    elif choice == "b":
        account = input("請輸入帳號：")
        password = input("請輸入密碼：")

        if account in users:
            if users[account] == password:
                print("登入成功!")
            else:
                print("密碼錯誤!")
        else:
            print("帳號不存在，請先註冊!")

    # 退出
    elif choice == "c":
        print("系統已退出")
        break

    # 輸入錯誤
    else:
        print("輸入錯誤，請輸入 a、b 或 c")

    print()