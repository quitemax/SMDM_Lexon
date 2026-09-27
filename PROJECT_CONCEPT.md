# LEGAL-CODE --- formalizacja prawa jako wykonywalnego modelu reguł

> **Status dokumentu:** koncepcja / blueprint projektu\
> **Przeznaczenie:** dokument nadrzędny dla ludzi i przyszłych agentów
> AI pracujących nad repozytorium\
> **Język projektu:** polski\
> **Pierwszy domenowy eksperyment:** polskie Prawo spółdzielcze\
> **Cel:** stworzenie formalnego, audytowalnego modelu przepisów prawa,
> który pozwala reprezentować podmioty, stany, zdarzenia, uprawnienia,
> obowiązki, zakazy, kompetencje, terminy i zależności między normami.

------------------------------------------------------------------------

## 1. Idea projektu

Projekt bada możliwość przekształcenia tekstu prawnego w formalny model
przypominający połączenie:

-   modelu domenowego,
-   ontologii,
-   języka DSL,
-   systemu reguł,
-   maszyny stanów,
-   event sourcing,
-   grafu zależności,
-   oraz częściowo interpretera / „silnika wykonawczego" prawa.

Punktem wyjścia jest intuicja:

> **Ustawę można traktować częściowo jak specyfikację systemu: definiuje
> obiekty, ich właściwości, dozwolone działania, obowiązki, zakazy,
> procedury, warunki, wyjątki, terminy i skutki zdarzeń.**

Nie należy jednak utożsamiać formalizacji z prawem.

Formalny model jest **reprezentacją prawa**, a nie samym prawem. Każda
transformacja tekstu ustawy do modelu może zawierać interpretację i musi
być możliwa do prześledzenia do źródła.

------------------------------------------------------------------------

# 2. Główny cel

Celem pierwszej fazy nie jest stworzenie systemu udzielającego
„wiążących odpowiedzi prawnych".

Celem jest stworzenie:

1.  formalnego modelu wybranego fragmentu prawa,
2.  języka umożliwiającego zapis tego modelu,
3.  silnika pozwalającego wykonywać reguły na określonym stanie
    faktycznym,
4.  mechanizmu wskazywania źródeł każdej reguły,
5.  mechanizmu oznaczania niepewności i konieczności interpretacji,
6.  narzędzi umożliwiających agentom AI dalszą pracę nad modelem.

Projekt powinien odpowiadać na pytanie:

> **Jak daleko można doprowadzić formalizację rzeczywistego prawa bez
> udawania, że niejednoznaczność prawa nie istnieje?**

------------------------------------------------------------------------

# 3. Pierwsza domena: Prawo spółdzielcze

Pierwszym materiałem badawczym jest polskie Prawo spółdzielcze.

Powód wyboru:

-   posiada wyraźne pojęcia domenowe,
-   definiuje organizację,
-   definiuje członkostwo,
-   opisuje organy,
-   określa kompetencje,
-   zawiera procedury,
-   zawiera terminy,
-   opisuje uchwały,
-   opisuje prawa i obowiązki,
-   posiada wiele relacji między przepisami,
-   naturalnie prowadzi do modelu stanów i zdarzeń.

Pierwszy eksperyment powinien być mały.

**Nie należy od razu formalizować całej ustawy.**

Rekomendowany pierwszy milestone:

> formalizacja niewielkiego, spójnego fragmentu ustawy, np.
> kilkunastu--kilkudziesięciu artykułów, wraz z pełnym śladem źródłowym.

------------------------------------------------------------------------

# 4. Fundamentalne założenia

## 4.1. Źródło prawa jest nadrzędne

Tekst źródłowy:

``` text
LAW TEXT
```

jest zawsze nadrzędny wobec:

``` text
FORMALIZATION
```

Formalizacja nie może zastępować tekstu źródłowego.

------------------------------------------------------------------------

## 4.2. Każda reguła musi mieć provenance

Każda formalna reguła powinna wiedzieć:

``` text
source:
    act
    article
    paragraph
    point
    source_text
```

Przykład:

``` yaml
id: R-PS-0001
source:
  act: "Prawo spółdzielcze"
  article: "1"
  paragraph: "1"
  text: "..."
```

Dzięki temu można przejść:

``` text
REGUŁA
  ↓
PRZEPIS
  ↓
TEKST ŹRÓDŁOWY
```

------------------------------------------------------------------------

## 4.3. Formalizacja ma poziom pewności

Każdy element modelu powinien mieć klasyfikację:

``` text
DIRECT
    bezpośrednie odwzorowanie przepisu

STRUCTURAL
    techniczna struktura wynikająca z przepisu

INFERRED
    wniosek wynikający z kilku przepisów

INTERPRETATIVE
    wymaga interpretacji

UNCERTAIN
    formalizacja niepewna

CONTESTED
    istnieją konkurencyjne interpretacje
```

Przykład:

``` yaml
formalization_status: DIRECT
```

versus:

