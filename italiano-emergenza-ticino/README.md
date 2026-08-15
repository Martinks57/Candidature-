# Italiano d'emergenza — Programme 60 jours (Tessin / FCTSA)

Programme d'apprentissage intensif de l'italien d'urgence préhospitalière, conçu pour un ambulancier francophone (DEA) préparant une transition vers le canton du Tessin — réseau **FCTSA** / **Ticino Soccorso 144**.

**Niveau de départ visé :** italien B2 général. Le programme ne réenseigne pas la grammaire de base ; il installe l'automatisme lexical du terrain.

---

## Contenu : 650 éléments sur 60 jours

| Bloc | Jours | Éléments | Contenu |
|---|---|---|---|
| [Bloc 1](bloc-1-jours-01-25.md) | 1 → 25 | 250 (10/jour) | Grammaire de terrain, connecteurs logiques, verbes d'action, orientation et espace, adjectifs fréquents |
| [Bloc 2](bloc-2-jours-26-50.md) | 26 → 50 | 250 (10/jour) | Bilan ABCDE, protocole SAMPLER, OPQRST, anatomie, symptômes, questions rituelles |
| [Bloc 3](bloc-3-jours-51-60.md) | 51 → 60 | 150 (15/jour) | Matériel de l'autoambulanza, transmissions radio 144, jargon tessinois et suisse |
| **Total** | **60** | **650** | |

Chaque élément comporte quatre colonnes : terme italien, traduction française, phrase d'exemple en contexte d'intervention, traduction de la phrase.

### Note sur la répartition du Bloc 3

Le cahier des charges initial demandait 10 à 11 éléments par jour *et* 150 éléments sur les jours 51 à 60 — deux contraintes arithmétiquement incompatibles (10 jours × 11 = 110 au maximum). La priorité a été donnée aux **totaux exacts** (250 / 250 / 150 = 650) : les jours 51 à 60 comptent donc 15 éléments chacun. Ce bloc étant essentiellement du vocabulaire concret (matériel, sigles, statuts radio), la charge cognitive par élément y est plus faible que dans les blocs 1 et 2 — la densité accrue reste soutenable.

---

## Méthode d'utilisation quotidienne

Prévoir **30 à 40 minutes par jour**, en trois temps :

1. **Découverte (10 min).** Lire le tableau du jour à voix haute. Prononcer chaque phrase d'exemple en entier — jamais le mot isolé. La mémorisation d'un terme d'urgence hors phrase ne survit pas au stress de l'intervention.
2. **Restitution active (15 min).** Cacher la colonne italienne et reformuler depuis le français. C'est le sens FR → IT qui compte : sur le terrain, vous partirez toujours de votre pensée en français.
3. **Simulation (10 min).** Enchaîner à voix haute 3 à 5 phrases du jour dans un scénario fictif d'intervention. À partir du jour 26, imposer systématiquement la structure du bilan (ABCDE puis SAMPLER).

### Révision espacée

Réviser le contenu du jour J aux jours **J+1, J+3, J+7, J+21**. Le fichier Anki fourni gère cet espacement automatiquement — c'est sa raison d'être.

### Jalons de progression

| Jour | Compétence attendue |
|---|---|
| 25 | Conduire un dialogue de terrain complet (accès, installation, réassurance) sans recours au français |
| 40 | Dérouler une anamnèse SAMPLER entière de mémoire |
| 50 | Réaliser un bilan ABCDE verbalisé à voix haute en moins de 3 minutes |
| 60 | Transmettre un cas au Pronto Soccorso et tenir un échange radio avec la centrale 144 |

---

## Exports pour flashcards

Deux formats sont générés dans [`exports/`](exports/) :

| Fichier | Format | Usage |
|---|---|---|
| `exports/vocabolario-650.csv` | CSV, UTF-8 avec BOM | Excel, Numbers, Google Sheets, Quizlet |
| `exports/anki-650.txt` | TSV avec en-têtes Anki | Import direct dans Anki |

### Import dans Anki

1. Anki → *Fichier* → *Importer* → sélectionner `exports/anki-650.txt`
2. Les en-têtes `#separator:tab`, `#html:true` et `#tags column:5` configurent l'import automatiquement.
3. Choisir un type de note à **4 champs** : Italien, Français, Exemple IT, Exemple FR.
4. Chaque carte est taguée `italiano_urgenza`, `bloc1|bloc2|bloc3` et `giornoNN` — ce qui permet d'étudier bloc par bloc, ou de filtrer un jour précis (`tag:giorno42`).

**Sens de révision recommandé :** créer les cartes en **Français → Italien**. La reconnaissance passive (IT → FR) est déjà acquise à un niveau B2 ; c'est la production active qui manque en intervention.

### Régénérer les exports

Après toute modification des fichiers Markdown :

```bash
python3 tools/export.py
```

Le script vérifie l'intégrité du programme — 60 jours présents, 650 éléments exactement, aucun doublon de terme au sein d'un même jour — et échoue si une de ces conditions n'est pas remplie.

---

## Particularités linguistiques suisses intégrées

Le programme ne transmet pas l'italien d'Italie mais celui pratiqué au Tessin :

| Terme retenu | Équivalent italien d'Italie | Remarque |
|---|---|---|
| medicamento | farmaco | Usage suisse standard, présent dans tout le SAMPLER |
| autoambulanza | ambulanza | Terme officiel des services tessinois |
| Pronto Soccorso | Pronto Soccorso | Identique, mais désigne le service hospitalier de destination |
| posteggio | parcheggio | Helvétisme courant |
| formulario | modulo | Helvétisme administratif |
| natel | cellulare, telefonino | Helvétisme, largement compris au Tessin |
| picchetto | reperibilità | Service de garde, terme suisse standard |
| cassa malati | assicurazione sanitaria | Système LAMal |

Sont également couverts : numéros d'urgence suisses (144, 117, 118, 1414), Rega et elisoccorso, FCTSA, EOC, Croce Verde, réseau radio Polycom, capacité de discernement et directives anticipées, ricovero a scopo di assistenza.

---

## Structure du dépôt

```
italiano-emergenza-ticino/
├── README.md
├── bloc-1-jours-01-25.md      250 éléments
├── bloc-2-jours-26-50.md      250 éléments
├── bloc-3-jours-51-60.md      150 éléments
├── tools/
│   └── export.py              génération CSV + Anki, contrôle d'intégrité
└── exports/
    ├── vocabolario-650.csv
    └── anki-650.txt
```
