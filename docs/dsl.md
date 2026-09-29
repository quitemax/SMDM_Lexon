# DSL

STATUS: DRAFT dla składni wykonywalnej (Phase 3, jeszcze nie istnieje).
Konwencja nazewnicza (Phase 0) i schemat plików `rules/`/`procedures/`
(niżej, od 2026-09-28) są **STRUCTURAL i wymuszone** — patrz
`schema/legal-rule.schema.json`.

Pełna specyfikacja gramatyki DSL zostanie napisana dopiero przy budowie
parsera (Phase 3, patrz ROADMAP.md). Na razie formalizacje w `law/*/rules/`,
`law/*/ontology/`, itd. są zapisywane jako zwykłe pliki YAML/Markdown zgodne
z poniższą konwencją identyfikatorów i strukturą pól z PROJECT_CONCEPT.md
(sekcje 7–20) — to jest **model danych**, nie jeszcze **język wykonywalny**
(patrz AGENTS.md sekcja 59: prosty jawny model przed skomplikowanym
kompilatorem).

## Konwencja identyfikatorów (AGENTS.md sekcja 38, potwierdzona)

```
R-<AKT>-NNNN     Rule           np. R-PS-0016
E-<AKT>-NNNN     Event          np. E-PS-0001
C-<AKT>-NNNN     Concept        np. C-PS-0001  (pojęcie nieostre)
I-<AKT>-NNNN     Interpretation np. I-PS-0001
OBS-NNNN         Observation    np. OBS-0001   (bez prefiksu aktu — obserwacje
                                                bywają międzyaktowe)
T-<AKT>-NNNN-MM  Test           np. T-PS-0016-01 (MM = numer testu dla reguły)
```

`<AKT>` — skrót aktu, dwie-trzy litery, przypisywane raz i niezmienne:

```
PS   Prawo spółdzielcze
USM  Ustawa o spółdzielniach mieszkaniowych   (od 2026-09-29 w użyciu - patrz law/ustawa-o-spoldzielniach-mieszkaniowych/)
```

Numeracja `NNNN` jest sekwencyjna w obrębie pary (typ, akt) i **nie** jest
przypisywana 1:1 do numeru artykułu — jeden artykuł może dać kilka reguł
(AGENTS.md sekcja 12), a jedna reguła może wymagać kilku artykułów
(AGENTS.md sekcja 13). Powiązanie z artykułem żyje wyłącznie w polu `source`,
nigdy w samym ID.

Encje (`ENTITY`) i relacje (`RELATION`) **nie** dostają numerycznych ID —
są identyfikowane nazwą (np. `Spółdzielnia`, `Członek`, `MEMBER_OF`), zgodnie
z PROJECT_CONCEPT.md sekcja 7–8.

## Klucz jednostki źródłowej (normalized/)

Segmentacja tekstu w `law/<akt>/normalized/` (czysta segmentacja, bez
formalizacji semantycznej) używa klucza czytelnego dla człowieka, osobnego od
powyższych ID reguł:

```
<AKT>-ART-<numer artykułu, wypełniony zerami do 3 cyfr><opcjonalna litera>
```

Przykłady: `PS-ART-015`, `PS-ART-016`, `PS-ART-016A` (Art. 16a).

**Rozszerzenie (2026-09-29, USM):** dla jednostek wstawionych nowelizacją
z numerem w nawiasie kwadratowym BEZ litery (np. `Art. 24[1]`, częste w
Ustawie o spółdzielniach mieszkaniowych), klucz dopisuje wstawkę po
myślniku: `USM-ART-024-1` (Art. 24[1]). Rozwiązywanie do `eId`: usuń
zera wiodące z numeru, zamień `-` na `_`, dodaj prefiks `art_` →
`art_24_1`. Patrz `law/ustawa-o-spoldzielniach-mieszkaniowych/normalized/akoma-ntoso/README.md`.

**Aktualizacja (2026-09-28):** format pliku pod tym kluczem zmienił się z
ad-hoc YAML (jeden plik na artykuł) na **Akoma Ntoso XML** (jeden plik na
cały akt) — patrz `docs/decisions/ADR-0001-akoma-ntoso-eli.md` i
`law/prawo-spoldzielcze/normalized/akoma-ntoso/README.md`. Sam klucz
`PS-ART-NNN` się nie zmienił - teraz odpowiada 1:1 atrybutowi
`eId="art_{numer}"` w pliku `normalized/akoma-ntoso/<akt>.xml`, zamiast
osobnemu plikowi `art-<numer>.yaml`. Żaden z ~60 istniejących plików w
`rules/`, `procedures/`, `ontology/` nie wymagał zmiany dzięki temu, że
klucz cytowania pozostał stabilny (AGENTS.md sekcja 38).

## Schemat plików `rules/`/`procedures/` (od 2026-09-28)

STATUS: **STRUCTURAL, wymuszony.** Do 2026-09-28 pliki w `law/*/rules/` i
`law/*/procedures/` nie miały żadnego wymuszonego wspólnego kształtu poza
konwencją nazewniczą wyżej — audyt repo to zidentyfikował jako blokujące
sensowne testy. Patrz `docs/decisions/ADR-0002-unified-rule-schema.md` dla
pełnego kontekstu (w tym analizy OASIS LegalRuleML, z którego zaczerpnięto
słownictwo pojęciowe — bez przejmowania formatu XML).

