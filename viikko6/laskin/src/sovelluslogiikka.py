from abc import ABC, abstractmethod
class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen = arvo

    def _paivita(self, arvo):
        self._edellinen = self._arvo
        self._arvo = arvo

    def miinus(self, operandi):
        self._paivita(self._arvo - operandi)

    def plus(self, operandi):
        self._paivita(self._arvo + operandi)

    def nollaa(self):
        self._paivita(0)

    def aseta_arvo(self, arvo):
        self._paivita(arvo)

    def kumoa(self):
        self._arvo, self._edellinen = self._edellinen, self._arvo

    def arvo(self):
        return self._arvo

class BinaariOperaatio(ABC):
    def __init__(self, logiikka, io):
        self.io = io
        self.sovelluslogiika = logiikka

    def suorita(self):
        self.laske()

    @abstractmethod
    def laske(self):
        pass

class Summa(BinaariOperaatio):
    def __init__(self, logiikka, io):
        super().__init__(logiikka, io)

    def laske(self):
        return self.sovelluslogiika.plus(int(self.io()))

class Erotus(BinaariOperaatio):
    def __init__(self, logiikka, io):
        super().__init__(logiikka, io)

    def laske(self):
        return self.sovelluslogiika.miinus(int(self.io()))

class Nollaus(BinaariOperaatio):
    def __init__(self, logiikka, io):
        super().__init__(logiikka, io)

    def laske(self):
        return self.sovelluslogiika.nollaa()

class Kumoa(BinaariOperaatio):
    def __init__(self, logiikka, io):
        super().__init__(logiikka, io)

    def laske(self):
        return self.sovelluslogiika.kumoa()
