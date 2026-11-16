# Beoordelingsrubric — verduidelijking 16 november 2026

Deze rubric verwerkt de verduidelijking van de leerkracht: leesbaarheid en programmeerconcepten beoordelen de uitwerking van de hele oefening. Een duidelijke naam of één invoerinstructie levert niet automatisch punten op. Deze uitleg vervangt de eerdere interpretatie die volle leesbaarheid toeliet voor een duidelijke maar nauwelijks uitgewerkte oplossing.

De bestaande code voor automatische voorstellen past deze verduidelijking nog niet toe. Ook de opgeslagen beoordelingen en PDF's van 15 november zijn hiermee nog niet opnieuw beoordeeld. De analyse en kandidaten voor herbeoordeling staan privé bij het beoordelingsdossier. Gebruik oude scores dus niet als voorbeelden van deze aangescherpte rubric.

Op 16 november is 3NW1 volledig herbeoordeeld in een apart dossier: `private/selection-2026-regrade-3nw1-2026-11-16/`. Daar staan de nieuwe beoordeling en vergelijking met de vorige scores. Het oorspronkelijke dossier en de eerdere PDF's zijn behouden. 3NW2 en 3NW4 zijn nog niet herbeoordeeld volgens deze verduidelijking.

## Maxima en niveaus

| Oefeningen | Functioneel | Leesbaarheid | Programmeerconcepten | Wiskundeconcepten |
|---|---:|---:|---:|---:|
| Eerste vijf, elk | 1 | 1 | 2 | 1 |
| Mobit | 0,5 | 0,5 | 0,5 | 0,5 |

De toets blijft op 27. Normale niveaus: functioneel 0/1, leesbaarheid en wiskunde 0/0,5/1, programmeren 0/1/2. Bij Mobit: functioneel 0/0,5 en de overige categorieën 0/0,25/0,5. Er worden geen nieuwe tussenpunten toegevoegd.

## Leesbaarheid

Beoordeel of **alle benodigde gegevens, invoeren en uitvoeronderdelen** herkenbaar en overzichtelijk zijn uitgewerkt. Controleer passende namen, duidelijke invoervragen, begrijpelijke berekeningsrollen, inspringing en de uitvoer in alle benodigde gevallen. Een fraaie naam in één regel bewijst dit niet.

- **1 punt:** de volledige benodigde gegevensstroom en uitvoer zijn uitgewerkt en goed te volgen. De gebruikte namen zijn passend en duidelijk.
- **0,5 punt:** een substantieel, samenhangend deel is begrijpelijk uitgewerkt, maar benodigde onderdelen ontbreken of zijn onduidelijk.
- **0 punten:** er is onvoldoende uitwerking om deze kwaliteit voor de oefening aan te tonen: bijvoorbeeld alleen een naam, alleen invoer of invoer met een onafgemaakte voorwaarde.

Voor Mobit worden deze punten 0,5/0,25/0. De aanwezigheid van namen of het ontbreken van stijlproblemen is geen zelfstandig bewijs voor volle punten. Ontbrekende uitvoer verhindert volle punten; het bepaalt zonder bronlezing niet automatisch of nul of gedeeltelijk passend is.

"Alle benodigde variabelen" gaat over de betekenis van de gegevens. Verplicht geen specifieke namen of extra variabelen: een berekening rechtstreeks in `print` mag. Eén gezamenlijke `print` kan de uitvoer van meerdere takken verzorgen. Exacte uitvoertekst en rekenkundige juistheid horen bij hun eigen categorieën; die bepalen niet op zichzelf de leesbaarheid.

## Programmeerconcepten

Beoordeel de **gezamenlijke toepassing** van de voor de oefening benodigde invoer, correcte datatypes, toekenningen, verwerking, vergelijkingen, Booleaanse logica, keuzes, inspringing en uitvoer. Invoer lezen is één element; er is geen vast punt voor invoer en een tweede vast punt voor selectie.

- **2 punten:** de benodigde concepten zijn in de volledige oefening correct toegepast. Keuzes en gegevensverwerking vormen een samenhangend geheel.
- **1 punt:** een substantieel, relevant onderdeel combineert meerdere concepten correct, terwijl belangrijke onderdelen ontbreken of verkeerd zijn toegepast.
- **0 punten:** alleen een begin of skelet is zichtbaar, zonder betekenisvol uitgewerkte verwerking. Alleen `input`, ook met `int` of `float`, is onvoldoende voor een punt.

Voor Mobit worden deze punten 0,5/0,25/0. Een voorwaarde achter `else` beperkt de programmeerscore tot maximaal de helft. Dit is een bovengrens, geen gegarandeerd half punt. Beoordeel hoeveel verder correct is uitgewerkt.

