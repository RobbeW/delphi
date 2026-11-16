# Analyse — Echte Evaluatie De Selectie (3NW)

Onderzocht op 14 november 2026. Analyse van de ZIP, het interne inzendmanifest, de losse scoresheet en de overeenkomende lokale opdrachten, referentieoplossingen en testbestanden. De oorspronkelijke bestanden zijn ongewijzigd. Leerlingprogramma's zijn niet uitgevoerd en er zijn geen individuele rubricpunten toegekend.

## Bevestigde puntenverdeling

| Oefening | Functioneel | Leesbaarheid | Programmeerconcepten | Wiskundeconcepten | Maximum |
|---|---:|---:|---:|---:|---:|
| Colruyt | 1 | 1 | 2 | 1 | 5 |
| Driehoeksongelijkheid | 1 | 1 | 2 | 1 | 5 |
| Leeftijd hond | 1 | 1 | 2 | 1 | 5 |
| Taille-heup verhouding | 1 | 1 | 2 | 1 | 5 |
| Ideale lichaamsmassa | 1 | 1 | 2 | 1 | 5 |
| Mobit deelfietsen | 0,5 | 0,5 | 0,5 | 0,5 | 2 |
| **Totaal** | **5,5** | **5,5** | **10,5** | **5,5** | **27** |

Mobit heeft vier eigen maxima van 0,5. Een algemene halvering van een gewone oefening zou 2,5 opleveren en is dus onjuist. De toegelaten tussenliggende puntniveaus zijn nog niet bevestigd; de maxima bepalen die niveaus niet vanzelf. Er is geen omzetting naar /20 vastgelegd.

## Bestanden en aansluiting

- De ZIP bevat 356 Python-bestanden en één CSV-manifest met 356 inzendingen. Iedere combinatie van account en oefening komt eenmaal voor. Een volledige pogingengeschiedenis is niet meegeleverd.
- Het interne manifest heeft onder meer bestandsnaam, account-ID, oefening-ID, inzending-ID, aanmaakdatum en platformstatus. Het is een ander bestand dan de losse scoresheet.
- De losse scoresheet bevat 74 accounts en één rij `maximum`. Die maximumrij is geen leerling. Het automatische totaal is /6: één binaire score per oefening.
- Er zijn 71 accounts met klaslabel: 3nw1 telt 21, 3nw2 telt 25 en 3nw4 telt 25. Drie accounts hebben geen klaslabel.
- Alle 71 accounts met klaslabel hebben minstens één bestand. Eén account zonder klaslabel heeft één taille-heupinzending; de overige twee ongelabelde accounts hebben geen bestanden. Neem ongelabelde accounts niet stilzwijgend in een klasrapport op; hun rol is nog onbekend.
- Alle 356 manifestregels verwijzen naar bestaande bronbestanden; er zijn geen extra Python-bestanden, dubbele paden of dubbele inzending-ID's. Alle accountgegevens en statussen sluiten aan op de losse scoresheet.
- Het archief doorstaat de integriteitscontrole en bevat geen versleutelde bestanden, symlinks of onveilige relatieve paden. Er is niets uitgepakt of uitgevoerd.
- De inzendingstijdstippen lopen van 12 november 2026 om 08:39:15 tot 13 november 2026 om 11:16:51, telkens +0100.

## Overzicht van de 71 accounts met klaslabel

De onderstaande waarden zijn platformstatussen, geen rubricbeoordelingen. De ene ongelabelde taille-heupinzending is hier buiten gehouden; die staat in het manifest als correct.

| Oefening | Python-bestand aanwezig | Platform correct | Platform wrong | Compilatiefout | Runtimefout | Niet gestart |
|---|---:|---:|---:|---:|---:|---:|
| Colruyt | 71 | 44 | 21 | 1 | 5 | 0 |
| Driehoeksongelijkheid | 69 | 44 | 21 | 3 | 1 | 2 |
| Leeftijd hond | 58 | 38 | 16 | 3 | 1 | 13 |
| Taille-heup verhouding | 67 | 31 | 16 | 13 | 7 | 4 |
| Ideale lichaamsmassa | 61 | 39 | 15 | 3 | 4 | 10 |
| Mobit deelfietsen | 29 | 2 | 19 | 7 | 1 | 42 |
| **Totaal oefening/accountcombinaties** | **355** | **198** | **108** | **30** | **19** | **71** |

