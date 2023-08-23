#Bank

name = 'Nurdan'
accountNo = '12132132'
remainder = 3000


SadAccount = {
    'name' : 'Sadik Taran',
    'accountNo' : '13245678',
    'remainder' : 3000,
    'addAccount' : 2000
}

NurAccount = {
    'name': 'Nurdan Kolay',
    'accountNo': '12345678',
    'remainder': 2000,
    'addAccount' : 1000
}

def moneyPull(account, count):
    print(f"Hello {account['name']}")

    if (account['remainder'] >= count):
        account['remainder'] -= count
        print('you can take money.')
    else:
        sum = account['remainder'] + account['addAccount']

        if (sum >= count):
            addAccountUsage = input('Add second account (y/n)')

            if addAccountUsage == 'e':

                addAccountUsagee = count - account['remainder']
                account['remainder'] = 0
                account['addAccount'] -= addAccountUsagee

                print('you take your money')
            else:
                print(f"{account['accountNo']} number {account['remainder']}")
        else:
            print('insufficient')

moneyPull(SadAccount, 3000)
moneyPull(SadAccount, 2000)