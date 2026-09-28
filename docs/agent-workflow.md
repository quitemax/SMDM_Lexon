# Workflow agenta

STATUS: DRAFT — opisuje workflow faktycznie stosowany przy normalizacji
Prawa spółdzielczego (249 artykułów), nie tylko teoretyczny plan.

## Normalizacja (Warstwa 1, AKN) — praktyka

1. **READ**: przeczytać fragment tekstu źródłowego z submodułu (nie z
   pamięci, nie zgadywać treści).
2. **SEGMENT**: podzielić na jednostki (Część/Tytuł/Dział/Rozdział/
   Oddział/Artykuł/§/punkt), zachowując numerację i luki (artykuły
   uchylone jako tombstone, `status="repealed"`/`"omitted"`).
3. **MAP**: przepisać strukturę na elementy AKN wg ustalonego mapowania
   (`normalized/akoma-ntoso/README.md`) — nie wymyślać nowego mapowania
   ad-hoc dla każdego fragmentu.
4. **PRESERVE FOOTNOTES**: sprawdzić, czy fragment niesie przypisy
   źródłowe (`[N)]` w tekście) — jeśli tak, zachować jako `<lexon:note>`
   lub `<authorialNote>`, nigdy pominąć.
5. **VERIFY 1:1**: napisać/uruchomić skrypt porównujący tekst wyekstrahowany
   z nowego XML z tekstem źródłowym, linia po linii, po odrzuceniu
   linków Markdown. Zero tolerancji dla nieprzeanalizowanych rozbieżności
   — każda musi być wyjaśniona (link Markdown / przypis / prawdziwy błąd).
6. **COMMIT** małym, samodzielnym commitem z liczbami z kroku 5 w opisie.

To jest **rzeczywiście wykonane** 8 razy przy budowie
`normalized/akoma-ntoso/prawo-spoldzielcze.xml` (patrz historia commitów
i `ROADMAP.md`) — nie jest to hipotetyczny proces.

## Formalizacja (Warstwa 2, semantyka) — praktyka

1. Przeczytać znormalizowaną jednostkę (AKN, nie tekst źródłowy z pamięci).
2. Zidentyfikować: podmioty → encje (czy już istnieją w `model/` lub
   `law/<akt>/ontology/entities/`? nie duplikować bez powodu).
3. Zidentyfikować normy: definicja / warunek / prawo / obowiązek / zakaz
   / dozwolenie / procedura — jedna jednostka źródłowa może dać kilka
   reguł (AGENTS.md sekcja 12); jedna reguła może wymagać kilku jednostek
   (AGENTS.md sekcja 13).
4. Zidentyfikować pojęcia nieostre — nie sprowadzać do warunku
   boolowskiego, utworzyć `CONCEPT` albo przynajmniej `open_textured_terms`
   na regule z notatką, że `CONCEPT` jeszcze nie utworzony.
5. Sprawdzić krzyżowo z innymi już sformalizowanymi jednostkami — czy
   ta norma odsyła do/jest odsyłana przez coś już istniejącego (np.
   `R-PS-0011` ↔ `R-PS-0003`/`R-PS-0016`, `R-PS-0031` ↔ statut realnej
   spółdzielni → `OBS-0001`). Nie formalizować w izolacji.
6. Nadać `id` z właściwej sekwencji (`docs/dsl.md`), `source.normalized_ref`,
   `formalization_status`, `validity` (domyślnie `consolidated_text_as_of`
   z `law/<akt>/source/README.md`, chyba że wiadomo inaczej).
7. **Zbudowane od 2026-09-28:** uruchomić `py schema/validate_rules.py`
   przed commitem — 0 `ERROR` jest warunkiem koniecznym (schemat,
   `docs/decisions/ADR-0002-unified-rule-schema.md`); `WARNING` przeczytać
   i albo poprawić, albo potwierdzić, że odzwierciedla prawdziwą
   nieostrość źródła (nie zgadywać, żeby uciszyć ostrzeżenie). Pisanie
   testu (`T-PS-NNNN-MM`) — wciąż nie wykonane systematycznie, plan:
   po ustabilizowaniu schematu.

## Co odróżnia "zrobione" od "wygląda zrobione"

Konkretne kryterium używane w tym repo: **skrypt, nie wrażenie**.
Każde twierdzenie "zgodne z źródłem" w tym repo jest poparte wynikiem
skryptu porównującego (liczba jednostek tekstu, liczba identycznych,
wyjaśnienie każdej rozbieżności) — nie deklaracją "sprawdziłem, wygląda
dobrze". Jeśli narzędzie nie zadziałało lub weryfikacja nie została
wykonana, stan to `SOURCE_VERIFICATION_PENDING` (AGENTS.md sekcja 51),
nie milczące założenie, że jest OK.

## Role agentów (PROJECT_CONCEPT.md sekcja 53) — status

Nie zaimplementowane jako osobne, wyspecjalizowane persony/skrypty —
dotychczasowa praca robiona przez jednego agenta ogólnego wykonującego
sekwencyjnie role Source/Ontology/Rule/Reviewer opisane koncepcyjnie.
Rozdzielenie na osobne role ma sens dopiero przy większej skali/równoległej
pracy wielu agentów — nie jest to teraz priorytetem.