Voor alle 74 accounts samen bevat het archief 199 correcte, 108 foute, 30 compilatiefout- en 19 runtimefoutinzendingen. Er zijn daarnaast 88 niet-gestarte combinaties zonder bestand. Hun afwezigheid sluit aan op de scoresheet; het betreft geen mislukte extractie.

Alle 356 bestanden zijn als tekst gelezen en statisch geparseerd. Er zijn 326 syntactisch parseerbaar en 30 met een syntax- of inspringfout, overeenkomend met het aantal platformcompilatiefouten. Vier parseerbare bestanden bevatten geen uitvoerbare statements. Eventuele opmerkingen of zichtbaar denkwerk moeten nog bekeken worden voordat die als volledig leeg worden beoordeeld. Parseerbaarheid bewijst geen correcte werking.

## Oefeningen en rubricinterpretatie

De bronnen hieronder staan onder `content/02-Hoofdstuk 2 - Selectie/7-Evaluatie/`. Iedere genoemde map bevat `description/description.nl.md`, `solution/solution.nl.py` en `evaluation/tests.yaml`. De namen sluiten aan op de export. De ZIP bevat geen exacte versie van de Dodona-opgaven of tests. Op 14 november bevestigde de gebruiker de gebruikte taille-heuptestset door de volledige YAML te leveren; de 30 gevallen komen inhoudelijk overeen met het lokale testbestand. Voor de overige oefeningen en de exacte opgaveteksten blijft de revisiekoppeling nog te bevestigen.

| Oefening / bronmap | Programmeerconcepten | Wiskundeconcepten en controlepunten |
|---|---|---|
| Colruyt — `08 Colruyt` | Invoer en conversie; variabelen en berekeningen; passende selectie; afronding en uitvoer. | €3,29 per verpakking; twee verpakkingen geven 20% korting, meer dan twee 30%; juiste kortingsfactor en afronding op twee decimalen. |
| Driehoeksongelijkheid — `10 Driehoeksongelijkheid` | Drie invoeren; vergelijkingen en samengestelde booleaanse logica; correcte keuze en uitvoer. | Alle drie de ongelijkheden moeten gelden. Gelijkheid vormt geen driehoek. Een gelijkwaardige correcte aanpak is toegestaan. |
| Leeftijd hond — `11 Leeftijd hond` | Meerdere gevallen onderscheiden en de juiste berekening aan een tak koppelen. | Eerste jaar 15, tweede jaar 9 extra, daarna 5 per extra jaar: `24 + (leeftijd - 2) * 5`. Controleer 1, 2 en 3. |
| Taille-heup verhouding — `07 Taille-heup` | Gemengde invoertypen; verhouding berekenen; geslacht en risicocategorie combineren met passende voorwaarden. | Taille/heup; mannen: <0,94, daarna tot en met 1,00; vrouwen: <0,80, daarna tot en met 0,90. De referentie classificeert vóór afronding en rondt alleen de getoonde verhouding af. |
| Ideale lichaamsmassa — `09 Lichaamsgewicht` | Bereikselectie; berekeningen per tak; bericht buiten het toepassingsgebied. | Onder 12 maanden: `0.5 * maanden + 4`. Vanaf 12 tot en met 120: `2 * (maanden / 12) + 10`. Daarboven melding; één decimaal. |
| Mobit — `12 Mobit deelfietsen` | Tijd in blokken omzetten, takken correct kiezen en berekeningsresultaten bewaren/gebruiken. Geen specifieke lus nodig. | Begonnen blokken van 20 minuten naar boven afronden; cumulatief drie blokken à €0,45, drie à €0,65, drie à €0,80, daarna €1 per blok. Onder vier minuten €0,29. Controleer onder andere 3/4, 20/21, 60/61, 120/121 en 180/181 minuten. |

Leesbaarheid wordt bij alle oefeningen apart beoordeeld: betekenisvolle namen, begrijpelijke structuur en passende inspringing, volgens wat in de klas is aangeleerd. Aanwezigheid van `if` of een formule is op zichzelf onvoldoende bewijs van correcte concepttoepassing.