Schemat wykonywalny: `schema/legal-rule.schema.json` (JSON Schema 2020-12).
Walidacja: `py schema/validate_rules.py`.

### Rdzeń, wymagany w każdym pliku

| Pole | Typ | Uwagi |
|---|---|---|
| `id` | string | `R-PS-NNNN` |
| `norm_type` | enum | `DEFINITION`\|`CONDITION`\|`RIGHT`\|`OBLIGATION`\|`PROHIBITION`\|`PERMISSION`\|`POWER`\|`COMPETENCE`\|`STRUCTURAL`\|`PROCEDURE` (AGENTS.md sekcja 20) |
| `title` | string | |
| `source.act`, `source.normalized_ref` | string albo lista | lista dla reguł wieloartykułowych (AGENTS.md sekcja 13), np. `R-PS-0003` |
| `source.article`, `source.paragraph` | string albo lista | opcjonalne co do `paragraph` |
| `validity.from`, `validity.to` | data (`to` może być `null`) | **nowe** — czasowa stosowalność normy (AGENTS.md sekcja 23), nie samej formalizacji. Domyślnie = `consolidated_text_as_of` z `law/<akt>/source/README.md`, dopóki nie odnotowano nowelizacji |
| `formalization_status` | enum | `DIRECT`\|`STRUCTURAL`\|`INFERRED`\|`INTERPRETATIVE`\|`UNCERTAIN`\|`CONTESTED` (AGENTS.md sekcja 7) |
| `tests` | lista | może być pusta, dopóki testy nie istnieją |
| `subject` | string | wymagane, **z wyjątkiem** `norm_type: PROCEDURE` |
| `name`, `actors`, `steps` | — | wymagane **tylko dla** `norm_type: PROCEDURE`, zamiast `subject` |

Pola zależne od `norm_type` (`items`, `effect`, `asserts`/`purpose`,
`legal_basis_hierarchy`, `exceptions`, `holder`...) **zostają opcjonalne i
niesplaszczone** — różnice między nimi są semantyczne, nie stylistyczne
(AGENTS.md sekcja 56), schemat ich nie ujednolica na siłę.

### Pola LegalRuleML-inspirowane (opcjonalne, cross-cutting)

- **`strength`**: `STRICT` (domyślne, gdy pole nieobecne) albo
  `DEFEASIBLE`. Odwzorowuje LegalRuleML `StrictStrength`/
  `DefeasibleStrength`. Używać **tylko** gdy reguła (albo jej fragment,
  np. jedna z kilku `grounds` w procedurze) zależy od pojęcia
  `OPEN_TEXTURED` z `concepts/` — patrz `R-PS-0005` (cała reguła) i
  `R-PS-0016.grounds.wykluczenie` (tylko ta podstawa) jako przykłady.
  Zwykłe wyjątki wprost z tekstu ustawy (`exceptions`) **nie** czynią
  reguły `DEFEASIBLE` — to inny mechanizm (enumerowany carve-out, nie
  otwarta ocena okoliczności).
- **`overridden_by`**: lista ID reguł, które mają pierwszeństwo (LegalRuleML
  `Override`). Wypełniać wyłącznie dla udokumentowanego `CONFLICT`
  (AGENTS.md sekcja 31) — nigdy jako domysł. Żaden plik jeszcze go nie ma.

### Walidacja poza JSON Schema

`schema/validate_rules.py` sprawdza dodatkowo (raportowane jako `ERROR` —
blokujące — albo `WARNING` — informacyjne, bo czasem to prawidłowe
odzwierciedlenie tego, że ustawa/statut nie rozstrzyga, np. `R-PS-0003`
`admitting_body` — patrz AGENTS.md sekcja 50):

- duplikaty `id` (`ERROR`),
- `source.normalized_ref` rozwiązywalny do realnego `eId` w
  `normalized/akoma-ntoso/*.xml` (`WARNING`, ta sama logika zera wiodące
  co w `docs/provenance.md`),
- `subject`/`holder`/`actors.*` zawierające nazwę znanej encji z
  `model/entities/` lub `law/<akt>/ontology/entities/` (`WARNING`).

## Minimalna propozycja składni docelowej (Phase 3+)

Bez zmian względem PROJECT_CONCEPT.md sekcja 39 — `ENTITY`, `RELATION`,
`EVENT`, `RULE` jako punkt wyjścia, potem `OBLIGATION`, `RIGHT`,
`PROHIBITION`, `POWER`, `DEADLINE`, `EXCEPTION`, `PROCEDURE`. Nie
projektujemy tu jeszcze konkretnej gramatyki (np. formatu tokenów) — dopóki
model danych (YAML) z Phase 1–2 się nie ustabilizuje na Art. 15–28, każda
przedwczesna decyzja składniowa byłaby zgadywaniem (AGENTS.md sekcja 59).
