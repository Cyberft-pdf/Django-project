import pygame
import ephem

# Vytvoření objektu pro Mars
mars = ephem.Mars()

# Nastavení data a času
date = ephem.now()

# Výpočet polohy Marsu
mars.compute(date)

# Získání rektascenze a deklinace Marsu
ra = mars.ra
dec = mars.dec

# Výpis polohy Marsu
print("Aktuální poloha Marsu:")
print("Rektascenze:", ra)
print("Deklinace:", dec)
