# ROADMAP

> Ten plik jest żywym dokumentem. Aktualizuj go po zamknięciu każdego celu i
> gdy zmienia się priorytet. Fazy pochodzą z `PROJECT_CONCEPT.md` (sekcja 52),
> tu są rozbite na konkretne, sprawdzalne zadania osadzone w realnym materiale
> źródłowym z `external/SMDM_Knowledge_Base`.

Status ogólny: **normalizacja kompletna — cała ustawa, 249 artykułów**,
w formacie Akoma Ntoso XML (`normalized/akoma-ntoso/prawo-spoldzielcze.xml`,
patrz `docs/decisions/ADR-0001-akoma-ntoso-eli.md` i sekcję "NORMALIZACJA
KOMPLETNA" niżej). **Reguły/procedury: Dział III (Art. 15-34) w pełni
sformalizowany (2026-09-29)** — 40 reguł/procedur (`R-PS-0001..0040`),
plus kontekst z Tytułu I (Art. 1-3, 5, 14). Poza Art. 23, 33, 34
(w całości uchylone) i poza tym działem, cała reszta znormalizowanego
materiału (Art. 35-281) jest **wyłącznie znormalizowana, bez żadnych
reguł** — poza zakresem pierwszego wybranego fragmentu (patrz niżej).
**Wszystkie 40 reguł/procedur mają teraz testy (2026-09-29)** — 91
plików w `tests/legal/`, GIVEN/WHEN/THEN, `status: SPECIFIED` (nie
wykonane - `engine/evaluator/` wciąż puste, ADR-0003). Szczegóły w
sekcji "Testy dla Dział III" niżej.

**USM (Ustawa o spółdzielniach mieszkaniowych) - rozpoczęta (2026-09-29):**
drugi akt w `law/`. Fragment (Art. 1, 2, 3, 15, 24[1], 26) znormalizowany
w AKN, 11 reguł (`R-USM-0001..0011`) formalizuje Art. 1-3 - w tym
`R-USM-0007`/`R-USM-0008`, które **rozwiązują `OBS-0001`** (status
RESOLVED - patrz `law/prawo-spoldzielcze/interpretations/OBS-0001-lex-specialis-usm-membership.md`):
członkostwo w spółdzielni mieszkaniowej powstaje/ustaje ex lege wraz z
tytułem prawnym do lokalu, nie przez deklarację+uchwałę ani
wykluczenie/wykreślenie z Prawa spółdzielczego - to teraz jawny,
sprawdzalny graf odesłań (`disapplies`/`references`) między regułami
USM i PS, nie tylko obserwacja. Żadna reguła USM nie ma jeszcze testu.
Szczegóły: sekcja "Formalizacja USM: start" niżej.

**Kolejność ustalona z użytkownikiem (2026-09-29):** dokończyć pisanie
reguł (Dział III — ZROBIONE) → testy (ZROBIONE) → formalizacja USM
(**w toku** - Art. 1-3 zrobione, Art. 15/24[1]/26 własna treść i testy
pozostają) → Phase 3 (silnik, `engine/`, na bazie ADR-0003).

**Przystanek analityczny (2026-09-28):** przed powrotem do pisania reguł
zrobiono audyt repo (skrypty walidujące, nie wrażenia) — patrz
`docs/architecture.md`, `docs/legal-model.md`, `docs/versioning.md`.
Ustalenia i decyzje:

1. **Zero błędów integralności** (martwe referencje, kolizje ID,
   osierocone encje/pojęcia) — fundament jest solidny.
2. **ZROBIONE (2026-09-28):** brak wymuszonego schematu `rules/`/
   `procedures/` — każdy plik miał inny zestaw pól. Naprawione:
   `docs/decisions/ADR-0002-unified-rule-schema.md` (ACCEPTED),
   `schema/legal-rule.schema.json` (JSON Schema 2020-12, rdzeń wspólny +
   pola zależne od `norm_type`), `schema/validate_rules.py` (walidator:
   schemat + duplikaty ID + rozwiązywalność `normalized_ref`/`subject`/
   `holder`/`actors`). Zaczerpnięte z realnie przeczytanego OASIS
   LegalRuleML Core Spec v1.0: `strength` (STRICT/DEFEASIBLE) i
   `overridden_by` — bez przejmowania formatu XML. Wszystkie 15 plików
   przechodzą walidację (0 ERROR, 0 WARNING).
3. **ZROBIONE (2026-09-28):** 0/15 reguł/procedur miało pole `validity`
   mimo że AGENTS.md sekcja 23 je dokumentuje. Retrofit: 15/15 ma teraz
   `validity.from: "2026-03-23"` (= `consolidated_text_as_of` aktu),
   `validity.to: null`. Dodatkowo `strength: DEFEASIBLE` na `R-PS-0005`
   (cała reguła) i `R-PS-0016.grounds.wykluczenie` (tylko ta podstawa) —
   jedyne dwa miejsca w 15 plikach zależne od pojęć `OPEN_TEXTURED`.
4. **Decyzja podjęta i wykonana:** encje/relacje współdzielone z
   przyszłymi aktami (Osoba, Spółdzielnia, Członek, Zarząd,
   RadaNadzorcza, WalneZgromadzenie, Statut, MEMBER_OF, ORGAN_OF,
   HAS_STATUTE) przeniesione z `law/prawo-spoldzielcze/ontology/` do
   `model/` — zanim przybędzie więcej reguł wskazujących na stare
   miejsce. Stany/zdarzenia (`MembershipStatus` i 12 eventów) zostają
   przy akcie — to mechanizm specyficzny dla Prawa spółdzielczego,
   wyparty w praktyce przez USM dla SM (OBS-0001). Uzasadnienie pełne:
   `docs/architecture.md`.
5. **ZROBIONE (2026-09-28):** spike porównawczy — `R-PS-0003` ręcznie
   przepisany do składni Catala (`docs/spikes/R-PS-0003-membership-admission.catala_en`,
   nieskompilowany — brak toolchainu OCaml w tym środowisku, jawnie
   odnotowane). Decyzja: `docs/decisions/ADR-0003-execution-backend.md`
   (ACCEPTED) — **własny evaluator Python, nie Catala.** Deontyka/
   terminy w Catali dobrze pasują, ale kluczowy element naszego modelu
   (event sourcing, stan w czasie, `ontology/states/`+`events/`) nie ma
   w Catali natywnego odpowiednika — `scope` jest czystą funkcją
   input→output. Wzorzec `label`/`exception` zapożyczony jako
   inspiracja dla `strength`/`overridden_by` (ADR-0002).
6. **Świadomie odłożone (niski priorytet):** ocena LKIF jako inspiracji
   ontologicznej — nasz słownik (RIGHT/OBLIGATION/PROHIBITION/PERMISSION/
   POWER) już jest blisko, bez formalnej analizy.

Kolejność ustalona z użytkownikiem (2026-09-28): **dokumentacja
(zrobione) → encje (zrobione) → schemat/LegalRuleML (zrobione,
2026-09-28) → spike Catala (zrobione, 2026-09-28).** Cała ta sekwencja
zamknięta. Nowa kolejność ustalona z użytkownikiem (2026-09-29):
**dokończyć pisanie reguł dla Dział III (ZROBIONE, 2026-09-29, patrz
sekcja "Dokończenie pisania reguł" niżej) → formalizacja USM (następny
krok) → Phase 3 (silnik, na bazie ADR-0003).**

**Zwrot architektoniczny (2026-09-28):** patrz `docs/LEXON_CONTEXT.md` i
`docs/decisions/ADR-0001-akoma-ntoso-eli.md`. Warstwa dokumentowa
(`normalized/`) przeszła z ad-hoc YAML na Akoma Ntoso + wzorzec ELI, żeby
nie wymyślać od nowa istniejących standardów. Warstwa semantyczna
(`rules/`, `procedures/`) dostała analogiczny, mniejszy zwrot tego samego
dnia: wymuszony schemat inspirowany OASIS LegalRuleML (słownictwo, nie
format XML) — patrz `docs/decisions/ADR-0002-unified-rule-schema.md`.
`ontology/`/`concepts/`/`interpretations/` poza zakresem tej decyzji.

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

**Zawartość — sformalizowana 2026-09-29, patrz sekcja "Dokończenie
pisania reguł: Dział III" niżej:**

- Art. 29 — przedawnienie roszczeń (3 lata), wyjątek dla nieruchomości →
  `R-PS-0034`.
- Art. 30 — obowiązek Zarządu prowadzenia rejestru członków → `R-PS-0035`
  (obowiązek) + `R-PS-0036` (prawo wglądu, 4 kategorie uprawnionych).
  Odpowiada niemal dosłownie statutowemu § 11 realnej spółdzielni
  mieszkaniowej.
- Art. 31 — obowiązek Zarządu wydania odpisu statutu/regulaminów →
  `R-PS-0037`, jawnie powiązane z `R-PS-0004` item R3 (Art. 18 §2 pkt 3)
  jako jego odpowiednik po stronie obowiązku, nie połączone w jeden plik
  - inny SUBJECT (Zarząd vs Członek), inny norm_type.
- Art. 32 — fakultatywna podstawa "postępowania wewnątrzspółdzielczego" →
  `R-PS-0038` (permission) + `R-PS-0039` (zawieszenie przedawnienia) +
  `R-PS-0040` (zakaz ograniczenia drogi sądowej). **Korekta względem
  wcześniejszej notatki w tym pliku:** R-PS-0016 (Art. 24 §6-9) nie
  "odsyła" do Art. 32 - to własna, ustawowa ścieżka odwołania wpisana
  bezpośrednio w Art. 24, odrębna od fakultatywnego, statutowego
  postępowania z Art. 32. Nie są tożsame, mimo powierzchownego
  podobieństwa (obie to "odwołanie od uchwały organu") - nie połączone
  jawnym odesłaniem bez potwierdzenia w tekście (AGENTS.md sekcja 50).
- Art. 33, 34 — uchylone, brak treści.

------------------------------------------------------------------------

## Dokończenie pisania reguł: Dział III (2026-09-29)

**Decyzja użytkownika:** dokończyć pisanie reguł, potem formalizacja
USM, na końcu Phase 3 - patrz status ogólny na początku tego pliku.
"Dokończyć" ustalone jako: sformalizować resztę pierwszego wybranego
fragmentu (Dział III, Art. 15-34, patrz "Decyzja: pierwszy fragment do
formalizacji" niżej), nie całą ustawę (249 artykułów) - to nigdy nie
było celem Phase 2, patrz PROJECT_CONCEPT.md sekcja 3 (kilkanaście-
kilkadziesiąt artykułów jako rozsądny zakres pierwszego fragmentu).

**Zrobione:** 25 nowych reguł (`R-PS-0015`, `R-PS-0017..0040` - `0016`
zajęte przez procedurę Art. 24) dla Art. 16a, 19-22, 25-32. Pełna lista
z norm_type i artykułem źródłowym: `law/prawo-spoldzielcze/rules/README.md`.
Wszystkie od razu w schemacie ADR-0002 (z `validity`, nie retrofitowane
później). `py schema/validate_rules.py`: 0 błędów, 0 ostrzeżeń na 40
plikach.

Dwa przypadki domykają zidentyfikowane wcześniej luki:

- Art. 16a miał `RELATION` (`inherits_shares_from`) bez `RULE` niosącej
  faktyczną treść normatywną (AGENTS.md sekcja 16 vs 19) - teraz
  `R-PS-0015` + `R-PS-0017`.
- Art. 22 i Art. 25 §1 miały już zdarzenia (`MemberResigned`,
  `MemberDied`) w `ontology/events/`, ale żadna `RULE` nie niosła normy,
  która je faktycznie wywołuje (AGENTS.md sekcja 18: EVENT != RULE) -
  teraz `R-PS-0023`, `R-PS-0024`.

**Dział III jest teraz w pełni sformalizowany** - jedyne niesformalizowane
artykuły w tym dziale (23, 33, 34) są w całości uchylone.

**Świadomie poza zakresem tego kroku:**

- Art. 26 §2 odsyła do Art. 125 §5a (poza Działem III) - zachowane jako
  nierozwinięte odesłanie w `R-PS-0027`, nie sformalizowane teraz.

------------------------------------------------------------------------

## Testy dla Dział III (2026-09-29)

**Decyzja użytkownika:** po dokończeniu reguł - testy, potem USM.

**Zrobione:** `schema/legal-test.schema.json` + `schema/validate_tests.py`
(patrz `tests/README.md`), a następnie 91 plików `tests/legal/T-PS-NNNN-MM.yaml`
- co najmniej jeden test (zwykle POSITIVE + NEGATIVE, plus BOUNDARY tam,
gdzie reguła ma realny próg liczbowy albo termin) dla wszystkich 40
reguł/procedur w `rules/`+`procedures/`. `py schema/validate_tests.py`:
0 błędów, 0 ostrzeżeń, 0 reguł bez testu.

Zasady zastosowane konsekwentnie przy pisaniu (nie każda reguła dostała
mechanicznie tę samą liczbę testów):

- Normy ramowe bez własnych przesłanek (`R-PS-0010`, `R-PS-0019`,
  `R-PS-0032`) dostały tylko test POSITIVE, z jawną notatką dlaczego
  wymyślony test NEGATIVE byłby fikcją (AGENTS.md sekcja 8 - nie chować
  niepewności, w tym przypadku "nie ma czego negować").
- Pojęcia OPEN_TEXTURED (`R-PS-0005`, `R-PS-0016.grounds.wykluczenie`) -
  GIVEN traktuje predykat jako już rozstrzygnięty przez organ
  rozpoznający sprawę, nigdy jako wyliczony ze wzoru (AGENTS.md sekcja 9).
- Terminy bez ustawowo określonej sankcji za przekroczenie
  (`R-PS-0003` krok 2, `R-PS-0013` krok 2) - test graniczny zatrzymuje
  się na "czy termin jeszcze biegnie", `result: "UNKNOWN"` dla stanu po
  terminie, zamiast zgadywać skutek (AGENTS.md sekcja 50).
- Wyjątek odsyłający do niesformalizowanego artykułu (`R-PS-0027` E1,
  Art. 125 §5a) - nie testowany, z wyjaśnieniem wprost w pliku testu.
- Testy graniczne z kilkoma powiązanymi punktami (np. n = minimum-1/
  minimum/minimum+1) użyły pola `cases` w jednym pliku zamiast rozbijania
  na kilka osobnych ID (AGENTS.md sekcja 28 przedstawia je jako jeden
  zestaw).

Wszystkie testy mają `status: SPECIFIED` - żaden silnik ich nie wykonał
(`engine/evaluator/` puste, ADR-0003). Wartość już teraz: pisanie ich
wymusiło dokładniejsze spojrzenie na warunki/wyjątki/granice niż samo
pisanie reguł - kilka nietrywialnych rozróżnień (np. R-PS-0033 dwa
niezależne terminy, R-PS-0022 dwie niezależne bramki blokujące zwrot)
wypłynęło właśnie przy tej pracy.

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

## NORMALIZACJA KOMPLETNA (2026-09-28)

Dodano Część III (Art. 268-281, 14 artykułów: Rozdział 1 — Zmiany w
przepisach obowiązujących, w większości `status="omitted"` bo to
jednorazowe nowelizacje innych ustaw bez własnej treści w tekście
jednolitym; Rozdział 2 — Przepisy przejściowe i końcowe, kończące się
uchyleniem poprzedniej ustawy z 1961 r. i datą wejścia w życie
1983-01-01). Zweryfikowano skryptem: **14 jednostek tekstu, 14
identycznych, 0 różnic** — najprostszy, bezbłędny fragment całej
konwersji.

**Cała ustawa Prawo spółdzielcze jest teraz w jednym pliku Akoma Ntoso
XML: 249 artykułów, Część I-III (w tym IIA), zweryfikowanych 1:1 wobec
źródła partiami, z 0 rzeczywistymi rozbieżnościami treści w żadnej z
nich.** Po drodze znaleziono i jawnie zachowano (nie pominięto) 7
przypisów niosących realną treść prawną, w tym jeden przypadek
(Art. 108a) gdzie uchylenie przepisu samo zostało uchylone wyrokiem
Trybunału Konstytucyjnego. Jedna niepewność jawnie oznaczona jako
UNKNOWN zamiast zgadywana (Art. 125 §1 pkt 2).

**Co dalej, świadomie odłożone:**

- Reguły/procedury (Phase 2) sformalizowane są wciąż tylko dla
  fragmentu Art. 1-24 (patrz status ogólny na początku pliku) — cała
  reszta (Działy IV, VII-XIII, Tytuł II, Część II, IIA, III) jest
  wyłącznie znormalizowana, zero reguł. To naturalny priorytet na
  kolejny krok, razem z testami (nikt jeszcze nie istnieje w `tests/`).
- Walidacja względem oficjalnego schematu XSD Akoma Ntoso 3.0 — nadal
  tylko dobra forma XML, nie pełna zgodność ze schematem (brak
  narzędzia w tym środowisku).
- ELI URI nadal CONSTRUCTED, nie zweryfikowane na żywo.
- Formalizacja Ustawy o spółdzielniach mieszkaniowych (OBS-0001) —
  wciąż nierozpoczęta, a to ona, nie Prawo spółdzielcze, jest
  faktycznie kluczowa dla realnej spółdzielni mieszkaniowej z
  Knowledge Base.

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
- ~~Nie formalizować na razie `Ustawa o spółdzielniach mieszkaniowych`...~~
  — **nieaktualne, patrz sekcja "Formalizacja USM: start" niżej.** Ten
  wpis też błędnie zakładał, że Art. 15 jest przepisem o powstaniu
  członkostwa (skorygowane w OBS-0001 KOREKTA - to Art. 3 ust. 3[2]).

------------------------------------------------------------------------

## Formalizacja USM: start (2026-09-29)

**Decyzja użytkownika:** po testach, formalizacja USM jako kolejny krok
(status ogólny na początku pliku).

**Zrobione:**

- Szkielet katalogu `law/ustawa-o-spoldzielniach-mieszkaniowych/`
  (source/, normalized/, ontology/, rules/, procedures/, concepts/,
  interpretations/), analogiczny do `law/prawo-spoldzielcze/`.
- `source/README.md`: Dz.U. 2026 poz. 889, tekst jednolity, stan na
  2026-06-10 (inna data niż PS - dwa niezależnie konsolidowane akty).
- Normalizacja **fragmentu** (nie całej ustawy - 55 artykułów, w tym
  duże wstawki jak Rozdział 2[1], 19 artykułów): Art. 1, 2, 3, 15,
  24[1], 26, w Akoma Ntoso. Wybór uzasadniony nie parzystością/rozmiarem,
  tylko tym, że rozwiązuje `OBS-0001`. Zweryfikowane 1:1 (71/71 jednostek
  tekstu, 0 rozbieżności). Nowa reguła `eId` dla wstawek bez litery
  (`Art. 24[1]` -> `art_24_1`) - patrz `normalized/akoma-ntoso/README.md`
  tego aktu.
- **Odkrycie przy czytaniu tekstu (nie zgadywane wcześniej):** USM-ART-001
  §7-9 jest wprost, ustawowym potwierdzeniem lex_specialis - wylicza,
  których przepisów PS się NIE stosuje (wystąpienie/wykluczenie/
  wykreślenie w §8; udziały/wpisowe/deklaracja w §9, z wyjątkiem dla
  Art. 3). To mocniejsza podstawa niż to, co OBS-0001 miało wcześniej
  (tylko empiryczny dowód z jednego statutu) - **skorygowano OBS-0001**
  (błędne cytaty "Art. 15"/"Art. 24[1], 26" jako przepisy o powstaniu/
  ustaniu członkostwa - to w rzeczywistości Art. 3 ust. 3[2]/6/7, Art. 15
  i 24[1]/26 są tylko cytowane przez Art. 3 dla dwóch szczególnych
  przypadków).
- Ontologia: encja `Lokal`, pięć relacji `HAS_*_PRAWO`/`HAS_ROSZCZENIE_*`,
  własna (nie współdzielona z PS) maszyna stanów `MembershipStatus`
  (2 stany + null, znacznie prostsza niż PS-owa - bo brak uznania
  organu na tym poziomie), dwa zdarzenia `MembershipArose`/
  `MembershipCeased` (po jednym typie z polem enum zamiast 7+9 osobnych
  typów - te przesłanki są alternatywne, nie sekwencyjne).
- 11 reguł (`R-USM-0001..0011`) dla Art. 1-3. `R-USM-0007`/`R-USM-0008`
  (powstanie/ustanie członkostwa) **rozwiązują OBS-0001** - status
  zmieniony z UNRESOLVED na RESOLVED. `R-PS-0003`/`R-PS-0016`
  zaktualizowane: `scope_note` cytuje teraz konkretne reguły USM,
  plus jawne pole `references` w obie strony.
- `py schema/validate_rules.py`: 0 błędów, 0 ostrzeżeń na 51 plikach
  (40 PS + 11 USM). Przy okazji naprawiono dwie realne luki w
  narzędziach, znalezione właśnie dlatego, że to pierwszy drugi akt:
  `schema/legal-rule.schema.json`/`legal-test.schema.json` miały wzorce
  ID zahardkodowane na `R-PS-`/`T-PS-` (uogólnione do dowolnego
  prefiksu aktu), `normalized_ref_to_eid` nie obsługiwał wzorca
  `USM-ART-024-1` (dodano).

**Świadomie poza zakresem tego kroku:**

- Art. 15, 24[1], 26 - znormalizowane i cytowane przez Art. 3, ale ich
  WŁASNA treść (np. Art. 24[1] §2-6 - rozliczenie funduszu remontowego,
  Art. 26 §1-3 - terminy zawiadomień, uchwała o przejściu na reżim UWL)
  nie ma jeszcze własnych reguł.
- Żadna reguła USM nie ma testu (`T-USM-*` jeszcze nie istnieje) -
  naturalny następny krok w ramach kontynuacji formalizacji USM, zanim
  przejdziemy do Phase 3.
- Reszta ustawy (Art. 4-14, 8[1]-8[3], 9[1]-14, 16-17[19], 18-23, 25,
  27-27[4], 28-55) - nieznormalizowana, do rozszerzenia w miarę potrzeby.

------------------------------------------------------------------------

## Jak aktualizować ten plik

Po zamknięciu zadania: zaznacz `[x]`, dopisz zaobserwowane `UNKNOWN`/
`WARNING` (patrz AGENTS.md sekcja 61), i jeśli zmienia się zakres kolejnej
fazy — zaktualizuj sekcję zamiast dopisywać sprzeczne notatki na końcu pliku.
