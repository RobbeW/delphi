"""Explainable, provisional rubric suggestions. Teacher review remains explicit.

Math probes use the supplied/public test cases. Additional boundary probes never
silently replace historical functional evidence. No learner Python is executed.
"""
import ast
import math
import io
import tokenize
import re
from .evaluator import run, parse_source

VERSION = 'selectie-proposals-v2'
NUMBER = re.compile(r'(?<![\w.])[-+]?(?:\d+\.\d+|\d+)(?![\w.])')
PRACTICE = {
    'Colruyt': 'Controleer 1, 2 en 4 verpakkingen. Bereken eerst aantal × 3,29 en pas daarna de juiste kortingsfactor toe.',
    'Driehoeksongelijkheid': 'Probeer 4, 5, 2 en daarna 2, 3, 5. Alle drie de sommen moeten strikt groter zijn dan de overblijvende zijde.',
    'Leeftijd hond': 'Controleer leeftijden 1, 2 en 3. Na de eerste twee jaren tel je 5 × (leeftijd - 2) bij 24 op.',
    'Taille-heup verhouding': 'Bereken eerst taille / heup. Zoek daarna in de tabel de risicocategorie die bij het geslacht en die verhouding hoort.',
    'Ideale lichaamsmassa': 'Controleer 11, 12 en 120 maanden. Gebruik in de tweede formule maanden / 12 als leeftijd in jaren.',
    'Mobit deelfietsen': 'Controleer 3, 4, 60 en 63 minuten. Rond het aantal blokken naar boven af en tel de kosten van de eerdere tariefgroepen mee.',
}


def _calls(node, name):
    return [x for x in ast.walk(node) if isinstance(x, ast.Call)
            and isinstance(x.func, ast.Name) and x.func.id == name]


def _numbers(text):
    return [float(m.group()) for m in NUMBER.finditer(text)]


def _category(text):
    text = ' '.join(text.lower().split())
    if 'geen driehoek' in text:
        return 'geen driehoek'
    if 'een driehoek' in text:
        return 'een driehoek'
    for label in ('sterk verhoogd', 'verhoogd', 'laag'):
        if label in text:
            return label
    if 'te oud' in text:
        return 'te oud'
    return None


def _line_list(nodes):
    return ', '.join(str(n) for n in sorted({x.lineno for x in nodes})[:8])


def conditional_else(code):
    """Find invalid else conditions in original source, ignoring comments and strings."""
    tokens = []
    try:
        for token in tokenize.generate_tokens(io.StringIO(code).readline):
            tokens.append(token)
    except (tokenize.TokenError, IndentationError):
        pass
    ignored = {tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT,
               tokenize.COMMENT, tokenize.ENDMARKER}
    significant = [t for t in tokens if t.type not in ignored]
    starts=set(); at_start=True; depth=0; statement=0; statements={}
    for t in tokens:
        if t.type==tokenize.NEWLINE:at_start=True;statement+=1
        elif t.type not in ignored:
            statements[t.start]=statement
            if at_start and depth==0:starts.add(t.start)
            at_start=False
            if t.type==tokenize.OP:
                if t.string in ('(', '[', '{'):depth+=1
                elif t.string in (')', ']', '}'):depth=max(0,depth-1)
    lines = [t.start[0] for i, t in enumerate(significant[:-1])
             if t.type == tokenize.NAME and t.string == 'else' and t.start in starts
             and statements[t.start]==statements[significant[i+1].start]
             and significant[i + 1].string != ':']
    names = {t.string for t in significant if t.type == tokenize.NAME}
    return sorted(set(lines)), bool('if' in names or 'input' in names)


