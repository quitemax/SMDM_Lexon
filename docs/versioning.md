# Wersjonowanie prawa

STATUS: DRAFT — opisuje stan faktyczny. Poziom reguły (walidacja pola
`validity`) zbudowany 2026-09-28; `AS_OF`/event sourcing nadal
NIEROZPOCZĘTE (Phase 3, patrz niżej).

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

## Poziom reguły (zbudowane od 2026-09-28)

AGENTS.md sekcja 23 dokumentuje wzorzec:

```yaml
validity:
  from: "2026-03-23"
  to: null
```

**Fakt (zmierzony, nie szacowany): 15/15 plików w `rules/`+`procedures/`
ma to pole** — retrofit wykonany przy ADR-0002
(`docs/decisions/ADR-0002-unified-rule-schema.md`), wymuszony teraz przez
`schema/legal-rule.schema.json` (walidacja: `py schema/validate_rules.py`).
Wszystkie 15 mają `from: "2026-03-23"` (ten sam `consolidated_text_as_of`
co poziom aktu) i `to: null` — żadna z formalizowanych jednostek nie ma
udokumentowanej nowelizacji ani daty wygaśnięcia. To wartość odziedziczona
z aktu, nie odrębnie zbadana per-artykuł — jeśli kiedyś okaże się, że
konkretny artykuł miał inną datę wejścia w życie niż konsolidacja całego
tekstu, trzeba to skorygować per plik, a nie zgadywać teraz.

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
