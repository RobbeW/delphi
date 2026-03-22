# Project Delphi

Project Delphi is een webgebaseerde leeromgeving voor Python in de klas.  
De toepassing is ontworpen om computationeel denken + Python te oefenen en snelle feedback te geven.

De naam *Delphi* verwijst naar de Griekse site Delphi en vormt een inhoudelijke spiegel met de Python in de Klas-oefenreeks op Dodona.

## Mythologische context voor Delphi en Python

In de Griekse mythologie is Python (Πύθων) de slang die in Delphi leefde, een plaats die door de oude Grieken als het centrum van de aarde werd beschouwd.  
Python werd verbonden met het orakel van Delphi en met de aardgodin Gaia.  
In de latere mythe doodt Apollo Python en neemt hij de orakelplaats over, waarna Delphi uitgroeit tot een van de meest gezaghebbende religieuze centra in de Grieks-Romeinse wereld.

## Doelstelling

Project Delphi ondersteunt leerlingen en lesgevers bij:

- het oefenen van programmeerconcepten in een gecontroleerde browseromgeving;
- het uitvoeren en evalueren van oefeningen met testcases;
- het opvolgen van voortgang en het documenteren van resultaten.

Deze omgeving is bedoeld voor educatief gebruik. 

## Functionaliteiten

- Python-code uitvoeren in de browser, gebaseerd op Papyros.
- Oefeningen laden vanuit een gestructureerde `content/`-catalogus.
- Evaluatie met testcases en detailweergave per testcase.
- Invoerondersteuning voor `input()` via runtime-inputveld.
- PDF-export van reeksen met leerlinggegevens en rubric voor feedback.
- Lokale opslag van code, pogingen, tijd en evaluatiestatus per oefening.
- Ingebouwd formularium en ondersteunende UI voor klasgebruik.

## Technisch

- Front-end: `index.html`, `styles.css`, `app.js`
- Runtime: Papyros (Python/JavaScript in browser)
- Contentindex: zie `tools/build-catalog.mjs`

## Projectstructuur

```text
.
├── app.js
├── index.html
├── styles.css
├── input-sw.js
├── papyros-python-worker.js
├── papyros-javascript-worker.js
├── content/
│   ├── catalog.json
│   └── <hoofdstuk>/<subhoofdstuk>/<oefening>/...
├── tools/
│   └── build-catalog.mjs
├── LICENSE
└── THIRD_PARTY_NOTICES.md
```

## Lokale opstart

### Vereisten

- Een lokale webserver (vereist voor service worker en `input()`-ondersteuning)
- Node.js (nodig om `catalog.json` opnieuw op te bouwen)

### Starten in ontwikkeling

1. Start een lokale server in de projectmap:

```bash
python3 -m http.server 8000
```

2. Open:

```text
http://localhost:8000
```

Gebruik de toepassing niet via `file://`, omdat service workers dan niet correct werken.

## Werken met content

Plaats oefeningen in deze mappenstructuur:

```text
content/
  01-Hoofdstuk/
    01-Subhoofdstuk/
      01-Oefening/
        description/description.nl.md
        evaluation/tests.yaml   # optionee
        starter/starter.py      # optioneel
```

Bouw nadien de catalogus opnieuw op:

```bash
node tools/build-catalog.mjs
```


## Evaluatie en feedback

- Evaluatie gebeurt op basis van testbestanden in `evaluation/`.
- Resultaten tonen een samenvatting en testcase-details in een uitklapbaar overzicht.
- Bij export naar PDF is een rubric voorzien voor leerkrachtfeedback.


## Licenties

- Projectlicentie: zie [LICENSE](LICENSE)
- Third-party licenties en notices (waaronder Papyros MIT): zie [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)

## Contact

Voor vragen, feedback of samenwerking:

- https://robbewulgaert.be/contact
**OPGELET:** dit project is louter voor educatieve doeleinden en de ontwikkelaar(s) belooft geen support voor dit webplatform. 
Dit is ontwikkelt als hobby-project. Wens je vakinhoudelijke en vakdidactische ondersteuning voor de oefenreeks? Wend je tot onze uitgelichtte cursus op Dodona! 
