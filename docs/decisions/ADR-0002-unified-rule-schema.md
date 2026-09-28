# ADR-0002 — Jednolity, wymuszony schemat dla `rules/`/`procedures/`, inspirowany LegalRuleML

## Context

Po ukończeniu normalizacji całego aktu (249 artykułów, Akoma Ntoso) i przed
powrotem do pisania reguł, przeprowadzono audyt warstwy semantycznej
(`ontology/`, `rules/`, `procedures/`, `concepts/`) skryptami walidującymi
(nie "na wrażenie"). Ustalenia:

- **Zero błędów integralności** (martwe referencje, kolizje ID, osierocone
  encje/pojęcia) — ten fundament jest solidny i ADR go nie zmienia.
- **Brak wymuszonego schematu.** Wszystkie 15 istniejących plików
  (`rules/R-PS-0001..0014.yaml` minus uchylone, `procedures/R-PS-0003,
  0012, 0013, 0016`) mają wspólny rdzeń (`id`, `norm_type`, `title`,
  `source`, `formalization_status`, `tests`), ale różny zestaw pól
  specyficznych dla typu normy (`effect` vs `items` vs `asserts`/`purpose`
  vs `legal_basis_hierarchy`) — nic to nigdy nie waliduje.
- **0/15 plików ma pole `validity`**, mimo że AGENTS.md sekcja 23 i
  `law/prawo-spoldzielcze/source/README.md` już to pole zakładają
  (`consolidated_text_as_of: 2026-03-23` jako `valid_from`).
- Użytkownik: pisanie testów "na samym YAML" nie ma sensu bez
  jednolitego, wymuszonego Legal IR — testy potrzebują czegoś, co można
  mechanicznie zweryfikować (wymagane pola, poprawne enumy, rozwiązywalne
  odniesienia), nie tylko czytać.
- `docs/LEXON_CONTEXT.md` flagował LegalRuleML (OASIS) jako "najważniejszy
  standard do przeanalizowania", ale nigdy faktycznie nie przeczytany.
  Zrobiono to teraz (OASIS LegalRuleML Core Specification v1.0,
  <https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/legalruleml-core-spec-v1.0.html>).

### Co z LegalRuleML jest tu istotne

LegalRuleML rozróżnia m.in.:

- **Deontykę**: `Obligation`/`Permission`/`Prohibition`/`Right` jako
  odrębne typy (już mamy — `norm_type`, AGENTS.md sekcja 20).
- **Defeasibility**: `StrictStrength` (wniosek pewny, gdy przesłanka
  prawdziwa) vs `DefeasibleStrength` (wniosek domniemany, obalalny) oraz
  `Override` (reguła A ma pierwszeństwo przed regułą B). To pojęcie,
  którego u nas dotąd brakowało jako jawnego pola — mieliśmy tylko
  `exceptions` (wyjątki wprost z tekstu ustawy) i `open_textured`/
  `open_textured_terms` (odesłania do `concepts/`), bez rozróżnienia
  "reguła ścisła z enumerowanymi wyjątkami" od "reguła z natury obalalna,
  bo zależy od pojęcia nieostrego".
- **Temporal validity**: `TemporalCharacteristic`/`forStatus`/`atTime` —
  potwierdza, że nasze `validity.from`/`validity.to` (AGENTS.md sekcja 23)
  to nie nasz wymysł, tylko zgrubne odwzorowanie tego samego pojęcia.
- **Provenance**: `LegalSource`/`References`/`appliesSource` — potwierdza
  kształt naszego `source` (już mamy `act`/`article`/`paragraph`/
  `normalized_ref`).

### Czego z LegalRuleML świadomie NIE bierzemy

- **Formatu XML.** LegalRuleML jest zapisywany jako XML/RuleML
  (`<lrml:Obligation>`, `<ruleml:if>`/`<ruleml:then>`...). Zgodnie z
  PROJECT_CONCEPT.md priorytetem "prosty parser + jawny model + prosty
  evaluator" (AGENTS.md sekcja 59) i tym, że warstwa semantyczna jest
  wciąż w fazie MVP, zostajemy w YAML. Nie jesteśmy zgodni (conformant)
  z LegalRuleML — jesteśmy nim **inspirowani** w słownictwie pojęciowym.
- **`SuborderList`, `PenaltyStatement`/`ReparationStatement`,
  `Alternatives`.** Żaden z 15 sformalizowanych przepisów tego dotąd nie
  wymaga (brak sankcji/kar w Art. 1-28 poza samym wykluczeniem, które już
  mamy jako `PROCEDURE`; brak konkurencyjnych interpretacji poza
  `R-PS-0005`, które i tak jest już oznaczone `INTERPRETATIVE`). Dodanie
  tych konstruktów bez realnego przypadku użycia byłoby modelowaniem
  ponad potrzebę (AGENTS.md sekcja 15, sekcja 59) — odłożone do momentu,
  gdy pojawi się przepis, który tego faktycznie wymaga.
- **`Context`/`Authority`/`Jurisdiction` jako osobne elementy.** Na razie
  wszystko dotyczy jednego aktu i jednej jurysdykcji (Polska); `source.act`
  już to niesie. Rozdzielenie odłożone do momentu formalizacji drugiego
  aktu (np. USM), gdy realnie pojawi się potrzeba odróżnienia.

