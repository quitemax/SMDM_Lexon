# normalized/akoma-ntoso/

Tekst źródłowy ustawy w formacie [Akoma Ntoso](http://www.akomantoso.org/)
(OASIS LegalDocML 3.0), zastępujący poprzednią, ad-hoc reprezentację YAML
(jeden plik na artykuł) — decyzja z 2026-09-28, patrz
`docs/decisions/ADR-0001-akoma-ntoso-eli.md` i `docs/LEXON_CONTEXT.md`
(sekcja 12.1, 18, 19: "nie wymyślaj ponownie istniejących standardów").

## Zawartość

`prawo-spoldzielcze.xml` — **jeden plik na cały akt** (zgodnie z typową
praktyką AKN, w odróżnieniu od poprzedniego podejścia "jeden plik na
artykuł"), obejmujący **Art. 1–59** (Dział I–IV w całości, czyli cały
Tytuł I aż do końca Działu IV — Organy spółdzielni, z rozdziałami: Walne
zgromadzenie, Rada nadzorcza, Zarząd, Przepisy wspólne dla rady i zarządu,
Zebrania grup członkowskich).

Weryfikacja tekstu:

- Art. 1-34: zweryfikowano skryptem 1:1 przeciwko poprzednim 37 plikom
  YAML przed ich usunięciem — 111 jednostek tekstu, 0 rozbieżności.
- Art. 35-59 (Dział IV): zweryfikowano skryptem 1:1 bezpośrednio przeciwko
  tekstowi źródłowemu z Knowledge Base (linia po linii, po usunięciu
  nagłówków/kotwic) — 130 jednostek tekstu, 125 identycznych, 5 różniących
  się wyłącznie usunięciem składni linków Markdown dodanych przez ostatni
  commit KB (np. `[art. 6](#art-6)` → `art. 6`, zgodnie z tym samym
  podejściem co przy Art. 1-34) — **0 rzeczywistych rozbieżności treści**.
  Dział IV zawiera notację `§ 4[1]`-`§ 4[4]` (wstawione paragrafy, zapis
  źródła z nawiasami kwadratowymi zamiast indeksu górnego) - zachowana
  verbatim, eId: `art_35__par_4_1` itd. (podkreślnik zamiast nawiasu, bo
  eId nie może zawierać nawiasów kwadratowych).

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

- Art. 60 i dalej (Dział V, VI — uchylone w całości; Dział VII — Gospodarka
  spółdzielni, i dalsze) — do dodania jako kolejne `<hcontainer name="dzial">`
  w tym samym pliku, dział po dziale, zgodnie z ustalonym tempem.
- Walidacja względem oficjalnego schematu XSD Akoma Ntoso 3.0 — zrobiono
  tylko walidację dobrej formy XML (`xml.etree.ElementTree`) i ręczną
  weryfikację 1:1 przeciwko poprzedniej wersji YAML. Brak zainstalowanego
  walidatora AKN w tym środowisku — odnotowane jako `UNKNOWN`, nie
  przemilczane.
