# normalized/akoma-ntoso/

Tekst źródłowy ustawy w formacie [Akoma Ntoso](http://www.akomantoso.org/)
(OASIS LegalDocML 3.0), zastępujący poprzednią, ad-hoc reprezentację YAML
(jeden plik na artykuł) — decyzja z 2026-09-28, patrz
`docs/decisions/ADR-0001-akoma-ntoso-eli.md` i `docs/LEXON_CONTEXT.md`
(sekcja 12.1, 18, 19: "nie wymyślaj ponownie istniejących standardów").

## Zawartość

`prawo-spoldzielcze.xml` — **jeden plik na cały akt** (zgodnie z typową
praktyką AKN, w odróżnieniu od poprzedniego podejścia "jeden plik na
artykuł"), obejmujący **Art. 1–112** (Dział I–XI w całości — Tytuł I do
końca Działu XI, Podział spółdzielni).

Weryfikacja tekstu (wszystkie partie zweryfikowane skryptem, 0 rzeczywistych
rozbieżności treści):

- Art. 1-34: 1:1 przeciwko poprzednim 37 plikom YAML przed ich usunięciem
  — 111 jednostek tekstu, 0 rozbieżności.
- Art. 35-59 (Dział IV): 1:1 bezpośrednio przeciwko tekstowi źródłowemu z
  Knowledge Base — 130 jednostek tekstu, 125 identycznych, 5 różniących
  się wyłącznie usunięciem składni linków Markdown dodanych przez commit
  KB (np. `[art. 6](#art-6)` → `art. 6`). Zawiera notację `§ 4[1]`-`§ 4[4]`
  (wstawione paragrafy, zapis źródła z nawiasami kwadratowymi zamiast
  indeksu górnego) zachowaną verbatim, eId: `art_35__par_4_1` itd.
  (podkreślnik zamiast nawiasu, bo eId nie może zawierać nawiasów
  kwadratowych).
- Art. 60-90 (Dział V, VI — uchylone w całości, bez artykułów; Dział VII):
  1:1 przeciwko źródłu — 36 jednostek tekstu, 35 identycznych, 1 różniąca
  się tym samym wzorcem usuniętego linku Markdown. Zawiera jeden artykuł
  ze statusem innym niż "uchylony": **Art. 83 = `status="omitted"`**
  (źródło: "(pominięty)", nie "(uchylony)") — świadomie odróżnione, bo to
  inne pojęcie prawne (numer pominięty przy numeracji, nie przepis
  uchylony) - patrz sekcja "Decyzje mapowania" niżej.
- Art. 91-102 (Dział VIII — Lustracja, IX — Łączenie się spółdzielni): 1:1
  przeciwko źródłu — 52 jednostki tekstu, 50 identycznych, 2 różniące się
  tym samym wzorcem usuniętego linku Markdown. Dział VIII zawiera dalsze
  wstawione paragrafy (`§ 1[1]`, `§ 1[2]`, `§ 2[1]`, `§ 4[1]`) oraz
  Art. 93b, którego źródło numeruje ustępy jako gołe `1.`/`2.`/`3.`/`4.`
  (bez `§`) — zachowane verbatim jako `<num>1.</num>` itd., nie
  ujednolicone do `§ 1.` (AGENTS.md sekcja 30: nie "naprawiaj" tekstu
  źródłowego nawet dla spójności notacji).
- Art. 103-112 (Dział X — uchylony w całości, bez artykułów; Dział XI —
  Podział spółdzielni): 1:1 przeciwko źródłu — 28 jednostek tekstu, 23
  identycznych, 5 różniących się tym samym wzorcem usuniętego linku
  Markdown. **Znalezisko:** Art. 108a niesie w źródle przypis `[2)]`
  przy numerze artykułu - to nie link, tylko marker przypisu. Treść
  przypisu (sekcja "Przypisy" na końcu pliku źródłowego) mówi, że artykuł
  był uchylony od 2003-01-15, ale **to uchylenie utraciło moc 2005-04-28
  na mocy wyroku Trybunału Konstytucyjnego (sygn. K 42/02)** - czyli
  artykuł od tamtej pory znów obowiązuje. To realny, znaczący przykład
  złożonej historii legislacyjnej (temporalność, o której mówi
  `docs/LEXON_CONTEXT.md` sekcja 10), więc **zachowany jawnie**, nie
  pominięty - jako `<lexon:note marker="2)" type="legislative-history">`
  dołączony do `<article eId="art_108a">`, w naszej przestrzeni nazw (AKN
  nie ma oczywistego kanonicznego miejsca na przypis przywiązany do całego
  artykułu, a nie do fragmentu tekstu - `authorialNote` jest elementem
  inline). Sprawdzone: to jedyny taki przypis w całej dotąd
  skonwertowanej części ustawy (Art. 1-112).

## Decyzje mapowania (własne, nie zweryfikowane wobec oficjalnego polskiego profilu AKN)

Nie znaleziono w naszych źródłach potwierdzonego, oficjalnego polskiego
profilu Akoma Ntoso (ISAP/Sejm nie publikują aktów w AKN — działają na
PDF/HTML/RTF). Poniższe mapowanie struktury polskiej ustawy jest więc
**naszą decyzją projektową** (AGENTS.md sekcja 57), a nie odtworzeniem
istniejącego standardu:

| Polska struktura | Element AKN                      | Uzasadnienie |
|---|---|---|
| Część           | `<part>`                          | kanoniczny element hierarchiczny AKN |
| Tytuł           | `<hcontainer name="tytul">`       | AKN nie ma jednoznacznie potwierdzonego, bezpiecznego kanonicznego elementu hierarchicznego dla tego poziomu — użyto generycznego `hcontainer`, który standard wprost przewiduje dla struktur specyficznych dla jurysdykcji |
| Dział           | `<hcontainer name="dzial">`       | jw. |
| Artykuł         | `<article>`                       | kanoniczny |
| §               | `<paragraph>`                     | kanoniczny |
| punkt (1), 2)…) | `<point>` w `<list>`               | kanoniczny |
| (uchylony)      | atrybut `status="repealed"` + zachowany tekst `(uchylony)` w `<p>` | AKN's standardowy atrybut statusu; tekst zachowany dla wierności źródłu (AGENTS.md sekcja 30) |
| (pominięty)     | atrybut `status="omitted"` (Art. 83) | Odróżnione od "uchylony" - to inne pojęcie (numer pominięty w numeracji, nie przepis, który obowiązywał i został uchylony). Wartość własna, `status` w AKN jest słownikiem otwartym. |
| dział w całości uchylony (Dział V, VI) | `<hcontainer status="repealed">` bez żadnych `<article>` | Wierne odwzorowanie źródła - w tekście źródłowym Art. 60-66 nie istnieją nawet jako pojedyncze jednostki "(uchylony)" (inaczej niż np. Art. 4, 8, 9...) - tekst przechodzi wprost z Art. 59 (koniec Działu IV) do nagłówków "Dział V. (uchylony)" / "Dział VI. (uchylony)" bez treści, po czym Dział VII zaczyna się od Art. 67. Luka w numeracji (60-66) jest więc odwzorowana na poziomie działu, nie artykułu - zgodnie z tym, jak faktycznie wygląda źródło, a nie wg naszej własnej konwencji z innych działów. |
| ustęp numerowany bez `§` (Art. 93b: `1.`/`2.`/`3.`/`4.`) | `<paragraph>` z `<num>1.</num>` (bez `§`) | To nadal strukturalnie ten sam poziom co `§`, ale zapisany w źródle inną notacją (styl "ust." typowy dla nowszych, unijno-implementacyjnych przepisów) - zachowane verbatim zamiast ujednolicone do `§ N.`, żeby nie "poprawiać" tekstu źródłowego (AGENTS.md sekcja 30). |
| przypis dołączony do całego artykułu (Art. 108a: `[2)]`) | `<lexon:note marker="..." type="legislative-history">` (nasza przestrzeń nazw) | AKN ma `authorialNote` dla przypisów w treści tekstu (inline), ale nie oczywisty kanoniczny element na przypis dotyczący całego artykułu jako takiego. Zamiast zgadywać/naciągać AKN, użyto już istniejącej własnej przestrzeni `lexon:` (ta sama, co w `<meta><proprietary>`), z jawnym `type` opisującym charakter przypisu. |

