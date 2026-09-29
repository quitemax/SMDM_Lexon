# rules/

Formalne reguły dla USM, schemat wymuszony jak w `law/prawo-spoldzielcze/rules/`
- patrz `docs/decisions/ADR-0002-unified-rule-schema.md`.

Zawiera **cały obecny zasięg normalizacji** (Art. 1, 2, 3, 15, 24[1],
26):

- `R-USM-0001` — STRUCTURAL: odesłanie rezydualne do Prawa spółdzielczego
  (Art. 1 §7).
- `R-USM-0002` — PROHIBITION: wyłączenie PS ws. wystąpienia/wykluczenia/
  wykreślenia (Art. 1 §8) - disapplies R-PS-0016, R-PS-0023.
- `R-USM-0003` — PROHIBITION: wyłączenie PS ws. udziałów/wpisowego/
  deklaracji (Art. 1 §9) - disapplies R-PS-0003, R-PS-0018, R-PS-0020,
  R-PS-0021, R-PS-0022; wyjątek E1 (Art. 3).
- `R-USM-0004` — DEFINITION: lokal, dom jednorodzinny, wartość rynkowa,
  osoba bliska (Art. 2).
- `R-USM-0005` — CONDITION: kto jest członkiem - osoba fizyczna, cztery
  tytuły + założyciel; małżonkowie wspólnie (Art. 3 §1-2).
- `R-USM-0006` — CONDITION: kto jest członkiem - osoba prawna, właściciel
  lokalu (roszczenie o przyjęcie + PS Art. 16 odpowiednio), garaż,
  najemca (Art. 3 §3, 3[1], 3[3], 3[4]).
- `R-USM-0007` — CONDITION: **powstanie członkostwa ex lege**, siedem
  zdarzeń, triggers_event MembershipArose (Art. 3 §3[2]) - rdzeń
  rozwiązania `OBS-0001`.
- `R-USM-0008` — CONDITION: **ustanie członkostwa ex lege**, osiem
  zdarzeń, triggers_event MembershipCeased (Art. 3 §6-7) - rdzeń
  rozwiązania `OBS-0001`.
- `R-USM-0009` — CONDITION: wielu uprawnionych do jednego tytułu - tylko
  jeden członek, z terminem 12 miesięcy (Art. 3 §5).
- `R-USM-0010` — CONDITION: wiele tytułów prawnych jednego członka -
  utrata dopiero przy utracie wszystkich, ogranicza R-USM-0008 (Art. 3
  §8).
- `R-USM-0011` — CONDITION: ustanie członkostwa założycieli bez prawa do
  lokalu w 3 lata (Art. 3 §9).
- `R-USM-0012` — RIGHT: roszczenie osób bliskich po wygaśnięciu
  lokatorskiego prawa wskutek śmierci uprawnionego (Art. 15 §2, §2[1]).
- `R-USM-0013` — CONDITION: zachowanie tego roszczenia - termin roczny,
  rozstrzygnięcie sądu/wybór spółdzielni przy wielu uprawnionych,
  zawiadomienie, odpowiedzialność solidarna (Art. 15 §4).
- `R-USM-0014` — OBLIGATION: wypłata wartości rynkowej lokalu przy
  wygaśnięciu roszczeń (Art. 15 §6) - UNCERTAIN co do adresata wypłaty
  w gałęzi "brak uprawnionych osób", patrz `note`.
- `R-USM-0015` — RIGHT: roszczenie o przyjęcie do spółdzielni przy
  ustaniu członkostwa przed zawarciem umowy o budowę lokalu (Art. 15 §7).
- `R-USM-0016` — POWER: uchwała większości właścicieli o przejściu na
  reżim UWL (Art. 24[1] §1).
- `R-USM-0017` — STRUCTURAL: ta uchwała nie narusza spółdzielczych praw
  do lokali (Art. 24[1] §2) - UNCERTAIN co do zakresu podmiotowego
  przesłanki E7 w R-USM-0008, patrz `note`.
- `R-USM-0018` — RIGHT: współwłasność funduszu remontowego przy ustaniu
  członkostwa właściciela lokalu (Art. 24[1] §3-4).
- `R-USM-0019` — OBLIGATION: rozliczenie funduszu remontowego (Art.
  24[1] §5).
- `R-USM-0020` — OBLIGATION: udział właścicieli w kosztach wspólnego
  korzystania od powstania wspólnoty mieszkaniowej (Art. 24[1] §6).
- `R-USM-0021` — STRUCTURAL: wyodrębnienie własności ostatniego lokalu -
  reżim UWL, termin 14 dni na zawiadomienie (Art. 26 §1, §3-4) - patrz
  `note` o zduplikowanym w źródle obowiązku zawiadomienia (§1 zdanie
  drugie = §3, dosłownie).
- `R-USM-0022` — POWER: uchwała większości o odpowiednim stosowaniu Art.
  27 zamiast pełnego reżimu UWL, termin 3 miesięcy (Art. 26 §2).

Poza Art. 4-14, 8[1]-8[3], 9[1]-14, 16-17[19], 18-23, 25, 27-27[4],
28-55, które nie są znormalizowane (patrz `../normalized/`), **cały
znormalizowany fragment ma już reguły** - żadna świadomie odłożona
treść nie pozostaje bez formalizacji w obrębie Art. 1, 2, 3, 15, 24[1],
26.
