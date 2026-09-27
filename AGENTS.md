# AGENTS.md --- instrukcje dla agentów projektu LEGAL-CODE

> Ten plik jest instrukcją operacyjną dla agentów AI pracujących w
> repozytorium LEGAL-CODE.
>
> Dokument nadrzędny opisujący koncepcję projektu znajduje się w
> `PROJECT_CONCEPT.md`.

------------------------------------------------------------------------

# 1. Misja agenta

Twoim zadaniem jest pomagać w tworzeniu **audytowalnego formalnego
modelu prawa**, a nie generować „odpowiedzi prawnicze" na podstawie
intuicji.

Projekt bada, jak dużą część prawa można reprezentować jako:

-   encje,
-   relacje,
-   stany,
-   zdarzenia,
-   normy,
-   warunki,
-   obowiązki,
-   zakazy,
-   uprawnienia,
-   kompetencje,
-   procedury,
-   terminy,
-   wyjątki,
-   zależności między normami.

Najważniejsza zasada:

``` text
SOURCE > MODEL
MODEL > GUESS
```

Jeżeli czegoś nie da się ustalić na podstawie źródła lub jawnie
oznaczonej interpretacji, **nie zgaduj**.

------------------------------------------------------------------------

# 2. Dokumenty, które agent musi znać

Przed rozpoczęciem większej pracy przeczytaj:

``` text
PROJECT_CONCEPT.md
AGENTS.md
README.md
ROADMAP.md
```

Jeżeli zadanie dotyczy konkretnej domeny, przeczytaj również odpowiednie
dokumenty w:

``` text
docs/
law/
model/
tests/
```

Nie zakładaj, że wcześniejsza rozmowa z innym agentem była poprawna.

Repozytorium jest źródłem prawdy dla stanu projektu.

------------------------------------------------------------------------

# 3. Hierarchia źródeł prawdy

W przypadku konfliktu informacji stosuj następującą hierarchię:

``` text
1. Aktualne źródło prawa
2. Historyczne źródło prawa właściwe dla daty
3. Jawnie zatwierdzona formalizacja
4. Testy projektu
5. Dokumentacja projektu
6. Wcześniejsze propozycje agentów
7. Domysł agenta
```

Pozycja 7 nie jest źródłem prawdy.

------------------------------------------------------------------------

# 4. Podstawowa zasada provenance

Każda formalna reguła musi mieć możliwość wskazania:

``` text
RULE
  ↓
SOURCE
  ↓
ACT
  ↓
ARTICLE
  ↓
PARAGRAPH / POINT
  ↓
SOURCE TEXT
```

Minimalny przykład:

``` yaml
id: R-PS-0001

source:
  act: "Prawo spółdzielcze"
  article: "1"
  paragraph: "1"

source_text: "..."

formalization_status: DIRECT
```

Jeżeli nie da się wskazać źródła:

``` text
NIE TWÓRZ REGUŁY PRAWA.
```

Możesz natomiast utworzyć:

``` text
HYPOTHESIS
```

lub:

``` text
DESIGN_PROPOSAL
```

jeżeli jest to potrzebne do rozwoju architektury.

------------------------------------------------------------------------

# 5. Rozdzielenie prawa od modelu

Agent musi stale rozróżniać:

``` text
SOURCE LAW
FORMAL MODEL
INTERPRETATION
IMPLEMENTATION
ASSUMPTION
```

Przykład:

``` text
SOURCE:
    Ustawa mówi X.

FORMALIZATION:
    X reprezentujemy jako Rule R-123.

INTERPRETATION:
    Przyjmujemy, że pojęcie Y oznacza Z.

IMPLEMENTATION:
    W kodzie sprawdzamy Y == Z.

ASSUMPTION:
    Na potrzeby testu przyjmujemy, że dokument jest skuteczny.
```

Nigdy nie należy zlewać tych warstw.

------------------------------------------------------------------------

# 6. Klasyfikacja każdego wyniku

Każda istotna informacja powinna być możliwa do zaklasyfikowania jako:

``` text
FACT
INFERENCE
INTERPRETATION
ASSUMPTION
UNKNOWN
```

## FACT

Bezpośrednio wynika ze źródła.

``` text
FACT:
    Art. X stanowi Y.
```

## INFERENCE

Logicznie wynika z kilku faktów.

``` text
INFERENCE:
    Skoro A i B, to w modelu zachodzi C.
```

## INTERPRETATION

Wymaga wyboru znaczenia.

``` text
INTERPRETATION:
    Termin X interpretujemy jako Y.
```

## ASSUMPTION

Założenie techniczne lub testowe.

``` text
ASSUMPTION:
    Dla testu przyjmujemy datę D.
```

## UNKNOWN

Brakuje informacji.

``` text
UNKNOWN:
    Źródła nie pozwalają ustalić X.
```

------------------------------------------------------------------------

# 7. Status formalizacji

Każdy element formalizacji powinien mieć jeden z poziomów:

``` text
DIRECT
STRUCTURAL
INFERRED
INTERPRETATIVE
UNCERTAIN
CONTESTED
```

## DIRECT

Prawie bezpośrednie odwzorowanie tekstu.

## STRUCTURAL

Techniczna reprezentacja konstrukcji prawnej.

## INFERRED

Wniosek z kilku przepisów.

## INTERPRETATIVE

Wymaga interpretacji.

## UNCERTAIN

Nie wiadomo, czy formalizacja jest poprawna.

## CONTESTED

Istnieją konkurencyjne interpretacje.

------------------------------------------------------------------------

# 8. Nigdy nie ukrywaj niepewności

Nie zamieniaj:

``` text
nie wiadomo
```

na:

``` text
false
```

ani:

``` text
prawdopodobnie
```

na:

``` text
true
```

Jeżeli system nie może ustalić wyniku:

``` text
UNKNOWN
```

lub:

``` text
UNRESOLVED
```

jest prawidłowym wynikiem.

------------------------------------------------------------------------

# 9. Pojęcia nieostre

Szczególną ostrożność zachowuj dla pojęć takich jak:

``` text
niezwłocznie
ważny interes
szczególnie uzasadniony przypadek
rażące naruszenie
istotne naruszenie
należyta staranność
odpowiedni termin
```

Nie twórz arbitralnych funkcji:

``` python
is_serious_violation(x) == True
```

jeżeli prawo nie dostarcza takiego kryterium.

Zamiast tego:

``` text
CONCEPT "rażące naruszenie"

TYPE:
    OPEN_TEXTURED

REQUIRES:
    INTERPRETATION
```

------------------------------------------------------------------------

# 10. Praca z tekstem ustawy

Podczas formalizacji przepisu wykonaj kolejno:

``` text
1. Zidentyfikuj tekst źródłowy.
2. Ustal wersję czasową.
3. Ustal strukturę artykułu.
4. Znajdź odesłania do innych przepisów.
5. Zidentyfikuj podmioty.
6. Zidentyfikuj przedmioty.
7. Zidentyfikuj czynności.
8. Zidentyfikuj warunki.
9. Zidentyfikuj skutki.
10. Zidentyfikuj wyjątki.
11. Zidentyfikuj terminy.
12. Zidentyfikuj kompetencje.
13. Zidentyfikuj relacje z innymi normami.
14. Dopiero wtedy zaproponuj formalizację.
```

Nie zaczynaj od kodu.

------------------------------------------------------------------------

# 11. Jednostka pracy: legal unit

Podstawową jednostką pracy powinien być jeden:

``` text
artykuł
paragraf
punkt
ustęp
```

lub inna wyraźna jednostka normatywna.

Dla każdego legal unit powinien istnieć:

``` text
source
analysis
formalization
tests
provenance
```

------------------------------------------------------------------------

# 12. Nie zakładaj, że jeden artykuł = jedna reguła

Jeden przepis może zawierać:

``` text
definition
+
permission
+
obligation
+
exception
+
condition
```

Przykład:

``` text
Art. X
    ├── Definition R-001
    ├── Obligation R-002
    ├── Exception R-003
    └── Deadline R-004
```

Rozbijaj przepis semantycznie.

------------------------------------------------------------------------

# 13. Nie zakładaj, że jedna reguła = jeden artykuł

Jedna norma może być zbudowana z:

``` text
Art. 10
+
Art. 20
+
Art. 35
```

Jeżeli reguła wymaga kilku przepisów, provenance powinien zawierać
wszystkie:

``` yaml
sources:
  - article: 10
  - article: 20
  - article: 35
```

------------------------------------------------------------------------

# 14. Odesłania między przepisami

Każde odesłanie powinno być jawnie zapisane.

Przykład:

``` text
Art. 20
    references Art. 35
```

Model:

``` yaml
references:
  - target: R-PS-0035
    type: LEGAL_REFERENCE
```

Nie kopiuj automatycznie treści przepisu, jeżeli można zachować relację.

------------------------------------------------------------------------

# 15. Entity

Encje reprezentują obiekty domeny prawnej.

Przykłady:

``` text
Osoba
Spółdzielnia
Członek
Zarząd
RadaNadzorcza
WalneZgromadzenie
Uchwała
Statut
Nieruchomość
Dokument
```

Encja powinna zawierać tylko właściwości potrzebne do reprezentacji
prawa.

Nie twórz modelu biznesowego ponad zakres projektu bez powodu.

------------------------------------------------------------------------

# 16. Relation

Relacje są równie ważne jak encje.

Przykłady:

``` text
MEMBER_OF
ORGAN_OF
SUPERVISES
REPRESENTS
OWNS
ADOPTED_BY
APPOINTED_BY
SUBJECT_TO
```

Relacja powinna być jawna.

Nie ukrywaj ważnej relacji w arbitralnym polu tekstowym.

------------------------------------------------------------------------

# 17. State

Stan reprezentuje właściwości świata w określonym momencie.

Przykłady:

``` text
Membership:
    PENDING
    ACTIVE
    TERMINATED

Resolution:
    PROPOSED
    ADOPTED
    REJECTED
    EFFECTIVE
```

Jeżeli przepis opisuje zmianę, rozważ model:

``` text
BEFORE
    ↓
EVENT
    ↓
AFTER
```

------------------------------------------------------------------------

# 18. Event

Event opisuje fakt, który wydarzył się w świecie.

Przykłady:

``` text
MemberJoined
MemberResigned
ResolutionAdopted
BoardMemberElected
MeetingConcluded
DeadlineExpired
```

Event nie jest tym samym co norma.

``` text
EVENT:
    coś się wydarzyło

RULE:
    prawo określa, co z tego wynika
```

------------------------------------------------------------------------

# 19. Rule

Reguła powinna być reprezentowana jako jawna struktura:

``` text
RULE
    SOURCE
    SUBJECT
    ACTION
    CONDITIONS
    EXCEPTIONS
    EFFECT
    TEMPORAL_SCOPE
    FORMALIZATION_STATUS
```

Nie twórz „magicznych" funkcji, których znaczenie istnieje wyłącznie w
kodzie.

------------------------------------------------------------------------

# 20. Normative types

Rozróżniaj:

``` text
OBLIGATION
PROHIBITION
PERMISSION
RIGHT
POWER
COMPETENCE
```

Nie traktuj ich jako synonimów.

Przykładowo:

``` text
PERMISSION != RIGHT
RIGHT != POWER
OBLIGATION != PROCEDURE
```

Jeżeli semantyczna różnica jest niejasna, zaznacz ją w dokumentacji
zamiast arbitralnie ją rozstrzygać.

------------------------------------------------------------------------

# 21. Procedures

Procedury powinny być reprezentowane jako sekwencje lub grafy kroków.

Przykład:

``` text
PROCEDURE AdoptResolution

1. Convene
2. Verify quorum
3. Present proposal
4. Vote
5. Determine result
6. Record resolution
```

Każdy krok może mieć:

``` text
PRECONDITION
ACTION
POSTCONDITION
DEADLINE
EXCEPTION
```

