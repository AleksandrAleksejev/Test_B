# C-OSA: väike moodul klassi ja abifunktsioonidega.
# Ülesanne: kirjuta teste, et leida vigased funktsioonid!

class BankAccount:
    def __init__(self, owner, balance=0):
        """owner: sõne, balance: mitte-negatiivne täisarv"""
        if not owner or not isinstance(owner, str):
            raise ValueError("Omanik peab olema mittetühi sõne")
        if balance < 0:
            raise ValueError("Algne saldo ei tohi olla negatiivne")
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        """Lisa positiivne summa saldole."""
        if amount <= 0:
            raise ValueError("Deposiit peab olema positiivne")
        self._balance += amount

    def withdraw(self, amount):
        """Võta positiivne summa välja; saldo ei tohi miinusesse minna."""
        if amount <= 0:
            raise ValueError("Väljamakse peab olema positiivne")
        if amount > self._balance:
            raise ValueError("Pole piisavalt raha kontol")
        self._balance -= amount

    def transfer_to(self, other, amount):
        """Kanna teisele kontole; valideeri mõlemad pooled ja summa."""
        if not isinstance(other, BankAccount):
            raise ValueError("Teine konto peab olema BankAccount objekt")
        if amount <= 0:
            raise ValueError("Ülekande summa peab olema positiivne")
        if amount > self._balance:
            raise ValueError("Pole piisavalt raha ülekandmiseks")
        self._balance -= amount
        other._balance += amount

    def balance(self):
        """Tagasta hetkene saldo (int)."""
        return self._balance

def fibonacci(n):
    """Tagasta n-s Fibonacci arv (0->0, 1->1); n>=0."""
    if n < 0:
        raise ValueError("Fibonacci arv ei ole defineeritud negatiivsete arvude jaoks")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def prime_factors(n):
    """Tagasta n algtegurid kasvavas järjekorras; n>=2."""
    if n < 2:
        raise ValueError("Algtegurid on defineeritud ainult arvude >= 2 jaoks")
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def moving_average(values, window):
    """Liikuv keskmine; window>0; tagasta float-väärtuste list."""
    if window <= 0:
        raise ValueError("Aken peab olema positiivne")
    if len(values) < window:
        return []
    result = []
    for i in range(len(values) - window + 1):
        avg = sum(values[i:i + window]) / window
        result.append(avg)
    return result

def normalize_scores(scores):
    """Normaliseeri [0..100] -> [0.0..1.0]; väljaspool olevad väärtused ValueError."""
    for score in scores:
        if score < 0 or score > 100:
            raise ValueError("Skoorid peavad olema vahemikus [0, 100]")
    return [score / 100.0 for score in scores]
