# DSL

STATUS: DRAFT — konwencja nazewnicza ustalona (Phase 0); składnia
wykonywalna jeszcze nie istnieje (Phase 3).

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
USM  Ustawa o spółdzielniach mieszkaniowych   (nieużywane jeszcze — zarezerwowane)
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
Plik: `law/<akt>/normalized/art-<numer><litera>.yaml` (np. `art-016a.yaml`).

## Minimalna propozycja składni docelowej (Phase 3+)

Bez zmian względem PROJECT_CONCEPT.md sekcja 39 — `ENTITY`, `RELATION`,
`EVENT`, `RULE` jako punkt wyjścia, potem `OBLIGATION`, `RIGHT`,
`PROHIBITION`, `POWER`, `DEADLINE`, `EXCEPTION`, `PROCEDURE`. Nie
projektujemy tu jeszcze konkretnej gramatyki (np. formatu tokenów) — dopóki
model danych (YAML) z Phase 1–2 się nie ustabilizuje na Art. 15–28, każda
przedwczesna decyzja składniowa byłaby zgadywaniem (AGENTS.md sekcja 59).
