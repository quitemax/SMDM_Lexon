# tests/

Testy prawne (GIVEN/WHEN/THEN per reguła), regresyjne i jednostkowe silnika —
patrz PROJECT_CONCEPT.md sekcje 33–35, AGENTS.md sekcje 26–29.

```
unit/        testy komponentów silnika (parser, evaluator, ...)
legal/       testy per reguła/przepis, pozytywne i negatywne
regression/  testy pilnujące, że zmiana jednej reguły nie psuje innych
fixtures/    współdzielone dane testowe (stany, zdarzenia)
```

## `legal/` — zbudowane od 2026-09-29

Schemat: `schema/legal-test.schema.json`. Walidacja: `py schema/validate_tests.py`.
Jeden plik = jeden test `T-PS-NNNN-MM.yaml`, gdzie `NNNN` wskazuje regułę
(`rule: R-PS-NNNN`), a `MM` numeruje testy tej reguły. Struktura zgodna z
AGENTS.md sekcje 26-28: `category: POSITIVE|NEGATIVE|BOUNDARY`,
`given`/`when`/`then` (albo `cases` - lista kilku powiązanych punktów
granicznych pod jednym ID, np. n = minimum-1/minimum/minimum+1, zamiast
rozbijania na osobne pliki).

**Testy nie mają jeszcze silnika, który by je wykonał** (`engine/evaluator/`
jest puste, `docs/decisions/ADR-0003-execution-backend.md`, Phase 3
nierozpoczęta). Każdy plik ma pole `status: SPECIFIED` - opisany, nie
wykonany. `EXECUTED_PASS`/`EXECUTED_FAIL` są zarezerwowane na czas, gdy
Phase 3 faktycznie dostarczy evaluator - nie używać ich przedwcześnie,
żeby nie udawać zweryfikowania, którego nie ma (AGENTS.md sekcja 51).
Wartość tych testów już teraz: (1) wymuszają dokładne przemyślenie
warunków/wyjątków/granic każdej reguły - kilka realnych nieścisłości w
regułach znaleziono właśnie pisząc testy, nie pisząc reguł; (2) są
gotowym, jednoznacznym kontraktem, który przyszły evaluator będzie musiał
spełnić.

`py schema/validate_tests.py` zgłasza też (jako `WARNING`, nie `ERROR`):
reguły bez żadnego testu, i niezgodność między polem `tests:` w pliku
reguły a faktycznymi testami, które się do niej odwołują (`rule:`) - te
dwa pola muszą być aktualizowane razem.

## `unit/`, `regression/`, `fixtures/`

Nadal puste - `unit/` i `regression/` czekają na silnik (Phase 3);
`fixtures/` (współdzielone stany/zdarzenia) czeka, aż testy `legal/`
faktycznie zaczną go potrzebować (na razie każdy test niesie własny
`given` bez potrzeby współdzielenia).
