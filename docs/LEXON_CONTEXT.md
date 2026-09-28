# LEXON — KONTEKST PROJEKTU I KIERUNEK ARCHITEKTONICZNY

> **Status dokumentu:** kontekst architektoniczny, zbiór hipotez i decyzji
> kierunkowych — **nie** jest to jeszcze specyfikacja implementacyjna.
> Pochodzi z rozmowy przeprowadzonej z innym agentem, wklejony tu
> w całości jako materiał źródłowy dla dalszej pracy nad repozytorium.
> Patrz `docs/decisions/` po decyzje podjęte na jego podstawie.

## 1. Cel tego dokumentu

Ten dokument przekazuje agentowi obsługującemu projekt Lexon kontekst wynikający z wcześniejszych dyskusji projektowych.

Nie jest to jeszcze specyfikacja implementacyjna. Jest to **kontekst architektoniczny, zbiór hipotez i decyzji kierunkowych**, który powinien być uwzględniany przy dalszym projektowaniu.

Najważniejsza zasada:

> Nie zakładać, że Lexon musi być kolejnym kompletnym językiem programowania prawa. Należy najpierw ustalić, jaka warstwa rzeczywiście jest potrzebna ponad istniejącymi standardami i narzędziami.

---

# 2. Pierwotny pomysł

Punktem wyjścia był pomysł stworzenia języka formalizującego polskie prawo.

Intuicyjny model:

```text
tekst ustawy
    ↓
parser
    ↓
LEXON
    ↓
formalna reprezentacja prawa
```

Przykładowo przepis:

```text
Jeżeli X spełnia warunki A i B,
przysługuje mu prawo Y.
```

mógłby zostać zapisany jako formalna reguła:

```text
IF
    X satisfies A
    AND X satisfies B
THEN
    X HAS RIGHT Y
```

Jednak w trakcie dyskusji pomysł został rozszerzony.

---

# 3. Kluczowa ewolucja pomysłu

Lexon nie powinien być traktowany wyłącznie jako:

> „język programowania prawa”.

Znacznie ciekawsza koncepcja to:

> **Lexon jako Legal Semantic Intermediate Representation (Legal Semantic IR).**

Czyli warstwa pośrednia pomiędzy rzeczywistym prawem a różnymi systemami informatycznymi.

Docelowy model:

```text
                    PRAWO
                      │
                      ▼
             źródła prawne / AKN
                      │
                      ▼
              parser + analiza
                      │
                      ▼
              ┌──────────────┐
              │    LEXON     │
              │ Legal Semantic│
              │      IR      │
              └──────┬───────┘
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
    Catala         Python      TypeScript
       │             │             │
       ▼             ▼             ▼
    reguły        backend       aplikacja
```

Lexon nie musi być zatem końcowym językiem wykonywalnym.

---

# 4. Główna analogia: compiler / IR

Lexon powinien być projektowany częściowo analogicznie do Intermediate Representation w kompilatorach.

Przykład:

```text
C
C++
Rust
   │
   ▼
  LLVM IR
   │
   ├── x86
   ├── ARM
   └── WASM
```

Analogicznie:

```text
ustawa
rozporządzenie
orzeczenie
umowa
   │
   ▼
  LEXON IR
   │
   ├── Catala
   ├── Python
   ├── TypeScript
   ├── C#
   ├── SQL
   ├── LegalRuleML
   └── inne backendy
```

Najważniejszą własnością Lexona byłaby więc **niezależność modelu prawa od konkretnego języka implementacji**.

---

# 5. Dlaczego jest to interesujące

Obecnie różne systemy mogą implementować tę samą regułę prawną niezależnie:

```text
                         PRAWO
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       system A         system B         system C
          │                │                │
       własna           własna           własna
       implementacja    implementacja    implementacja
```

Powoduje to potencjalnie:

* duplikację pracy,
* różnice implementacyjne,
* problemy z aktualizacją,
* zależność od konkretnych dostawców,
* trudność audytowania,
* trudność ustalenia, skąd dokładnie pochodzi dana reguła.

Lexon mógłby umożliwić:

