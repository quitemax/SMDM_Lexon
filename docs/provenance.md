# Provenance

STATUS: DRAFT — opisuje działający łańcuch, zweryfikowany w praktyce
(nie hipotezę).

## Łańcuch (jak faktycznie działa)

```
RULE (rules/R-PS-0015.yaml)
    source.normalized_ref: "PS-ART-015"
    ↓
eId="art_15" w normalized/akoma-ntoso/prawo-spoldzielcze.xml
    ↓
<article eId="art_15"><num>Art. 15.</num>...</article>
    ↓
tekst źródłowy verbatim (§1-§5)
    ↓
external/SMDM_Knowledge_Base/przepisy-prawne/md/ustawa-prawo-spoldzielcze.md
    (submodule, pinned commit — patrz law/prawo-spoldzielcze/source/README.md)
```

Każda reguła/procedura ma pole `source` z co najmniej:

```yaml
source:
  act: "Prawo spółdzielcze"
  article: "15"          # numer artykułu (i opcjonalnie paragraf/punkt)
  normalized_ref: "PS-ART-015"   # klucz cytowania
```

## Klucz cytowania `PS-ART-NNN` ↔ `eId`

**Niespójność do wiedzenia (nie błąd, ale pułapka):** `docs/dsl.md`
dokumentuje `PS-ART-NNN` z zerami wiodącymi do 3 cyfr (`PS-ART-015`), ale
`eId` w pliku AKN **nie ma dopełnienia zerami** (`art_15`, nie `art_015`).

Reguła rozwiązywania: **usuń zera wiodące z części numerycznej, potem
dodaj prefiks `art_`, potem dołóż sufiks literowy małymi literami**.

```
PS-ART-015   -> art_15
PS-ART-016A  -> art_16a
PS-ART-024   -> art_24
```

Każdy skrypt walidujący (jak te używane przy weryfikacji normalizacji)
musi to uwzględnić — sprawdzone empirycznie: naiwne dopełnienie zerami po
stronie `eId` daje fałszywe alarmy o "martwych referencjach", które nie
są prawdziwe. Ta reguła jest teraz też zaimplementowana (nie tylko
opisana) w `schema/validate_rules.py` (`normalized_ref_to_eid`), które
uruchamiane jest przy każdej walidacji `rules/`/`procedures/` — patrz
`docs/decisions/ADR-0002-unified-rule-schema.md`.

## Wiele źródeł na jedną regułę

AGENTS.md sekcja 13 — jeśli reguła wymaga kilku artykułów, `normalized_ref`
jest listą:

```yaml
source:
  act: "Prawo spółdzielcze"
  article: ["16", "17"]
  normalized_ref: ["PS-ART-016", "PS-ART-017"]
```

Przykład: `procedures/R-PS-0003-membership-admission.yaml`.

## Odesłania między regułami (nie tylko do tekstu)

Oprócz `source` (odesłanie do tekstu), reguły mogą jawnie odsyłać do
innych reguł/obserwacji w polach `note`, `scope_note`, `related_rules`:

- `rules/R-PS-0011.yaml` (Art. 5 §1 pkt 5 — wymagana treść statutu)
  odsyła do `R-PS-0003`, `R-PS-0016` jako konkretyzacji tego wymogu.
- `procedures/R-PS-0003.yaml`, `R-PS-0016.yaml` mają `scope_note` odsyłający
  do `interpretations/OBS-0001-lex-specialis-usm-membership.md`.

To są dziś **pola tekstowe (proza), nie ustrukturyzowany graf** —
PROJECT_CONCEPT.md sekcja 26 i 43 przewidują docelowo prawdziwy "legal
provenance graph" (węzły + typowane krawędzie AMENDS/REFERENCES/EXCEPTS/...,
patrz `docs/LEXON_CONTEXT.md` sekcja 11). Nie zbudowany — świadomie
odnotowany dług, nie pomyłka.

## Przypisy źródłowe (footnotes) jako provenance

Tekst ustawy sam niesie przypisy o historii legislacyjnej (np. Art. 108a:
uchylenie z 2003 r. utraciło moc wyrokiem TK z 2005 r.). Zachowywane w
AKN jako `<lexon:note>` (przypis do całej jednostki) albo `<authorialNote>`
(przypis inline, standardowy element AKN) — nigdy pomijane. Patrz
`normalized/akoma-ntoso/README.md` po pełną listę i uzasadnienie każdego
wyboru między tymi dwoma.
