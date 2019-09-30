"""
CLUSTAL MUSCLE
Auteur: Demi van der Pasch

De functie van dit script is het verwerken van een percent identity
matrix afkomstig van ClustalO. De bruikbare percentages die zich hier in
bevinden worden gevisualiseerd in een histogram.
"""


# Hier worden packages geïmporteerd.
import re
import numpy as np
import matplotlib.pyplot as plt


class VerkrijgGegevens:

    def __init__(self, loc_best):
        # Deze variabele wordt bruikbaar gemaakt in de hele class.
        self.loc_best = loc_best

        # Hier wordt een lege lijst aangemaakt.
        self.perc_id = []

        # Hier wordt een functie aangeroepen.
        self.lees_bestand()

    def lees_bestand(self):
        """ Deze functie filtert de bruikbare percentages (zonder
        dubbele vergelijkingen) uit een percent identity matrix die af-
        komstig is van de tool ClustalO of Muscle. Al deze percentages
        worden toegevoegd aan een lijst.

        INPUT
        -   self.loc_best: (str) de locatie van het te openen bestand.

        OUTPUT
        -   self.perc_id: (list) bevat de bruikbare percentages uit een
            percent identity matrix van ClustalO.
        """

        # self.loc_best wordt gelezen. Wanneer deze niet wordt gevonden,
        # zal dit gemeld worden aan de hand van een print.
        try:
            bestand = open(self.loc_best, "r")
        except FileNotFoundError:
            print("Het door u gekozen bestand is niet gevonden.")
            exit()

        else:
            # Hier wordt geïtereerd over de regels in het bestand.
            for regel in bestand:

                # Hier worden middels een regular expression de headers
                # uit de regels gefilterd.
                if re.search("sp", regel):
                    match = re.search(r"(\d+):(\s)sp([^\s]+)", regel)

                try:
                    # De gevonden match wordt opgeslagen als header.
                    header = match.group()

                    # De headers en lege uiteinden van de regel worden
                    # uit de regel verwijderd.
                    regel = regel.replace(header, "")
                    regel = regel.rstrip()
                    regel = regel.lstrip()

                    # De regel wordt gesplitst.
                    regel = regel.split("100.0")

                    # Het eerste deel van de split wordt nogmaals ge-
                    # splitst en in een lijst geplaatst.
                    regel = list(regel[0].split(" "))

                    # Lege strings worden uit de lijst verwijderd.
                    while '' in regel:
                        regel.remove('')

                    # De percentages worden afgerond en in een lijst op-
                    # geslagen.
                    for perc in regel:
                        self.perc_id.append(round(float(perc)))

                except UnboundLocalError:
                    pass

                # Er bevinden zich "-nan" in de matrix, welke omgevormd
                # worden tot een value van 0.
                except ValueError:
                    perc = 0
                    self.perc_id.append(round(float(perc)))


class Histogram:

    def __init__(self, perc_id):
        # Deze variabele wordt bruikbaar gemaakt in de hele class.
        self.perc_id = perc_id

        # Hier wordt een lege lijst aangemaakt.
        self.perc_groep = []

        # Hier wordt een lege dictionary aangemaakt.
        self.perc_los = {}

        # Hier worden functies aangeroepen.
        self.bewerk_gegevens()
        self.maak_histogram()

    def bewerk_gegevens(self):
        """ Deze functie bewerkt de verkregen gegevens, zodat deze later
        in een histogram verwerkt kunnen worden. Het voorkomen van alle
        percent identities wordt bepaald, waarna de percentages als keys
        worden toegevoegd aan een dictionary en het bijbehorende voor-
        komen hiervan als values. Voor de nummering van de x-as wordt
        een lijst gevormd met de getallen 2 t/m 100 in stappen van 2.

        INPUT
        -   self.perc_id: (list) bevat de bruikbare percentages uit een
            percent identity matrix van ClustalO.

        OUTPUT
        -   self.perc_los: (dict)
                =>  Notatie = {percentage: voorkomen}
        -   self.perc_groep: (list) bevat de getallen 2 t/m 100 in
            stappen van 2.
        """

        # Hier wordt geïtereerd over de getallen 1 t/m 100.
        for x in range(1, 101):

            # Het voorkomen van elk percentage wordt geteld en toe-
            # gevoegd aan een dictionary.
            voorkomen = self.perc_id.count(x)
            self.perc_los[x] = voorkomen

        # Hier wordt geïtereerd over de getallen 2 t/m 101, met stappen
        # van 2. Deze getallen worden aan een lijst toegevoegd.
        for x in range(2, 102, 2):
            self.perc_groep.append(x)

    def maak_histogram(self):
        """ Deze functie visualiseert een dictionary met percentage
        identities en het voorkomen hiervan in de vorm van een
        histogram.

        INPUT
        -   self.perc_los: (dict) bevat alle percentage identities en
            het voorkomen hiervan.
                =>  Notatie = {percentage: voorkomen}
        -   self.perc_groep: (list) bevat de getallen 2 t/m 100 in
            stappen van 2.

        OUTPUT
        -   een histogram met op de x-as de verschillende groepen met
            percentage identities en op de y-as het voorkomen hiervan.
        """

        # De grootte van de grafiek wordt geregeld.
        plt.rcParams["figure.figsize"] = (25, 12)

        # De indeling van de grafiek wordt geregeld.
        indeling = np.arange(len(self.perc_los))
        x_indeling = np.arange(2, 102, 2)
        y_indeling = range(0, max(self.perc_los.values()), 500)

        # De achtergrond van de grafiek wordt donker gemaakt.
        plt.style.use(u'dark_background')

        # De indeling, waarden en kleur van de staven worden bepaald.
        plt.bar(indeling, list(self.perc_los.values()),
                color='mediumorchid')

        # De titels en opmaak hiervan worden aangemaakt.
        plt.title('Verdeling Percent Identity',
                  weight='semibold', fontsize=50)
        plt.xlabel('Percent identity (in %)',
                   weight='semibold', style='italic', fontsize=40)
        plt.ylabel('Aantal alignments',
                   weight='semibold', style='italic', fontsize=40)

        # De indeling, richting en lettergrootte van de benamingen bij
        # de x- en y-as worden bepaald.
        plt.xticks(x_indeling, self.perc_groep,
                   rotation='vertical', fontsize=30)
        plt.yticks(y_indeling, fontsize=30)

        # De layout wordt geminimaliseerd.
        plt.tight_layout()

        # De grafiek wordt weergegeven.
        plt.show()


def main():
    # De locatie van het te visualiseren bestand.
    loc_best = '/home/demivdpasch/Documents/Course 5/muscle_reviewed'

    # Hier worden classes aangeroepen.
    vg = VerkrijgGegevens(loc_best)
    Histogram(vg.perc_id)


main()