```text
                         PRAWO
                           │
                           ▼
                         LEXON
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       system A         system B         system C
```

Jedna formalna reprezentacja → wiele implementacji.

---

# 6. Automatyzacja zmian prawa

Jednym z najważniejszych potencjalnych zastosowań jest automatyczne reagowanie na zmiany legislacyjne.

Docelowy pipeline:

```text
Dziennik Ustaw / źródło prawa
             │
             ▼
        wykrycie zmiany
             │
             ▼
       różnica semantyczna
             │
             ▼
      zmiana modelu Lexon
             │
             ▼
      impact analysis
             │
             ▼
     dotknięte reguły
             │
             ▼
     dotknięty kod aplikacji
             │
             ▼
       wygenerowany diff
             │
             ▼
     wygenerowane testy
             │
             ▼
      review / CI / deploy
```

Przykładowo:

```text
OLD:
    age >= 50

NEW:
    age >= 55
```

Lexon powinien potencjalnie umieć reprezentować:

```text
LEGAL_CHANGE
    source: ...
    affected_rule: R-123
    old_condition:
        age >= 50
    new_condition:
        age >= 55
```

Następnie:

```text
R-123
 ↓
PayrollRule-17
 ↓
payroll_service.py
 ↓
tests/test_payroll_17.py
```

Ważne:

> Nie należy zakładać, że automatyczna zmiana kodu może być zawsze bezpieczna. System powinien umieć oznaczać zmiany wymagające interpretacji lub ręcznej akceptacji.

---

# 7. Traceability — śledzenie pochodzenia reguły

Jedną z najważniejszych potencjalnych właściwości Lexona jest pełny łańcuch pochodzenia:

```text
tekst prawa
    ↓
konkretny artykuł
    ↓
interpretacja
    ↓
reguła Lexon
    ↓
implementacja
    ↓
test
    ↓
wynik aplikacji
```

Przykładowo:

```text
wynik aplikacji
    ↓
RULE-0173
    ↓
Lexon AST node
    ↓
interpretation I-0042
    ↓
Kodeks pracy
    ↓
art. 152 § 1
    ↓
konkretny tekst źródłowy
    ↓
wersja aktu obowiązująca w danym czasie
```

To powinno być jednym z fundamentalnych założeń projektu.

---

# 8. Provenance jako element pierwszej klasy

Każdy element semantyczny powinien mieć możliwość wskazania źródła.

Przykładowo:

```yaml
rule:
  id: RULE-000173

  source:
    document: PL-KP
    article: "152"
    paragraph: "1"

  interpretation:
    id: INT-00031
    method: explicit
    confidence: high
```

Jeszcze lepiej, jeśli można wskazać dokładny fragment dokumentu:

```yaml
source:
  document: ...
  article: ...
  paragraph: ...
  text_span:
    start: ...
    end: ...
```

Provenance nie powinien być dodatkiem. Powinien być częścią modelu Lexon.

---

# 9. Rozdzielenie tekstu prawa od interpretacji

Nie należy zakładać:

```text
przepis → jedna bezdyskusyjna reguła
```

W prawie występują:

* niejednoznaczności,
* interpretacje,
* wyjątki,
* konflikty norm,
* uznanie administracyjne,
* pojęcia niedookreślone,
* różne stanowiska doktryny/orzecznictwa.

Dlatego Lexon powinien potencjalnie rozróżniać:

```text
SOURCE TEXT
    ↓
PROPOSITION
    ↓
INTERPRETATION
    ↓
LEXON RULE
```

Możliwe jest także:

```text
TEXT
 │
 ├── Interpretation A
 │      ↓
 │    Rule A
 │
 └── Interpretation B
        ↓
      Rule B
```

Lexon nie powinien „ukrywać” niepewności interpretacyjnej.

---

# 10. Temporalność

Prawo jest silnie zależne od czasu.

Nie wystarczy:

```text
rule = R123
```

Potrzebne są informacje typu:

```text
enacted_at
published_at
effective_from
effective_until
repealed_at
```

Ponadto poszczególne przepisy mogą mieć własne okresy obowiązywania i przepisy przejściowe.

