# Architektura

STATUS: DRAFT — opisuje faktycznie zbudowany system (na dzień 2026-09-28),
nie tylko plan. Aktualizować przy każdej zmianie warstwy.

## Warstwy (stan faktyczny)

```
┌─────────────────────────────────────────────────────────┐
│ 0. ŹRÓDŁO ZEWNĘTRZNE                                     │
│    external/SMDM_Knowledge_Base (git submodule)          │
│    przepisy-prawne/md/*.md, zrodla/md/statut.md itd.     │
└──────────────────────────┬────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ 1. WARSTWA DOKUMENTOWA — Akoma Ntoso + ELI               │
│    law/<akt>/normalized/akoma-ntoso/<akt>.xml            │
│    Jeden plik XML na cały akt. Metadane FRBR/ELI w meta. │
│    Decyzja: ADR-0001-akoma-ntoso-eli.md                  │
│    Status: KOMPLETNA dla Prawo spółdzielcze (249/249     │
│    artykułów, zweryfikowane 1:1 wobec źródła).           │
└──────────────────────────┬────────────────────────────────┘
                           ↓  cytowanie: PS-ART-NNN == eId="art_N"
┌─────────────────────────────────────────────────────────┐
│ 2. WARSTWA SEMANTYCZNA ("Legal IR" w budowie)            │
│    ontology/  (entities, relations, states, events)      │
│    rules/     (RULE/RIGHT/OBLIGATION/PROHIBITION/...)    │
│    procedures/ (PROCEDURE - kroki, warunki, terminy)     │
│    concepts/  (CONCEPT OPEN_TEXTURED - pojęcia nieostre)  │
│    interpretations/ (OBSERVATION, konflikty norm)         │
│                                                            │
│    Status: Prawo spółdzielcze - reguły tylko dla Art.     │
│    1-3, 5-7, 11, 12a, 14-18, 24. Reszta 249 artykułów -   │
│    wyłącznie znormalizowana (warstwa 1), zero semantyki.  │
│                                                            │
│    UWAGA: schemat plików w rules/procedures/ jest         │
│    obecnie ad-hoc (różne pola w różnych plikach) - patrz  │
│    docs/decisions/ADR-0002 (w przygotowaniu) po redesign  │
│    do jednolitego, wymuszonego schematu inspirowanego     │
│    LegalRuleML.                                           │
└──────────────────────────┬────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ 3. SILNIK WYKONAWCZY (engine/) - NIEROZPOCZĘTY (Phase 3) │
│    Kandydaci na backend: własny evaluator (Python) albo   │
│    Catala - do oceny małym spike'em przed decyzją.        │
└──────────────────────────┬────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│ 4. ZAPYTANIA / EXPLAINABILITY - NIEROZPOCZĘTE (Phase 4-6)│
│    WHY/WHAT/CAN/CANNOT, ścieżka RULE → CONDITION → STATE  │
│    → SOURCE, patrz PROJECT_CONCEPT.md sekcja 24-25.       │
└─────────────────────────────────────────────────────────┘
```

## Model warstwowy vs. `docs/LEXON_CONTEXT.md`

Ten dokument (kontekst architektoniczny "Lexon") proponuje docelowo:

```
LEXON LANGUAGE + LEXON AST + LEXON SEMANTIC IR
```

Obecna Warstwa 2 (`ontology/`, `rules/`, `procedures/`, `concepts/`) jest
najbliżej "LEXON LANGUAGE" w wersji roboczej — czytelnej dla człowieka,
ale **bez wymuszonego AST/IR**. To jest świadomie zidentyfikowany dług,
nie przeoczenie — patrz ADR-0002.

## Warstwa 2, rozdzielenie: `model/` vs `law/<akt>/ontology/`

Od 2026-09-28: encje i relacje, które są prawdopodobnie współdzielone
między aktami (Osoba, Spółdzielnia, Członek, Zarząd, RadaNadzorcza,
WalneZgromadzenie, Statut; relacje MEMBER_OF, ORGAN_OF, HAS_STATUTE) żyją
w `model/entities/`, `model/relations/` — nie w `law/prawo-spoldzielcze/`.

Encje i relacje, których kształt jest specyficzny dla konkretnego aktu
(np. Deklaracja i jej wymogi formy z Art. 16 Prawa spółdzielczego, Udział
z Art. 19-21) oraz **stany i zdarzenia** (MembershipStatus i jego 12
zdarzeń — to jest opis *mechanizmu* powstania/ustania członkostwa
according to Prawo spółdzielcze, a mechanizm ten jest wg OBS-0001 wyparty
przez USM dla spółdzielni mieszkaniowych) zostają w
`law/prawo-spoldzielcze/ontology/`.

Zasada: **encja (co to jest) bywa współdzielona; mechanizm (jak to się
zmienia w czasie, wg którego aktu) rzadko jest** — dlatego stany/zdarzenia
domyślnie zostają przy akcie, nawet jeśli encja, do której się odnoszą,
jest w `model/`.

## Provenance (skrót, pełny opis: `docs/provenance.md`)

```
RULE.source.normalized_ref (np. "PS-ART-015")
    ↓
eId="art_15" w normalized/akoma-ntoso/prawo-spoldzielcze.xml
    ↓
<num>Art. 15.</num> + <content><p>tekst źródłowy</p></content>
```

## Mentalny model (bez zmian względem AGENTS.md sekcja 65)

```
SOURCE LAW → PARSER (AKN) → LEGAL IR (w budowie) → FORMAL MODEL →
VALIDATOR (skrypty ad-hoc, nie CI) → RULE ENGINE (brak) → QUERY (brak)
```
