# Model prawny

STATUS: DRAFT — przykłady z faktycznie zbudowanego modelu, nie
hipotetyczne. Schemat pól (jakie klucze YAML) jest obecnie ad-hoc — patrz
ADR-0002 po redesign do jednolitego schematu. To, co poniżej opisuje,
jest stabilne: *jakie kategorie pojęć rozróżniamy*, nie *jak dokładnie są
zapisane*.

## Entity

Obiekt domeny. Minimalne właściwości potrzebne do reprezentacji prawa
(AGENTS.md sekcja 15).

Przykład (`model/entities/spoldzielnia.yaml`):

```yaml
entity: "Spółdzielnia"
definition:
  source: "PS-ART-001 §1"
  formalization_status: DIRECT
  asserts: [dobrowolne_zrzeszenie, osób, o_nieograniczonej_liczbie, ...]
properties:
  - name: minimum_member_count
    source: "PS-ART-015 §1, §5"
```

Encje żyją w `model/entities/` (współdzielone między aktami) albo
`law/<akt>/ontology/entities/` (specyficzne dla aktu) — patrz
`docs/architecture.md`.

## Relation

Relacje są pierwszorzędne, nie ukryte we właściwościach encji
(PROJECT_CONCEPT.md sekcja 8).

Przykład (`model/relations/member_of.yaml`):

```yaml
relation: "MEMBER_OF"
from: "Członek"
to: "Spółdzielnia"
attributes:
  - name: status
    type: "-> MembershipStatus"
```

Stan (`status`) żyje na relacji, nie na encji `Członek` — bo to, "czy
ktoś jest w tej konkretnej spółdzielni", jest właściwością relacji, nie
osoby.

## State

Maszyna stanów przypisana do relacji lub encji.

Przykład (`law/prawo-spoldzielcze/ontology/states/membership_status.yaml`):
9 stanów (`DECLARED`, `ACTIVE`, `REJECTED`, `WITHDRAWN`,
`PENDING_EXCLUSION`, `EXCLUDED`, `PENDING_STRUCK_OFF`, `STRUCK_OFF`,
`DECEASED`), 12 przejść, każde z eventem-wyzwalaczem.

Stany żyją przy akcie (`law/<akt>/`), nawet jeśli encja jest w `model/` —
patrz uzasadnienie w `docs/architecture.md`.

## Event

Zdarzenie = fakt, który zaszedł. Nie jest normą.

Przykład: `DeclarationSubmitted`, `MemberAdmitted`, `CooperativeRegistered`
— każdy z `payload`, `triggers_transition`, `source`.

## Rule / normative types

Rozróżniamy (AGENTS.md sekcja 20 — nie synonimy):

| Typ | Przykład w repo | Sens |
|---|---|---|
| `DEFINITION` | `R-PS-0007` (Art. 1 §1) | definicja legalna |
| `RIGHT` | `R-PS-0004` (Art. 18 §2) | uprawnienie |
| `OBLIGATION` | `R-PS-0006` (Art. 18 §5) | obowiązek |
| `PROHIBITION` | `R-PS-0005` (Art. 18 §3) | zakaz (tu: INTERPRETATIVE) |
| `PERMISSION` | `R-PS-0008` (Art. 1 §2) | dozwolenie, nie obowiązek |
| `CONDITION` | `R-PS-0001`, `R-PS-0002` (Art. 15) | warunek/kwalifikacja |
| `STRUCTURAL` | `R-PS-0009`, `R-PS-0010` | norma ramowa/organizacyjna |
| `PROCEDURE` | `R-PS-0003`, `R-PS-0012`, `R-PS-0013`, `R-PS-0016` | sekwencja kroków |

`POWER`/`COMPETENCE` (PROJECT_CONCEPT.md sekcja 16) — zdefiniowane
koncepcyjnie, jeszcze nie użyte w żadnej regule (organy są modelowane
minimalnie, patrz `ontology/entities/zarzad.yaml` itd.).

## Procedure

Sekwencja kroków z `precondition`/`postcondition`/`deadline`/rozgałęzieniami.
Najbardziej złożony przykład: `R-PS-0016` (wykluczenie/wykreślenie) — 5
kroków, rozgałęzienie Rada Nadzorcza vs. Walne Zgromadzenie, odroczona
skuteczność (§10).

## Deadline

Nigdy goła liczba (AGENTS.md sekcja 22). Zawsze: `start_event`,
`duration`, `unit`, `type`. Przykład w `R-PS-0003` (miesiąc na uchwałę o
przyjęciu, 2 tygodnie na zawiadomienie).

## Concept (pojęcie nieostre)

`OPEN_TEXTURED`, `requires: INTERPRETATION`. Przykłady: `C-PS-0001`
("rażące niedbalstwo"), `C-PS-0002` ("dobre obyczaje") — obie
`UNRESOLVED`, świadomie nie sprowadzone do warunku boolowskiego.

Decyzja projektowa udokumentowana przy okazji: "wina umyślna" (ta sama
norma, Art. 24 §2) **nie** jest oznaczona jako `OPEN_TEXTURED` — to
ugruntowana doktrynalnie kategoria, nie klauzula generalna. Zapisane w
`normalized/akoma-ntoso/` przy Art. 24 jako uwaga.

## Exception

Nie spłaszczać `"może, jeśli A, chyba że B"` do `if A: allow`
(AGENTS.md sekcja 56). Przykład: Art. 21 (zakaz żądania zwrotu wpłat,
z wyjątkiem wpłat przekraczających wymaganą liczbę udziałów) — wyjątek
zachowany jako osobny fakt, nie wchłonięty w warunek główny.
