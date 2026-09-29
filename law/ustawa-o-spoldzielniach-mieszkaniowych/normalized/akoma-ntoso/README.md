# normalized/akoma-ntoso/

Tekst źródłowy tej ustawy w formacie Akoma Ntoso, tak samo jak
`law/prawo-spoldzielcze/normalized/akoma-ntoso/` — patrz tamten README
dla pełnego uzasadnienia standardu (ADR-0001) i tabeli mapowania
ogólnej. Tu tylko różnice i to, co specyficzne dla tego aktu i tego
fragmentu.

## Zawartość

`ustawa-o-spoldzielniach-mieszkaniowych.xml` — **fragment, nie cała
ustawa** (w odróżnieniu od Prawa spółdzielczego, gdzie normalizacja
jest kompletna). Zawiera **Art. 1, 2, 3, 15, 24[1], 26** — wybrane, żeby
rozwiązać `OBS-0001` (Prawo spółdzielcze,
`interpretations/OBS-0001-lex-specialis-usm-membership.md`): Art. 1
ust. 7-9 ustala wprost, które przepisy Prawa spółdzielczego się NIE
stosują do spółdzielni mieszkaniowych (wystąpienie/wykluczenie/
wykreślenie, udziały i wpisowe, obowiązek deklaracji), Art. 3 niesie
całą materię członkostwa (kto jest członkiem, kiedy powstaje - ust.
3[2], siedem zdarzeń, kiedy ustaje - ust. 6-7), Art. 15 jest
przepisem pomocniczym cytowanym przez Art. 3 ust. 3[2] pkt 5-6 (termin
roczny dla przypadku śmierci uprawnionego), Art. 24[1] i Art. 26 są
przepisami, do których odsyła Art. 3 ust. 7 jako dodatkowe przesłanki
ustania członkostwa (przejście zarządu nieruchomością na reżim ustawy
o własności lokali).

Weryfikacja: skrypt porównujący 71 jednostek tekstu (linie źródła po
usunięciu numeracji ustępów/punktów i składni linków Markdown) z 71
elementami `<p>` w XML — **71/71 identyczne, 0 rozbieżności**.

## Różnice względem mapowania Prawa spółdzielczego

1. **Brak poziomów Część/Tytuł/Dział.** Ta ustawa ma tylko Rozdział
   bezpośrednio pod `<body>` (`<hcontainer name="rozdzial">`).
2. **Ustępy bez `§`.** Źródło numeruje ustępy gołymi liczbami (`1.`,
   `2.`...), nie `§ 1.` jak Prawo spółdzielcze domyślnie. Zachowane
   verbatim jako `<num>1.</num>` — ten sam wzorzec, co już zastosowano
   dla PS Art. 93b (patrz PS README, sekcja mapowania).
3. **Jednostki wstawione nowelizacją z numerem w nawiasie kwadratowym
   bez litery** (`Art. 24[1]`, `ust. 3[2]`, `pkt 1[1]`) — nowa reguła
   `eId`, nie potrzebna dotąd w PS (tam wstawki miały zawsze literę:
   `Art. 16a`, `§ 4[1]` już używał tego wzorca na poziomie paragrafu).
   Rozszerzenie: nawias zamienia się na podkreślnik na dowolnym
   poziomie (artykuł/paragraf/punkt) — `Art. 24[1]` → `art_24_1`,
   `ust. 3[2]` → `art_3__par_3_2`, `pkt 1[1])` → `art_1__par_2__pkt_1_1`.
4. **Fragment, nie całość** — patrz `lexon:coverage` w pliku XML. Luki
   w numeracji artykułów (np. brak Art. 4-14 między Art. 3 i Art. 15)
   oznaczają "nieznormalizowane", **nie** "uchylone" — to inne pojęcie
   niż luki w kompletnej normalizacji PS, gdzie każda luka jest jawnie
   wyjaśniona (uchylenie/pominięcie). Status `repealed` w tym pliku jest
   używany tylko dla jednostek faktycznie tu obecnych, które źródło
   samo oznacza jako `(uchylony)` (Art. 15 ust. 1, Art. 3 ust. 4, Art. 1
   ust. 2 pkt 1[1]).

Brak przypisów (`lexon:note`/`authorialNote`) w tym fragmencie -
sprawdzone: żaden z sześciu artykułów nie niesie markera przypisu w
źródle (ustawa ma 21 przypisów ogółem, ale żaden nie jest dołączony do
Art. 1, 2, 3, 15, 24[1] ani 26).

## Klucz cytowania `USM-ART-NNN`

Patrz `lexon:citationKey` w pliku XML i `../../source/README.md`.
Analogiczny do `PS-ART-NNN`, z dodatkiem `-{wstawka}` dla jednostek jak
`Art. 24[1]` → `USM-ART-024-1`.

## Czego tu nie ma

- Reszta ustawy (Art. 4-14, 8[1]-8[3], 9[1]-14, 16-17[19], 18-23, 25,
  27-27[4], 28-55) — do znormalizowania w miarę potrzeby przy dalszej
  formalizacji USM, nie teraz.
- Walidacja względem oficjalnego schematu XSD AKN 3.0 — jak w PS, tylko
  dobra forma XML + weryfikacja 1:1 wobec źródła, `UNKNOWN` co do
  zgodności ze schematem.
