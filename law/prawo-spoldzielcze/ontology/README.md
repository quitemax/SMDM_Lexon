# ontology/

Encje, relacje, stany i zdarzenia domeny Prawa spółdzielczego,
specyficzne dla mechanizmu tego aktu (Art. 1–28) — patrz
PROJECT_CONCEPT.md sekcje 7–10.

**Od 2026-09-28: encje/relacje współdzielone z innymi aktami przeniesione
do `model/`** (Osoba, Spółdzielnia, Członek, Zarząd, RadaNadzorcza,
WalneZgromadzenie, Statut, MEMBER_OF, ORGAN_OF, HAS_STATUTE) —
uzasadnienie w `docs/architecture.md`.

```
entities/    ENTITY  - Deklaracja, Udział
                       (pozostałe w model/entities/)
relations/   RELATION - DECLARES, ADMITTED_BY, EXCLUDED_BY,
                        INHERITS_SHARES_FROM, BENEFICIARY_OF
                        (MEMBER_OF, ORGAN_OF, HAS_STATUTE w model/relations/)
states/      STATE   - cykl życia członkostwa (MembershipStatus) - zostaje
                       tutaj celowo, patrz uzasadnienie niżej
events/      EVENT   - CooperativeRegistered, DeclarationSubmitted,
                       MemberAdmitted, ... (12 razem, patrz plik stanu)
```

Każdy plik niesie `source` (klucz jednostki z `../normalized/`) i
`formalization_status`. Organy (Zarząd, RadaNadzorcza, WalneZgromadzenie —
teraz w `model/entities/`) są modelowane minimalnie — tylko jako podmioty
SUBJECT/POWER występujące w Art. 15-28, bez pełnego ustroju (skład,
kadencja), bo to poza zakresem tego fragmentu (patrz ROADMAP.md,
uzasadnienie wyboru fragmentu, pkt 2).

**Dlaczego `states/`/`events/` zostają tutaj, a nie w `model/`:**
`MembershipStatus` opisuje *mechanizm* Prawa spółdzielczego (deklaracja →
uchwała → członkostwo; wykluczenie/wykreślenie). Wg
`interpretations/OBS-0001-lex-specialis-usm-membership.md` ten mechanizm
jest w praktyce wyparty przez Ustawę o spółdzielniach mieszkaniowych dla
spółdzielni mieszkaniowych (członkostwo powstaje/ustaje ex lege wraz z
prawem do lokalu). Encja `Członek` (kim/czym jest) jest więc współdzielona
(`model/`), ale *jak zmienia się jej status w czasie* zależy od aktu —
USM będzie potrzebować własnej, innej maszyny stanów, nie tej samej.