``` yaml
formalization_status: INTERPRETATIVE
interpretation_note: >
  Pojęcie "szczególnie uzasadniony przypadek"
  nie posiada deterministycznego kryterium.
```

------------------------------------------------------------------------

# 5. Model prawny

Projekt powinien rozdzielać kilka warstw.

``` text
┌──────────────────────────────┐
│        SOURCE LAW            │
│      tekst ustawy            │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       LEGAL ONTOLOGY         │
│ podmioty / pojęcia / relacje │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       LEGAL RULES            │
│ obowiązki / zakazy / prawa   │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       LEGAL STATE             │
│ aktualny stan świata          │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       RULE ENGINE             │
│ zastosowanie norm             │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│       ANALYSIS / QUERY        │
└──────────────────────────────┘
```

------------------------------------------------------------------------

# 6. Podstawowe pojęcia DSL

Docelowy język może przypominać:

``` text
ENTITY
EVENT
STATE
RULE
RIGHT
OBLIGATION
PROHIBITION
PERMISSION
POWER
PROCEDURE
DEADLINE
EXCEPTION
CONDITION
EVIDENCE
SOURCE
```

Nie należy zakładać, że wszystkie te konstrukcje muszą od razu istnieć w
pierwszej wersji.

------------------------------------------------------------------------

# 7. Entity --- obiekty świata prawnego

Przykład:

``` text
ENTITY Spółdzielnia {
    HAS members: Set<Członek>
    HAS management: Zarząd
    HAS supervisory_board: RadaNadzorcza
    HAS general_assembly: WalneZgromadzenie

    PROPERTY membership_count: Integer
}
```

Inne przykładowe encje:

``` text
Osoba
Członek
Zarząd
RadaNadzorcza
WalneZgromadzenie
Uchwała
Statut
Fundusz
Majątek
Nieruchomość
OświadczenieWoli
Posiedzenie
Kadencja
```

------------------------------------------------------------------------

# 8. Relacje

Nie wszystko powinno być właściwością.

Przykład:

``` text
Członek --MEMBER_OF--> Spółdzielnia

Zarząd --ORGAN_OF--> Spółdzielnia

RadaNadzorcza --SUPERVISES--> Zarząd

Uchwała --ADOPTED_BY--> WalneZgromadzenie
```

Docelowo relacje powinny tworzyć graf.

------------------------------------------------------------------------

# 9. Stany

Prawo często opisuje nie obiekty, lecz zmiany ich stanu.

Przykład członkostwa:

``` text
PENDING
    ↓
ACTIVE
    ↓
TERMINATED
```

Przykład uchwały:

``` text
PROPOSED
    ↓
VOTED
    ↓
ADOPTED
    ↓
EFFECTIVE
```

Nie należy zakładać, że każdy przepis powoduje zmianę stanu.

------------------------------------------------------------------------

# 10. Events

Zdarzenia są zmianami w świecie.

Przykłady:

``` text
MemberJoined
MemberResigned
MemberExcluded

GeneralAssemblyConvenes
ResolutionProposed
ResolutionAdopted
ResolutionRejected

BoardMemberElected
BoardMemberTermEnded

DocumentSubmitted
DeadlineExpired
```

Przykład:

``` text
EVENT MemberJoined {
    person: Osoba
    cooperative: Spółdzielnia
    date: Date
}
```

------------------------------------------------------------------------

# 11. Reguły

Najważniejszy element systemu.

Przykład:

``` text
RULE R-001 {

    WHEN:
        MemberJoined(person, cooperative)

    THEN:
        Membership(
            person,
            cooperative,
            status = ACTIVE
        )
}
```

------------------------------------------------------------------------

# 12. Obowiązki

Obowiązek powinien być osobnym typem od zwykłej reguły.

``` text
OBLIGATION O-001 {

    SUBJECT:
        Zarząd

    ACTION:
        perform(X)

    TRIGGER:
        EventY

    DEADLINE:
        EventY + 14 days
}
```

System może dzięki temu odpowiedzieć:

``` text
QUERY obligations(subject = Zarząd)
```

------------------------------------------------------------------------

# 13. Uprawnienia

``` text
RIGHT R-001 {

    HOLDER:
        Członek

    ACTION:
        inspect(Document)

    CONDITION:
        membership.status == ACTIVE
}
```

------------------------------------------------------------------------

# 14. Zakazy

``` text
PROHIBITION P-001 {

    SUBJECT:
        Zarząd

    ACTION:
        perform(X)

    CONDITION:
        Y
}
```

------------------------------------------------------------------------

# 15. Dozwolenia

``` text
PERMISSION P-002 {

    SUBJECT:
        Spółdzielnia

    ACTION:
        conduct_social_activity

    CONDITION:
        ...
}
```

Ważne:

``` text
PERMISSION != OBLIGATION
```

To fundamentalna różnica semantyczna.

------------------------------------------------------------------------

# 16. Kompetencje

W prawie szczególnie ważne jest rozróżnienie:

``` text
RIGHT
```

