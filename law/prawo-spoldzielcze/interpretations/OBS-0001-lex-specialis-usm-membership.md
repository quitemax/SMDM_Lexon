# OBS-0001 — Ustawa o spółdzielniach mieszkaniowych jako lex specialis wobec Art. 16–17 i Art. 24 Prawa spółdzielczego

```yaml
id: OBS-0001
type: OBSERVATION
status: UNRESOLVED
affects:
  - "Prawo spółdzielcze, Art. 16"
  - "Prawo spółdzielcze, Art. 16a"
  - "Prawo spółdzielcze, Art. 17"
  - "Prawo spółdzielcze, Art. 24"
discovered_during: "Porównanie Art. 15-28 Prawa spółdzielczego ze statutem realnej spółdzielni mieszkaniowej (ROADMAP.md, Phase 0)"
```

## FACT (tekst ustawy)

Prawo spółdzielcze przewiduje dla wszystkich spółdzielni jeden ogólny
mechanizm:

- **powstanie członkostwa**: złożenie deklaracji + uchwała organu
  spółdzielni o przyjęciu, podjęta w terminie miesiąca od złożenia
  deklaracji (Art. 16–17),
- **ustanie członkostwa z przyczyn leżących po stronie organizacji**:
  wykluczenie (wina umyślna / rażące niedbalstwo, niezgodność z dobrymi
  obyczajami) albo wykreślenie (niewykonywanie obowiązków statutowych bez
  winy) — Art. 24, z prawem odwołania do walnego zgromadzenia lub
  zaskarżenia do sądu.

## FACT (statut realnej spółdzielni mieszkaniowej)

`external/SMDM_Knowledge_Base/zrodla/md/statut.md`:

- **§ 10 ust. 1** — członkostwo w tej spółdzielni **powstaje z chwilą**
  zdarzeń związanych z prawem do lokalu (nabycie roszczenia o ustanowienie
  spółdzielczego lokatorskiego prawa, nabycie ekspektatywy własności,
  nabycie spółdzielczego własnościowego prawa, zawarcie umowy o
  ustanowienie prawa do lokalu, upływ terminu z art. 15 ust. 4 ustawy usm,
  rozstrzygnięcie sądu/wybór spółdzielni) — **nie** z chwilą uchwały o
  przyjęciu po złożeniu deklaracji w rozumieniu Art. 16 Prawa spółdzielczego.
  Zarząd jedynie **potwierdza** (uchwała deklaratywna) powstałe już z mocy
  prawa członkostwo (§ 10 ust. 1 pkt 7).
- Wyjątek: dla **właściciela lokalu, który nie jest jeszcze członkiem**,
  faktycznie stosowany jest mechanizm bliski Art. 16–17 — deklaracja +
  uchwała Zarządu, tym razem **konstytutywna** (§ 10 ust. 2, pkt 1–5) — z
  odwołaniem do **Rady Nadzorczej** w terminie 14 dni, rozpatrywanym w
  ciągu 3 miesięcy (nie do walnego zgromadzenia, jak sugerowałby domyślny
  tryb Art. 24 § 6 dla wykluczenia — to inna procedura, ale pokazuje, że
  organem, któremu statut powierza sprawy członkowskie w pierwszej
  instancji, jest **Zarząd**, a organem odwoławczym **Rada Nadzorcza**).
- **§ 17** — członkostwo **ustaje** wyłącznie wskutek utraty tytułu prawnego
  do lokalu (wygaśnięcie/zbycie prawa, wygaśnięcie roszczenia) lub śmierci,
  oraz w przypadkach z **art. 24¹ ust. 1 i art. 26 ustawy usm**.
- **§§ 18–24 statutu — całość przepisów, które odpowiadałyby trybowi
  wykluczenia/wykreślenia z Art. 24 Prawa spółdzielczego — są `(skreślony)`.**
  Ta spółdzielnia nie posiada więc statutowego trybu wykluczenia/wykreślenia
  członka w rozumieniu Art. 24 Prawa spółdzielczego.

## INTERPRETATION / klasyfikacja konfliktu

```text
CONFLICT (potencjalny, w sensie zakresu zastosowania, nie sprzeczności treści)

Rule (ogólna):
    Prawo spółdzielcze Art. 16-17 — powstanie członkostwa przez
    deklarację + uchwałę o przyjęciu
    Prawo spółdzielcze Art. 24 — ustanie członkostwa przez
    wykluczenie/wykreślenie

Rule (szczególna, dla spółdzielni mieszkaniowych):
    Ustawa o spółdzielniach mieszkaniowych, Art. 15 — powstanie
    członkostwa ex lege wraz z nabyciem prawa do lokalu
    Ustawa o spółdzielniach mieszkaniowych, Art. 24[1], Art. 26 —
    ustanie członkostwa

Resolution mechanism:
    lex_specialis (ustawa o spółdzielniach mieszkaniowych jest ustawą
    szczególną wobec Prawa spółdzielczego dla spółdzielni mieszkaniowych)

REQUIRES:
    formalizacja Ustawy o spółdzielniach mieszkaniowych (Art. 15, 24[1], 26),
    obecnie poza zakresem (patrz AGENTS.md sekcja 3 — jeden akt/fragment
    naraz). Do czasu tej formalizacji status pozostaje UNRESOLVED, a nie
    automatycznie rozstrzygnięty.
```

## Co to oznacza dla bieżącej formalizacji Art. 15–28

1. Art. 15–28 Prawa spółdzielczego **są nadal poprawnym celem formalizacji**
   — to obowiązujący tekst ogólnej ustawy, punkt odniesienia dla wszystkich
   spółdzielni, w tym rezydualnie dla spółdzielni mieszkaniowych w zakresie,
   którego USM nie reguluje odmiennie (np. Art. 18 prawa/obowiązki, Art.
   19–21 udziały i wpisowe, Art. 25–28 wypłata udziałów, dziedziczenie).
2. Reguły formalizowane z **Art. 16, 16a, 17, 24** muszą mieć jawną adnotację
   `SCOPE_NOTE` wskazującą na OBS-0001 — że dla spółdzielni mieszkaniowej
   zastosowanie tych przepisów jest **ograniczone/wyparte** przez USM Art.
   15, 24¹, 26 w zakresie odpowiednio: powstania i ustania członkostwa
   związanego z prawem do lokalu.
3. **Nie wolno** formalizować Art. 16–17 lub Art. 24 jako "tej samej"
   procedury, którą w rzeczywistości stosuje ta konkretna spółdzielnia —
   byłoby to sprzeczne z FACT ustalonym powyżej i naruszałoby zasadę
   `SOURCE > MODEL` (AGENTS.md sekcja 1).
4. Formalizacja USM Art. 15/24¹/26 to osobne, przyszłe zadanie — dodane do
   `ROADMAP.md`.

## Status

`UNRESOLVED` — brak formalizacji USM. Do rewizji przy formalizacji Ustawy
o spółdzielniach mieszkaniowych.
