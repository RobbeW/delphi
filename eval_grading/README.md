# Selectie nakijken

Een lokale nakijkstudio voor **Echte Evaluatie - De Selectie (3NW)**. Je krijgt per leerling één PDF met een totaalscore op 27, het overzicht van zes oefeningen en per oefening vier rubriekscores, een motivatie en gerichte feedback. De toepassing verstuurt niets.

## Openen

Dubbelklik op **Start nakijken.command** op macOS. De startknop gebruikt een aanwezige Python met ReportLab, bereidt de batch voor en opent de lokale nakijkstudio. Stop de server met Ctrl-C in het terminalvenster. Er wordt niets automatisch geïnstalleerd.

Ontbreekt de omgeving, installeer vanuit de projectmap:

```sh
python3 -m venv eval_grading/.venv
eval_grading/.venv/bin/python -m pip install -r eval_grading/requirements.txt
```

Handmatig starten:

```sh
python3 -m eval_grading.app prepare
python3 -m eval_grading.app serve --open
```

`prepare` zoekt precies één ZIP en één CSV onder `2026-2027`. Geef bij andere bestanden `--archive`, `--scoresheet` en eventueel `--content-root` mee. De standaardinhoud staat onder `content/02-Hoofdstuk 2 - Selectie/7-Evaluatie/`. Een andere werkmap geef je met `--workspace PAD` vóór het commando.

## Nakijken en PDF vrijgeven

1. Kies een klas en leerling. Open een oefening en bekijk de broncode, oorspronkelijke platformstatus, lokale tests en het leerdoel.
2. Controleer elk van de vier voorgestelde scores. Pas de score, motivatie en feedback waar nodig aan; vink het criterium aan wanneer je het hebt nagekeken. Open criteria zijn geen nul.
3. Controleer de leerlinggerichte teksten **Wat al lukt** en **Volgende stap**.
4. Vul je naam in, bevestig de bron en bewaar de beoordeling. **Bewaar en keur goed** is beschikbaar zodra alle 24 criteria ingevuld en nagekeken zijn.
5. Download de definitieve leerling-PDF. Kies in het klasfilter een klas voor de ZIP met uitsluitend goedgekeurde leerling-PDF's. De CSV bevat de actuele goedgekeurde totaalscores en alle 24 criteriumscores.

Niet bewaarde wijzigingen blokkeren downloads en navigatie naar een andere leerling. Na een opgeslagen wijziging is de eerdere goedkeuring ongeldig. Een definitieve download of klasexport wordt altijd vanuit de huidige goedgekeurde revisie gemaakt. Oude reeds gedownloade of op schijf bewaarde PDF's zijn historische kopieën; verspreid de actuele versie via de nakijkstudio.

## Punten en voorstellen

**Rubric verduidelijkt op 16 november 2026:** zie [de inhoudelijke beoordelingsrubric](RUBRIC.md). Leesbaarheid betreft alle benodigde gegevens, invoeren en uitvoer. Invoer alleen levert geen programmeerpunt op. De huidige automatische voorstellen en de eerdere eindbeoordelingen passen deze verduidelijking nog niet toe; zij vereisen inhoudelijke herbeoordeling voordat ze als gecorrigeerde resultaten worden gebruikt.

**3NW1 is inmiddels volledig herbeoordeeld.** De nieuwe beoordeling en vergelijking staan in `private/selection-2026-regrade-3nw1-2026-11-16/`. De standaardwerkmap en eerdere PDF's bevatten nog de oorspronkelijke beoordelingen; 3NW2 en 3NW4 zijn nog niet herbeoordeeld.

| Oefeningen | Functioneel | Leesbaarheid | Programmeerconcepten | Wiskundeconcepten | Totaal |
|---|---:|---:|---:|---:|---:|
| Eerste vijf, elk | 1 | 1 | 2 | 1 | 5 |
| Mobit | 0,5 | 0,5 | 0,5 | 0,5 | 2 |
| Hele toets | 5,5 | 5,5 | 10,5 | 5,5 | 27 |

De tussenliggende niveaus zijn **kalibratievoorstellen**: normaal werking 0/1, leesbaarheid en wiskunde 0/0,5/1, programmeren 0/1/2; Mobit werking 0/0,5 en de andere criteria 0/0,25/0,5. Controleer deze interpretatie bij het nakijken. De maxima zijn door de leerkracht bevestigd.