od:

``` text
POWER / COMPETENCE
```

Przykładowo:

``` text
POWER {

    HOLDER:
        RadaNadzorcza

    ACTION:
        appoint(X)

    OBJECT:
        Zarząd
}
```

Kompetencja organu może wpływać na ważność późniejszej czynności.

------------------------------------------------------------------------

# 17. Procedury

Procedura powinna być reprezentowana jako graf kroków.

Przykład:

``` text
PROCEDURE AdoptResolution {

    STEP 1:
        convene_meeting

    STEP 2:
        verify_quorum

    STEP 3:
        present_resolution

    STEP 4:
        vote

    STEP 5:
        calculate_result

    STEP 6:
        record_resolution
}
```

Możliwe warunki:

``` text
STEP 2
REQUIRES:
    quorum >= required_quorum
```

------------------------------------------------------------------------

# 18. Terminy

Termin nie powinien być zwykłą liczbą.

``` text
DEADLINE D-001 {

    START:
        EventA

    DURATION:
        14 days

    TYPE:
        statutory

    EXPIRES:
        ...
}
```

W przyszłości należy uwzględnić:

-   dni kalendarzowe,
-   dni robocze,
-   terminy liczone od zdarzenia,
-   terminy zawite,
-   terminy instrukcyjne,
-   przesunięcie terminu,
-   dzień wolny,
-   moment rozpoczęcia biegu,
-   moment skuteczności.

------------------------------------------------------------------------

# 19. Wyjątki

Prawo jest pełne konstrukcji:

``` text
co do zasady X

z wyjątkiem Y
```

DSL powinien mieć:

``` text
EXCEPTION E-001 {

    APPLIES_TO:
        Rule R-001

    WHEN:
        ConditionY

    EFFECT:
        disable R-001
}
```

Ale należy bardzo uważać z mechanicznym rozumieniem wyjątków.

Wyjątek może:

-   wyłączać normę,
-   modyfikować normę,
-   tworzyć odrębną normę,
-   ograniczać zakres zastosowania,
-   dotyczyć tylko określonego podmiotu.

------------------------------------------------------------------------

# 20. Warunki nieostre

To jeden z najważniejszych problemów projektu.

Przykłady:

``` text
ważny interes
szczególnie uzasadniony przypadek
niezwłocznie
rażące naruszenie
istotne naruszenie
należyta staranność
```

Nie należy udawać, że można je bezpośrednio zapisać:

``` text
if szczegolnie_uzasadniony == true
```

Zamiast tego:

``` text
CONCEPT "szczególnie uzasadniony przypadek" {

    TYPE:
        OPEN_TEXTURED

    REQUIRES:
        interpretation

    POSSIBLE_SOURCES:
        statute
        case_law
        doctrine
        factual_context
}
```

------------------------------------------------------------------------

# 21. Trzy poziomy wykonywalności

Każda norma powinna mieć ocenę:

## Level 1 --- deterministic

Da się rozstrzygnąć mechanicznie.

``` text
IF members.count >= 10
THEN condition = TRUE
```

## Level 2 --- contextual

Potrzebne są dane ze świata.

``` text
IF person.is_member_of(cooperative)
```

## Level 3 --- interpretative

Potrzebna jest interpretacja.

``` text
IF conduct == "rażące naruszenie"
```

To pozwoli systemowi powiedzieć:

``` text
DETERMINISTIC: TRUE
CONTEXTUAL: TRUE
INTERPRETATIVE: UNRESOLVED
```

zamiast wygenerować fałszywą pewność.

------------------------------------------------------------------------

# 22. Legal State

Silnik powinien mieć jawny stan świata.

Przykład:

``` yaml
cooperative:
  id: SM-001
  name: "SM Example"

members:
  - id: P-001
    status: ACTIVE

board:
  members:
    - P-010

supervisory_board:
  members:
    - P-020

events:
  - type: MemberJoined
    date: 2026-01-10
```

Stan może być:

``` text
snapshot
```

ale preferowany model historii:

``` text
EVENT LOG
    ↓
STATE RECONSTRUCTION
```

------------------------------------------------------------------------

# 23. Event sourcing

Każda istotna zmiana powinna być możliwa do odtworzenia:

``` text
2026-01-01
    CooperativeCreated

2026-01-03
    PersonJoined

2026-01-20
    PersonElectedToBoard

2026-02-10
    ResolutionAdopted
```

Stan na dowolny dzień:

``` text
STATE_AT(2026-01-15)
```

powinien być rekonstruowalny z historii.

To jest niezwykle ważne przy analizie prawnej.

------------------------------------------------------------------------

# 24. Legal queries

Docelowy system powinien obsługiwać zapytania.

Przykłady:

``` text
SHOW entities of type Członek

SHOW obligations of Zarząd

SHOW rights of Member(P-001)

CAN RadaNadzorcza perform X?

IS resolution R-123 valid?

WHAT rules were triggered by event E-123?

WHAT deadlines are active?

WHY is action X prohibited?

WHICH RULES apply to this state?

WHAT WAS THE LEGAL STATE ON 2026-05-01?
```