------------------------------------------------------------------------

# 22. Deadlines

Nie zapisuj terminów wyłącznie jako:

``` text
14
```

Potrzebne są co najmniej:

``` text
START_EVENT
DURATION
UNIT
TYPE
EXPIRATION_RULE
```

Przykład:

``` yaml
deadline:
  start: ResolutionAdopted
  duration: 14
  unit: DAYS
  type: STATUTORY
```

------------------------------------------------------------------------

# 23. Wersjonowanie

Prawo jest czasowe.

Nigdy nie zakładaj:

``` text
current law == law applicable to historical event
```

Każdy model prawa powinien mieć wersję.

Przykład:

``` yaml
validity:
  from: 2026-03-23
  to: null
```

Zapytania powinny docelowo obsługiwać:

``` text
AS_OF 2025-01-01
```

------------------------------------------------------------------------

# 24. Historyczne stany

Jeżeli pytanie dotyczy przeszłości:

``` text
WHAT WAS THE STATE ON DATE D?
```

należy używać:

``` text
event history
+
law version applicable at D
```

Nie wystarczy aktualny model.

------------------------------------------------------------------------

# 25. Event sourcing

Preferowany sposób modelowania zmian:

``` text
EVENT LOG
    ↓
STATE RECONSTRUCTION
```

Przykład:

``` text
2026-01-01 MemberJoined
2026-02-01 BoardMemberElected
2026-04-01 MemberResigned
```

Stan na:

``` text
2026-03-01
```

powinien wynikać z pierwszych dwóch zdarzeń.

------------------------------------------------------------------------

# 26. Testowanie

Każda istotna reguła musi mieć test.

Minimalny test:

``` text
GIVEN
WHEN
THEN
```

Przykład:

``` text
GIVEN:
    member.status = ACTIVE

WHEN:
    query member rights

THEN:
    right X is present
```

------------------------------------------------------------------------

# 27. Testy negatywne

Nie wystarczą testy pozytywne.

Dodawaj:

``` text
invalid state
missing condition
missing permission
expired deadline
wrong actor
wrong organ
exception active
```

Przykład:

``` text
GIVEN:
    member.status = TERMINATED

WHEN:
    query active membership rights

THEN:
    right X is NOT available
```

------------------------------------------------------------------------

# 28. Testy graniczne

Dla liczb:

``` text
n = minimum - 1
n = minimum
n = minimum + 1
```

Dla terminów:

``` text
before deadline
at deadline
after deadline
```

Dla stanów:

``` text
before event
during transition
after event
```

------------------------------------------------------------------------

# 29. Testy regresyjne

Zmiana formalizacji jednego przepisu nie może niezauważenie zmienić
wyników innych.

Przed commitem uruchom dostępne testy.

Jeżeli testy nie istnieją, utwórz je dla nowej funkcjonalności.

------------------------------------------------------------------------

# 30. Agent nie może „naprawiać" prawa

Jeżeli tekst źródłowy wydaje się:

-   niespójny,
-   dziwny,
-   redundantny,
-   niepraktyczny,
-   archaiczny,

nie zmieniaj go.

Modeluj rzeczywisty tekst.

Możesz zgłosić:

``` text
OBSERVATION
```

ale nie zmieniaj normy.

------------------------------------------------------------------------

# 31. Konflikty

Jeżeli dwie reguły wydają się sprzeczne:

``` text
NIE WYBIERAJ AUTOMATYCZNIE ZWYCIĘZCY.
```

Zapisz:

``` text
CONFLICT
    Rule A
    Rule B
```

Następnie wskaż potencjalne mechanizmy:

``` text
hierarchy
lex specialis
lex posterior
scope
temporal validity
```

Jeżeli nie można rozstrzygnąć konfliktu mechanicznie:

``` text
UNRESOLVED
```

------------------------------------------------------------------------

# 32. Interpretacje

Jeżeli agent musi dokonać interpretacji:

``` text
NIE UKRYWAJ JEJ W KODZIE.
```

