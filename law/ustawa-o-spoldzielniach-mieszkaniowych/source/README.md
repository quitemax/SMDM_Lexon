# source/

Tekst źródłowy: `external/SMDM_Knowledge_Base/przepisy-prawne/md/ustawa-o-spoldzielniach-mieszkaniowych.md`
(submodule — nie kopiujemy treści, żeby zachować jedno źródło prawdy i jego wersjonowanie).

## Wersja / stan prawny (FACT)

Ustalone na podstawie
`external/SMDM_Knowledge_Base/przepisy-prawne/README.md` (sekcja "Stan na
26-27.09.2026", tabela "1. Ustrój spółdzielni"):

```yaml
act: "Ustawa o spółdzielniach mieszkaniowych"
act_date: "2000-12-15"
dz_u: "Dz.U. 2026 poz. 889"
text_type: "tekst jednolity"
consolidated_text_as_of: "2026-06-10"
downloaded_around: "2026-09-26/27"
pending_unconsolidated_amendment: null
```

`text_type: "tekst jednolity"` i `pending_unconsolidated_amendment: null` -
wywnioskowane z ogólnej zasady pobierania opisanej w KB README ("dla
każdego aktu szukano najnowszego obowiązującego tekstu jednolitego...
Jeśli po tekście jednolitym istniała już nowelizacja, której jeszcze nie
ujednolicono, pobrano dodatkowo tę nowelizację jako osobny plik") - dla
tego aktu, w odróżnieniu od np. Prawa budowlanego czy ustawy o dozorze
technicznym, **żaden taki osobny plik `-nowelizacja-*` nie istnieje**
(sprawdzone: brak `ustawa-o-spoldzielniach-mieszkaniowych-nowelizacja-*`
w `przepisy-prawne/md/`). Tabela źródłowa nie powtarza słowa "tekst
jednolity" przy tym wierszu wprost (robi to tylko przy niektórych aktach,
np. ustawie o własności lokali) - to nie jest sprzeczność, tylko
niekonsekwentny styl tej samej tabeli, nie inny stan faktyczny.

Konwersja źródłowa: z PDF (nie z HTML - ten akt nie miał dostępnego
tekstu HTML u źródła), własnym skryptem `pdf_to_md.py`, nie modelem AI
(patrz KB README, sekcja "Stan konwersji do Markdown"). Status: **gotowe**
("Gotowe: ... `ustawa-o-spoldzielniach-mieszkaniowych` ..."). Żadna
zidentyfikowana utrata treści przy konwersji tego pliku (w odróżnieniu od
2 innych aktów, gdzie odnotowano utratę `cite-box` - ten problem dotyczy
tylko plików konwertowanych z HTML, nie z PDF).

Submodule pinned commit (`external/SMDM_Knowledge_Base`):
`7fcaed372cbe56f58c3ee4aa1d5fb6eee15b83ee` - ten sam, do którego przypięty
jest `law/prawo-spoldzielcze/source/README.md`; nie zmieniany osobno dla
tego aktu.

Ten `consolidated_text_as_of: 2026-06-10` jest wartością `valid_from` dla
wszystkich jednostek normalizowanych w `../normalized/` i reguł w
`../rules/` formalizowanych na podstawie tego stanu, dopóki nie zostanie
odnotowana nowsza nowelizacja (patrz AGENTS.md sekcja 23) - **inna data
niż `2026-03-23` używana dla Prawa spółdzielczego**, bo to dwa niezależnie
konsolidowane akty; nie zakładać, że mają tę samą datę stanu prawnego.

## Numeracja jednostek - odróżnienie od Prawa spółdzielczego

Ten akt używa tej samej konwencji nawiasu kwadratowego dla artykułów
wstawionych nowelizacją (`Art. 6[1]`, `Art. 8[1]`, `Art. 17[1]`...) jak
Prawo spółdzielcze (`Art. 8[2]`, `Art. 12a`...), ale intensywniej - m.in.
cały Rozdział 2[1] (`Art. 17[1]`-`Art. 17[19]`, 19 artykułów) i Rozdział
1[1] (`Art. 8[1]`-`Art. 8[3]`) to w całości wstawki. Klucz cytowania
`USM-ART-NNN` (patrz `docs/dsl.md`, do zaktualizowania) musi to
odwzorować tak samo, jak już rozwiązano dla `PS-ART-016A` (`docs/provenance.md`).
