from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglal(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in self.foglalasok:
                    if foglalas.szoba == szoba and foglalas.datum == datum:
                        print("Ez a szoba már foglalt ezen a napon!")
                        return None
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return foglalas
        print("Hibás szobaszám!")
        return None

    def lemond(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print("Foglalás sikeresen törölve!")
                return
        print("Nem található ilyen foglalás!")

    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}, Ár: {foglalas.szoba.ar}")

def adatok_feltoltese(szalloda):
    szoba1 = EgyagyasSzoba("101")
    szoba2 = KetagyasSzoba("102")
    szoba3 = EgyagyasSzoba("103")
    szalloda.uj_szoba(szoba1)
    szalloda.uj_szoba(szoba2)
    szalloda.uj_szoba(szoba3)

    szalloda.foglalasok = [
        Foglalas(szoba1, datetime(2024, 5, 15)),
        Foglalas(szoba2, datetime(2024, 5, 17)),
        Foglalas(szoba3, datetime(2024, 5, 19)),
        Foglalas(szoba1, datetime(2024, 5, 20)),
        Foglalas(szoba2, datetime(2024, 5, 22))
    ]

def main():
    szalloda = Szalloda("Példa Szálloda")
    adatok_feltoltese(szalloda)

    while True:
        print("\n1 - Foglalás")
        print("2 - Lemondás")
        print("3 - Foglalások listázása")
        print("0 - Kilépés")

        valasztas = input("\nVálassz egy műveletet: ")

        if valasztas == "1":
            szobaszam = input("Add meg a szobaszámot: ")
            datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                if datum < datetime.now():
                    print("Hibás dátum! Csak jövőbeli foglalás lehetséges.")
                    continue
                foglalas = szalloda.foglal(szobaszam, datum)
                if foglalas:
                    print(f"Foglalás sikeres! Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}, Ár: {foglalas.szoba.ar}")
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "2":
            szobaszam = input("Add meg a szobaszámot: ")
            datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                szalloda.lemond(szobaszam, datum)
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "3":
            print("\nFoglalások:")
            szalloda.foglalasok_listazasa()

        elif valasztas == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás! Kérlek, válassz a felsorolt lehetőségek közül.")

if __name__ == "__main__":
    main()
