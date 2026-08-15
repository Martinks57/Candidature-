#!/usr/bin/env python3
"""Extrait les 650 éléments des fichiers Markdown du programme et génère :

  - exports/vocabolario-650.csv  : CSV (séparateur virgule, UTF-8 BOM, ouvrable dans Excel)
  - exports/anki-650.txt         : TSV importable directement dans Anki

Usage : python3 tools/export.py
"""

import csv
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
EXPORTS = RACINE / "exports"

SOURCES = [
    ("Bloc 1 - Socle de terrain", "bloc-1-jours-01-25.md"),
    ("Bloc 2 - Bilan medical", "bloc-2-jours-26-50.md"),
    ("Bloc 3 - Materiel, radio 144, Ticino", "bloc-3-jours-51-60.md"),
]

TITRE_JOUR = re.compile(r"^##\s+Jour\s+(\d+)\s+[—-]\s+(.*)$")
SEPARATEUR = re.compile(r"^\|[\s:|-]+\|$")


def decouper_ligne(ligne):
    """Renvoie les cellules d'une ligne de tableau Markdown, ou None."""
    if not ligne.startswith("|") or not ligne.endswith("|"):
        return None
    return [c.strip() for c in ligne[1:-1].split("|")]


def extraire(chemin, bloc):
    """Parcourt un fichier Markdown et renvoie ses lignes de vocabulaire."""
    jour = theme = None
    lignes = []

    for brute in chemin.read_text(encoding="utf-8").splitlines():
        ligne = brute.strip()

        entete = TITRE_JOUR.match(ligne)
        if entete:
            jour, theme = int(entete.group(1)), entete.group(2).strip()
            continue

        if SEPARATEUR.match(ligne):
            continue

        cellules = decouper_ligne(ligne)
        if not cellules or len(cellules) != 4:
            continue
        if cellules[0].startswith("Terme"):  # ligne d'en-tête du tableau
            continue
        if jour is None:
            raise SystemExit(f"{chemin.name}: tableau rencontré avant tout titre de jour")

        italien, francais, exemple, trad_exemple = cellules
        lignes.append(
            {
                "bloc": bloc,
                "jour": jour,
                "theme": theme,
                "italien": italien,
                "francais": francais,
                "esempio": exemple,
                "exemple_fr": trad_exemple,
            }
        )

    return lignes


def ecrire_csv(lignes, destination):
    with destination.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Bloc", "Jour", "Theme", "Italien", "Francais", "Esempio (IT)", "Exemple (FR)"]
        )
        for e in lignes:
            writer.writerow(
                [e["bloc"], e["jour"], e["theme"], e["italien"],
                 e["francais"], e["esempio"], e["exemple_fr"]]
            )


def ecrire_anki(lignes, destination):
    """TSV Anki : recto, verso, exemple IT, exemple FR, tags.

    Les trois lignes '#' en tête sont lues par Anki pour configurer l'import.
    """
    with destination.open("w", encoding="utf-8", newline="") as f:
        f.write("#separator:tab\n")
        f.write("#html:true\n")
        f.write("#tags column:5\n")
        for e in lignes:
            tags = f"italiano_urgenza bloc{e['bloc'][5]} giorno{e['jour']:02d}"
            champs = [
                e["italien"],
                e["francais"],
                f"<i>{e['esempio']}</i>",
                e["exemple_fr"],
                tags,
            ]
            f.write("\t".join(c.replace("\t", " ") for c in champs) + "\n")


def main():
    toutes = []
    for bloc, nom in SOURCES:
        chemin = RACINE / nom
        if not chemin.exists():
            raise SystemExit(f"Fichier source manquant : {chemin}")
        lignes = extraire(chemin, bloc)
        print(f"{nom:32s} {len(lignes):4d} éléments")
        toutes.extend(lignes)

    EXPORTS.mkdir(exist_ok=True)
    ecrire_csv(toutes, EXPORTS / "vocabolario-650.csv")
    ecrire_anki(toutes, EXPORTS / "anki-650.txt")

    # Contrôle d'intégrité : 60 jours, 650 éléments, aucun doublon italien par jour.
    jours = sorted({e["jour"] for e in toutes})
    attendus = list(range(1, 61))
    if jours != attendus:
        manquants = sorted(set(attendus) - set(jours))
        raise SystemExit(f"Jours manquants ou en trop : {manquants}")

    doublons = set()
    vus = set()
    for e in toutes:
        cle = (e["jour"], e["italien"].lower())
        if cle in vus:
            doublons.add(cle)
        vus.add(cle)
    if doublons:
        raise SystemExit(f"Doublons détectés : {sorted(doublons)}")

    print(f"\nTotal : {len(toutes)} éléments sur {len(jours)} jours")
    if len(toutes) != 650:
        raise SystemExit(f"ERREUR : {len(toutes)} éléments au lieu de 650")
    print("Exports écrits dans", EXPORTS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
