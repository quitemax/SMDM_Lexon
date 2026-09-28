# Wersjonowanie prawa

STATUS: DRAFT — opisuje stan faktyczny, w tym jawnie brakujący element.

## Poziom aktu (zbudowane, działa)

`law/prawo-spoldzielcze/source/README.md` przypina:

```yaml
act: "Prawo spółdzielcze"
dz_u: "Dz.U. 2026 poz. 521"
text_type: "tekst jednolity"
consolidated_text_as_of: "2026-03-23"
```

Ten sam `consolidated_text_as_of` jest w `FRBRExpression` pliku AKN
(`normalized/akoma-ntoso/prawo-spoldzielcze.xml`). Gdy submoduł
`external/SMDM_Knowledge_Base` się aktualizuje, sprawdzamy `git diff` i
odnotowujemy, czy to zmiana kosmetyczna (jak dotąd 2x — dodanie spisu
treści/linków) czy merytoryczna (jeszcze nie wystąpiło) — patrz commity
"Update SMDM_Knowledge_Base submodule".

## Poziom reguły (ZAPLANOWANE, ale **nie zbudowane**)

AGENTS.md sekcja 23 dokumentuje wzorzec:

```yaml
validity:
  from: "2026-03-23"
  to: null
```

**Fakt (zmierzony, nie szacowany): 0 z 15 plików w `rules/`+`procedures/`
ma to pole.** To jest jawnie odnotowany dług, do naprawienia przy
redesignie schematu (ADR-0002) — nie przeoczenie, które ma zostać
przemilczane.

## Zapytania `AS_OF` (NIEROZPOCZĘTE)

PROJECT_CONCEPT.md sekcja 36 przewiduje `AS_OF 2025-06-01` jako typ
zapytania. Nie istnieje żaden silnik, który mógłby to wykonać (Phase 3
nierozpoczęta) — patrz `docs/architecture.md`.

## Event sourcing (model zaprojektowany, nie wykonywany)

`ontology/states/membership_status.yaml` + 12 zdarzeń w
`ontology/events/` są zaprojektowane pod event sourcing (stan = redukcja
historii zdarzeń), zgodnie z AGENTS.md sekcja 25. Nie ma jeszcze
mechanizmu, który faktycznie odtwarzałby stan na podstawie listy
zdarzeń — to jest zadanie Phase 3 (silnik), nie ontologii.

## Nowelizacja jako zmiana modelu, nie edycja w miejscu

AGENTS.md sekcja 53: nie modyfikować historycznej wersji w miejscu. Nie
przetestowane jeszcze w praktyce (żadna nowelizacja merytoryczna nie
wystąpiła w okresie pracy nad tym repo) — zasada jest zapisana, ale nie
ma jeszcze przykładu jej zastosowania do realnej zmiany treści.
