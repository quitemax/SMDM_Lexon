# ROADMAP

> Ten plik jest żywym dokumentem. Aktualizuj go po zamknięciu każdego celu i
> gdy zmienia się priorytet. Fazy pochodzą z `PROJECT_CONCEPT.md` (sekcja 52),
> tu są rozbite na konkretne, sprawdzalne zadania osadzone w realnym materiale
> źródłowym z `external/SMDM_Knowledge_Base`.

Status ogólny: normalizacja w formacie Akoma Ntoso XML
(`normalized/akoma-ntoso/prawo-spoldzielcze.xml`, patrz
`docs/decisions/ADR-0001-akoma-ntoso-eli.md`) — aktualny zasięg zawsze w
`lexon:coverage` tego pliku (jedno źródło prawdy, nie duplikowane tu, bo
przy tempie "po kilka działów naraz" ten opis szybko się rozjeżdżał).
**Reguły/procedury sformalizowane tylko dla Art. 1-3, 5-7, 11, 12a,
14-18, 24** (Art. 4, 8-10, 12, 13, 33, 34 uchylone) — cała reszta
znormalizowanego materiału (Działy IV, VII-IX, XI-XIII, Tytuł II Dział I)
jest **wyłącznie znormalizowana, bez żadnych reguł**. **Żadna reguła nie
ma jeszcze testu.**

**Decyzja (2026-09-28):** dokończyć normalizację całej ustawy (249
artykułów), nie tylko Tytułu I - mimo że Tytuł II/Część II-III nie
dotyczą bezpośrednio spółdzielni mieszkaniowej. Tempo: kilka działów
naraz (ostatnio trzy).

**Zwrot architektoniczny (2026-09-28):** patrz `docs/LEXON_CONTEXT.md` i
`docs/decisions/ADR-0001-akoma-ntoso-eli.md`. Warstwa dokumentowa
(`normalized/`) przeszła z ad-hoc YAML na Akoma Ntoso + wzorzec ELI, żeby
nie wymyślać od nowa istniejących standardów. Warstwa semantyczna
(`ontology/`, `rules/`, `procedures/`, `concepts/`) na razie **bez zmian**
- to osobna, nierozstrzygnięta jeszcze decyzja (LegalRuleML jako możliwy
przyszły punkt odniesienia, nie przyjęty).

------------------------------------------------------------------------

## Decyzja: pierwszy fragment do formalizacji

**Wybrany fragment:** Ustawa Prawo spółdzielcze, **Dział III — Członkowie,
ich prawa i obowiązki**, **Art. 15–28** (14 artykułów).

Źródło: `external/SMDM_Knowledge_Base/przepisy-prawne/md/ustawa-prawo-spoldzielcze.md`.

**FACT** — zakres tego działu obejmuje:

- Art. 15 — kto może być członkiem, minimalna liczba członków.
- Art. 16, 16a — deklaracja członkowska, dziedziczenie udziałów.
- Art. 17 — przyjęcie w poczet członków (organ właściwy, termin, tryb,
  odwołanie od odmowy).
- Art. 18 — prawa i obowiązki członka.
- Art. 19–21 — udziały, wpisowe, odpowiedzialność za straty, zwrot wpłat.
- Art. 22 — wystąpienie za wypowiedzeniem.
- Art. 24 — wykluczenie / wykreślenie (organ właściwy, odwołanie, sąd,
  skuteczność).
- Art. 25–28 — ustanie członkostwa wskutek śmierci, wypłata udziałów.

**Dlaczego ten fragment (uzasadnienie wyboru):**

1. Wielkość zgodna z rekomendacją PROJECT_CONCEPT.md sekcja 3
   (kilkanaście–kilkadziesiąt artykułów, tu: 14).
2. Jest samodzielny semantycznie — da się go sformalizować bez konieczności
   wcześniejszego opracowania organów spółdzielni (Zarząd, Rada Nadzorcza
   pojawiają się tu tylko jako SUBJECT/POWER, nie trzeba ich w pełni
   modelować).
3. Zawiera reprezentatywny przekrój typów norm z PROJECT_CONCEPT.md:
   DEFINITION (Art. 15), OBLIGATION (Art. 19 — wniesienie wpisowego),
   PROCEDURE (Art. 17 — przyjęcie, Art. 24 — wykluczenie/wykreślenie z
   odwołaniem i terminami sądowymi), RIGHT (Art. 18), DEADLINE (terminy w
   Art. 17 §3, Art. 24 §5/§6/§9), EXCEPTION (np. Art. 21 wyjątek od zakazu
   żądania zwrotu wpłat) oraz co najmniej jedno pojęcie nieostre wprost w
   tekście: **"rażące niedbalstwo"** i **"dobre obyczaje"** (Art. 24 §2) —
   dobry, wczesny test na OPEN_TEXTURED (patrz PROJECT_CONCEPT.md sekcja 20).