------------------------------------------------------------------------

# 25. Explainability

Każdy wynik musi być wyjaśnialny.

Nigdy:

``` text
INVALID
```

bez uzasadnienia.

Tylko:

``` text
RESULT:
    INVALID / UNCERTAIN

REASON:
    Rule R-031

SOURCE:
    Prawo spółdzielcze
    Art. X §Y

CHAIN:
    Event E-100
        ↓
    Condition C-021
        ↓
    Rule R-031
        ↓
    Violation V-001

UNCERTAINTY:
    none
```

------------------------------------------------------------------------

# 26. Legal provenance graph

Docelowo:

``` text
SOURCE ARTICLE
      │
      ▼
FORMAL RULE
      │
      ▼
CONDITION
      │
      ▼
STATE
      │
      ▼
LEGAL EFFECT
```

Przykład:

``` text
Art. 42 §2
    ↓
R-042-002
    ↓
requires_quorum
    ↓
quorum = false
    ↓
procedure_invalid
```

------------------------------------------------------------------------

# 27. Konflikty norm

System powinien wykrywać potencjalne konflikty.

``` text
RULE A:
    Zarząd MAY perform X

RULE B:
    Zarząd MUST NOT perform X
```

Nie należy automatycznie wybierać jednej.

System powinien zgłosić:

``` text
CONFLICT DETECTED

Rules:
    A
    B

Possible resolution mechanisms:
    hierarchy
    lex_specialis
    lex_posterior
    temporal_scope
    subject_scope

REQUIRES:
    legal interpretation
```

------------------------------------------------------------------------

# 28. Hierarchia prawa

Docelowo model powinien znać źródła prawa:

``` text
Konstytucja
    ↓
Ustawa
    ↓
Rozporządzenie
    ↓
Akt prawa miejscowego
```

Oraz odrębnie:

``` text
Statut
Regulamin
Uchwała
Zarządzenie
```

Nie należy automatycznie traktować wszystkich tych dokumentów jako
równorzędnych źródeł.

------------------------------------------------------------------------

# 29. Statut jako konfiguracja systemu

Bardzo interesujący przypadek:

``` text
LAW
    ↓
GENERAL RULES

STATUT
    ↓
DOMAIN-SPECIFIC RULES
```

Statut może konkretyzować obszary pozostawione przez ustawę.

Model:

``` text
STATUT SM_X {

    CONFIGURES:
        ...

    DEFINES:
        ...

    CANNOT_OVERRIDE:
        mandatory_statutory_rules
}
```

To powinno być osobnym obszarem badań.

------------------------------------------------------------------------

# 30. Nie budować od razu „AI prawnika"

Projekt nie powinien zaczynać się od:

``` text
PDF -> LLM -> odpowiedź
```

To jest zbyt niekontrolowane.

Preferowany pipeline:

``` text
SOURCE
  ↓
PARSER / EXTRACTION
  ↓
STRUCTURED LEGAL TEXT
  ↓
FORMALIZATION
  ↓
VALIDATION
  ↓
RULE ENGINE
  ↓
QUERY
```

LLM może pomagać w:

-   ekstrakcji,
-   proponowaniu formalizacji,
-   wykrywaniu relacji,
-   generowaniu testów,
-   wyszukiwaniu niespójności,
-   wyjaśnianiu tekstu,

ale formalny model powinien być jawny i audytowalny.

------------------------------------------------------------------------

# 31. Rola agenta AI

Przyszły agent powinien działać jako współtwórca modelu, a nie jako
autorytet prawny.

Agent może:

``` text
READ source
EXTRACT definitions
PROPOSE entities
PROPOSE rules
PROPOSE relations
PROPOSE tests
FIND ambiguities
FIND missing references
CHECK consistency
```

Agent NIE powinien bez oznaczenia:

``` text
invent legal rule
resolve ambiguity silently
replace source law
present interpretation as literal text
```

------------------------------------------------------------------------

# 32. Workflow agenta

Rekomendowany workflow:

``` text
1. READ source
2. IDENTIFY legal units
3. IDENTIFY definitions
4. IDENTIFY actors
5. IDENTIFY rights
6. IDENTIFY obligations
7. IDENTIFY prohibitions
8. IDENTIFY permissions
9. IDENTIFY powers
10. IDENTIFY conditions
11. IDENTIFY exceptions
12. IDENTIFY temporal rules
13. IDENTIFY cross-references
14. PROPOSE formalization
15. VALIDATE against source
16. WRITE tests
17. FLAG ambiguity
18. COMMIT
```

Każdy etap powinien być możliwy do przejrzenia przez człowieka.

------------------------------------------------------------------------

# 33. Testy prawne

Każda formalna reguła powinna mieć test.

Przykład:

``` text
TEST R-001-001

GIVEN:
    cooperative.members = 5

WHEN:
    MemberJoined(P-100)

THEN:
    cooperative.members.count == 6
```

