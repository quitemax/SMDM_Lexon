# law/

Formalizowane akty prawne, jeden katalog per akt (slug zgodny z nazewnictwem
w `external/SMDM_Knowledge_Base/przepisy-prawne/md/`).

Struktura każdego aktu (patrz PROJECT_CONCEPT.md, sekcja 38):

```
<akt>/
    source/           tekst źródłowy (odwołanie do external/, nie kopia)
    normalized/       tekst podzielony na jednostki (artykuł/§/pkt) ze stabilnymi ID
    ontology/         encje i relacje domeny
    rules/            formalne reguły (RULE/OBLIGATION/RIGHT/PROHIBITION/POWER/...)
    procedures/       procedury jako grafy kroków
    concepts/         pojęcia nieostre (OPEN_TEXTURED) wymagające interpretacji
    interpretations/  jawnie oznaczone interpretacje i konflikty norm
```

Pierwszy domenowy eksperyment: `prawo-spoldzielcze/` (kompletnie
znormalizowany, Dział III w pełni sformalizowany z regułami i testami).

Drugi akt (od 2026-09-29): `ustawa-o-spoldzielniach-mieszkaniowych/` —
sfragmentowana normalizacja (Art. 1, 2, 3, 15, 24[1], 26), wybrana
celowo do rozwiązania `OBS-0001` (Prawo spółdzielcze,
`interpretations/OBS-0001-lex-specialis-usm-membership.md`) - ustalenia,
że ta ustawa jest lex specialis wobec Prawa spółdzielczego dla
spółdzielni mieszkaniowych w zakresie powstania/ustania członkostwa.