`eId` używa schematu `art_{numer}[__par_{numer}[__pkt_{numer}]]`, np.
`art_24__par_10__pkt_2`.

## Klucz cytowania `PS-ART-NNN`

Istniejący klucz `PS-ART-NNN` używany w `../../rules/`, `../../procedures/`,
`../../ontology/` (pole `source.normalized_ref`) **nie został zmieniony** —
odpowiada teraz 1:1 atrybutowi `eId="art_{numer}"` w tym pliku XML, zamiast
osobnemu plikowi YAML. Np. `PS-ART-015` = `eId="art_15"`. Decyzja: nie
przepisywać ~60 istniejących plików reguł/ontologii tylko dlatego, że
zmienił się format warstwy dokumentowej (AGENTS.md sekcja 36 — zasada
minimalnej zmiany; sekcja 38 — ID nie zmienia się z powodu zmiany formatu
pliku).

## ELI (European Legislation Identifier)

Metadane `FRBRWork`/`FRBRExpression`/`FRBRManifestation` w `<meta>` używają
URI w formie `https://eli.gov.pl/eli/DU/2026/521`, zgodnej ze standardowym
wzorcem polskiego ELI. **Status: CONSTRUCTED, nie zweryfikowany** wywołaniem
sieciowym względem `eli.gov.pl`/ISAP w tej sesji — patrz pole
`lexon:eliStatus` w `<proprietary>` wewnątrz pliku XML po pełne
zastrzeżenia, w tym: numer pozycji Dziennika Ustaw z pierwotnego
uchwalenia (1982 r.) jest `UNKNOWN` (nieustalony w naszych źródłach — nie
zgadywany), więc `FRBRWork` tymczasowo ponownie używa pozycji tekstu
jednolitego (2026 poz. 521) jako zastępczego zakotwiczenia identyfikatora.

## Czego tu nie ma (jeszcze)

- Art. 113 i dalej (Dział XII — Likwidacja, XIII — Upadłość, i dalej
  Tytuł II oraz Część II, III) — do dodania jako kolejne
  `<hcontainer name="dzial">` w tym samym pliku, dział po dziale.
- Walidacja względem oficjalnego schematu XSD Akoma Ntoso 3.0 — zrobiono
  tylko walidację dobrej formy XML (`xml.etree.ElementTree`) i ręczną
  weryfikację 1:1 przeciwko poprzedniej wersji YAML. Brak zainstalowanego
  walidatora AKN w tym środowisku — odnotowane jako `UNKNOWN`, nie
  przemilczane.