Ale również test negatywny:

``` text
TEST R-001-002

GIVEN:
    condition_X = false

WHEN:
    action_X

THEN:
    rule_X does not apply
```

------------------------------------------------------------------------

# 34. Testy regresyjne

Zmiana jednej reguły nie może niezauważenie zmienić wyników innych.

``` text
tests/
    article_001/
    article_002/
    membership/
    organs/
    resolutions/
    deadlines/
    exceptions/
```

------------------------------------------------------------------------

# 35. Testy źródłowe

Każdy przepis powinien mieć możliwość sprawdzenia:

``` text
SOURCE TEXT
    ↓
EXPECTED FORMALIZATION
    ↓
ACTUAL FORMALIZATION
```

W razie zmiany ustawy:

``` text
SOURCE VERSION CHANGED
        ↓
affected rules
        ↓
affected tests
        ↓
agent review
```

------------------------------------------------------------------------

# 36. Wersjonowanie prawa

To absolutnie kluczowe.

Nie wystarczy:

``` text
PrawoSpółdzielcze.dsl
```

Potrzebujemy:

``` text
PrawoSpoldzielcze/
    2026-03-23/
    2026-...
```

Każdy model powinien mieć:

``` text
valid_from
valid_to
source_version
```

Przykład:

``` yaml
rule:
  id: R-123

validity:
  from: 2026-03-23
  to: null
```

Zapytanie powinno móc określić:

``` text
AS_OF 2025-06-01
```

------------------------------------------------------------------------

# 37. Najważniejszy test projektu

System powinien umieć powiedzieć:

> „Nie mogę tego rozstrzygnąć na podstawie formalnego modelu."

To jest **sukces**, a nie porażka.

Przykład:

``` text
QUERY:
    Czy działanie X było "rażącym naruszeniem"?

RESULT:
    UNRESOLVED

REASON:
    Pojęcie jest niedookreślone.

REQUIRES:
    interpretation

RELEVANT SOURCES:
    ...
```

Nigdy nie należy wymuszać:

``` text
TRUE / FALSE
```

jeżeli model tego nie uzasadnia.

------------------------------------------------------------------------

# 38. Proponowana struktura repozytorium

``` text
legal-code/
│
├── README.md
├── PROJECT_CONCEPT.md
├── AGENTS.md
├── CONTRIBUTING.md
├── LICENSE
│
├── docs/
│   ├── architecture.md
│   ├── legal-model.md
│   ├── dsl.md
│   ├── provenance.md
│   ├── uncertainty.md
│   ├── versioning.md
│   └── agent-workflow.md
│
├── law/
│   └── prawo-spoldzielcze/
│       ├── source/
│       ├── normalized/
│       ├── ontology/
│       ├── rules/
│       ├── procedures/
│       ├── concepts/
│       └── interpretations/
│
├── model/
│   ├── entities/
│   ├── relations/
│   ├── events/
│   ├── states/
│   └── rules/
│
├── engine/
│   ├── parser/
│   ├── evaluator/
│   ├── state/
│   ├── queries/
│   └── provenance/
│
├── tests/
│   ├── unit/
│   ├── legal/
│   ├── regression/
│   └── fixtures/
│
├── agents/
│   ├── extraction/
│   ├── formalization/
│   ├── validation/
│   └── review/
│
└── examples/
    ├── simple_cooperative/
    └── resolution_validation/
```

Struktura może zostać zmieniona po rozpoczęciu implementacji.

------------------------------------------------------------------------

# 39. Minimalny DSL --- propozycja

Pierwsza wersja może wyglądać tak:

``` text
ENTITY Spółdzielnia {
    HAS members: Set<Członek>
}

ENTITY Członek {
    HAS person: Osoba
}

RELATION MEMBER_OF(Członek, Spółdzielnia)

EVENT MemberJoined {
    person: Osoba
    cooperative: Spółdzielnia
}

RULE MemberJoinedCreatesMembership {

    SOURCE:
        PrawoSpółdzielcze.Art1

    WHEN:
        MemberJoined(person, cooperative)

    THEN:
        MEMBER_OF(person, cooperative)
}
```

Potem:

``` text
OBLIGATION
RIGHT
PROHIBITION
POWER
DEADLINE
EXCEPTION
PROCEDURE
```

------------------------------------------------------------------------

# 40. Przykład pełnego przepisu

Docelowy zapis może mieć postać:

``` text
RULE R-PS-001 {

    SOURCE {
        ACT: "Prawo spółdzielcze"
        ARTICLE: 1
        PARAGRAPH: 1
        TEXT: "..."
    }

    SUBJECT:
        Spółdzielnia

    NORM_TYPE:
        DEFINITION

    ASSERTS:
        Spółdzielnia IS
            dobrowolne_zrzeszenie
            osób
            o_nieograniczonej_liczbie
            o_zmiennym_składzie
            o_zmiennym_funduszu_udziałowym

    PURPOSE:
        wspólna_działalność
        w_interesie_członków

    FORMALIZATION_STATUS:
        DIRECT
}
```