def enrich(code, title, maxima, tests, criteria, feedback):
    """Return extra evidence while editing only provisional nonfunctional marks."""
    def mark(key, points, reason):
        criteria[key].update(points=points, rationale=reason)

    if not code.strip():
        for key in ('leesbaarheid', 'programmeerconcepten', 'wiskundeconcepten'):
            mark(key, 0, 'Er is geen programma ingediend voor deze oefening.')
        feedback.update(strength='Er is geen ingediende oplossing beschikbaar.',
                        improve='Werk deze oefening uit en dien je programma in.')
        return {'proposal_version': VERSION, 'review_required': True}
    try:
        tree = parse_source(code)
    except SyntaxError as exc:
        else_lines, recognizable = conditional_else(code)
        reason = 'Achter else komt geen voorwaarde. Gebruik elif voor een extra voorwaarde.'
        if else_lines:
            mark('programmeerconcepten', maxima[2] / 2 if recognizable else 0, reason)
        feedback.update(strength='Je hebt een aanzet ingediend.',
                        improve=reason if else_lines else f'Controleer de schrijfwijze en inspringing rond regel {exc.lineno}.')
        return {'proposal_version': VERSION, 'review_required': True,
                'conditional_else': bool(else_lines), 'conditional_else_lines': else_lines,
                'pending_reason': 'Kijk de leesbaarheid en berekeningen na.'}

    nodes = list(ast.walk(tree))
    if not tree.body:
        for key in ('leesbaarheid', 'programmeerconcepten', 'wiskundeconcepten'):
            mark(key, None, 'Je code bevat alleen opmerkingen of lege regels.')
        feedback.update(strength='Er staan nog geen uitvoerbare instructies in je inzending.',
                        improve='Zet je aanpak om in invoer, berekeningen, keuzes en uitvoer.')
        return {'proposal_version': VERSION, 'review_required': True, 'pending_reason': 'Geen uitvoerbare instructies.'}

    assignments = [n for n in nodes if isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign))]
    names = {n.id for n in nodes if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}
    # Single-letter mathematical names are normal for sides, mass and ratios.
    allowed_short = {'a', 'b', 'c', 'm', 'p', 'n'} | ({'x','y','z'} if title=='Driehoeksongelijkheid' else set())
    obscure = sorted(n for n in names if len(n) == 1 and n not in allowed_short)
    long_lines = [i for i, line in enumerate(code.splitlines(), 1) if len(line) > 120]
    cramped = [i for i, line in enumerate(code.splitlines(), 1)
               if ';' in line.split('#', 1)[0] and line.split('#', 1)[0].count('=') > 1]
    if obscure or long_lines or cramped:
        issues = []
        if obscure:
            issues.append('Kies duidelijkere namen voor ' + ', '.join(obscure[:5]) + '.')
        if long_lines:
            issues.append('Splits de lange instructies op regels ' + ', '.join(map(str, long_lines[:5])) + '.')
        if cramped:
            issues.append('Zet de toewijzingen op regels ' + ', '.join(map(str, cramped[:5])) + ' elk op een eigen regel.')
        mark('leesbaarheid', maxima[1] / 2, ' '.join(issues))
    else:
        mark('leesbaarheid', maxima[1], 'De gebruikte namen zijn passend en duidelijk.')

    inputs = _calls(tree, 'input')
    required_inputs = 3 if title in ('Driehoeksongelijkheid', 'Taille-heup verhouding') else 1
    casts = _calls(tree, 'int') + _calls(tree, 'float')
    converted = sum(bool(_calls(n, 'input')) for n in casts)
    input_anchor = len(inputs) == required_inputs and converted >= (2 if title == 'Taille-heup verhouding' else required_inputs)
    selections = [n for n in nodes if isinstance(n, ast.If)]
    comparisons = [n for n in nodes if isinstance(n, ast.Compare)]
    bare_conditions = [n for n in selections if not any(isinstance(x, ast.Compare) for x in ast.walk(n.test))]
    truthy_or = [n for n in nodes if isinstance(n, ast.BoolOp) and isinstance(n.op, ast.Or)
                 and any(isinstance(x, ast.Constant) and bool(x.value) for x in n.values)]
    triangle_chain = title == 'Driehoeksongelijkheid' and any(
        isinstance(n, ast.If) and n.orelse and isinstance(n.orelse[0], ast.If)
        and isinstance(n.test, ast.Compare)
        and any(isinstance(x, ast.BinOp) and isinstance(x.op, ast.Add) for x in ast.walk(n.test))
        for n in selections)
    selection_anchor = bool(selections and comparisons and _calls(tree, 'print')) and not (bare_conditions or truthy_or or triangle_chain)
    anchors = int(input_anchor) + int(selection_anchor)
    mark('programmeerconcepten', maxima[2] * anchors / 2,
         ('Je gebruikt een correct datatype voor je invoer. ' if input_anchor else 'Controleer de volgorde en het datatype van je invoer. ')
         + ('Je gebruikt vergelijkingen om keuzes te maken en resultaten te tonen.' if selection_anchor else 'Werk de selectie uit met volledige, passende voorwaarden.'))

    side_sums={(n.lineno,n.col_offset) for cmp in comparisons for n in ast.walk(cmp)
               if isinstance(n,ast.BinOp) and isinstance(n.op,ast.Add)
               and sum(isinstance(x,ast.Name) for x in ast.walk(n))>=2}

    evidence = []
    math_ok = 0
    math_tested = 0
    unknown = 0
    errors = 0
    first_failure = None
    for stdin, expected in tests:
        result = run(code, stdin)
        if result['state'] == 'unsupported':
            unknown += 1
            continue
        errors += result['state']=='error'
        expected_numbers = _numbers(expected)
        expected_category = _category(expected)
        actual_category = _category(result.get('output', ''))
        values = _numbers(result.get('output', ''))
        calculated_values=[v for event in result.get('prints',[]) for arg in event['arguments'] if arg['calculated'] for v in _numbers(str(arg['value']))]
        tolerance = .051 if title == 'Ideale lichaamsmassa' else .0051
        numeric_match = result['state']=='ok' and len(values)==len(expected_numbers)>0 and all(math.isclose(x,y,rel_tol=1e-8,abs_tol=tolerance) for x,y in zip(expected_numbers,values))
        printed_calculation=bool(expected_numbers) and all(any(math.isclose(x,y,rel_tol=1e-8,abs_tol=tolerance) for y in calculated_values) for x in expected_numbers)
        if title == 'Driehoeksongelijkheid':
            used_sums=any((n['line'],n['column']) in side_sums for n in result.get('calculations',[]))
            passed = result['state'] == 'ok' and actual_category == expected_category and used_sums
        elif expected_category == 'te oud':
            passed = result['state']=='ok' and actual_category == 'te oud'
        elif title == 'Taille-heup verhouding':
            passed = numeric_match and printed_calculation and actual_category == expected_category
        else:
            passed = numeric_match and printed_calculation
        math_tested += 1
        math_ok += passed
        if not passed and first_failure is None:
            first_failure = {'input': stdin, 'expected': expected.strip(),
                             'actual': result.get('output', '').strip(), 'state': result['state']}
        if len(evidence) < 5:
            evidence.append({'input': stdin, 'expected': expected.strip(), 'actual': result.get('output', '').strip(),
                             'state': result['state'], 'mathematical_probe_passed': passed})

    if unknown or not math_tested or (errors==math_tested and not math_ok):
        mark('wiskundeconcepten', None, 'De berekeningen moeten nog worden nagekeken.')
    else:
        fraction = 1 if math_ok == math_tested else .5 if math_ok else 0
        mark('wiskundeconcepten', maxima[3] * fraction,
             ('Je berekeningen en voorwaarden kloppen.' if fraction==1 else
              'Een deel van je berekeningen of voorwaarden klopt.' if fraction==.5 else
              'Je berekeningen of voorwaarden kloppen nog niet.'))

    if criteria['functioneel']['points'] == maxima[0]:
        strength = 'Je programma geeft de juiste uitvoer.'
    elif math_tested and math_ok == math_tested and not unknown:
        strength = 'Je berekeningen kloppen.'
    elif input_anchor:
        strength = 'Je leest de gevraagde gegevens in met een correct datatype.'
    else:
        strength = 'Je hebt een eerste versie van je oplossing ingediend.'
    issues = []
    if truthy_or:
        issues.append('Na or moet opnieuw een volledige voorwaarde staan.')
    if triangle_chain:
        issues.append('Controleer de drie driehoeksongelijkheden samen met and.')
    if bare_conditions:
        issues.append('Gebruik een vergelijking als voorwaarde, bijvoorbeeld leeftijd < 12.')
    if not input_anchor:
        issues.append('Lees de gevraagde gegevens in de juiste volgorde en kies een correct datatype.')
    if first_failure:
        issues.append(PRACTICE[title])
    if not issues and criteria['functioneel']['points'] == 0:
        issues.append('Controleer je uitvoer, afronding en grensgevallen.')
    if not issues and not selection_anchor:
        issues.append('Gebruik voorwaarden om de juiste uitvoer te kiezen.')
    if not issues and (obscure or long_lines or cramped):
        issues.append(criteria['leesbaarheid']['rationale'])
    feedback.update(strength=strength, improve=' '.join(issues[:2]) or 'Je oplossing is correct. Test je code ook met andere invoer.')
    return {'proposal_version': VERSION, 'review_required': True,
            'math_probes': {'tested': math_tested, 'passed': math_ok, 'unsupported': unknown,
                            'method': 'rekenresultaten en relevante categorie; uitvoertekst apart bij werking',
                            'examples': evidence, 'first_failure': first_failure},
            'structural_review': {'input_anchor': input_anchor, 'selection_anchor': selection_anchor,
                                  'warning_lines': sorted({x.lineno for x in truthy_or + bare_conditions})}}
