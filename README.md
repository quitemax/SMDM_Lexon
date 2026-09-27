# LEGAL-CODE (SMDM_Lexon)

Formalizacja prawa jako wykonywalnego, audytowalnego modelu reguł.
Pierwszy domenowy eksperyment: polskie **Prawo spółdzielcze**, w kontekście
faktycznej spółdzielni mieszkaniowej.

Zanim zaczniesz pracować w tym repozytorium (człowiek lub agent AI),
przeczytaj w tej kolejności:

1. [`PROJECT_CONCEPT.md`](PROJECT_CONCEPT.md) — koncepcja i architektura projektu.
2. [`AGENTS.md`](AGENTS.md) — obowiązujące zasady pracy agentów AI w tym repozytorium.
3. [`ROADMAP.md`](ROADMAP.md) — aktualne cele i najbliższe kroki.

Najważniejsza zasada projektu:

```
SOURCE > MODEL
MODEL > GUESS
```

Jeżeli czegoś nie da się ustalić na podstawie źródła, model mówi `UNKNOWN` —
nigdy nie zgaduje.

## Struktura repozytorium

```
PROJECT_CONCEPT.md   koncepcja / blueprint
AGENTS.md            instrukcje dla agentów AI
ROADMAP.md           cele i kolejne kroki

docs/                dokumentacja architektury, DSL, provenance, wersjonowania
law/                 formalizacja per akt prawny (pierwszy: prawo-spoldzielcze/)
model/               warstwa modelu wspólna dla wielu aktów (entities/relations/events/states/rules)
engine/              parser, evaluator, stan, zapytania, provenance (jeszcze nie rozpoczęte)
tests/               testy prawne, jednostkowe, regresyjne
agents/              zakres i zasady pracy per rola agenta (extraction/formalization/validation/review)
examples/            end-to-end scenariusze demonstracyjne
external/            zewnętrzne repozytoria źródłowe (submoduły)
```

## Źródła prawa

Teksty aktów prawnych i dokumenty konkretnej spółdzielni (statut, regulaminy)
znajdują się w osobnym repozytorium
[`SMDM_Knowledge_Base`](https://github.com/quitemax/SMDM_Knowledge_Base),
podlinkowanym tutaj jako git submodule w `external/SMDM_Knowledge_Base`.

Nie kopiujemy treści aktów do tego repozytorium — `law/<akt>/source/`
zawiera tylko odwołanie do pliku w submodule. Dzięki temu jest jedno źródło
prawdy, a każda formalizacja może wskazać dokładną, przypiętą wersję tekstu
(patrz `AGENTS.md`, sekcje 23, 53).

Klonowanie razem z submodułem:

```
git clone --recurse-submodules https://github.com/quitemax/SMDM_Lexon.git
```

lub, jeśli repo jest już sklonowane:

```
git submodule update --init --recursive
```

## Status

Projekt jest na etapie **Phase 0 (research)** — patrz `ROADMAP.md`. Nie ma
jeszcze działającego parsera, evaluatora ani sformalizowanej żadnej reguły.