------------------------------------------------------------------------

# 41. Przykład normy operacyjnej

``` text
RULE R-PS-XYZ {

    SOURCE {
        ACT: "Prawo spółdzielcze"
        ARTICLE: "..."
    }

    SUBJECT:
        Zarząd

    ACTION:
        represent(cooperative)

    NORM_TYPE:
        POWER

    CONDITIONS:
        representation_requirements_met == true

    EFFECT:
        legal_act.may_bind(cooperative)

    FORMALIZATION_STATUS:
        STRUCTURAL
}
```

------------------------------------------------------------------------

# 42. Przykład normy nieostrej

``` text
RULE R-PS-ABC {

    SOURCE {
        ACT: "Prawo spółdzielcze"
        ARTICLE: "..."
    }

    SUBJECT:
        Członek

    CONDITION:
        conduct_is("rażące")

    CONCEPT:
        rażące

    SEMANTIC_TYPE:
        OPEN_TEXTURED

    REQUIRES:
        INTERPRETATION

    FORMALIZATION_STATUS:
        INTERPRETATIVE
}
```

------------------------------------------------------------------------

# 43. Graf prawa

Docelowo projekt powinien móc wygenerować graf:

``` text
                 ┌──────────────┐
                 │   ART. 1     │
                 └──────┬───────┘
                        │
                        ▼
                ┌──────────────┐
                │ Spółdzielnia │
                └──────┬───────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Członkowie     Zarząd       Statut
          │            │
          ▼            ▼
       prawa       kompetencje
          │            │
          └──────┬─────┘
                 ▼
             procedury
                 │
                 ▼
              uchwały
                 │
                 ▼
             skutki prawne
```

Graf może być bardzo przydatny dla agentów.

------------------------------------------------------------------------

# 44. Możliwa przyszła funkcja: impact analysis

Jeżeli zmieni się:

``` text
Art. 18
```

system powinien móc powiedzieć:

``` text
AFFECTED RULES:
    R-018-001
    R-018-004
    R-031-002

AFFECTED ENTITIES:
    Członek

AFFECTED PROCEDURES:
    MembershipAdmission

AFFECTED TESTS:
    17

AFFECTED DOCUMENTS:
    ...
```

To byłaby bardzo praktyczna funkcja.

------------------------------------------------------------------------

# 45. Możliwa przyszła funkcja: legal diff

Porównanie wersji prawa:

``` text
LAW VERSION A
        vs.
LAW VERSION B
```

wynik:

``` text
ADDED:
    R-123

REMOVED:
    R-087

MODIFIED:
    R-021

SEMANTIC IMPACT:
    membership
    board
    resolution
```

To może być jedna z najbardziej użytecznych funkcji projektu.

------------------------------------------------------------------------

# 46. Możliwa przyszła funkcja: analiza konkretnego stanu faktycznego

Przykład:

``` yaml
case:
  cooperative: SM_X
  event:
    type: ResolutionAdopted
    date: 2026-09-20

  facts:
    quorum: 0.42
    required_quorum: 0.50
    board_present: true
```

Następnie:

``` text
ANALYZE CASE
```

wynik:

``` text
APPLICABLE RULES:
    R-001
    R-022
    R-031

TRIGGERED:
    R-031

CONDITION:
    quorum >= required_quorum

RESULT:
    FALSE

LEGAL STATUS:
    PROCEDURAL CONDITION NOT SATISFIED

SOURCE:
    Art. ...
```

------------------------------------------------------------------------

# 47. Zasada „nie ukrywaj interpretacji"

Jeżeli agent proponuje:

``` text
condition = quorum >= 50%
```

musi istnieć informacja:

``` text
WHY:
    source text says "..."
```

oraz:

``` text
INTERPRETATION:
    "50%" interpreted as ...
```

Nie wolno dopuścić do sytuacji:

``` text
LLM hallucination
    ↓
formal rule
    ↓
system treats it as law
```

To jest jedno z głównych zagrożeń projektu.

------------------------------------------------------------------------

# 48. Zasada dwóch źródeł

Jeżeli to możliwe, formalizacja powinna rozdzielać:

``` text
SOURCE TEXT
```

od:

``` text
INTERPRETATION
```

Przykład:

``` yaml
source:
  article: 123

interpretation:
  type: doctrine
  reference: ...
```

W przyszłości:

``` text
SOURCE
INTERPRETATION
CASE_LAW
DOCTRINE
COMMENTARY
```

powinny być osobnymi kategoriami.

------------------------------------------------------------------------

# 49. Czego NIE robić na początku

Nie zaczynać od:

-   całej ustawy,
-   wszystkich ustaw,
-   automatycznej interpretacji,
-   chatbota,
-   UI,
-   mikroserwisów,
-   bazy danych produkcyjnej,
-   rozproszonej architektury,
-   RAG jako głównego mechanizmu,
-   automatycznego generowania prawa.

