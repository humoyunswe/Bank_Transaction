from accounts import table_of_accounts, create_account, deposit_plus, deposit_minus, trans_history

def main():
    table_of_accounts()
    while True:
        print('''
    1. Account yaratish
    2. Deposit qoshish
    3. Deposit dan ishlatish
    4. Otkazmalar tarixini ko'rish
    5. Chiqish
    ''')
        choice = int(input("Buyruqni tanlang: "))

        if choice == 1:
            id_card = input("Account raqami: ")
            name = input("Account egasini ismi: ")
            create_account(id_card, name)

        elif choice == 2:
            id_card = input("Account raqami: ")
            amount = float(input("Qancha pul qoshmoqchisiz: "))
            deposit_plus(id_card, amount)

        elif choice == 3:
            id_card = input("Account raqami: ")
            amount = float(input("Qancha pul olmoqchisiz: "))
            deposit_minus(id_card, amount)

        elif choice == 4:
            id_card = input("Account raqami: ")
            trans_history(id_card)

        elif choice == 5:
            print("Chiqish...")
            break

        else:
            print("Notog'ri komanda. Iltimos boshqatan urinib koring.")

if __name__ == '__main__':
    main()