Docelowo pytanie:

> „Jaką regułę zastosować do zdarzenia z dnia X?”

powinno być formalnie rozwiązywalne.

Przykładowo:

```text
EVENT_DATE
    ↓
LEGAL VERSION
    ↓
APPLICABLE PROVISION
    ↓
LEXON RULE
```

Temporalność powinna być jednym z fundamentalnych elementów modelu, a nie dodatkiem.

---

# 11. Graf zależności prawnych

Lexon powinien potencjalnie tworzyć graf relacji pomiędzy normami.

Przykładowe relacje:

```text
AMENDS
REPEALS
DEPENDS_ON
EXCEPTS
OVERRIDES
IMPLEMENTS
REFERENCES
DERIVES_FROM
INTERPRETS
```

Przykład:

```text
N100
 ├── AMENDS → N101
 ├── REFERENCES → N102
 └── IMPLEMENTS → N103
                         │
                         ▼
                    APPLICATION
```

Dzięki temu zmiana jednej normy może uruchomić analizę wpływu:

```text
changed rule
    ↓
dependent rules
    ↓
business rules
    ↓
application components
    ↓
tests
```

---

# 12. Istniejące technologie i standardy

Lexon nie powinien ignorować istniejącego ekosystemu.

## 12.1 Akoma Ntoso

Akoma Ntoso jest standardem strukturyzowania dokumentów prawnych i parlamentarnych.

Powinien być traktowany jako:

> **źródłowy format dokumentu / document representation.**

Lexon nie powinien wymyślać własnego odpowiednika:

```text
article
paragraph
point
reference
```

Zamiast tego powinien umieć konsumować Akoma Ntoso.

Model:

```text
Akoma Ntoso
     ↓
Lexon parser
```

---

## 12.2 ELI

European Legislation Identifier powinien być wykorzystywany do:

* identyfikacji aktów,
* URI,
* metadanych,
* wersji,
* relacji między dokumentami.

Nie należy tworzyć konkurencyjnego systemu identyfikacji prawa bez bardzo mocnego powodu.

Model:

```text
ELI
 ↓
document identity / metadata
 ↓
Lexon
```

---

## 12.3 LKIF

Legal Knowledge Interchange Format jest istotnym źródłem inspiracji dla:

* ontologii prawnych,
* podstawowych pojęć prawnych,
* relacji między pojęciami,
* reprezentacji wiedzy.

Nie należy jednak bezrefleksyjnie kopiować całej architektury LKIF.

Podejście:

> **reuse concepts / ontology ideas, but keep Lexon's own internal model.**

---

## 12.4 LegalRuleML

To najważniejszy istniejący standard, który należy dokładnie przeanalizować.

LegalRuleML obejmuje m.in.:

* normy,
* obowiązki,
* uprawnienia,
* zakazy,
* permissions,
* deontykę,
* warunki,
* wyjątki,
* defeasibility,
* temporalność,
* jurysdykcję,
* priorytety,
* źródła norm,
* relacje norm ↔ tekst.

Dlatego Lexon nie powinien udawać, że te mechanizmy trzeba wymyślić od zera.

Podejście:

```text
Lexon AST
    ↕
LegalRuleML adapter
```

Semantyka może być kompatybilna, ale wewnętrzna reprezentacja Lexona nie musi być kopią LegalRuleML.

---

## 12.5 Catala

Catala jest wykonywalnym językiem programowania przeznaczonym do formalizacji prawa.

Lexon nie powinien próbować kopiować Catali.

Catala powinno być traktowane potencjalnie jako:

> **backend / target language dla Lexona.**

Model:

```text
Lexon
   ↓
Catala
   ↓
executable implementation
```

W przyszłości podobnie można rozważać:

```text
Lexon → Python
Lexon → TypeScript
Lexon → C#
Lexon → SQL
Lexon → OPA/Rego
...
```

---

# 13. Najważniejsza decyzja architektoniczna

Lexon powinien być rozdzielony na:

```text
LEXON LANGUAGE
        +
LEXON AST
        +
LEXON SEMANTIC IR
```

