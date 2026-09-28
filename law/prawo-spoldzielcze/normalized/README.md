# normalized/

Tekst aktu podzielony na jednostki normatywne (artykuł / § / punkt) ze stabilnymi
identyfikatorami źródłowymi, bez formalizacji semantycznej — czysta segmentacja.

Zawiera Art. 1–34, czyli **Dział I, II i III w całości** (koniec Tytułu I.
Przepisy wspólne przed Działem IV — Organy spółdzielni):

- Dział I. Spółdzielnia i jej statut (Art. 1–5)
- Dział II. Tryb zakładania i rejestrowania spółdzielni (Art. 6–14, w tym 8a, 12a)
- Dział III. Członkowie, ich prawa i obowiązki (Art. 15–34, w tym 16a)

Jeden plik YAML na artykuł (`art-NNN[litera].yaml`), klucz `PS-ART-NNN` (patrz
`docs/dsl.md`). Artykuły uchylone (Art. 4, 8, 8a, 9, 10, 12, 13, 23, 33, 34)
są pustymi jednostkami-tombstone (`repealed: true`) — zachowane, żeby luki w
numeracji były jawne, a nie milczące. Art. 6 §3–§6 i Art. 29 §2 są uchylone
na poziomie paragrafu, nie całego artykułu — reprezentowane analogicznie
(`repealed: true` na paragrafie).

**Uwaga (2026-09-28):** Dział III formalizowano najpierw tylko do Art. 28
(błędne założenie, że tam się kończy) — Art. 29–34 dociągnięto później, gdy
spis treści z Knowledge Base ujawnił, że dział sięga do Art. 34. Reguły
(Phase 2) są na razie sformalizowane tylko dla Art. 15–28 z tego działu;
Art. 29–34 mają na razie wyłącznie normalizację (patrz ROADMAP.md).

Art. 1 §1 zawiera legalną definicję Spółdzielni — sformalizowaną już jako
`ontology/entities/spoldzielnia.yaml` (blok `definition`) i `rules/R-PS-0007.yaml`.

Źródło i przypięta wersja: `../source/README.md` (Dz.U. 2026 poz. 521,
stan na 2026-03-23).