Controleer het datatype op de plaats van gebruik. `input` levert tekst; voor numerieke vergelijkingen en berekeningen is een passend numeriek datatype nodig. Een latere conversie kan correct zijn. Een `float` ergens in de code bewijst niet dat alle benodigde invoeren correct worden verwerkt. Een tekstinvoer voor het geslacht hoeft juist niet numeriek te worden.

Verplicht niet letterlijk `if`, `elif` én `else` als een andere geldige structuur dezelfde gevallen afhandelt. Geneste keuzes, correcte onafhankelijke controles en equivalente oplossingen kunnen volledig correct zijn. Een formulefout wist op zichzelf correct toegepaste programmeerconcepten niet uit; een syntaxfout wist evenmin automatisch alle zichtbare kennis uit.

## Functioneel en wiskundeconcepten

Functioneel blijft gekoppeld aan het historische platformresultaat. Nieuwe diagnostische tests vervangen dat bewijs niet stilzwijgend.

Wiskunde beoordeelt de aantoonbare formules, modellen, verhoudingen, eenheden en grenzen. Een formule kan wiskundig juist zijn terwijl een programmeerfout de uitvoering verhindert. Het ontbreken van de rest van de wiskundige uitwerking telt wel mee. Ontbrekende programmaonderdelen worden bij iedere categorie op de eigen grond beoordeeld; geen automatische nul voor alle categorieën bij iedere fout.

## Oefeningsdekking

Deze checklist beschrijft rollen en gevraagde uitvoer, geen verplichte lijst variabelen of aantallen instructies.

| Oefening | Benodigde gegevens en verwerking | Benodigde uitvoer |
|---|---|---|
| Colruyt | Aantal verpakkingen; prijs en passende kortingsgevallen; totaal en afronding | De totaalprijs voor elk benodigd aantal |
| Driehoeksongelijkheid | Drie afzonderlijke zijden; de drie strikte ongelijkheden en een gezamenlijke beslissing | Zowel een driehoek als geen driehoek kunnen melden |
| Leeftijd hond | Numerieke hondenleeftijd; de drie leeftijdsgevallen en omzetting naar mensenjaren | Het aantal mensenjaren voor alle leeftijdsgevallen |
| Taille-heup | Geslacht als tekst; taille en heup als numerieke gegevens; verhouding; risico per geslacht en bereik | Zowel de verhouding als de risicocategorie |
| Ideale lichaamsmassa | Leeftijd in maanden; beide leeftijdsformules en omzetting van maanden naar jaren; bovengrens | Massa voor beide toepasselijke groepen en melding voor te hoge leeftijd |
| Mobit | Fietstijd; kort tarief; begonnen blokken en cumulatieve tariefgroepen | Kostprijs voor alle tariefgroepen |

## Kalibratievoorbeelden

| Ingediende uitwerking | Leesbaarheid normaal | Programmeerconcepten normaal | Reden |
|---|---:|---:|---|
| Alleen `leeftijd = input(...)` | 0 | 0 | Alleen een begin; numeriek datatype, verwerking, keuzes en uitvoer ontbreken |
| Alleen `leeftijd = int(input(...))` | 0 | 0 | Correct datatype voor één invoer bewijst nog geen uitgewerkte oefening |
| Drie zijden inlezen, gevolgd door `if zijde` | 0 | 0 | Er is nog geen substantieel uitgewerkte vergelijking, beslissing of uitvoer |
| Taille, heup en geslacht inlezen en de verhouding correct berekenen; geen risico of uitvoer | Hoogstens 0,5 | Hoogstens 1 | Een samenhangend deel is uitgewerkt; belangrijke delen ontbreken. Motiveer brongebonden of gedeeltelijk credit passend is |
| Hele oefening duidelijk uitgewerkt, met correcte datatypes en keuzes, maar een verkeerde rekenformule | Kan 1 zijn | Kan 2 zijn | Beoordeel de formulefout bij wiskunde en het resultaat bij functioneel |

Een losse naam zoals `tijd` krijgt ook bij Mobit geen leesbaarheidspunt. Een positief commentaar kan een goede naam of correcte invoer benoemen zonder daarvoor automatisch punten toe te kennen.

## Vereiste onderbouwing bij herbeoordeling

Leg per oefening vast welke gegevensrollen, invoeren, uitvoeronderdelen en programmeerconcepten nodig zijn, welke aanwezig zijn en wat ontbreekt. Motiveer het gekozen niveau met de ingediende code. Een algemene tekst over passende namen is onvoldoende als enige onderbouwing voor volle leesbaarheid.

Lees alle antwoorden opnieuw voor een herziene eindbeoordeling. De structurele screening vindt duidelijke risico's, maar mist bijvoorbeeld ontbrekende takken, lege `print`-instructies en slechts gedeeltelijk afgedekte uitvoer. Aantallen variabelen, `input`, `if` of `print` zijn aanwijzingen en geen scoringsformule.
