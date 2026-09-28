# ADR-0001 — Akoma Ntoso jako format warstwy dokumentowej (`normalized/`), ELI jako wzorzec identyfikatorów

## Context

Projekt zaczął formalizację Prawa spółdzielczego od ad-hoc formatu YAML dla
warstwy `normalized/` (segmentacja tekstu na artykuły/paragrafy/punkty, bez
formalizacji semantycznej) — jeden plik na artykuł, klucz `PS-ART-NNN`.

Po sformalizowaniu Art. 1-34 (Dział I-III) w tym formacie, dyskusja z innym
agentem (zapisana w `docs/LEXON_CONTEXT.md`) postawiła pytanie: czy projekt
nie wymyśla od nowa rozwiązań, które już istnieją jako standardy? Kluczowe
wnioski z tej dyskusji (sekcje 12.1, 12.2, 19):

- **Akoma Ntoso** (OASIS LegalDocML) jest ustalonym standardem
  strukturyzowania dokumentów prawnych — projekt "nie powinien wymyślać
  własnego odpowiednika: article, paragraph, point, reference", tylko
  "umieć konsumować Akoma Ntoso".
- **ELI** (European Legislation Identifier) powinien być używany do
  identyfikacji aktów/wersji zamiast tworzenia konkurencyjnego systemu.
- Zasada projektowa (sekcja 19): "Nie wymyślaj ponownie istniejących
  standardów tylko dlatego, że można je zaprojektować ładniej."

Użytkownik zdecydował się przyjąć tę rekomendację i zastąpić ad-hoc YAML
w `normalized/` prawdziwym Akoma Ntoso + ELI, konwertując od razu całą
dotychczas znormalizowaną treść (Art. 1-34), zamiast najpierw robić mały
eksperyment porównawczy na jednym artykule (mimo że `docs/LEXON_CONTEXT.md`
sekcja 18 rekomendowała to jako pierwszy krok — decyzja świadoma,
odnotowana tu jako odstępstwo).

## Decision

1. **`normalized/` przechodzi z "jeden YAML na artykuł" na "jeden plik
   Akoma Ntoso XML na cały akt"** — `law/<akt>/normalized/akoma-ntoso/<akt>.xml`.
   Zgodne z typową praktyką AKN (dokument = wyrażenie jednej wersji aktu),
   w odróżnieniu od poprzedniego podejścia.
2. **Mapowanie polskiej struktury ustawy na elementy AKN jest naszą
   decyzją projektową**, nie odtworzeniem potwierdzonego oficjalnego
   polskiego profilu (nie znaleziono takiego w naszych źródłach — ISAP nie
   publikuje w AKN). Część→`part`, Tytuł/Dział→`hcontainer` (element
   generyczny, który AKN explicite przewiduje dla struktur specyficznych
   dla jurysdykcji), Artykuł→`article`, §→`paragraph`, punkt→`point`.
   Pełne uzasadnienie w `law/prawo-spoldzielcze/normalized/akoma-ntoso/README.md`.
3. **ELI URI są konstruowane wg standardowego wzorca** (`https://eli.gov.pl/eli/DU/{rok}/{pozycja}`),
   **nie zweryfikowane** wywołaniem sieciowym w tej sesji. Oznaczone jawnie
   jako `CONSTRUCTED`, nie `FACT` (AGENTS.md sekcja 6, 51).
4. **Klucz cytowania `PS-ART-NNN` pozostaje niezmieniony** i teraz
   odpowiada `eId="art_{numer}"` w pliku XML. Istniejące ~60 plików w
   `rules/`, `procedures/`, `ontology/` (referencjonujące `PS-ART-NNN` w
   polu `source.normalized_ref`) **nie zostały zmienione** — zmiana
   formatu warstwy dokumentowej jest przezroczysta dla warstwy semantycznej
   ponad nią.
5. **Warstwy `ontology/`, `rules/`, `procedures/`, `concepts/` (nasza
   dotychczasowa "Lexon Semantic IR" w rozumieniu `docs/LEXON_CONTEXT.md`
   sekcja 3) pozostają na razie bez zmian** — nadal ad-hoc YAML. Ta decyzja
   dotyczy wyłącznie warstwy dokumentowej (odpowiednik "Akoma Ntoso /
   parser" z architektury w `docs/LEXON_CONTEXT.md` sekcja 15), nie
   warstwy semantycznej ("LEXON" właściwy). LegalRuleML jako punkt
   odniesienia dla semantyki norm — **nie przyjęty w tym kroku**, poza
   zakresem tej decyzji.

## Alternatives considered

- **Kontynuować ad-hoc YAML** — odrzucone: prowadzi do wymyślania od nowa
  rozwiązań (segmentacja, referencje, metadane wersji), które AKN już ma,
  wbrew wprost sformułowanej zasadzie projektowej w `docs/LEXON_CONTEXT.md`.
- **Mały eksperyment porównawczy na jednym artykule przed pełną konwersją**
  (rekomendacja `docs/LEXON_CONTEXT.md` sekcja 18) — odrzucone na tym
  etapie na wyraźne życzenie użytkownika; ryzyko: nieodkryte problemy ze
  skalowaniem mapowania AKN mogą ujawnić się dopiero przy Dziale IV i
  dalszych (organy, gospodarka, likwidacja — bardziej złożone struktury
  niż Dział I-III).
- **Pełne przyjęcie LegalRuleML już teraz dla warstwy reguł** — odrzucone
  jako przedwczesne; ten ADR dotyczy tylko warstwy dokumentowej.

## Consequences

- 37 plików `normalized/art-*.yaml` usunięte, zastąpione jednym plikiem
  XML. Zweryfikowano skryptem 1:1 przed usunięciem: 111 jednostek tekstu,
  0 rozbieżności.
- Walidacja XML ograniczona do dobrej formy (`xml.etree.ElementTree`) —
  **brak walidacji względem oficjalnego schematu XSD Akoma Ntoso 3.0**
  w tym środowisku (nie zainstalowano narzędzia). Odnotowane jako
  `UNKNOWN`, nie przemilczane — ryzyko: nasze użycie `hcontainer`/`status`
  może nie być w 100% zgodne ze schematem, mimo że jest zgodne z duchem
  standardu.
- Dalsza normalizacja (Dział IV i kolejne) będzie rozszerzać ten sam plik
  XML, dział po dziale, zamiast tworzyć nowe pliki YAML.
- ELI URI wymagają weryfikacji/korekty, gdy pojawi się dostęp do
  potwierdzenia rzeczywistego adresu w `eli.gov.pl`/ISAP (obecnie
  CONSTRUCTED, nie FACT).
- Ten ADR nie rozstrzyga, czy/kiedy warstwa semantyczna (`ontology/`,
  `rules/`) przejdzie na LegalRuleML lub inny standard z
  `docs/LEXON_CONTEXT.md` — to osobna, przyszła decyzja.

## Status

`ACCEPTED` dla warstwy dokumentowej (`normalized/`). Mapowanie AKN i ELI
oznaczone jako robocze/do weryfikacji w miarę rozszerzania pokrycia na
kolejne działy.