Język źródłowy może być przyjazny człowiekowi:

```text
RIGHT Employee
    TO AnnualLeave
    WHEN EmploymentDuration >= 6 months
```

Natomiast wewnętrznie:

```yaml
Norm:
  id: ...
  subject:
    type: Employee

  modality:
    type: Right

  action:
    type: AnnualLeave

  conditions:
    - comparison:
        left: EmploymentDuration
        operator: GTE
        right: 6_months
```

Następnie AST/IR może być tłumaczony do:

```text
LegalRuleML
Catala
Python
TypeScript
SQL
...
```

---

# 14. Elementy, które prawdopodobnie warto zrobić samemu

Najbardziej prawdopodobne obszary własnej implementacji:

## 14.1 Lexon AST

Własna, typowana reprezentacja drzewa semantycznego.

## 14.2 Semantic IR

Warstwa niezależna od konkretnego formatu źródłowego i konkretnego backendu.

## 14.3 Provenance

Pełne śledzenie:

```text
law → interpretation → rule → code → test
```

## 14.4 Interpretation model

Oddzielenie:

```text
what the law literally says
```

od:

```text
how we formally interpreted it
```

## 14.5 Dependency graph

Relacje pomiędzy normami, przepisami, interpretacjami i implementacjami.

## 14.6 Version graph

Nie tylko wersjonowanie plików, ale wersjonowanie prawa i jego semantycznych konsekwencji.

## 14.7 Impact analysis

Mechanizm odpowiadający na:

> „Co w systemie może się zmienić, jeśli zmieni się ten przepis?”

## 14.8 Code generation mapping

Mapowanie:

```text
Lexon rule
    ↓
domain concept
    ↓
application implementation
```

---

# 15. Potencjalna architektura całego systemu

```text
                       OFFICIAL SOURCES
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
            ISAP             RCL            EUR-Lex
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                    DOCUMENT INGESTION
                              │
                              ▼
                     Akoma Ntoso / ELI
                              │
                              ▼
                     LEGAL PARSER
                              │
                              ▼
                   SEMANTIC EXTRACTION
                              │
                              ▼
                    ┌────────────────┐
                    │     LEXON      │
                    │                │
                    │ Legal Semantic │
                    │      IR        │
                    └───────┬────────┘
                            │
            ┌───────────────┼────────────────┐
            │               │                │
            ▼               ▼                ▼
      LegalRuleML        Catala        Application DSL
            │               │                │
            │               ▼                ▼
            │           executable       software
            │
            ▼
       legal knowledge
```

---

# 16. Docelowy system zmian prawa

Docelowo możliwy jest pipeline:

```text
                    NEW LEGISLATION
                          │
                          ▼
                    DOCUMENT DIFF
                          │
                          ▼
                   SEMANTIC DIFF
                          │
                          ▼
                    LEXON UPDATE
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
        impact graph   rule diff    new tests
             │            │            │
             └────────────┼────────────┘
                          ▼
                    CODE GENERATION
                          │
                          ▼
                       REVIEW
                          │
                          ▼
                         CI
                          │
                          ▼
                       DEPLOY
```

Nie należy jednak zakładać pełnej automatyzacji. System powinien potrafić zatrzymać się przy:

```text
AMBIGUOUS INTERPRETATION
HUMAN JUDGMENT REQUIRED
CONFLICTING AUTHORITIES
LOW CONFIDENCE
UNRESOLVED NORM
```

---

# 17. Najważniejsza hipoteza badawcza projektu

Projekt nie powinien zaczynać się od pytania:

> „Jak zaprojektować składnię Lexona?”

Najpierw należy odpowiedzieć:

> **„Jaki minimalny model semantyczny jest potrzebny, aby reprezentować prawo niezależnie od sposobu jego późniejszej implementacji?”**

Dopiero później:

```text
semantic model
      ↓
AST
      ↓
syntax
      ↓
compiler
```

---

# 18. Zalecany pierwszy eksperyment

Nie budować od razu całego parsera polskiego prawa.

Wybrać **jeden niewielki, rzeczywisty fragment polskiego prawa**, najlepiej zawierający:

