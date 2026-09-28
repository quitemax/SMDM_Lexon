# schema/

JSON Schema (2020-12) dla warstwy semantycznej. Waliduje rdzeń każdego
pliku w `law/<akt>/rules/` i `law/<akt>/procedures/` — patrz
`docs/decisions/ADR-0002-unified-rule-schema.md` i `docs/dsl.md`.

- `legal-rule.schema.json` — jedyny plik na razie. Wspólny dla `rules/`
  i `procedures/` (rozróżnienie przez `norm_type: PROCEDURE`), bo oba
  dzielą ten sam rdzeń provenance/validity/formalization_status.

- `validate_rules.py` — walidator (`jsonschema` + PyYAML). Uruchomienie:
  `py schema/validate_rules.py`. Sprawdza wszystkie pliki w
  `law/*/rules/*.yaml` i `law/*/procedures/*.yaml` względem
  `legal-rule.schema.json`, plus to, czego JSON Schema nie wyrazi:
  duplikaty `id`, `subject`/`holder`/`actors` rozwiązywalne do encji w
  `model/entities/` lub `law/<akt>/ontology/entities/`, `normalized_ref`
  rozwiązywalny do realnego `eId` w `normalized/akoma-ntoso/*.xml`.

Nie waliduje `ontology/`, `concepts/`, `interpretations/` — te mają
inny, prostszy kształt i nie były częścią audytu, który uzasadnił ten
schemat (patrz ADR-0002, Context).