Utwórz jawny element:

``` yaml
interpretation:
  id: I-001
  source_rules:
    - R-001
  statement: "..."
  rationale: "..."
  status: PROPOSED
```

------------------------------------------------------------------------

# 33. Konkurencyjne interpretacje

Jeżeli istnieją dwie sensowne interpretacje:

``` text
INTERPRETATION I-001
INTERPRETATION I-002
```

Nie redukuj ich do:

``` text
TRUE
FALSE
```

Możliwe:

``` text
CONTESTED
```

------------------------------------------------------------------------

# 34. Orzecznictwo i doktryna

Nie traktuj:

``` text
statute
case_law
doctrine
commentary
```

jako jednego typu źródła.

Model powinien je rozróżniać.

Przykład:

``` yaml
source:
  type: CASE_LAW
```

lub:

``` yaml
source:
  type: DOCTRINE
```

Tekst ustawy powinien pozostać odrębnym źródłem.

------------------------------------------------------------------------

# 35. AI jako narzędzie, nie źródło prawa

LLM może:

``` text
propose
summarize
extract
classify
generate tests
find candidate relations
```

LLM nie jest źródłem normy.

Nie zapisuj:

``` text
SOURCE:
    ChatGPT
```

Jeżeli agent coś proponuje, jest to:

``` text
PROPOSAL
```

dopóki nie zostanie zweryfikowane.

------------------------------------------------------------------------

# 36. Zasada minimalnej zmiany

Pracując nad istniejącym repozytorium:

``` text
DO NOT REWRITE UNRELATED FILES.
```

Preferuj małe, logiczne zmiany.

Jeżeli zadanie dotyczy:

``` text
R-001
```

nie zmieniaj bez powodu:

``` text
R-100
R-101
engine/query.py
README
```

------------------------------------------------------------------------

# 37. Zasada małych commitów

Preferowany styl:

``` text
commit 1:
    add source article

commit 2:
    add ontology

commit 3:
    add rule

commit 4:
    add tests
```

zamiast:

``` text
implement everything
```

Małe commity ułatwiają audyt formalizacji.

------------------------------------------------------------------------

# 38. Naming

Preferowane stabilne ID:

``` text
R-PS-0001
E-PS-0001
C-PS-0001
I-PS-0001
T-PS-0001
```

gdzie:

``` text
R = Rule
E = Event
C = Concept
I = Interpretation
T = Test
PS = Prawo Spółdzielcze
```

ID nie powinno zmieniać się tylko dlatego, że zmieniła się nazwa pliku.

------------------------------------------------------------------------

# 39. Dokumentowanie decyzji

Jeżeli agent podejmuje ważną decyzję architektoniczną, zapisz ją w:

``` text
docs/decisions/
```

Preferowany format:

``` text
ADR-0001-title.md
```

Struktura:

``` text
# Context

# Decision

# Alternatives

# Consequences

# Status
```

------------------------------------------------------------------------

# 40. Praca nad DSL

Jeżeli zmieniasz DSL:

1.  Zaktualizuj specyfikację.
2.  Zaktualizuj parser.
3.  Dodaj test parsera.
4.  Dodaj przykład.
5.  Zaktualizuj dokumentację.
6.  Sprawdź istniejące reguły.
7.  Uruchom testy regresyjne.

Nie zmieniaj składni bez aktualizacji dokumentacji.

------------------------------------------------------------------------

# 41. Parser ≠ interpreter

Rozróżniaj:

``` text
PARSER
```

od:

``` text
RULE ENGINE
```

Parser odpowiada:

``` text
"Co oznacza struktura pliku DSL?"
```

Engine odpowiada:

``` text
"Co dzieje się po zastosowaniu tej reguły do stanu?"
```

------------------------------------------------------------------------

# 42. Legal IR

Docelowo warto mieć pośrednią reprezentację:

``` text
SOURCE
   ↓
NORMALIZED LEGAL TEXT
   ↓
LEGAL IR
   ↓
DSL / ENGINE
```

Legal IR powinien być niezależny od konkretnej składni DSL.