* definicje,
* warunki,
* wyjątek,
* zależność między przepisami,
* element temporalny.

Następnie reprezentować ten sam fragment w:

1. oryginalnym tekście prawa,
2. Akoma Ntoso,
3. LegalRuleML,
4. Catala,
5. hipotetycznym Lexon AST,
6. hipotetycznym Lexon syntax,
7. kodzie docelowej aplikacji.

Porównać:

```text
co każdy standard potrafi?
czego nie potrafi?
co jest niewygodne?
co jest nadmiarowe?
co trzeba interpretować?
co jest deterministyczne?
co wymaga człowieka?
```

Dopiero na tej podstawie należy zamrażać specyfikację Lexona.

---

# 19. Zasada projektowa

Najważniejsza zasada dla przyszłego agenta:

> **Nie wymyślaj ponownie istniejących standardów tylko dlatego, że można je zaprojektować ładniej.**

Najpierw sprawdź, czy dana funkcjonalność jest już dobrze rozwiązana przez:

* Akoma Ntoso,
* ELI,
* LKIF,
* LegalRuleML,
* RuleML,
* Catala,
* inne istniejące standardy Law as Code.

Własne rozwiązanie wprowadzaj wtedy, gdy:

1. istniejący standard nie obsługuje potrzebnego przypadku,
2. jego model jest zbyt sztywny,
3. wymusza niepotrzebne zależności,
4. nie nadaje się do roli IR,
5. albo Lexon potrzebuje innego poziomu abstrakcji.

**Kompatybilność powinna być preferowana nad kopiowaniem.**

---

# 20. Robocza definicja Lexona

Na obecnym etapie najlepsza robocza definicja brzmi:

> **Lexon is a language-independent, typed, version-aware semantic intermediate representation for formalizing legal norms, their interpretations, temporal validity, provenance, dependencies and implementation mappings.**

Po polsku:

> **Lexon jest niezależną od języka implementacji, typowaną i świadomą wersji semantyczną reprezentacją pośrednią prawa, służącą do formalizacji norm prawnych, ich interpretacji, obowiązywania w czasie, pochodzenia, zależności oraz mapowania na implementacje informatyczne.**

Ta definicja jest robocza i może zostać zmieniona po wykonaniu pierwszego eksperymentu porównawczego.

---

# 21. Stan projektu po tej dyskusji

### Nieustalone

* składnia Lexona,
* pełny AST,
* system typów,
* model deontyczny,
* model temporalny,
* sposób reprezentacji wyjątków,
* model interpretacji,
* sposób generowania kodu,
* zakres automatyzacji.

### Hipotezy

* Lexon powinien być IR, nie tylko DSL.
* Lexon powinien być niezależny od backendu.
* Akoma Ntoso powinno być używane jako warstwa dokumentowa.
* ELI powinno być używane do identyfikacji/metadanych.
* LKIF powinno być źródłem inspiracji ontologicznej.
* LegalRuleML powinno być punktem odniesienia dla semantyki norm.
* Catala powinno być traktowane jako potencjalny backend.
* provenance, temporalność i dependency graph powinny być fundamentalnymi elementami Lexona.

### Następny krok

Przeprowadzić **eksperyment porównawczy na jednym rzeczywistym polskim przepisie** przed rozpoczęciem właściwego projektowania języka.

---

# 22. Meta-zasada dla agenta

Agent pracujący nad projektem powinien zachowywać się bardziej jak architekt kompilatora niż autor kolejnego formatu XML.

Przy każdej decyzji projektowej należy pytać:

```text
Czy to jest:

1. źródło prawa?
2. reprezentacja dokumentu?
3. reprezentacja wiedzy?
4. reprezentacja normy?
5. semantyczny IR?
6. język wykonywalny?
7. backend?
```

Jeżeli dana funkcja należy naturalnie do istniejącej warstwy, należy preferować integrację.

Jeżeli funkcja znajduje się pomiędzy istniejącymi warstwami i nie ma dobrego wspólnego modelu — jest to potencjalne miejsce dla Lexona.
