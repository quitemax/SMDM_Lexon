# procedures/

Procedury jako grafy kroków (np. AdoptResolution, MembershipAdmission) —
patrz PROJECT_CONCEPT.md sekcja 17, AGENTS.md sekcja 21.

Zawiera:

- `R-PS-0003-membership-admission.yaml` — przyjęcie w poczet członków
  (Art. 16-17): 3 kroki, 2 terminy ustawowe (miesiąc na uchwałę, 2 tygodnie
  na zawiadomienie).
- `R-PS-0016-exclusion-or-strike-off.yaml` — wykluczenie albo wykreślenie
  (Art. 24): 5 kroków z rozgałęzieniem trybu odwołania (Rada Nadzorcza vs.
  Walne Zgromadzenie) i odroczoną skutecznością (§10) — najbardziej złożona
  procedura w tym fragmencie.

Obie mają `scope_note` odsyłający do OBS-0001 (patrz
`../interpretations/`) — dla spółdzielni mieszkaniowej z Knowledge Base obie
w praktyce nie są głównym/jedynym trybem (USM jest lex specialis).

- `R-PS-0012-cooperative-founding.yaml` — założenie i zarejestrowanie
  spółdzielni (Art. 6, 7, 11): 4 kroki, progi minimalnej liczby założycieli,
  odpowiedzialność za czynności sprzed rejestracji. Krok 4 domyka lukę z
  Phase 1 (przejście `null -> ACTIVE` dla założycieli, wcześniej "poza
  zakresem").
- `R-PS-0013-statute-amendment.yaml` — zmiana statutu (Art. 12a): 3 kroki,
  1 termin ustawowy (30 dni), bez rozgałęzień — najprostsza procedura w tym
  fragmencie, dobry kontrast wobec R-PS-0016.
