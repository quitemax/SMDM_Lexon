# rules/

Formalne reguły dla USM, schemat wymuszony jak w `law/prawo-spoldzielcze/rules/`
- patrz `docs/decisions/ADR-0002-unified-rule-schema.md`.

Zawiera (Art. 1, 2, 3 - cały obecny zasięg poza Art. 15/24[1]/26, które
są tylko cytowane przez Art. 3, nie mają jeszcze własnych reguł poza
tym):

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

Art. 15, 24[1], 26 są znormalizowane (patrz `../normalized/`) i cytowane
przez R-USM-0007/0008, ale ich WŁASNA treść wykraczająca poza to
odesłanie (np. Art. 24[1] §2-6, Art. 26 §1-3 - mechanika rozliczenia
funduszu remontowego, terminy zawiadomień) nie jest jeszcze
sformalizowana - świadomie odłożone, poza zakresem potrzebnym do
rozwiązania `OBS-0001`.