4. Ma odpowiednik w realnym materiale organizacyjnym spółdzielni, co pozwala
   od razu skonfrontować formalny model z praktyką (patrz niżej):
   - `zarzad/przyjmowanie-w-poczet-czlonkow.md` (procedura wewnętrzna, 72
     linie) — bezpośredni odpowiednik Art. 16–17.
   - `zrodla/md/regulamin-przyjmowania-w-poczet-czlonkow-ustanawiania-praw-do-lokali-i-zamiany-mieszkan.md`
     (276 linii) — konkretyzacja statutowa trybu przyjęcia.
   - `zrodla/md/statut.md` — powinien wskazywać organ właściwy do przyjęcia
     (Art. 17 §4) oraz przyczyny wykluczenia/wykreślenia (Art. 24 §2–3) —
     **do zweryfikowania jako pierwszy krok pracy**, nie założone z góry.

**UNKNOWN (do ustalenia jako pierwszy krok, nie zgadywać):**

- Dokładna wersja/data stanu prawnego ustawy przypięta w submodule (do
  odczytania z metadanych aktu / `przepisy-prawne/README.md` w Knowledge Base).
- Czy `zrodla/md/statut.md` tej konkretnej spółdzielni faktycznie wskazuje
  Zarząd czy Radę Nadzorczą jako organ właściwy do przyjęcia — art. 17 §4
  pozostawia to statutowi.

------------------------------------------------------------------------

## Rozszerzenie normalizacji: Art. 1-14 (Dział I i II)

**Decyzja (2026-09-28):** na prośbę o normalizację "od początku" ustawy,
zamiast całych 249 artykułów naraz (co kłóciłoby się z AGENTS.md sekcja 3),
uzgodniono węższy, wciąż sensowny krok: dociągnąć normalizację do Art. 1
wstecz, czyli objąć całe Działy I-II, bezpośrednio poprzedzające już
sformalizowany Dział III.

**Zrobione:**

- [x] Znormalizowano Art. 1–14 (16 plików: 1,2,3,4,5,6,7,8,8a,9,10,11,12,12a,
      13,14 — w tym 7 artykułów/paragrafów uchylonych, zachowanych jako
      tombstone) w `law/prawo-spoldzielcze/normalized/`. Razem z Art. 15-28
      daje to pełne, ciągłe pokrycie normalizacyjne Art. 1-28.
- [x] Walidacja YAML tych 16 plików skryptem (jak dla Art. 15-28) — OK.
- [x] Zaktualizowano submoduł `external/SMDM_Knowledge_Base` do najnowszej
      wersji (18 commitów) — zweryfikowano `git diff`, że dotyczące
      Prawa spółdzielczego i USM zmiany to wyłącznie spis treści i linki
      międzyartykułowe, bez zmian merytorycznych w Art. 1-28.
- [x] Reguły (Phase 2) dla Art. 1-14:
      - `ontology/entities/spoldzielnia.yaml` wzbogacona o pełną definicję
        z Art. 1 §1 (blok `definition`, w formacie zgodnym z przykładem
        z PROJECT_CONCEPT.md sekcja 40) oraz o Art. 2, 3, 7, 11.
      - Nowa encja `ontology/entities/statut.yaml` i relacja
        `ontology/relations/has_statute.yaml`.
      - `rules/R-PS-0007..0011` (Art. 1 §1 DEFINITION, Art. 1 §2 PERMISSION,
        Art. 2 STRUCTURAL, Art. 3 STRUCTURAL, Art. 5 OBLIGATION z jawnymi
        odesłaniami do R-PS-0003/0004/0006/0016).
      - `procedures/R-PS-0012-cooperative-founding.yaml` (Art. 6, 7, 11) i
        `R-PS-0013-statute-amendment.yaml` (Art. 12a).
      - `rules/R-PS-0014.yaml` (Art. 14, Monitor Spółdzielczy).
      - Nowy event `CooperativeRegistered` + przejście `null -> ACTIVE` w
        `ontology/states/membership_status.yaml` — **domyka lukę z Phase 1**
        ("poza zakresem: założyciele stają się członkami z rejestracją").
      - Weryfikacja skryptem: 12 eventów, 9 stanów, każde przejście pokryte
        (jak przy Art. 15-28).

**Nie zrobione jeszcze (świadomie, poza zakresem tego kroku):**

- Art. 4, 6 §3-§6, 8, 8a, 9, 10, 12, 13 — uchylone, brak treści do
  formalizacji (celowo pominięte).
- Art. 6 §2a (grupy producentów rolnych) sformalizowane tylko jako próg
  liczbowy w `founder_count_thresholds` procedury R-PS-0012, bez pełnej
  formalizacji tej poddomeny (nierelewantna dla spółdzielni mieszkaniowej).
- Testy (GIVEN/WHEN/THEN) dla nowych reguł/procedur — jeszcze żadna reguła
  w całym repo (Art. 1-28) nie ma testu; to zaległość ogólna, nie tylko
  tego kroku.