## Decision

1. **Wspólny rdzeń, wymuszony dla każdego pliku w `rules/`/`procedures/`:**
   `id`, `norm_type`, `title`, `source` (`act`, `article`, `normalized_ref`,
   opcjonalnie `paragraph`; `article`/`normalized_ref` mogą być stringiem
   albo listą — już tak jest dla reguł wieloartykułowych jak `R-PS-0003`),
   **nowe: `validity`** (`from`, `to`), `formalization_status`, `tests`.
2. **Pola zależne od `norm_type` pozostają zależne od typu**, nie
   spłaszczamy ich do jednego uniwersalnego kształtu (AGENTS.md sekcja 56
   — nie upraszczaj nadmiernie). `PROCEDURE` wymaga `name`/`actors`/`steps`
   zamiast `subject`; pozostałe typy wymagają `subject`. Pola takie jak
   `items`, `effect`, `asserts`/`purpose`, `legal_basis_hierarchy`,
   `exceptions` zostają opcjonalne i semantycznie takie, jak dziś — bo już
   dobrze odzwierciedlają różnice między definicją, uprawnieniem z listą
   pozycji, a normą ramową.
3. **Nowe pole opcjonalne `strength`** (`STRICT` domyślnie / `DEFEASIBLE`)
   — LegalRuleML-inspirowane. Stosowane tylko tam, gdzie reguła (albo jej
   fragment) zależy od pojęcia `OPEN_TEXTURED` z `concepts/` i dlatego jest
   z natury obalalna, a nie tylko ma enumerowane wyjątki wprost z ustawy.
   Retrofit: `R-PS-0005` (cała reguła — trzy przesłanki open-textured),
   `R-PS-0016.grounds.wykluczenie` (tylko ta podstawa, nie `wykreślenie`).
4. **Nowe pole opcjonalne `overridden_by`/`overrides`** (lista ID reguł,
   LegalRuleML `Override`) — zdefiniowane w schemacie, ale **nie
   dodawane teraz do żadnego pliku**, bo żaden udokumentowany konflikt
   reguł jeszcze nie istnieje (AGENTS.md sekcja 31 — CONFLICT to osobny,
   jawny konstrukt, nie zgadujemy konfliktów, żeby wypełnić pole).
5. **Walidator** (`tools/validate_rules.py`) sprawdza schemat
   (`schema/legal-rule.schema.json`, JSON Schema 2020-12) + to, czego
   schemat nie wyrazi: `normalized_ref` rozwiązywalny do realnego `eId` w
   AKN, `subject`/`holder` rozwiązywalne do encji w `model/` lub
   `law/prawo-spoldzielcze/ontology/entities/`, brak duplikatów ID.
6. **Retrofit wszystkich 15 istniejących plików**: dodanie `validity.from:
   "2026-03-23"` / `validity.to: null` (per `source/README.md`, to samo
   `consolidated_text_as_of` już przyjęte dla całej normalizacji), plus
   pkt 3 dla dwóch plików. Bez zmiany istniejącej treści merytorycznej.

## Alternatives

- **Przyjąć LegalRuleML XML wprost** (parsować/emitować `<lrml:...>`).
  Odrzucone: ciężar implementacyjny (parser XML + walidacja względem XSD
  LegalRuleML) nieproporcjonalny do 15 reguł w MVP; koliduje z
  PROJECT_CONCEPT.md/AGENTS.md sekcja 59 (prosty parser na start).
  Pozostaje możliwe jako format eksportu w Phase 3+, jeśli zajdzie
  potrzeba interoperacyjności z zewnętrznym silnikiem LegalRuleML.
- **Zostać bez schematu, tylko konwencja w dokumentacji.** Odrzucone:
  to jest dokładnie stan, który audyt zidentyfikował jako blokujący
  sensowne testy — konwencja nieegzekwowana mechanicznie już raz
  doprowadziła do rozjazdu między 15 plikami.
- **Jeden sztywny wspólny kształt dla wszystkich `norm_type`.** Odrzucone:
  wymusiłoby albo puste pola-atrapy (np. `items: []` dla `STRUCTURAL`),
  albo utratę realnych różnic semantycznych (AGENTS.md sekcja 56).

## Consequences

- Każda przyszła reguła musi przejść walidator przed commitem (nowy krok
  w workflow z AGENTS.md sekcja 46/40 — dodać do `docs/agent-workflow.md`).
- Retrofit 15 plików to małe, mechaniczne zmiany (dodanie 1 bloku), commit
  osobno od tej ADR i osobno od walidatora (AGENTS.md sekcja 37).
- `strength`/`overridden_by` zostają w słowniku, ale used sparingly —
  ryzyko do pilnowania: nie zacząć dodawać ich "na wszelki wypadek" przy
  przyszłych regułach bez realnej podstawy w tekście/konflikcie.
- Nie blokuje planowanego na koniec spike'u Catala (`R-PS-0003`) — schemat
  YAML jest wejściem do ręcznego tłumaczenia, nie zależy od niego.

## Status

ACCEPTED — 2026-09-28.
