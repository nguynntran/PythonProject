from bank_acount import *

Nguyen = BankAccount(1000, "Nguyen")
Thuy = BankAccount(2000, "Thuy")

# Nguyen.getBalance()

# Thuy.getBalance()

# Nguyen.deposit(800)

# Nguyen.withdraw(2000)

# Thuy.withdraw(500)

# Thuy.transfer(3000, Nguyen)

Dong = SavingAcct(1000, "Dong")

Dong.deposit(100)

Dong.transfer(100, Nguyen)