Najpierw:

``` text
kilkanaście przepisów
+
formalny model
+
DSL
+
parser
+
walidator
+
testy
```

------------------------------------------------------------------------

# 50. Minimalny MVP

MVP powinno umieć:

``` text
1. Wczytać źródło prawa.

2. Zidentyfikować przepisy.

3. Nadać im stabilne ID.

4. Zdefiniować Entity.

5. Zdefiniować Rule.

6. Powiązać Rule ze źródłem.

7. Zdefiniować Event.

8. Zdefiniować State.

9. Uruchomić regułę.

10. Wygenerować wynik.

11. Pokazać provenance.

12. Pokazać uncertainty.
```

------------------------------------------------------------------------

# 51. Kryterium sukcesu MVP

MVP jest udane, jeśli dla przykładowego stanu:

``` text
STATE
    +
EVENT
```

system potrafi wygenerować:

``` text
RULES APPLIED
STATE CHANGES
RIGHTS CREATED
OBLIGATIONS CREATED
DEADLINES CREATED
PROHIBITIONS TRIGGERED
SOURCES
UNCERTAINTIES
```

i człowiek może przejść od każdego wyniku z powrotem do przepisu.

------------------------------------------------------------------------

# 52. Roadmap

## Phase 0 --- research

-   wybrać fragment ustawy,
-   zebrać źródło,
-   ustalić wersję czasową,
-   opracować konwencję ID,
-   zaprojektować minimalny model.

## Phase 1 --- ontology

-   Entity,
-   Relation,
-   State,
-   Event.

## Phase 2 --- rules

-   Rule,
-   Right,
-   Obligation,
-   Prohibition,
-   Permission,
-   Power.

## Phase 3 --- execution

-   state engine,
-   event engine,
-   evaluator.

## Phase 4 --- provenance

-   source mapping,
-   citations,
-   rule lineage.

## Phase 5 --- uncertainty

-   ambiguous concepts,
-   interpretation nodes,
-   confidence.

## Phase 6 --- legal queries

-   WHY,
-   WHAT,
-   CAN,
-   MUST,
-   CANNOT,
-   WHAT CHANGED.

## Phase 7 --- versioning

-   historical law,
-   amendments,
-   semantic diff.

## Phase 8 --- agent tooling

-   extraction agent,
-   formalization agent,
-   reviewer agent,
-   test-generation agent.

------------------------------------------------------------------------

# 53. Agent roles

Można docelowo rozdzielić agentów.

### Source Agent

Zajmuje się:

``` text
retrieval
normalization
article segmentation
version identification
```

### Ontology Agent

Zajmuje się:

``` text
entities
relations
concepts
```

### Rule Agent

Zajmuje się:

``` text
norms
conditions
effects
```

### Test Agent

Generuje:

``` text
positive cases
negative cases
edge cases
regression tests
```

### Reviewer Agent

Sprawdza:

``` text
source coverage
contradictions
missing rules
unsupported assumptions
```

### Human Reviewer

Podejmuje decyzje tam, gdzie potrzebna jest interpretacja.

------------------------------------------------------------------------

# 54. Zasada dla agentów

Agent powinien zawsze rozróżniać:

``` text
FACT
INFERENCE
INTERPRETATION
ASSUMPTION
UNKNOWN
```

Przykład:

``` text
FACT:
    Art. X mówi Y.

INFERENCE:
    Y implies Z under model M.

INTERPRETATION:
    Pojęcie A rozumiemy jako B.

ASSUMPTION:
    Przyjmujemy, że dokument jest ważny.

UNKNOWN:
    Brak danych pozwalających rozstrzygnąć C.
```

------------------------------------------------------------------------

# 55. Docelowa wizja

Jeżeli eksperyment się powiedzie, można dojść do systemu:

``` text
                    LAW
                     │
          ┌──────────┴──────────┐
          │                     │
       SOURCE               INTERPRETATION
          │                     │
          └──────────┬──────────┘
                     ▼
               LEGAL MODEL
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       ENTITIES     RULES     EVENTS
          │          │          │
          └──────────┼──────────┘
                     ▼
                LEGAL STATE
                     │
                     ▼
                RULE ENGINE
                     │
                     ▼
                  QUERY
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        RESULT     REASONS    SOURCES
```

Najważniejsza idea:

> **Nie budujemy maszyny, która „zna prawo". Budujemy formalny model,
> który pozwala eksperymentalnie sprawdzić, jak dużą część prawa można
> reprezentować jako system jawnych obiektów, stanów i reguł.**

------------------------------------------------------------------------

# 56. Pierwszy konkretny eksperyment

Pierwsze zadanie po utworzeniu repozytorium:

``` text
TASK-001

Formalizować wybrany niewielki fragment
Prawa spółdzielczego.

Deliverables:

1. source/
2. normalized/
3. ontology/
4. rules/
5. tests/
6. provenance/
7. README z opisem decyzji.
```

Każda reguła:

