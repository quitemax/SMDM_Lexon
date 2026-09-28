# model/

Ogólny (niezależny od konkretnego aktu) warstwowy model formalny: Entity,
Relation, Event, State, Rule — patrz PROJECT_CONCEPT.md sekcje 5–21,
Roadmap Phase 1–2.

Konkretne, przypisane do aktu formalizacje żyją w `law/<akt>/ontology|rules`.
Ten katalog jest miejscem na definicje wspólne / wielo-aktowe (np. Spółdzielnia
jako encja używana zarówno przez Prawo spółdzielcze, jak i Ustawę o
spółdzielniach mieszkaniowych).

Zawiera (od 2026-09-28, przeniesione z `law/prawo-spoldzielcze/ontology/`
— decyzja: encja jest współdzielona, jeśli jej *tożsamość* (czym jest) ma
sens niezależnie od aktu; mechanizm zmiany stanu wg konkretnego aktu
zostaje przy akcie, patrz `docs/architecture.md`):

- `entities/`: Osoba, Spółdzielnia, Członek, Zarząd, RadaNadzorcza,
  WalneZgromadzenie, Statut.
- `relations/`: MEMBER_OF, ORGAN_OF, HAS_STATUTE.
- `events/`, `states/`: nadal puste — stany/zdarzenia są dotąd wyłącznie
  specyficzne dla mechanizmów Prawa spółdzielczego (np. `MembershipStatus`
  zostaje w `law/prawo-spoldzielcze/ontology/states/`, bo według OBS-0001
  ten mechanizm jest w praktyce wyparty przez USM dla spółdzielni
  mieszkaniowych — inny akt może wymagać innej maszyny stanów dla tej
  samej encji `Członek`).
- `rules/`: nadal puste — żadna reguła nie jest jeszcze na tyle
  ogólna/międzyaktowa, żeby żyła tutaj zamiast przy akcie.

Ryzyko do pilnowania: gdy zacznie się formalizacja USM, sprawdzić, czy
te encje faktycznie nadają się bez zmian, czy USM wymaga innych
właściwości (wtedy: rozszerzyć tu, nie duplikować w
`law/ustawa-o-spoldzielniach-mieszkaniowych/`).