Werking gebruikt de oorspronkelijke platformstatus als historisch bewijs. De andere drie rubrieken worden onafhankelijk voorgesteld: een fout programma krijgt niet automatisch overal nul. Leesbaarheid gebruikt eenvoudige aanwijzingen rond namen en structuur. Programmering gebruikt passende invoer/conversies en selectie, met signalen voor bekende fouten. Wiskunde gebruikt de rekenresultaten en relevante categorieën bij de beschikbare voorbeelden. Deze voorstellen vervangen je inhoudelijke broncontrole niet: een structuurcontrole bewijst niet dat elke tak juist is, en een geslaagde testset bewijst niet alle mogelijke gevallen.

Er wordt geen ingezonden Python via `exec`, `eval` of een subprocess uitgevoerd. Een beperkte interpreter controleert de ondersteunde instructies met limieten. Onbekende constructies, syntaxproblemen en niet aantoonbare conceptkennis blijven waar nodig open. Er wordt geen externe AI-dienst gebruikt. De oorspronkelijke taille-heupset van 30 gevallen is door de leerkracht bevestigd; de overige lokale testrevisies zijn diagnostiek. De vrouwelijke exacte grenzen ontbreken in die taille-set en worden niet stilzwijgend als nieuwe strafgevallen toegevoegd.

## Lokale bestanden en batches

Originele ZIP/CSV blijven ongewijzigd. De werkmap `private/selection-2026/` bevat de basisbeoordeling, huidige docentbeslissingen en rapporten. De standaardbatch bevat de 71 leerlingen met klaslabel. Drie ongelabelde accounts worden apart geteld. Je kunt die expliciet opnemen met `prepare --include-unlabelled` in een **nieuwe** werkmap.

```sh
python3 -m eval_grading.app drafts
python3 -m eval_grading.app teacher-csv --output eval_grading/private/goedgekeurde-scores.csv
python3 -m eval_grading.app release --class-name '3nw1' --output eval_grading/private/3nw1-goedgekeurd.zip
```

De voorlopige PDF's staan in `private/selection-2026/drafts/`, per klas en leerling. De voorbereide batch bevat ook `voorlopige-leerling-pdfs.zip` en `voorlopig-overzicht.csv` in dezelfde werkmap. Deze startbestanden zijn voorlopige snapshots; maak na correcties actuele PDF's via de nakijkstudio. Definitieve versies staan onder `final/`. Bij iedere PDF hoort een privémanifest met de bronbinding en beoordelingsrevisie. Bewaar de **volledige werkmap samen met de originele invoer** als besloten back-up. De toepassing weigert gewijzigde bronnen, rubric of beoordelingslogica; maak bij een bewuste nieuwe versie een nieuwe werkmap en behoud het vorige dossier.

`private/`, de invoer-ZIP/CSV en de lokale omgeving zijn uitgesloten van Git. Houd ze privé en serveer deze projectmap niet als openbare website met echte leerlingbestanden erin. De nakijkstudio zelf bedient alleen zijn eigen vaste webbestanden en gecontroleerde API, bindt uitsluitend op 127.0.0.1 en gebruikt een sessietoken. Leerling-PDF's bevatten geen e-mailadressen, interne bestandspaden of bronhashes.

## Ontwikkelcontrole

Voor de synthetische tests is naast ReportLab ook `pypdf` nodig:

```sh
python3 -m unittest discover -s eval_grading/tests -v
node --check eval_grading/app/web/app.js
```

De tests gebruiken fictieve leerlingen en controleren intake, veilige interpretatie, onafhankelijke scorevoorstellen, bronbinding, revisies, goedkeuring en PDF-uitvoer. Browsertests en PDF-rendercontrole voor deze oplevering zijn vastgelegd in de lokale harness-run; echte leerlinggegevens blijven daarbuiten.

Een voorwaarde achter `else` kost punten voor programmeerconcepten: het voorstel is maximaal 1/2, of 0,25/0,5 bij Mobit. Gebruik `elif` voor een extra voorwaarde. Dit verandert de oorspronkelijke code en de score voor werking niet.