``` text
RULE-ID
SOURCE
SOURCE-TEXT
FORMALIZATION
RATIONALE
STATUS
TESTS
```

------------------------------------------------------------------------

# 57. Definition of Done dla pojedynczego przepisu

Przepis jest „opracowany", jeśli:

``` text
[ ] źródło jest znane
[ ] wersja prawa jest znana
[ ] tekst został zachowany
[ ] przepisy powiązane zostały zidentyfikowane
[ ] encje zostały zidentyfikowane
[ ] relacje zostały zidentyfikowane
[ ] normy zostały zidentyfikowane
[ ] warunki zostały zidentyfikowane
[ ] wyjątki zostały zidentyfikowane
[ ] skutki zostały zidentyfikowane
[ ] formalizacja została wykonana
[ ] status formalizacji został oznaczony
[ ] test został utworzony
[ ] provenance działa
[ ] niepewności są jawne
```

------------------------------------------------------------------------

# 58. Najważniejsze pytania badawcze projektu

Projekt nie jest tylko projektem programistycznym.

Ma również komponent badawczy.

Należy sprawdzić:

1.  Jak dużą część typowego przepisu można formalizować
    deterministycznie?
2.  Które konstrukcje prawne najgorzej poddają się formalizacji?
3.  Czy można stworzyć uniwersalny DSL dla różnych ustaw?
4.  Czy jeden model reguł wystarcza dla prawa cywilnego,
    administracyjnego i spółdzielczego?
5.  Jak reprezentować normy kolizyjne?
6.  Jak reprezentować wyjątki?
7.  Jak reprezentować pojęcia nieostre?
8.  Jak reprezentować orzecznictwo?
9.  Jak reprezentować konkurencyjne interpretacje?
10. Jak wykrywać zmianę znaczenia normy po nowelizacji?
11. Czy formalizacja może automatycznie wykrywać niespójności?
12. Czy można wygenerować testy z przepisów?
13. Czy można wykonać analizę skutków nowelizacji?
14. Jak dużo pracy można bezpiecznie delegować agentom AI?
15. Gdzie musi pozostać człowiek?

------------------------------------------------------------------------

# 59. Filozofia projektu

Najważniejszą zasadą jest:

> **Formalizować maksymalnie dużo, ale twierdzić minimalnie dużo.**

Jeżeli przepis jest jednoznaczny:

``` text
FORMALIZE
```

Jeżeli zależy od danych:

``` text
REQUEST DATA
```

Jeżeli jest nieostry:

``` text
MARK AS INTERPRETATIVE
```

Jeżeli istnieje konflikt:

``` text
SURFACE CONFLICT
```

Jeżeli nie wiadomo:

``` text
SAY UNKNOWN
```

Nigdy:

``` text
GUESS
```

------------------------------------------------------------------------

# 60. Potencjalna długoterminowa wartość

Jeżeli projekt okaże się wykonalny, jego zastosowania mogą wykraczać
poza Prawo spółdzielcze:

``` text
Prawo spółdzielcze
        ↓
Kodeks cywilny
        ↓
Ustawa o własności lokali
        ↓
Prawo budowlane
        ↓
Ustawa o rachunkowości
        ↓
Prawo podatkowe
        ↓
...
```

Szczególnie interesujący byłby później model:

``` text
SPÓŁDZIELNIA MIESZKANIOWA
        │
        ├── Prawo spółdzielcze
        ├── Ustawa o własności lokali
        ├── Prawo budowlane
        ├── Ustawa o rachunkowości
        ├── Kodeks cywilny
        └── przepisy podatkowe
```

Wtedy pojedynczy stan rzeczywisty mógłby być analizowany przez wiele
nakładających się systemów norm.

------------------------------------------------------------------------

# 61. Ostateczny eksperyment

Najbardziej ambitny test projektu brzmi:

> Czy można wprowadzić do systemu kompletny, historycznie określony stan
> prawny konkretnej spółdzielni, a następnie odtworzyć z formalnego
> modelu odpowiedź na pytanie: „co spółdzielnia, jej organy i jej
> członkowie mogą, muszą i czego nie mogą zrobić w danej sytuacji?"

Jeżeli tak, projekt przechodzi z:

``` text
"ciekawego DSL-a"
```

do:

``` text
formalnego modelu normatywnego świata.
```

To jest właściwy długoterminowy cel eksperymentu.

------------------------------------------------------------------------

# 62. Zasada końcowa dla przyszłych agentów

Każdy agent pracujący nad projektem powinien pamiętać:

``` text
SOURCE > MODEL
MODEL > GUESS

TRACEABILITY > CONVENIENCE
EXPLICIT UNCERTAINTY > FALSE PRECISION
TESTED RULE > UNTESTED RULE
HUMAN REVIEW > SILENT INTERPRETATION
```

A przede wszystkim:

> **Jeżeli nie potrafisz wskazać, z którego fragmentu prawa wynika dana
> reguła, nie przedstawiaj jej jako reguły prawa.**
