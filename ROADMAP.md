# ROADMAP

> Ten plik jest żywym dokumentem. Aktualizuj go po zamknięciu każdego celu i
> gdy zmienia się priorytet. Fazy pochodzą z `PROJECT_CONCEPT.md` (sekcja 52),
> tu są rozbite na konkretne, sprawdzalne zadania osadzone w realnym materiale
> źródłowym z `external/SMDM_Knowledge_Base`.

Status ogólny: **Phase 0 — research**, zadanie 0 w toku (wybór fragmentu
zamknięty, patrz niżej).

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

## Phase 0 — research (w toku)

- [x] Wybrać fragment ustawy do formalizacji (patrz decyzja wyżej).
- [x] Zidentyfikować repozytorium źródłowe i podłączyć je jako submodule
      (`external/SMDM_Knowledge_Base`).
- [x] Zaprojektować i utworzyć szkielet struktury repozytorium
      (`law/`, `model/`, `engine/`, `tests/`, `agents/`, `docs/`, `examples/`).
- [ ] Ustalić i zapisać wersję/datę stanu prawnego ustawy Prawo spółdzielcze
      używaną jako punkt odniesienia (`law/prawo-spoldzielcze/source/README.md`
      obecnie oznaczony `SOURCE_VERIFICATION_PENDING`).
- [ ] Opracować i zapisać w `docs/dsl.md` minimalną, ale realną konwencję ID
      (patrz AGENTS.md sekcja 38: `R-PS-0001`, `E-PS-0001`, ...) — potwierdzić
      lub zmodyfikować propozycję z PROJECT_CONCEPT.md.
- [ ] Przeczytać `zrodla/md/statut.md` w zakresie członkostwa i porównać z
      Art. 15–28, zanotować rozbieżności/konkretyzacje jako materiał wejściowy
      do `interpretations/`.

## Phase 1 — ontology (następne)

- [ ] Zdefiniować encje: `Spółdzielnia`, `Osoba`, `Członek`, `Udział`,
      `Deklaracja`, `Zarząd`, `RadaNadzorcza`, `WalneZgromadzenie` (w zakresie
      potrzebnym dla Art. 15–28) w `law/prawo-spoldzielcze/ontology/`.
- [ ] Zdefiniować relacje: `MEMBER_OF`, `DECLARES`, `ADMITTED_BY`,
      `EXCLUDED_BY`.
- [ ] Zdefiniować stany: cykl życia członkostwa —
      `DECLARED -> PENDING -> ACTIVE -> (WITHDRAWN | EXCLUDED | EXPELLED | DECEASED)`
      — na podstawie Art. 16-17 (wejście) i Art. 22, 24-25 (wyjście).
- [ ] Zdefiniować zdarzenia: `DeclarationSubmitted`, `MemberAdmitted`,
      `AdmissionRejected`, `MemberResigned`, `MemberExcluded`,
      `MemberStruckOff`, `MemberDied`.

## Phase 2 — rules

- [ ] Sformalizować Art. 15 jako `RULE` typu `DEFINITION`/`CONDITION`
      (status: DIRECT).
- [ ] Sformalizować Art. 16–17 jako `PROCEDURE` (złożenie deklaracji →
      uchwała o przyjęciu w terminie miesiąca → zawiadomienie w terminie
      dwóch tygodni) z jawnymi `DEADLINE`.
- [ ] Sformalizować Art. 18 jako zestaw `RIGHT`/`OBLIGATION`.
- [ ] Sformalizować Art. 24 jako `PROCEDURE` z rozgałęzieniem (wykluczenie
      vs. wykreślenie), `DEADLINE` na odwołanie/zaskarżenie, oraz jawnie
      oznaczyć "rażące niedbalstwo" i "dobre obyczaje" jako `CONCEPT` typu
      `OPEN_TEXTURED` w `concepts/`.
- [ ] Każda reguła: provenance do artykułu/paragrafu, `formalization_status`.

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

------------------------------------------------------------------------

## Jak aktualizować ten plik

Po zamknięciu zadania: zaznacz `[x]`, dopisz zaobserwowane `UNKNOWN`/
`WARNING` (patrz AGENTS.md sekcja 61), i jeśli zmienia się zakres kolejnej
fazy — zaktualizuj sekcję zamiast dopisywać sprzeczne notatki na końcu pliku.
