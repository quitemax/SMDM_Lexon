# Niepewność i status formalizacji

STATUS: DRAFT — z realnymi przykładami z repozytorium.

## Dwie odrębne skale (nie mylić)

1. **Klasyfikacja stwierdzenia** (AGENTS.md sekcja 6): `FACT` /
   `INFERENCE` / `INTERPRETATION` / `ASSUMPTION` / `UNKNOWN`. Używana w
   rozumowaniu/dyskusji (np. w `ROADMAP.md`, `OBS-0001`), **nie jako pole
   YAML** w regułach.
2. **Status formalizacji reguły** (AGENTS.md sekcja 7): `DIRECT` /
   `STRUCTURAL` / `INFERRED` / `INTERPRETATIVE` / `UNCERTAIN` /
   `CONTESTED`. To **jest** pole YAML (`formalization_status`) na każdej
   regule/procedurze/koncepcie/encji.

## Rozkład w repozytorium (na dzień 2026-09-28)

Zmierzone (nie szacowane):

```
STRUCTURAL:      23 pliki
DIRECT:          19 plików
UNCERTAIN:        2 pliki  (C-PS-0001, C-PS-0002)
INFERRED:         2 pliki  (ExclusionOverturned, StruckOffOverturned)
INTERPRETATIVE:   1 plik   (R-PS-0005)
CONTESTED:        0 plików (jeszcze nie wystąpiło)
```

## Przykład `INTERPRETATIVE`

`rules/R-PS-0005.yaml` (Art. 18 §3 — ograniczenie prawa wglądu do umów):
trzy przesłanki ocenne (`uzasadniona obawa`, `cele sprzeczne z interesem
spółdzielni`, `znaczna szkoda`) oznaczone w polu `open_textured_terms`,
ale **jeszcze nie** przekształcone w osobne pliki `CONCEPT` — bo reguła
nie jest jeszcze testowana. To jest jawnie odnotowane w `note` tej
reguły, nie przemilczane.

## Przykład `UNCERTAIN` (Concept)

`concepts/C-PS-0001.yaml` ("rażące niedbalstwo"), `C-PS-0002.yaml`
("dobre obyczaje"): `type: OPEN_TEXTURED`, `resolution_status: UNRESOLVED`.
Świadomie **nie** sprowadzone do funkcji boolowskiej (AGENTS.md sekcja 9)
— to jest **sukces projektu**, nie porażka (PROJECT_CONCEPT.md sekcja 37).

## Przykład `INFERRED`

`ontology/events/exclusion_overturned.yaml`: zdarzenie nienazwane
wprost w ustawie, wywnioskowane *a contrario* z Art. 24 §10 (który
wylicza tylko przesłanki *skuteczności* wykluczenia — brak którejkolwiek
z nich, przy uwzględnionym odwołaniu, oznacza powrót do `ACTIVE`).
Oznaczone `INFERRED`, nie `DIRECT`, żeby ta różnica siły dowodowej była
widoczna.

## UNKNOWN jawnie zapisany, nie zgadywany

Dwa konkretne przykłady w repo:

- `law/prawo-spoldzielcze/normalized/akoma-ntoso/prawo-spoldzielcze.xml`,
  `lexon:note` przy Art. 125 §1 pkt 2: odesłanie "art. 272" w źródle jest
  niejednoznaczne (dosłowny numer artykułu vs. nierozdzielony zapis
  "art. 27[2]"). Zachowane verbatim + oznaczone `UNKNOWN`.
- `docs/decisions/ADR-0001-akoma-ntoso-eli.md`: numer pozycji Dz.U.
  pierwotnego uchwalenia ustawy (1982 r.) jest `UNKNOWN` — `FRBRWork`
  tymczasowo używa pozycji tekstu jednolitego jako zastępczej.

## Zasada (AGENTS.md sekcja 64, w praktyce)

Gdy do wyboru: ładna, pewna odpowiedź vs. uczciwa z `UNKNOWN` — wybieramy
`UNKNOWN`. Zmierzone powyżej pokazuje, że to nie jest tylko deklaracja —
te przypadki faktycznie istnieją w repo i nie zostały "wygładzone".
