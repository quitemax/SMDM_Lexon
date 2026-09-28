# normalized/

Tekst aktu podzielony na jednostki normatywne (artykuł / § / punkt) ze stabilnymi
identyfikatorami źródłowymi, bez formalizacji semantycznej — czysta segmentacja.

Zawiera Art. 1–28: Dział I (Spółdzielnia i jej statut, Art. 1–5), Dział II
(Tryb zakładania i rejestrowania spółdzielni, Art. 6–14, w tym 8a i 12a) oraz
Dział III (Członkowie, ich prawa i obowiązki, Art. 15–28, w tym 16a). Jeden
plik YAML na artykuł (`art-NNN[litera].yaml`), klucz `PS-ART-NNN` (patrz
`docs/dsl.md`). Artykuły uchylone (Art. 4, 8, 8a, 9, 10, 12, 13, 23) są
pustymi jednostkami-tombstone (`repealed: true`) — zachowane, żeby luki w
numeracji były jawne, a nie milczące. Art. 6 §3–§6 są uchylone na poziomie
paragrafu, nie całego artykułu — reprezentowane analogicznie
(`repealed: true` na paragrafie).

Art. 1 §1 zawiera legalną definicję Spółdzielni — na razie tylko
znormalizowany tekst; pełna formalizacja jako `ontology/entities/spoldzielnia.yaml`
(czyli docelowo "klasa" w rozumieniu modelu danych) jest zaplanowana na
Phase 2, gdy przyjdzie kolej na reguły dla Działu I/II (patrz ROADMAP.md).

Źródło i przypięta wersja: `../source/README.md` (Dz.U. 2026 poz. 521,
stan na 2026-03-23).
