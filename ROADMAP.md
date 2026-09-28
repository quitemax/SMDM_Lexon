# ROADMAP

> Ten plik jest żywym dokumentem. Aktualizuj go po zamknięciu każdego celu i
> gdy zmienia się priorytet. Fazy pochodzą z `PROJECT_CONCEPT.md` (sekcja 52),
> tu są rozbite na konkretne, sprawdzalne zadania osadzone w realnym materiale
> źródłowym z `external/SMDM_Knowledge_Base`.

Status ogólny: **Phase 0, 1 i 2 (zaplanowany zakres na Art. 15-28) zamknięte.**
**Decyzja (2026-09-28):** zamiast normalizować całą ustawę (249 artykułów) na
raz, rozszerzono normalizację o Art. 1-14 (Dział I i II — definicja
spółdzielni, statut, zakładanie i rejestracja), bezpośrednio poprzedzające
już gotowy Dział III. Reguły (Phase 2) dla Art. 1-14 jeszcze nie napisane —
patrz nowa sekcja niżej.

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
- [ ] Walidacja YAML tych 16 plików skryptem (jak dla Art. 15-28) — **w
      toku, zablokowana przejściową awarią narzędzi shell (Bash/PowerShell)
      w tej sesji**. Do dokończenia przed commitem.

**Nie zrobione jeszcze (świadomie, poza zakresem tego kroku):**

- Reguły (Phase 2) dla Art. 1-14. Art. 1 §1 zawiera definicję legalną
  Spółdzielni - to bezpośredni kandydat do wzbogacenia
  `ontology/entities/spoldzielnia.yaml` (obecnie ta encja ma tylko
  właściwości potrzebne dla Art. 15-28, nie pełną definicję ustawową).
  Art. 5 (wymagana treść statutu) i Art. 6/11/12a (zakładanie, rejestracja,
  zmiana statutu) też się nadają na reguły, ale to następny krok, nie ten.
- Normalizacja Działu IV i dalszych (Organy spółdzielni, Art. 29 i dalej) —
  możliwy naturalny kolejny krok "do tyłu do przodu", ale nie ustalony.

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