- ~~Normalizacja Działu IV i dalszych (Organy spółdzielni, Art. 29 i dalej)~~
  — **błędne założenie, poprawione niżej: Dział III sięga do Art. 34, nie
  kończy się na Art. 28. Dział IV zaczyna się dopiero od Art. 35.**

------------------------------------------------------------------------

## Dokończenie normalizacji: Art. 29-34 (koniec Działu III)

**Odkrycie (2026-09-28):** przy przeglądaniu spisu treści dodanego przez
najnowszy commit Knowledge Base okazało się, że Dział III ("Członkowie, ich
prawa i obowiązki") w rzeczywistości obejmuje Art. 15-**34**, nie 15-28 jak
błędnie założono przy wyborze pierwszego fragmentu. Brakujące 6 artykułów
(29-34) to wciąż ten sam dział, więc — zgodnie z ustalonym tempem "dział po
dziale" — dociągnięto ich normalizację, zanim przejdziemy do Działu IV.

**Zrobione:**

- [x] Znormalizowano Art. 29-34 (6 plików, w tym Art. 33-34 uchylone i
      Art. 29 §2 uchylony na poziomie paragrafu) w
      `law/prawo-spoldzielcze/normalized/`. Dział III jest teraz w pełni
      znormalizowany (Art. 15-34), tak jak Dział I i II wcześniej.
- [x] Walidacja YAML — OK (37 plików razem w `normalized/`).

**Zawartość, do wykorzystania przy pisaniu reguł (nie zrobione jeszcze):**

- Art. 29 — przedawnienie roszczeń o wypłatę udziałów/nadwyżki/wkładów (3
  lata), wyjątek dla roszczeń o zwrot nieruchomości. DEADLINE dla reguł
  już sformalizowanych (Art. 25-28), ale jeszcze niesformalizowanych.
- Art. 30 — obowiązek Zarządu prowadzenia rejestru członków. Odpowiada
  niemal dosłownie statutowemu § 11 realnej spółdzielni mieszkaniowej.
- Art. 31 — obowiązek Zarządu wydania odpisu statutu/regulaminów na
  żądanie członka. **To druga strona prawa już sformalizowanego jako
  R-PS-0004 item R3** (Art. 18 §2 pkt 3) - kandydat do połączenia przy
  formalizacji reguł.
- Art. 32 — fakultatywna podstawa "postępowania wewnątrzspółdzielczego", do
  którego już odsyła sformalizowana procedura R-PS-0016 (Art. 24 §8-§9).
  Kolejny przykład normy złożonej z kilku artykułów (AGENTS.md sekcja 13).
- Art. 33, 34 — uchylone, brak treści.

------------------------------------------------------------------------

## Zwrot architektoniczny: Akoma Ntoso + ELI (2026-09-28)

**Kontekst:** użytkownik przekazał konspekt z rozmowy o architekturze
projektu "Lexon" (zapisany w `docs/LEXON_CONTEXT.md`), który stawia tezę:
nie wymyślać od nowa standardów formalizacji prawa (Akoma Ntoso, ELI, LKIF,
LegalRuleML, Catala), tylko integrować się z nimi tam, gdzie już dobrze
rozwiązują dany problem. Zamiast małego eksperymentu porównawczego
rekomendowanego w tym dokumencie (sekcja 18), zdecydowano od razu
przekonwertować całą dotychczasową normalizację (Art. 1-34).

**Zrobione:**

- [x] Zapisano `docs/LEXON_CONTEXT.md` (kontekst źródłowy, werbatim).
- [x] `docs/decisions/ADR-0001-akoma-ntoso-eli.md` — decyzja, alternatywy,
      konsekwencje.
- [x] `law/prawo-spoldzielcze/normalized/akoma-ntoso/prawo-spoldzielcze.xml`
      — Art. 1-34 w jednym pliku Akoma Ntoso XML (37 artykułów, w tym 10
      uchylonych), z metadanymi FRBR/ELI. Zweryfikowano skryptem 1:1
      przeciwko poprzednim 37 plikom YAML przed ich usunięciem: 111
      jednostek tekstu, 0 rozbieżności.
- [x] Usunięto `normalized/art-*.yaml` (37 plików) - zastąpione jednym
      plikiem XML.
- [x] Zaktualizowano `normalized/README.md`, `docs/dsl.md` — klucz
      `PS-ART-NNN` pozostał niezmieniony, teraz odpowiada `eId="art_N"` w
      XML. **Żaden z ~60 istniejących plików w `rules/`, `procedures/`,
      `ontology/` nie wymagał edycji** dzięki stabilności tego klucza.

**Świadomie NIE zrobione / otwarte:**

- Mapowanie polskiej struktury (Część/Tytuł/Dział/Rozdział) na elementy
  AKN (`part`/`hcontainer[tytul]`/`hcontainer[dzial]`) jest naszą własną
  decyzją, nie potwierdzonym oficjalnym polskim profilem AKN - do rewizji,
  jeśli taki profil się znajdzie.
- ELI URI (`https://eli.gov.pl/eli/DU/2026/521`) są CONSTRUCTED wg wzorca,
  nie zweryfikowane wywołaniem sieciowym względem `eli.gov.pl`/ISAP.
  Numer pozycji z pierwotnego uchwalenia (1982 r.) jest UNKNOWN.
- Walidacja tylko dobrej formy XML (`xml.etree.ElementTree`), nie
  względem oficjalnego schematu XSD Akoma Ntoso 3.0 (brak zainstalowanego
  narzędzia w tym środowisku).
- Warstwa semantyczna (`ontology/`, `rules/`, `procedures/`, `concepts/`)
  pozostaje ad-hoc YAML - ten zwrot dotyczył wyłącznie warstwy dokumentowej.
  LegalRuleML jako ewentualny przyszły punkt odniesienia - nierozstrzygnięte.
- Dział IV i dalsze będą rozszerzać ten sam plik XML (nowe `hcontainer`),
  nie tworzyć nowych plików.

**Aktualizacja — Dział IV dodany (2026-09-28, ten sam dzień):** rozszerzono
`normalized/akoma-ntoso/prawo-spoldzielcze.xml` o Art. 35-59 (Dział IV —
Organy spółdzielni, 5 rozdziałów: Walne zgromadzenie, Rada nadzorcza,
Zarząd, Przepisy wspólne dla rady i zarządu, Zebrania grup członkowskich).
26 artykułów (w tym 46a, 4 uchylone: 43, 47, 51, 53). Zweryfikowano
skryptem bezpośrednio przeciwko źródłu (nie przez pośredni YAML, którego
już nie ma) — 130 jednostek tekstu, 125 identycznych, 5 różniących się
wyłącznie usuniętą składnią linków Markdown (ten sam, spójny wzorzec co
przy Art. 1-34) — 0 rzeczywistych rozbieżności. Art. 35 zawiera notację
`§ 4[1]`-`§ 4[4]` (wstawione paragrafy) zachowaną verbatim. Reguły dla
Działu IV jeszcze nie napisane (sam Dział jest teraz "kandydatem" do
Phase 2, podobnie jak wcześniej Art. 19-23/25-32).

**Aktualizacja — Dział V, VI, VII dodane (2026-09-28, ten sam dzień):**
rozszerzono plik XML o Art. 60-90: Dział V i VI (oba w całości uchylone —
w źródle nie istnieją nawet jako pojedyncze artykuły "(uchylony)", tylko
jako puste nagłówki działów, `status="repealed"` bez `<article>`) oraz
Dział VII — Gospodarka spółdzielni (Art. 67-90, 25 artykułów w tym 88a,
13 uchylonych). Nowość: **Art. 83 ma `status="omitted"`, nie
`"repealed"`** — źródło mówi "(pominięty)", nie "(uchylony)", co jest
innym pojęciem prawnym (numer pominięty w numeracji, nie przepis
uchylony) — świadomie odróżnione zamiast spłaszczone do jednej etykiety.
Zweryfikowano skryptem przeciwko źródłu: 36 jednostek tekstu, 35
identycznych, 1 różniąca się tym samym wzorcem usuniętego linku Markdown
— 0 rzeczywistych rozbieżności. Reguły dla Działu VII jeszcze nie
napisane.

**Aktualizacja — Dział VIII, IX dodane (2026-09-28, na życzenie: dwa
działy naraz):** rozszerzono plik XML o Art. 91-102: Dział VIII — Lustracja
(Art. 91-95, w tym 93a/93b/93c dodane nowelizacją o RODO/ministrze
właściwym ds. budownictwa) i Dział IX — Łączenie się spółdzielni
(Art. 96-102). Nowość: **Art. 93b numeruje ustępy jako gołe `1.`/`2.`/
`3.`/`4.` (bez `§`)** — zachowane verbatim, nowy wiersz w tabeli mapowania
w `akoma-ntoso/README.md`. Dział VIII kontynuuje notację `§ N[M]` dla
wstawionych paragrafów (`§ 1[1]`, `§ 1[2]`, `§ 2[1]`, `§ 4[1]`).
Zweryfikowano skryptem przeciwko źródłu: 52 jednostki tekstu, 50
identycznych, 2 różniące się usuniętym linkiem Markdown — 0 rzeczywistych
rozbieżności. Reguły dla obu działów jeszcze nie napisane. Łączne pokrycie
normalizacyjne: Art. 1-102 (Dział I-IX), 103 artykuły w pliku XML.

**Aktualizacja — Dział X, XI dodane (2026-09-28):** rozszerzono plik XML
o Art. 103-112: Dział X (uchylony w całości, bez artykułów — jak Dział V,
VI wcześniej) i Dział XI — Podział spółdzielni (Art. 108, 108a, 108b,
109-112). **Znalezisko warte odnotowania:** Art. 108a niesie w źródle
przypis `[2)]` mówiący, że artykuł był uchylony od 2003-01-15, ale **to
uchylenie utraciło moc 2005-04-28 na mocy wyroku Trybunału
Konstytucyjnego (K 42/02)** — od tamtej pory znów obowiązuje. Zamiast
pominąć ten przypis (jak inne linki Markdown, które świadomie usuwamy),
zachowano go jawnie jako `<lexon:note marker="2)" type="legislative-history">`
przy `art_108a` — pierwszy w tej ustawie realny przykład złożonej
temporalności/historii legislacyjnej pojedynczego przepisu, o której mówi
`docs/LEXON_CONTEXT.md` sekcja 10. Zweryfikowano skryptem: 28 jednostek
tekstu, 23 identyczne, 5 różniących się usuniętym linkiem Markdown — 0
rzeczywistych rozbieżności treści. Reguły dla Działu XI jeszcze nie
napisane. Łączne pokrycie normalizacyjne: Art. 1-112 (Dział I-XI), 110
artykułów w pliku XML.

**Aktualizacja — Dział XII, XIII dodane: cały Tytuł I gotowy (2026-09-28):**
rozszerzono plik XML o Art. 113-137: Dział XII — Likwidacja spółdzielni
(17 artykułów: 113-129) i Dział XIII — Upadłość spółdzielni (8 artykułów:
130-137). **Dwa kolejne przypisy znalezione i zachowane:** Art. 126 §3
(`lexon:note`, marker `4)`) — drugie zdanie tego paragrafu uchylono
nowelizacją z 2025-11-29 (ustawa o KRS), obecny tekst pokazuje już tylko
pozostałe zdanie; Art. 129 (`authorialNote`, marker `5)`, tym razem
prawdziwy element AKN, bo przypis dotyczy jednego wyrażenia w zdaniu, nie
całej jednostki) — nazwa „Minister Edukacji Narodowej” z 1982 r. odpowiada
dziś innemu ministerstwu. **Niepewność jawnie odnotowana, nie zgadywana:**
Art. 125 §1 pkt 2 zapisuje odesłanie jako „art. 272” bez spacji/nawiasu —
niejasne, czy to dosłownie art. 272, czy nierozdzielony zapis art. 27[2]
(wstawiony artykuł) - zachowany verbatim, niepewność opisana w
`lexon:note`, nie rozstrzygnięta na siłę (AGENTS.md sekcja 50).
Zweryfikowano skryptem: 65 jednostek tekstu, 58 wprost identycznych, 7
różniących się wyłącznie usuniętymi linkami/przeniesionymi markerami
przypisów/poprawnie wydzielonym `authorialNote` (każde zweryfikowane
ręcznie) — 0 rzeczywistych rozbieżności treści.

**To domyka normalizację całego Tytułu I (Art. 1-137)** — wszystkich
przepisów wspólnych dla każdej spółdzielni. Łączne pokrycie: 135
artykułów w pliku XML.

**Decyzja (2026-09-28, ten sam dzień): dokończyć normalizację całej
ustawy**, nie zatrzymywać się na Tytule I. Tempo: kilka działów naraz
(zaczęto od trzech).

**Aktualizacja — Tytuł II, Dział I dodany (2026-09-28):** rozszerzono
plik XML o Art. 138-172 i 178 (Dział I — Spółdzielnie produkcji rolnej),
37 artykułów. Wprowadza nowy poziom hierarchii **Oddział** (poniżej
Rozdziału - `<hcontainer name="oddzial">`, 5 oddziałów w Rozdziale 1:
Przedmiot działalności i członkostwo, Wkłady gruntowe i pieniężne, Praca,
Dochodzenie i ochrona roszczeń z tytułu pracy, Fundusze i podział
dochodu). Rozdział 2 i 4 w całości uchylone (bez artykułów, jak
Dział V/VI/X) - stąd luka w numeracji Art. 173-177. Zweryfikowano
skryptem: 68 jednostek tekstu, 64 identyczne, 4 różniące się usuniętymi
linkami Markdown — 0 rzeczywistych rozbieżności. Reguły nie napisane
(Tytuł II jest agrarny, nie planujemy dla niego Phase 2). Łączne
pokrycie: 172 artykuły. Dalej: Dział II (Spółdzielnie kółek rolniczych)
i Dział III (Spółdzielnie pracy) tego samego Tytułu.

**Aktualizacja — Tytuł II dokończony: Dział II, III dodane (2026-09-28):**
rozszerzono plik XML o Art. 180 (Dział II, 1 artykuł) i Art. 181-203
(Dział III — Spółdzielnie pracy, 24 artykuły, w tym własny mini-kodeks
pracy spółdzielczej: wypowiedzenie, rozwiązanie umowy, wykluczenie z
naruszeniem prawa pracy). Zweryfikowano skryptem: 68 jednostek tekstu,
54 identyczne, 14 różniących się usuniętymi linkami Markdown (Dział III
ma dużo krzyżowych odesłań) — 0 rzeczywistych rozbieżności. **To domyka
cały Tytuł II i całą Część I ustawy.** Łączne pokrycie: 197 artykułów.
Dalej: Część II (Związki spółdzielcze, Krajowa Rada Spółdzielcza) i
Część III (zmiany w przepisach, przepisy przejściowe).

**Aktualizacja — Część II i IIA dodane (2026-09-28):** rozszerzono plik
XML o Art. 240-267 (Część II — Związki spółdzielcze, Krajowa Rada
Spółdzielcza, 41 artykułów) i Art. 267a-267d (Część IIA — Przepisy karne,
4 artykuły). **Część IIA ma w źródle niestandardowy nagłówek** (zwykły
tekst "CZĘŚĆ IIA PRZEPISY KARNE" bez formatowania Markdown, w
odróżnieniu od wszystkich innych Części/Tytułów/Działów) — potraktowana
mimo to jako pełnoprawna `<part>`, bo taka jest jej rzeczywista funkcja w
akcie. Kolejny (siódmy) przypis znaleziony i zachowany: Art. 259a §3
(`authorialNote`, marker `7)`) — „Sąd Wojewódzki” z tekstu ustawy to dziś
„Sąd Okręgowy” po reformie sądownictwa z 1999 r. Zweryfikowano skryptem
(poprawionym, żeby nie liczyć podwójnie zagnieżdżonych `<p>` wewnątrz
`authorialNote`): 104 jednostki tekstu, 95 identycznych, 9 różniących się
usuniętymi linkami/poprawnie wydzielonymi przypisami — 0 rzeczywistych
rozbieżności. Łączne pokrycie: 235 artykułów. **Zostaje już tylko Część
III** (Art. 268-281, zmiany w przepisach i przepisy przejściowe/końcowe)
— ostatnia część całej ustawy.

------------------------------------------------------------------------

## Phase 0 — research (w toku)

- [x] Wybrać fragment ustawy do formalizacji (patrz decyzja wyżej).
- [x] Zidentyfikować repozytorium źródłowe i podłączyć je jako submodule
      (`external/SMDM_Knowledge_Base`).
- [x] Zaprojektować i utworzyć szkielet struktury repozytorium
      (`law/`, `model/`, `engine/`, `tests/`, `agents/`, `docs/`, `examples/`).
- [x] Ustalić i zapisać wersję/datę stanu prawnego ustawy Prawo spółdzielcze
      używaną jako punkt odniesienia: **Dz.U. 2026 poz. 521, tekst jednolity,
      stan na 2026-03-23** (patrz `law/prawo-spoldzielcze/source/README.md`).
- [x] Przeczytać `zrodla/md/statut.md` w zakresie członkostwa i porównać z
      Art. 15–28. **Wynik jest istotny i nieoczywisty** — patrz
      `law/prawo-spoldzielcze/interpretations/OBS-0001-lex-specialis-usm-membership.md`:
      dla tej (i każdej) spółdzielni mieszkaniowej Ustawa o spółdzielniach
      mieszkaniowych (USM) działa jako lex specialis wobec Art. 16-17
      (powstanie członkostwa) i Art. 24 (wykluczenie/wykreślenie) Prawa
      spółdzielczego — członkostwo powstaje/ustaje ex lege wraz z prawem do
      lokalu (USM Art. 15, 24¹, 26), a statut tej spółdzielni ma nawet
      formalnie skreślone §§ 18-24 (tryb wykluczenia). Organem właściwym do
      uchwał członkowskich jest Zarząd, odwoławczym — Rada Nadzorcza (statut
      § 10 ust. 2). **Konsekwencja:** reguły dla Art. 16, 16a, 17, 24 muszą
      mieć `SCOPE_NOTE` odsyłający do OBS-0001; USM Art. 15/24¹/26 to osobne,
      przyszłe zadanie formalizacyjne (dodane niżej), nie robimy go teraz.
- [x] Opracować i zapisać w `docs/dsl.md` minimalną, ale realną konwencję ID
      (patrz AGENTS.md sekcja 38: `R-PS-0001`, `E-PS-0001`, ...) — potwierdzona
      bez zmian względem AGENTS.md, dodano skrót aktu `PS`/`USM` oraz osobny
      klucz dla jednostek `normalized/` (`PS-ART-015`, ...).
- [x] Znormalizować tekst Art. 15–28 — 15 plików w
      `law/prawo-spoldzielcze/normalized/` (14 artykułów + Art. 16a, plus
      pusta jednostka-tombstone dla Art. 23, oznaczonego w ustawie jako
      `(uchylony)`, żeby luka w numeracji była jawna). Segmentacja czysto
      strukturalna (paragrafy, punkty), bez formalizacji semantycznej.
      Zidentyfikowano przy okazji 2 pojęcia nieostre w Art. 24 §2 ("rażące
      niedbalstwo", "dobre obyczaje") — otagowane `open_textured_terms` jako
      materiał wejściowy do Phase 2/`concepts/`. "Wina umyślna" świadomie
      pominięta na tej liście (ugruntowana doktrynalnie kategoria, nie
      klauzula generalna) — decyzja odnotowana w `art-024.yaml`.

## Phase 1 — ontology (w toku)

- [x] Zdefiniować encje: `Spółdzielnia`, `Osoba`, `Członek`, `Udział`,
      `Deklaracja`, `Zarząd`, `RadaNadzorcza`, `WalneZgromadzenie` (w zakresie
      potrzebnym dla Art. 15–28) w `law/prawo-spoldzielcze/ontology/entities/`.
- [x] Zdefiniować relacje: `MEMBER_OF`, `ORGAN_OF`, `DECLARES`, `ADMITTED_BY`,
      `EXCLUDED_BY`, `INHERITS_SHARES_FROM`, `BENEFICIARY_OF` w
      `law/prawo-spoldzielcze/ontology/relations/`. `EXCLUDED_BY` niesie
      `SCOPE_NOTE` do OBS-0001 (w praktyce wyparte dla spółdzielni
      mieszkaniowych). Organ właściwy do `ADMITTED_BY`/`EXCLUDED_BY` celowo
      nie jest zakodowany na sztywno — Art. 17 §4 i Art. 24 §4 pozostawiają
      to statutowi.
- [x] Zdefiniować stany: cykl życia członkostwa (atrybut `status` na relacji
      `MEMBER_OF`) — `DECLARED -> ACTIVE -> (WITHDRAWN | EXCLUDED |
      STRUCK_OFF | DECEASED)`, plus `DECLARED -> REJECTED`. Nazwa `EXPELLED`
      z pierwotnego szkicu zamieniona na `STRUCK_OFF` (wykreślenie) dla
      jasności wobec `EXCLUDED` (wykluczenie) — patrz
      `law/prawo-spoldzielcze/ontology/states/membership_status.yaml`.
      Świadomie uproszczone: odroczona skuteczność wykluczenia/wykreślenia
      (Art. 24 §10) nie jest tu jeszcze modelowana - to zadanie Phase 2.
- [x] Zdefiniować zdarzenia: `DeclarationSubmitted`, `MemberAdmitted`,
      `AdmissionRejected`, `MemberResigned`, `MemberExcluded`,
      `MemberStruckOff`, `MemberDied` w
      `law/prawo-spoldzielcze/ontology/events/` — zweryfikowano skryptem, że
      każde przejście stanu ma odpowiadający mu event 1:1.

**Phase 1 zamknięta.**

> **Aktualizacja z Phase 2:** uproszczenie odnotowane wyżej (odroczona
> skuteczność wykluczenia/wykreślenia) zostało domknięte przy okazji
> formalizowania procedury dla Art. 24 — dodano stany `PENDING_EXCLUSION`/
> `PENDING_STRUCK_OFF` i 4 nowe eventy (`ExclusionBecameEffective`,
> `ExclusionOverturned`, `StruckOffBecameEffective`, `StruckOffOverturned`)
> w `ontology/states/` i `ontology/events/`. `MemberExcluded`/
> `MemberStruckOff` teraz oznaczają moment uchwały, nie moment skuteczności.

## Phase 2 — rules

- [x] Sformalizować Art. 15 jako `RULE` typu `CONDITION` (status: DIRECT) —
      `rules/R-PS-0001.yaml` (kto może być członkiem) i `rules/R-PS-0002.yaml`
      (minimalna liczba członków, SUBJECT: Spółdzielnia, nie Członek).
- [x] Sformalizować Art. 16–17 jako `PROCEDURE` (złożenie deklaracji →
      uchwała o przyjęciu w terminie miesiąca → zawiadomienie w terminie
      dwóch tygodni) z jawnymi `DEADLINE` —
      `procedures/R-PS-0003-membership-admission.yaml`.
- [x] Sformalizować Art. 18 jako zestaw `RIGHT`/`OBLIGATION` —
      `rules/R-PS-0004.yaml` (6 praw), `rules/R-PS-0006.yaml` (2 obowiązki).
      Dodatkowo `rules/R-PS-0005.yaml` (§3, PROHIBITION/ograniczenie prawa
      wglądu do umów) — status INTERPRETATIVE, 3 przesłanki ocenne
      zidentyfikowane jako open_textured_terms, ale CONCEPT dla nich jeszcze
      nie utworzony (nieblokujące, odnotowane w `concepts/README.md`).
- [x] Sformalizować Art. 24 jako `PROCEDURE` z rozgałęzieniem (wykluczenie
      vs. wykreślenie), `DEADLINE` na odwołanie/zaskarżenie, oraz jawnie
      oznaczyć "rażące niedbalstwo" i "dobre obyczaje" jako `CONCEPT` typu
      `OPEN_TEXTURED` w `concepts/` —
      `procedures/R-PS-0016-exclusion-or-strike-off.yaml`, `C-PS-0001`,
      `C-PS-0002`. Przy tej okazji domknięto uproszczenie z Phase 1
      (odroczona skuteczność, §10) — patrz wyżej.
- [x] Każda reguła: provenance do artykułu/paragrafu, `formalization_status`
      — sprawdzone, wszystkie 7 rekordów (`R-PS-0001,0002,0003,0004,0005,0006,0016`)
      mają oba pola.

**Phase 2 zamknięta dla zaplanowanego zakresu.** Świadomie NIE
sformalizowano jeszcze Art. 19-23, 25-28 (udziały, wystąpienie, śmierć,
wypłata udziałów) — to nie było częścią pierwotnie ustalonego minimalnego
zakresu Phase 2 (patrz wyżej), tylko naturalne rozszerzenie na później, gdy
przyjdzie czas na Phase 3 (evaluator) i trzeba będzie zdecydować, czy
poszerzać pokrycie przed czy po pierwszym działającym silniku.

## Phase 3 — execution

- [ ] Zaprojektować minimalny format `LEGAL STATE` (patrz PROJECT_CONCEPT.md
      sekcja 22) wystarczający do reprezentacji jednego członka i jednej
      spółdzielni.
- [ ] Napisać najprostszy możliwy evaluator (nawet bez pełnego parsera DSL —
      np. reguły jako dane w YAML + funkcja ewaluująca w Pythonie) —
      zgodnie z AGENTS.md sekcja 59 (prosty evaluator > skomplikowany compiler).
- [ ] Zdarzenie `DeclarationSubmitted` + `MemberAdmitted` odtwarzają stan
      `Membership.status = ACTIVE` (kryterium sukcesu MVP z PROJECT_CONCEPT.md
      sekcja 51, w miniaturze).

## Phase 4 — provenance & explainability

- [ ] Każdy wynik silnika potrafi odpowiedzieć `WHY` ze ścieżką
      RULE → CONDITION → STATE → SOURCE (Art. X §Y) — na przykładzie decyzji
      o przyjęciu lub wykluczeniu członka.

## Phase 5 — uncertainty

- [ ] `CONCEPT "rażące niedbalstwo"` i `CONCEPT "dobre obyczaje"` zwracają
      `UNRESOLVED` zamiast fałszywego `TRUE`/`FALSE` w testowym scenariuszu
      wykluczenia.

## Dalsze fazy (6–8)

Bez zmian względem `PROJECT_CONCEPT.md` sekcja 52 — legal queries,
versioning, agent tooling. Nie rozpoczynać przed zamknięciem Phase 0–3 na
fragmencie Art. 15–28.

------------------------------------------------------------------------

## Poza kolejnością faz, ale warte odnotowania już teraz

- **Statut jako konfiguracja (PROJECT_CONCEPT.md sekcja 29):** ponieważ mamy
  w Knowledge Base prawdziwy `zrodla/md/statut.md` konkretnej spółdzielni,
  fragment Art. 15–28 nadaje się też jako pierwszy test tej koncepcji —
  ustawa zostawia statutowi konkretyzację (organ właściwy do przyjęcia,
  przyczyny wykluczenia, terminy). To osobne zadanie badawcze, nie blokuje
  Phase 1–3, ale warto je zaplanować zaraz po nich.
- **Nie formalizować na razie** `Ustawa o spółdzielniach mieszkaniowych` ani
  pozostałych aktów w `przepisy-prawne/md/` — zgodnie z AGENTS.md sekcja 3,
  jeden mały fragment na raz.
- **Przyszłe zadanie (po zamknięciu Art. 15-28):** formalizacja Ustawy o
  spółdzielniach mieszkaniowych Art. 15 (powstanie członkostwa), Art. 24¹
  ust. 1 i Art. 26 (ustanie członkostwa) jako `law/ustawa-o-spoldzielniach-mieszkaniowych/`,
  z jawną relacją `lex_specialis` do `R-PS-*` reguł z Art. 16-17 i 24 —
  patrz `law/prawo-spoldzielcze/interpretations/OBS-0001-lex-specialis-usm-membership.md`.
  To pierwszy kandydat na test mechanizmu `CONFLICT`/`lex specialis` z
  PROJECT_CONCEPT.md sekcja 27 na realnym przykładzie, a nie tylko w teorii.

------------------------------------------------------------------------

## Jak aktualizować ten plik

Po zamknięciu zadania: zaznacz `[x]`, dopisz zaobserwowane `UNKNOWN`/
`WARNING` (patrz AGENTS.md sekcja 61), i jeśli zmienia się zakres kolejnej
fazy — zaktualizuj sekcję zamiast dopisywać sprzeczne notatki na końcu pliku.