Een steekproef uit parseerbare inzendingen met status `wrong` toont onder meer deze inhoudelijke verschillen: losse driehoeksvoorwaarden in een `if/elif`-keten; de vergeten aftrek van twee reeds verrekende hondenjaren; losse getallen achter `or` die de voorwaarde waar maken; maanden vermenigvuldigen in plaats van delen door twaalf; en Mobit-berekeningen waarvan het resultaat niet wordt opgeslagen of gebruikt. Dit zijn waarnemingen uit een steekproef, geen frequentiemeting of definitieve puntenaftrek.

Daarom mag `wrong` niet automatisch nul op alle vier de rubrieken worden. Een leerling kan een formule begrijpen maar een voorwaarde verkeerd schrijven, of selectie begrijpen maar een formule verkeerd opstellen. Iedere aftrek moet bij het eigen criterium passen. Een werkende oplossing kan eveneens conceptuele of leesbaarheidsbeperkingen hebben.

## Aandachtspunten in de lokale sleutel

1. Alle 30 verwachte taille-heupuitvoeren zijn gecontroleerd tegen de verhouding en de beschreven drempels; ze zijn correct. De gevallen `vrouw, 0.8, 100.0` en `vrouw, 0.9, 100.0` zijn geldige tests van kleine verhoudingen (0,008 en 0,009, beide afgerond 0,01 met laag risico). Ze testen de vrouwelijke grenzen 0,80 en 0,90 niet. De oorspronkelijke testset blijft historische beoordelingsbron. Aanvullende grensproeven, bijvoorbeeld 80/100 en 90/100, moeten afzonderlijk herkenbaar blijven en vormen zonder afgesproken beoordelingsregel geen automatische nieuwe puntenaftrek.
2. De taille-heupopgave vraagt afronding, maar legt de volgorde van classificeren en afronden niet helemaal expliciet vast. De referentie gebruikt de ongeronde verhouding. Bij geen van de 30 aangeleverde gevallen verandert de risicocategorie door eerst op twee decimalen af te ronden; de testset beslist dit onderscheid dus niet. Leg de interpretatie bij kalibratie vast voordat aanvullende gevallen tot puntenaftrek leiden.
3. Leeftijd nul bij de hond is niet expliciet uitgewerkt in de opgave. Maak daarvan geen nieuw beslissend strafgeval zonder het toegelaten invoerbereik te bevestigen.
4. De CSV bevat geen foutlopende testcase, verwachte uitvoer, leerlinguitvoer of volledige beoordelaarsfeedback. De status verklaart de foutoorzaak dus niet. Gerichte bronanalyse of later geïsoleerd opnieuw testen is nodig.

## Gevolgen voor de nakijkpipeline

Deze batch kan rechtstreeks uit native Python worden ingelezen; PDF-extractie is voor de huidige invoer overbodig. Gebruik het interne manifest voor bestandskoppeling en de losse scoresheet voor rooster en platformstatus. Houd de vier nieuwe criteriumscores gescheiden van de bestaande binaire automatische score.

Een eerste versie moet per oefening vier bewijsgebonden beoordelingen voorstellen, die apart bijgesteld kunnen worden. Bewaar de oorspronkelijke code, platformstatus en eventuele nieuwe testresultaten als onderscheiden bewijsbronnen. Behoud conceptpunten bij gedeeltelijke oplossingen wanneer het bewijs dat rechtvaardigt. Bouw een leerlingrapport en klasoverzicht uit dezelfde beoordeling op, met leerkrachtnazicht vóór definitieve vrijgave.

Voor implementatie/calibratie blijven drie concrete beslissingen over: welke ongelabelde accounts bij de beoordeling horen; de precieze niveaus voor gedeeltelijke concept- en leesbaarheidspunten, inclusief Mobit; en bevestiging van de resterende lokale opgaven/sleutels tegen de gebruikte opdrachtversie. De taille-heuptestset is door de gebruiker bevestigd. De maxima en het totaal van 27 zijn bevestigd.

## Controlebewijs

Een reproduceerbaar lokaal analysescript en uitsluitend geaggregeerde controles staan in `.harness/runs/2026-11-14-submission-analysis/`. Archiefintegriteit, volledige manifestdekking, unieke koppelingen, overeenkomst van identiteitsvelden/statussen, binaire resultaten, totaalsommen en behoud van de oorspronkelijke bestandshashes zijn gecontroleerd. Er zijn geen persoonsgegevens of individuele scores naar dit rapport of de harness-verslagen gekopieerd.
