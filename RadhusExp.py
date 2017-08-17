# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

# Bolånekostnader
# -------- kostnader ----------

# köpe pris på radhuset
huspris = 6e6

# Driftkostnad per år
drift = 40e3

# Ränta på privat och banklån
bankInterest = 3e-2
privateInterest = 1.6e-2

# Amorterning
amortering = 2e-2

# -------- Intäkter -----------

# Inkomster efter skatt, 31% skatt.
KarinInkomst = 29700 * 0.69
PetterInkomst = 28700 *0.69


# intäkter från ev inneboenden
Inneboende = 4000

# utfallet arv

arv = 0.25 * huspris

# ----------------

# Resultaträkning, per månad

# Del av totalbelopp som är lånat av banken
part = 0.5

# ev förskott på arv
brittisGift= 0

# Med amorteringen borträknad som avgift
# amortering = 0

# Antal inneboenden
inneboenden = 0
inkomst = KarinInkomst+PetterInkomst+inneboenden*Inneboende


# Utan något arv
kostnad = ((huspris*part -brittisGift)*bankInterest + (huspris*part-brittisGift)*amortering +huspris*part*privateInterest + drift -((huspris*part -brittisGift)*bankInterest)*0.3 )/12
resultat = inkomst  - kostnad

# Med utdelat arv
HusRed = huspris * 0.75
kostnadRed = ((HusRed-brittisGift)*bankInterest + (HusRed-brittisGift)*amortering + drift)/12
resultatRed = inkomst - kostnadRed

print(kostnad,kostnadRed, resultat)

# plt.bplot(kostnad)
# Med utfallet arv

# Funkar detta verkligen??