------------------------------------------------------------------------

# 43. Walidacja modelu

Model powinien być walidowany pod kątem:

``` text
missing source
duplicate IDs
broken references
invalid entity references
circular dependencies
invalid state transitions
unresolved required fields
conflicting rules
```

------------------------------------------------------------------------

# 44. Explainability jako wymaganie techniczne

Każdy wynik silnika powinien mieć możliwość odpowiedzi:

``` text
WHY?
```

Przykład:

``` text
RESULT:
    ACTION NOT PERMITTED

WHY:
    R-PS-0012

BECAUSE:
    condition C-004 = TRUE

SOURCE:
    Art. X §Y

INTERPRETATION:
    none
```

------------------------------------------------------------------------

# 45. Zakaz „magii"

Unikaj kodu:

``` python
if special_case:
    ...
```

jeżeli `special_case` nie ma formalnej definicji.

Preferuj:

``` python
if evaluate("C-PS-0042", state):
    ...
```

gdzie:

``` text
C-PS-0042
```

ma provenance.

------------------------------------------------------------------------

# 46. Minimalny workflow pojedynczego przepisu

Agent powinien wykonać:

``` text
READ
 ↓
PARSE
 ↓
IDENTIFY
 ↓
MODEL
 ↓
LINK
 ↓
TEST
 ↓
REVIEW
```

Praktycznie:

``` text
1. Pobierz tekst.
2. Zapisz źródło.
3. Nadaj source ID.
4. Zidentyfikuj encje.
5. Zidentyfikuj normy.
6. Zidentyfikuj warunki.
7. Zidentyfikuj skutki.
8. Zidentyfikuj odesłania.
9. Utwórz formalizację.
10. Oznacz poziom pewności.
11. Utwórz test.
12. Zweryfikuj provenance.
13. Uruchom testy.
```

------------------------------------------------------------------------

# 47. Definition of Done --- przepis

Przepis jest gotowy dopiero wtedy, gdy:

``` text
[ ] source identified
[ ] source version identified
[ ] source text preserved
[ ] article structure preserved
[ ] references identified
[ ] entities identified
[ ] relations identified
[ ] normative statements identified
[ ] conditions identified
[ ] effects identified
[ ] exceptions identified
[ ] temporal rules identified
[ ] formalization written
[ ] formalization status assigned
[ ] provenance complete
[ ] tests written
[ ] tests passing
[ ] ambiguities documented
[ ] unresolved issues documented
```

------------------------------------------------------------------------

# 48. Definition of Done --- reguła

Reguła jest gotowa, jeżeli:

``` text
[ ] ma stabilne ID
[ ] ma source
[ ] ma subject
[ ] ma norm type
[ ] ma warunki
[ ] ma effect
[ ] ma status formalizacji
[ ] ma test
[ ] test przechodzi
[ ] nie zawiera ukrytej interpretacji
[ ] wszystkie referencje są poprawne
```

------------------------------------------------------------------------

# 49. Definition of Done --- agent task

Zadanie agenta jest gotowe, jeżeli:

``` text
[ ] zmiana jest ograniczona do zakresu zadania
[ ] dokumentacja jest aktualna
[ ] testy przechodzą
[ ] nowe reguły mają provenance
[ ] interpretacje są oznaczone
[ ] niepewności są jawne
[ ] brak nieudokumentowanych założeń
[ ] wynik można odtworzyć
```

------------------------------------------------------------------------

# 50. Gdy brakuje danych

Nie zgaduj.

Zamiast:

``` text
Probably article 20.
```

napisz:

``` text
UNKNOWN:
    source article not verified.
```

Jeżeli można kontynuować bez tej informacji, kontynuuj z oznaczeniem.

Jeżeli informacja jest konieczna, zatrzymaj dany fragment pracy.

------------------------------------------------------------------------

# 51. Gdy narzędzie nie działa

Nie udawaj, że źródło zostało sprawdzone.

Zamiast:

``` text
Source verified.
```

gdy nie zostało zweryfikowane:

``` text
SOURCE_VERIFICATION_PENDING
```

------------------------------------------------------------------------

# 52. Gdy istnieje konflikt dokumentów

Jeżeli:

``` text
PROJECT_CONCEPT.md
```

mówi jedno, a:

``` text
AGENTS.md
```

drugie, należy:

1.  zgłosić konflikt,
2.  nie ukrywać go,
3.  ustalić właściwą decyzję,
4.  zaktualizować dokumenty.

------------------------------------------------------------------------

# 53. Gdy zmienia się prawo

Nie modyfikuj historycznej wersji w miejscu.

Preferuj:

``` text
law/
    prawo-spoldzielcze/
        versions/
            2026-03-23/
            2026-...
```

Nowelizacja powinna być reprezentowana jako zmiana modelu.

------------------------------------------------------------------------

# 54. Semantic diff

W przyszłości agent powinien pomagać wykrywać:

``` text
TEXT DIFF
```

oraz:

``` text
SEMANTIC DIFF
```

Przykład:

``` text
TEXT:
    "może" → "musi"

SEMANTIC:
    PERMISSION → OBLIGATION
```

To jest dużo ważniejsze niż zwykły diff tekstu.

------------------------------------------------------------------------

# 55. Zmiana jednego słowa może być zmianą semantyczną

Agent musi zwracać szczególną uwagę na:

``` text
może
musi
nie może
jest obowiązany
uprawniony
w szczególności
wyłącznie
co najmniej
nie później niż
z wyjątkiem
jeżeli
chyba że
```

Nie traktuj takich słów jako stylistycznych.

------------------------------------------------------------------------

# 56. Reguły nie mogą być nadmiernie upraszczane

Nie przekształcaj automatycznie:

``` text
"może, jeżeli A, chyba że B"
```

w:

``` text
if A:
    allow
```

Prawidłowa struktura może być:

``` text
PERMISSION
    IF A
    EXCEPT IF B
```

------------------------------------------------------------------------

# 57. Agent ma ujawniać decyzje projektowe

Jeżeli wybierasz:

``` text
"prawo podmiotu" = RIGHT
```

a nie:

``` text
PERMISSION
```

zapisz uzasadnienie.

Decyzje modelujące są częścią projektu badawczego.

------------------------------------------------------------------------

# 58. Priorytet jakości

Kolejność priorytetów:

``` text
1. Correct source mapping
2. Semantic correctness
3. Explicit uncertainty
4. Reproducibility
5. Testability
6. Simplicity
7. Performance
```

Nie optymalizuj wydajności kosztem audytowalności na wczesnym etapie.

------------------------------------------------------------------------

# 59. Priorytet dla pierwszej wersji

W MVP preferuj:

``` text
prosty parser
+
jawny model
+
prosty evaluator
+
dużo testów
```

nad:

``` text
skomplikowany compiler
+
LLM orchestration
+
distributed architecture
```

------------------------------------------------------------------------

# 60. Co agent powinien robić proaktywnie

Jeżeli zauważysz:

``` text
brak provenance
brak testu
broken reference
sprzeczność
nieoznaczoną interpretację
nieznaną wersję prawa
```

zgłoś to nawet wtedy, gdy nie było głównym tematem zadania.

Nie rozszerzaj jednak bez potrzeby zakresu zmian.

------------------------------------------------------------------------

# 61. Co agent powinien proponować

Jeżeli istnieje lepsza struktura:

``` text
PROPOSAL
```

Jeżeli istnieje potencjalny problem:

``` text
WARNING
```

Jeżeli istnieje pewny błąd:

``` text
ERROR
```

Przykład:

``` text
WARNING:
    Rule R-004 uses an open-textured concept.

PROPOSAL:
    create Concept C-004.

ERROR:
    Rule R-004 references missing Entity E-099.
```

------------------------------------------------------------------------

# 62. Styl komentarzy w kodzie

Komentarze powinny wyjaśniać:

``` text
WHY
```

a nie tylko:

``` text
WHAT
```

Źle:

``` python
# check quorum
```

Lepiej:

``` python
# Quorum is evaluated separately because the legal rule
# distinguishes procedural validity from the substantive effect.
```

Jeżeli komentarz opisuje prawo, dodaj provenance.

------------------------------------------------------------------------

# 63. Styl dokumentacji

Dokumentacja powinna być:

-   konkretna,
-   techniczna,
-   audytowalna,
-   wolna od marketingowego języka,
-   jasna co do niepewności.

Nie pisz:

``` text
System doskonale rozumie prawo.
```

Pisz:

``` text
System formalizuje reguły R-001–R-042.
12 reguł jest deterministycznych.
4 wymagają interpretacji.
2 pozostają nierozstrzygnięte.
```

------------------------------------------------------------------------

# 64. Ostateczna zasada agenta

Jeżeli masz do wyboru:

``` text
ładna odpowiedź
```

oraz:

``` text
uczciwa odpowiedź z UNKNOWN
```

wybierz:

``` text
UNKNOWN
```

Jeżeli masz do wyboru:

``` text
prosty model
```

oraz:

``` text
model pozornie dokładny, ale oparty na założeniach
```

wybierz:

``` text
prosty model + jawne ograniczenie
```

Jeżeli masz do wyboru:

``` text
automatyczna interpretacja
```

oraz:

``` text
jawne przedstawienie konkurencyjnych interpretacji
```

wybierz:

``` text
jawne przedstawienie interpretacji
```

------------------------------------------------------------------------

# 65. Mentalny model projektu

Pracując nad repozytorium, myśl o nim jak o kompilatorze:

``` text
             SOURCE LAW
                  │
                  ▼
               PARSER
                  │
                  ▼
             LEGAL IR
                  │
                  ▼
        ┌──────────────────┐
        │ FORMAL MODEL     │
        │ entities/rules   │
        │ events/states    │
        └────────┬─────────┘
                 │
                 ▼
             VALIDATOR
                 │
                 ▼
            RULE ENGINE
                 │
                 ▼
              QUERY
                 │
                 ▼
        EXPLAINABLE RESULT
```

Ale pamiętaj:

``` text
LAW ≠ PROGRAM
```

To jest eksperyment formalizacyjny, nie założenie, że prawo jest
dosłownie programem.

------------------------------------------------------------------------

# 66. Pierwsze zadanie przyszłego agenta

Po rozpoczęciu pracy nad repozytorium pierwszym krokiem powinno być:

``` text
READ:
    PROJECT_CONCEPT.md
    AGENTS.md
    README.md

THEN:
    inspect repository structure

THEN:
    report:
        current project state
        completed components
        missing components
        inconsistencies
        recommended next task
```

Agent nie powinien od razu tworzyć dużej ilości kodu.

Najpierw musi zrozumieć stan repozytorium.

------------------------------------------------------------------------

# 67. Najważniejszy test dojrzałości projektu

Pewnego dnia powinno być możliwe zadanie:

``` text
"Dlaczego system twierdzi, że działanie X
jest niedozwolone?"
```

i uzyskanie:

``` text
RULE R-0012
    ↓
CONDITION C-004
    ↓
STATE S-012
    ↓
SOURCE:
    Prawo spółdzielcze
    Art. X §Y

FORMALIZATION:
    ...

INTERPRETATION:
    ...

CONFIDENCE:
    ...
```

Jeżeli nie można przejść tej ścieżki, model nie jest jeszcze
wystarczająco audytowalny.

------------------------------------------------------------------------

# 68. Zakończenie

Ten projekt ma badać granicę pomiędzy:

``` text
tekst prawa
```

a:

``` text
formalny system reguł
```

Agent nie ma tej granicy zacierać.

Ma ją **mapować, dokumentować i testować**.

Najważniejsza zasada:

> **Nie chodzi o to, aby agent zawsze potrafił odpowiedzieć. Chodzi o
> to, aby zawsze było wiadomo, dlaczego odpowiedział, na jakiej
> podstawie i gdzie kończy się wiedza modelu.**
