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
  - "Ustawa o spółdzielniach mieszkaniowych, Art. 3"
  - "Ustawa o spółdzielniach mieszkaniowych, Art. 15"
  - "Ustawa o spółdzielniach mieszkaniowych, Art. 24[1]"
  - "Ustawa o spółdzielniach mieszkaniowych, Art. 26"
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
    Ustawa o spółdzielniach mieszkaniowych, Art. 3 ust. 3[2] —
    powstanie członkostwa ex lege, siedem odrębnych zdarzeń
    (nabycie roszczenia o prawo lokatorskie, nabycie ekspektatywy
    własności, zawarcie umowy o prawo własnościowe/lokatorskie,
    upływ terminu z Art. 15 ust. 4 w przypadku śmierci uprawnionego,
    rozstrzygnięcie sądu/wybór spółdzielni w tym samym przypadku,
    wpis spółdzielni do KRS dla założycieli)
    Ustawa o spółdzielniach mieszkaniowych, Art. 3 ust. 6-7 — ustanie
    członkostwa, sześć zdarzeń wprost (wygaśnięcie/zbycie prawa do
    lokalu, wygaśnięcie roszczenia, rozwiązanie umowy o budowę lokalu)
    plus dwa dodatkowe przypadki odsyłające do Art. 24[1] ust. 1 i
    Art. 26 (przejście na reżim ustawy o własności lokali)

Resolution mechanism:
    lex_specialis (ustawa o spółdzielniach mieszkaniowych jest ustawą
    szczególną wobec Prawa spółdzielczego dla spółdzielni mieszkaniowych)

REQUIRES:
    formalizacja Ustawy o spółdzielniach mieszkaniowych (Art. 1-3, 15,
    24[1], 26), obecnie poza zakresem (patrz AGENTS.md sekcja 3 — jeden
    akt/fragment naraz). Do czasu tej formalizacji status pozostaje
    UNRESOLVED, a nie automatycznie rozstrzygnięty.
```

**KOREKTA (2026-09-29), przy rozpoczęciu formalizacji USM:** ta
obserwacja, zapisana przed przeczytaniem pełnego tekstu USM, cytowała
"Art. 15" jako artykuł, w którym powstaje członkostwo ex lege. Po
faktycznym przeczytaniu tekstu (`external/SMDM_Knowledge_Base/przepisy-prawne/md/ustawa-o-spoldzielniach-mieszkaniowych.md`)
okazuje się to nieprecyzyjne: właściwym przepisem jest **Art. 3 ust.
3[2]** (siedem zdarzeń powodujących powstanie członkostwa). Art. 15
dotyczy węższej kwestii — roszczeń "osób bliskich" o zawarcie umowy po
wygaśnięciu spółdzielczego prawa lokatorskiego wskutek śmierci
uprawnionego — i jest cytowany przez Art. 3 ust. 3[2] pkt 5 tylko jako
źródło terminu (rok) dla TEGO JEDNEGO z siedmiu przypadków, nie jako
główny przepis o powstaniu członkostwa. Podobnie, Art. 24[1] i Art. 26
same w sobie nie stanowią wprost "członkostwo ustaje" — opisują
mechanizm przejścia zarządu nieruchomością na reżim ustawy o własności
lokali (uchwała większości właścicieli, wyodrębnienie ostatniego
lokalu); to **Art. 3 ust. 7** jest przepisem, który czyni z tych
przejść dodatkowe przesłanki ustania członkostwa. AGENTS.md sekcja 52
(konflikt dokumentów - zgłosić, nie ukrywać) i sekcja 60 (zgłaszaj
zauważone nieścisłości) - stąd ta jawna korekta zamiast cichej
poprawki. Nie zmienia to wniosku CONFLICT/lex_specialis powyżej, tylko
precyzuje, które artykuły faktycznie go niosą.

## Co to oznacza dla bieżącej formalizacji Art. 15–28

1. Art. 15–28 Prawa spółdzielczego **są nadal poprawnym celem formalizacji**
   — to obowiązujący tekst ogólnej ustawy, punkt odniesienia dla wszystkich
   spółdzielni, w tym rezydualnie dla spółdzielni mieszkaniowych w zakresie,
   którego USM nie reguluje odmiennie (np. Art. 18 prawa/obowiązki, Art.
   19–21 udziały i wpisowe, Art. 25–28 wypłata udziałów, dziedziczenie).
2. **ZROBIONE (2026-09-29):** `R-PS-0003` i `R-PS-0016` mają teraz
   `scope_note` wskazujący na OBS-0001 (status RESOLVED) i jawne pole
   `references` do konkretnych reguł USM (`R-USM-0002`/`R-USM-0006`/
   `R-USM-0007`/`R-USM-0008`), nie tylko na numery artykułów.
3. **Nie wolno** formalizować Art. 16–17 lub Art. 24 jako "tej samej"
   procedury, którą w rzeczywistości stosuje ta konkretna spółdzielnia —
   byłoby to sprzeczne z FACT ustalonym powyżej i naruszałoby zasadę
   `SOURCE > MODEL` (AGENTS.md sekcja 1).
4. Formalizacja USM Art. 1-3 - **ZROBIONE (2026-09-29)**,
   `law/ustawa-o-spoldzielniach-mieszkaniowych/rules/R-USM-0001..0011`.
   Art. 15, 24[1], 26 znormalizowane (AKN) i cytowane, ale ich własna
   treść poza to, co Art. 3 potrzebuje, jeszcze nie sformalizowana -
   patrz `rules/README.md` tego aktu.

## Status

`RESOLVED` (2026-09-29) — FACT strony USM ustalony poprawnie z tekstu
(patrz KOREKTA wyżej), i rdzeń konfliktu sformalizowany:
`R-USM-0007`/`R-USM-0008` (powstanie/ustanie członkostwa ex lege) oraz
`R-USM-0002`/`R-USM-0003` (wyraźne, ustawowe wyłączenie odpowiednich
przepisów PS) jawnie odsyłają do dysaplikowanych reguł PS
(`R-PS-0003`, `R-PS-0016`, `R-PS-0018`, `R-PS-0020`, `R-PS-0021`,
`R-PS-0022`, `R-PS-0023`) i odwrotnie. Mechanizm rozstrzygania
(lex_specialis) jest teraz wykonalny jako jawna reguła, nie tylko
obserwacja. Nadal otwarte: Art. 15/24[1]/26 mają własną treść poza to,
co Art. 3 cytuje (patrz `rules/README.md` USM) - nie blokuje to
rozwiązania tego konkretnego konfliktu, ale zostaje jako osobny,
dalszy krok formalizacji USM.
