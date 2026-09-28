# ontology/

Encje, relacje, stany i zdarzenia domeny Prawa spółdzielczego w zakresie
Art. 1–28 (definicja, zakładanie, statut, członkostwo) — patrz
PROJECT_CONCEPT.md sekcje 7–10.

```
entities/    ENTITY  - Osoba, Spółdzielnia (pełna definicja z Art. 1),
                       Statut, Członek, Deklaracja, Udział,
                       Zarząd, RadaNadzorcza, WalneZgromadzenie
relations/   RELATION - HAS_STATUTE, MEMBER_OF, ORGAN_OF, DECLARES,
                        ADMITTED_BY, EXCLUDED_BY, INHERITS_SHARES_FROM,
                        BENEFICIARY_OF
states/      STATE   - cykl życia członkostwa (MembershipStatus)
events/      EVENT   - CooperativeRegistered, DeclarationSubmitted,
                       MemberAdmitted, ... (12 razem, patrz plik stanu)
```

Każdy plik niesie `source` (klucz jednostki z `../normalized/`) i
`formalization_status`. Organy (Zarząd, RadaNadzorcza, WalneZgromadzenie) są
modelowane minimalnie — tylko jako podmioty SUBJECT/POWER występujące w
Art. 15-28, bez pełnego ustroju (skład, kadencja), bo to poza zakresem tego
fragmentu (patrz ROADMAP.md, uzasadnienie wyboru fragmentu, pkt 2).
