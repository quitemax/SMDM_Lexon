# rules/

Formalne reguły (RULE / OBLIGATION / RIGHT / PROHIBITION / PERMISSION / POWER)
z pełnym provenance do source/ (patrz PROJECT_CONCEPT.md sekcje 11–16,
AGENTS.md sekcje 4, 19–20). Schemat wymuszony od 2026-09-28 - patrz
`docs/decisions/ADR-0002-unified-rule-schema.md`, `schema/legal-rule.schema.json`.

Zawiera (Art. 1-3, 5, 14 - kontekst z Tytułu I; Art. 15-32 - Dział III,
kompletne poza artykułami uchylonymi):

- `R-PS-0001` — CONDITION: kto może być członkiem (Art. 15 §2-4).
- `R-PS-0002` — CONDITION: minimalna liczba członków (Art. 15 §1, §5).
- `R-PS-0004` — RIGHT: prawa członka, 6 pozycji (Art. 18 §1, §2, §4).
- `R-PS-0005` — PROHIBITION: ograniczenie prawa wglądu do umów, INTERPRETATIVE,
  DEFEASIBLE (Art. 18 §3).
- `R-PS-0006` — OBLIGATION: obowiązki członka (Art. 18 §5, §6).
- `R-PS-0007` — DEFINITION: legalna definicja Spółdzielni (Art. 1 §1) —
  bezpośredni odpowiednik przykładu z PROJECT_CONCEPT.md sekcja 40.
- `R-PS-0008` — PERMISSION: dozwolona działalność społeczna/oświatowo-kulturalna
  (Art. 1 §2).
- `R-PS-0009` — STRUCTURAL: podstawa prawna działania (Art. 2).
- `R-PS-0010` — STRUCTURAL: majątek jako własność członków (Art. 3).
- `R-PS-0011` — OBLIGATION: wymagana treść statutu, 8 pozycji, w tym jawne
  odesłania do R-PS-0003/0004/0006/0016 (Art. 5 §1).
- `R-PS-0014` — OBLIGATION: publikacja ogłoszeń w Monitorze Spółdzielczym
  (Art. 14).
- `R-PS-0015` — CONDITION: dziedziczenie udziałów przez spadkobiercę (Art. 16a).
- `R-PS-0017` — PROHIBITION: zakaz odmowy przyjęcia spadkobierców dziedziczących
  udziały (Art. 16a).
- `R-PS-0018` — OBLIGATION: obowiązki finansowe członka (wpisowe, udziały,
  pokrywanie strat) (Art. 19 §1-2).
- `R-PS-0019` — STRUCTURAL: brak osobistej odpowiedzialności członka za
  zobowiązania spółdzielni (Art. 19 §3).
- `R-PS-0020` — OBLIGATION: obowiązek zadeklarowania min. jednego udziału
  (Art. 20 §1).
- `R-PS-0021` — PERMISSION: statutowa możliwość wprowadzenia wkładów
  (Art. 20 §2).
- `R-PS-0022` — PROHIBITION: zakaz żądania zwrotu wpłat przed ustaniem
  członkostwa, z wyjątkiem nadwyżki (Art. 21).
- `R-PS-0023` — RIGHT: prawo wystąpienia za wypowiedzeniem, triggers_event
  MemberResigned (Art. 22).
- `R-PS-0024` — STRUCTURAL: skutek śmierci/ustania dla rejestru członków,
  triggers_event MemberDied (Art. 25 §1).
- `R-PS-0025` — OBLIGATION: wspólny pełnomocnik/zarządca przy wielu
  spadkobiercach (Art. 25 §2).
- `R-PS-0026` — OBLIGATION: wypłata udziału byłego członka (Art. 26 §1).
- `R-PS-0027` — PROHIBITION: brak prawa byłego członka do funduszu
  zasobowego (Art. 26 §2).
- `R-PS-0028` — RIGHT: rozporządzanie roszczeniami o wypłatę udziałów/wkładów
  (Art. 27 §1).
- `R-PS-0029` — CONDITION: zaspokojenie wierzyciela członka z udziałów
  dopiero po ustaniu członkostwa (Art. 27 §2).
- `R-PS-0030` — CONDITION: egzekucja z wkładów, termin wymagalności 6
  miesięcy od zajęcia (Art. 27 §3).
- `R-PS-0031` — POWER: pierwszeństwo spółdzielni do nabycia zajętych
  wkładów-środków produkcji (Art. 27 §4).
- `R-PS-0032` — PROHIBITION: wyłączenie wierzytelności spółdzielni z zajęcia
  (Art. 27 §5).
- `R-PS-0033` — OBLIGATION: przedłużona odpowiedzialność za straty po
  ustaniu członkostwa (Art. 28).
- `R-PS-0034` — CONDITION: przedawnienie roszczeń, 3 lata, z wyjątkiem
  roszczeń o zwrot nieruchomości (Art. 29 §1, §3).
- `R-PS-0035` — OBLIGATION: prowadzenie rejestru członków przez Zarząd
  (Art. 30).
- `R-PS-0036` — RIGHT: wgląd do rejestru członków, 4 kategorie uprawnionych
  (Art. 30).
- `R-PS-0037` — OBLIGATION: wydanie odpisu statutu/regulaminów, odpowiednik
  R-PS-0004 R3 (Art. 31).
- `R-PS-0038` — PERMISSION: statutowa możliwość wprowadzenia postępowania
  wewnątrzspółdzielczego (Art. 32 §1).
- `R-PS-0039` — STRUCTURAL: zawieszenie biegu przedawnienia na czas
  postępowania wewnątrzspółdzielczego (Art. 32 §2).
- `R-PS-0040` — PROHIBITION: zakaz ograniczenia drogi sądowej (Art. 32 §3).

Procedury (Art. 6-7-11, Art. 12a, Art. 16-17, Art. 24) są w
`../procedures/`, mimo wspólnej puli ID `R-PS-*` (patrz `docs/dsl.md`).

**Dział III (Art. 15-34) jest teraz w pełni sformalizowany** poza Art.
23, 33, 34 — wszystkie trzy w całości uchylone, brak treści do
formalizacji. Nadal niesformalizowane poza tym działem: Art. 4, 6 (poza
wątkiem procedury zakładania), 8-10, 12-13 (uchylone), i cała reszta
znormalizowanego aktu poza Dział I-III (Art. 35-281) — poza zakresem
wybranego na początku projektu fragmentu, patrz `ROADMAP.md`.
