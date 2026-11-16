"""Public exercise mapping and teacher-calibration defaults."""
EXERCISES = [
 ('colruyt', 'Colruyt', '08 Colruyt', 'korting en afronding'),
 ('driehoeksongelijkheid', 'Driehoeksongelijkheid', '10 Driehoeksongelijkheid', 'de drie strikte ongelijkheden'),
 ('leeftijd-hond', 'Leeftijd hond', '11 Leeftijd hond', 'de drie leeftijdsgevallen'),
 ('taille-heup', 'Taille-heup verhouding', '07 Taille-heup', 'de verhouding en risicogrenzen'),
 ('lichaamsmassa', 'Ideale lichaamsmassa', '09 Lichaamsgewicht', 'de formules per leeftijdsbereik'),
 ('mobit', 'Mobit deelfietsen', '12 Mobit deelfietsen', 'begonnen tijdsblokken en tarieven'),
]
DIMENSIONS = ('functioneel', 'leesbaarheid', 'programmeerconcepten', 'wiskundeconcepten')
NORMAL = (1, 1, 2, 1)
MOBIT = (.5, .5, .5, .5)

# Calibration prompts: the teacher checks meaning, not token presence.
DESCRIPTORS = {
 'colruyt': 'Bereken 3,29 euro per verpakking; twee verpakkingen krijgen 20% korting, meer dan twee 30%, afgerond op twee decimalen.',
 'driehoeksongelijkheid': 'Controleer alle drie strikte driehoeksongelijkheden; gelijke som vormt geen driehoek.',
 'leeftijd-hond': 'Het eerste jaar telt 15 mensenjaren, het tweede 9 extra, en elk volgend jaar 5 extra.',
 'taille-heup': 'Bereken taille gedeeld door heup en vergelijk de verhouding met de bij het geslacht passende risicogrenzen.',
 'lichaamsmassa': 'Gebruik 0,5 × maanden + 4 onder 12 maanden en 2 × (maanden / 12) + 10 tot en met 120 maanden; meld hogere leeftijden.',
 'mobit': 'Reken begonnen blokken van 20 minuten cumulatief aan volgens de vier tarieven; onder vier minuten kost de rit 0,29 euro.',
}
