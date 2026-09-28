# ADR-0003 — Backend wykonawczy Phase 3: własny evaluator, nie Catala

## Context

Od `ROADMAP.md` (sekcja "Przystanek analityczny", punkt 5): przed Phase
3 (silnik, `engine/evaluator/`, dotąd puste) zaplanowano mały spike
porównawczy — ręcznie przepisać jedną gotową procedurę do składni
Catala i sprawdzić dopasowanie, zanim zdecydujemy między własnym
evaluatorem (Python) a Catalą jako backendem. Kandydat: `R-PS-0003`
(przyjęcie w poczet członków, PS-ART-016/017) — wybrany, bo ma
najbogatszą strukturę z dotychczasowych 4 procedur (dwa etapy, dwa
terminy, warunek na treść zawiadomienia).

Wykonano: `docs/spikes/R-PS-0003-membership-admission.catala_en`,
ręczne przepisanie na podstawie realnie przeczytanej dokumentacji
Catali (`book.catala-lang.org`, sekcje 2-1, 2-2, 4-2, 5-1, 5-2, 5-3) —
nie z pamięci, nie zgadywane. **Nie sprawdzone kompilatorem** — w tym
środowisku nie ma zainstalowanego OCaml/opam/catala, a instalacja
całego toolchainu wyłącznie na potrzeby jednego pliku-spike'a byłaby
nieproporcjonalna (AGENTS.md sekcja 59). To ogranicza pewność wniosków
poniżej do poziomu "analiza dokumentacji + próba przepisania", nie
"zweryfikowane kompilacją" — odnotowane jawnie, nie ukryte
(AGENTS.md sekcja 51).

### Co spike pokazał

1. **Deontyka/warunkowość: dobre dopasowanie.** `definition X under
   condition ... consequence equals ...` oraz `label`/`exception`
   (reguła z wyjątkiem nadrzędnym) odwzorowują dokładnie to, co ADR-0002
   próbuje wyrazić w YAML polami `conditions`/`exceptions`/`strength`/
   `overridden_by`. Catala ma to jako natywną, sprawdzoną w produkcji
   (francuski kodeks podatkowy) konstrukcję językową, nie doklejony
   dodatek.
2. **Terminy: dobre dopasowanie.** Typ `duration` i arytmetyka dat
   (`data_zlozenia + termin_rozstrzygniecia_ze_statutu`) to naturalny,
   bezpośredni odpowiednik naszych pól `deadline.duration`/`unit`/
   `start_event` z YAML.
3. **Kluczowa niezgodność: Catala `scope` jest czystą funkcją
   input→output.** Nie ma natywnego konstruktu "wyemituj zdarzenie" ani
   mutowalnego stanu w czasie. Nasz model semantyczny jest w tym
   zbudowany odwrotnie — `ontology/states/membership_status.yaml` +
   12 zdarzeń w `ontology/events/`, event sourcing (AGENTS.md sekcja
   25), to jest **centralny**, nie peryferyjny element tego, jak
   reprezentujemy prawo w czasie. Catala nie eliminuje potrzeby
   event sourcingu — przesuwa ją do kodu hosta (Python/OCaml), który
   wywołuje `scope` jako czystą funkcję i dopiero na podstawie wyniku
   emituje zdarzenia. Catala rozwiązuje więc tylko część problemu
   (obliczenie wyniku), nie całość (utrwalenie historii, stan w czasie,
   `AS_OF`).
