class Bank:
    def __init__(self, bank_name, dep_list=None, cred_list=None):
        self.bank_name = bank_name
        self.dep_list = dep_list or []
        self.cred_list = cred_list or []

    def add_dep(self, deposit):
        self.dep_list.append(deposit)

    def delete_dep(self, deposit):
        self.dep_list.remove(deposit)

    def add_cred(self, credit):
        self.cred_list.append(credit)

    def delete_cred(self, credit):
        self.cred_list.remove(credit)

    def inf(self):
        print('Банк:', self.bank_name, 'Вклады :', ', '.join(map(str, self.dep_list)))
        print('Банк:', self.bank_name, 'Кредиты :', ', '.join(map(str, self.cred_list)))


class Deposit(Bank):
    def __init__(self, name, currency, annual_interest_rate, max_sum, min_sum, bank_name):
        Bank.__init__(self, bank_name)
        self.name = name
        self.currency = currency
        self.annual_interest_rate = annual_interest_rate
        self.max_sum = max_sum
        self.min_sum = min_sum
        self.bank = bank_name

    def info(self):
        print('Вклад:', self.name, 'Валюта:', self.currency, 'Процентная ставка:', self.annual_interest_rate, '%',
    'Минимальная сумма:', self.min_sum, 'Максимальная сумма:', self.max_sum, 'Банк:', self.bank_name)

    def finance_calc(self, amount, validity):
        self.amount = amount
        self.validity = validity
        percent = self.annual_interest_rate/100
        per_month = round(percent / 12, 3)
        for i in range(0, self.validity * 12):
            print('Месяц', i+1, ':', round(self.amount * ((1+per_month) ** (i+1))), self.currency)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Credit(Bank):
    def __init__(self, name, currency, annual_interest_rate, down_payment, bank_name):
        Bank.__init__(self, bank_name)
        self.name = name
        self.currency = currency
        self.annual_interest_rate = annual_interest_rate
        self.down_payment = down_payment
        self.bank_name = bank_name

    def info_credit(self):
        print('Вклад:', self.name, 'Валюта:', self.currency, 'Процентная ставка:', self.annual_interest_rate, '%',
    'Первоначальный взнос:', self.down_payment, '%', 'Банк:', self.bank_name)

    def fin_calc(self, total, validity):
        self.total = total
        self.validity = validity
        percent = self.annual_interest_rate / 100
        for i in range(0, self.validity * 12):
            print('Месяц', i + 1, ':', round((total*percent*(1+percent)**validity) / (12 * ((1 + percent)**validity-1)), 2), self.currency)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


d = Deposit('Годовой', 'euro', 10, 2000, 4, 'alfa')
d.info()
d.finance_calc(1000, 2)
c = Credit('Выгодный', 'euro', 20, 10, 'alfa')
c.info_credit()
c.fin_calc(100, 1)
b = Bank('prior')
b.add_dep(d)
b.add_cred(c)
b.inf()