class Services:
    def __init__(self, name, currency, annual_interest_rate, bank_name):
        self.name = name
        self.currency = currency
        self.annual_interest_rate = annual_interest_rate
        self.bank_name = bank_name


class Deposit(Services):
    def __init__(self, name, currency, annual_interest_rate, min_sum, max_sum, bank_name=None):
        Services.__init__(self, name, currency, annual_interest_rate, bank_name)
        self.min_sum = min_sum
        self.max_sum = max_sum

    def info(self):
        print('Вклад:', self.name, 'Валюта:', self.currency, 'Процентная ставка:', self.annual_interest_rate, '%',
    'Минимальная сумма:', self.min_sum, 'Максимальная сумма:', self.max_sum, 'Банк:', self.bank_name)

    def finance_calc(self, amount, validity):
        percent = self.annual_interest_rate/100
        per_month = round(percent / 12, 3)
        for i in range(0, validity * 12):
            print('Месяц', i+1, ':', round(amount * ((1+per_month) ** (i+1))), self.currency)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Credit(Services):
    def __init__(self, name, currency, annual_interest_rate, down_payment, bank_name=None):
        Services.__init__(self, name, currency, annual_interest_rate, bank_name)
        self.down_payment = down_payment

    def info(self):
        print('Кредит:', self.name, 'Валюта:', self.currency, 'Процентная ставка:', self.annual_interest_rate, '%',
    'Первоначальный взнос:', self.down_payment, '%', 'Банк:', self.bank_name)

    def fin_calc(self, amount, validity):
        percent = self.annual_interest_rate / 100
        for i in range(0, validity * 12):
            print('Месяц', i + 1, ':', round((amount*percent*(1+percent)**validity) /
    (12 * ((1 + percent)**validity-1)), 2), self.currency)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Bank:
    def __init__(self, bank_name, dep_list=None, cred_list=None):
        self.bank_name = bank_name
        self.dep_list = dep_list or []
        self.cred_list = cred_list or []

    def add_dep(self, deposit):
        self.dep_list.append(deposit)
        deposit.bank_name = self.bank_name

    def delete_dep(self, deposit):
        self.dep_list.remove(deposit)

    def add_cred(self, credit):
        self.cred_list.append(credit)
        credit.bank_name = self.bank_name

    def delete_cred(self, credit):
        self.cred_list.remove(credit)

    def calc_dep(self, deposit, amount, validity):
        for i in self.dep_list:
            if i == deposit:
                deposit.finance_calc(amount, validity)
            else:
                print('нет такого вклада!')

    def calc_cred(self, credit, amount, validity):
        for i in self.cred_list:
            if i == credit:
                credit.fin_calc(amount, validity)
            else:
                print('нет такого кредита!')

    def inf(self):
        print('Банк:', self.bank_name, 'Вклады :', ', '.join(map(str, self.dep_list)))
        print('Банк:', self.bank_name, 'Кредиты :', ', '.join(map(str, self.cred_list)))


dep1 = Deposit('Простой', 'usd', 10, 100, 1000)
dep2 = Deposit('Сложный', 'usd', 10, 100, 1000)
crd1 = Credit('для ИП', 'usd', 20, 10)
crd2 = Credit('для физ.лиц', 'usd', 15, 5)
dep1.info()
crd1.info()
bank1 = Bank('Prior')
bank1.add_cred(crd1)
bank1.inf()
bank1.delete_cred(crd1)
bank1.inf()
bank1.add_cred(crd1)
bank1.calc_cred(crd1, 200, 1)
bank1.calc_cred(crd2, 200, 1)