4. **PROCEDURE jako typ normy: słabsze dopasowanie.** Nasz `norm_type:
   PROCEDURE` niesie `actors`/`steps`/`triggers_event` — semantykę
   sekwencji akcji różnych podmiotów w czasie. W Catali każdy krok
   musiałby stać się osobnym `scope` (albo osobną zmienną w jednym
   `scope`, jak w spike'u) — sama struktura "krok, aktor, zdarzenie
   wyzwalane" nie ma dedykowanego odpowiednika, trzeba by ją emulować.
5. **Brak lokalizacji na polski.** Catala wspiera zlokalizowane słowa
   kluczowe tylko dla angielskiego (`.catala_en`) i francuskiego
   (`.catala_fr`) — nie ma `.catala_pl`. Część zamierzonej wartości
   "literate programming w języku ustawy" (PROJECT_CONCEPT.md,
   `docs/LEXON_CONTEXT.md`) nie przenosi się na polską ustawę — słowa
   kluczowe pozostają angielskie, tylko identyfikatory domenowe mogą
   być polskie (jak w spike'u).
6. **Koszt toolchainu.** OCaml/opam/dune — ciężki zależnościowo stack
   (potwierdzone: brak w obecnym środowisku deweloperskim), w
   sprzeczności z AGENTS.md sekcja 59 (prosty parser + jawny model +
   prosty evaluator jako priorytet MVP).

## Decision

1. **Nie przyjmujemy Catali jako backendu wykonawczego Phase 3.**
   Budujemy własny evaluator (Python), zgodnie z domyślnym kierunkiem
   z AGENTS.md sekcja 59 i PROJECT_CONCEPT.md.
2. **Zapożyczamy z Catali wzorzec `label`/`exception` jako inspirację
   projektową** dla tego, jak nasz docelowy evaluator powinien
   rozwiązywać priorytet między regułą a jej wyjątkami/`overridden_by`
   (ADR-0002) — nie jako format, tylko jako sprawdzony w praktyce
   wzorzec algorytmu (baza + nadpisania z warunkiem, rozstrzygane od
   najbardziej szczegółowego wyjątku w dół).
3. **Event sourcing (stan, zdarzenia, `AS_OF`) budujemy sami**, w
   Pythonie, jako część `engine/state/` — nie czekamy na to, aż jakiś
   zewnętrzny język prawny to rozwiąże za nas, bo żaden ze
   zbadanych (LegalRuleML w ADR-0002, teraz Catala) tego nie robi
   natywnie.
4. **Nie zamykamy tematu na zawsze.** Jeśli w przyszłości formalizacja
   USM albo innego aktu okaże się dominować obliczeniami czysto
   funkcyjnymi (jak francuski podatek dochodowy — dużo warunkowej
   arytmetyki, mało stanu w czasie), rewizja tej decyzji jest
   uzasadniona — ale to nowy ADR, nie cichy odwrót od tego.

## Alternatives

- **Przyjąć Catalę i budować event sourcing wokół niej** (Catala jako
  "warstwa obliczeniowa", Python jako "warstwa zdarzeń" wołająca ją).
  Odrzucone na tym etapie: dodaje cały toolchain OCaml do projektu dla
  korzyści, które ograniczają się do jednego z sześciu `norm_type`
  (głównie `CONDITION`/`RIGHT`/`OBLIGATION` bez komponentu czasowego) —
  nieproporcjonalny koszt wobec 15 istniejących reguł, z czego 4 to
  właśnie `PROCEDURE` (najsłabiej dopasowany przypadek).
- **Zainstalować toolchain i faktycznie skompilować spike**, żeby mieć
  pewność, nie tylko analizę dokumentacji. Odrzucone na tym etapie -
  koszt (instalacja OCaml/opam na Windows) nieproporcjonalny do celu
  (ocena dopasowania koncepcyjnego, nie budowa produkcyjnej integracji);
  możliwe do zrobienia później, jeśli decyzja z pkt 4 zostanie
  zrewidowana.

## Consequences

- `engine/evaluator/` w Pythonie, bez zewnętrznej zależności językowej,
  jest teraz jednoznacznym kierunkiem dla Phase 3 — odblokowuje
  planowanie tej fazy bez dalszej niepewności "może czekać na Catalę".
- `docs/spikes/R-PS-0003-membership-admission.catala_en` zostaje w
  repo jako udokumentowany dowód pracy i uzasadnienie decyzji (AGENTS.md
  sekcja 39: ważne decyzje architektoniczne dokumentowane), nie jest
  martwym kodem do usunięcia.
- Wzorzec `label`/`exception` z Catali powinien wpłynąć na projekt
  algorytmu rozstrzygania `overridden_by`/`strength` w `engine/`, gdy
  Phase 3 faktycznie się zacznie — do przypomnienia w
  `docs/architecture.md` przy aktualizacji Warstwy 3.

## Status

ACCEPTED — 2026-09-28.
