# ontology/

Encje, relacje, stany i zdarzenia domeny USM, specyficzne dla
mechanizmu tego aktu (obecny zasięg: Art. 1, 2, 3, 15, 24[1], 26) -
patrz PROJECT_CONCEPT.md sekcje 7-10.

Encje/relacje współdzielone z innymi aktami (Osoba, Spółdzielnia,
Członek, Zarząd, RadaNadzorcza, WalneZgromadzenie, Statut) żyją w
`model/`, nie tutaj - patrz `docs/architecture.md`.

```
entities/    ENTITY   - Lokal (definicja USM-ART-002, zakotwiczona w tym akcie)
relations/   RELATION - HAS_LOKATORSKIE_PRAWO, HAS_WLASNOSCIOWE_PRAWO,
                        HAS_ODREBNA_WLASNOSC, HAS_EKSPEKTATYWA_WLASNOSCI,
                        HAS_ROSZCZENIE_O_LOKATORSKIE_PRAWO
states/      STATE    - MembershipStatus (2 stany + null - własna
                        maszyna, NIE ta sama co law/prawo-spoldzielcze/,
                        patrz OBS-0001 i `note` w pliku stanu)
events/      EVENT    - MembershipArose, MembershipCeased (po jednym
                        typie zdarzenia na wielopodstawowy skutek, nie
                        osobny event na każdą z 7+9 przesłanek - patrz
                        `note` w plikach zdarzeń)
```

**Dlaczego `states/`/`events/` są tu, a nie w `model/`:** dokładnie ten
sam powód co w `law/prawo-spoldzielcze/ontology/README.md` - mechanizm
zmiany stanu członkostwa jest specyficzny dla aktu (tu: ex lege wraz z
tytułem prawnym do lokalu; w PS: deklaracja+uchwała albo
wykluczenie/wykreślenie), mimo że obie maszyny stanów dotyczą tej samej
współdzielonej encji `Członek`.

**Dlaczego `Lokal` nie jest w `model/`:** jego definicja (USM-ART-002)
odsyła do ustawy o własności lokali, niesformalizowanej w tym projekcie
- tożsamość pojęcia jest tu zakotwiczona w tym akcie, nie (jeszcze)
potwierdzona jako niezależna od niego. Do rewizji, jeśli/gdy ustawa o
własności lokali zostanie kiedyś formalizowana.
