# HOS-PV 2.0 — nezávislé vyhodnocení

Reprodukovatelné vyhodnocení práce M. Mazgal, *HOS-PV 2.0: Exceeding the
Shockley-Queisser Limit via Chiral-Induced Spin Selectivity, Dexter-Sensitized
Singlet Fission, and Altermagnetic Carrier Extraction* (Zenodo, 14. října 2026,
DOI [10.5281/zenodo.23364732](https://doi.org/10.5281/zenodo.23364732)).

Text je v [`PAPER.cs.md`](PAPER.cs.md), anglicky v [`PAPER.md`](PAPER.md).

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`README.md`](README.md) a [`PAPER.md`](PAPER.md).

**Ten mechanismus je v pořádku a ta hranice se skutečně posouvá — a tento
repozitář to potvrzuje od základů.** Model detailní rovnováhy je tu postavený
ze spektra ASTM G173-03 a Planckova zákona a než se použije, reprodukuje tři
publikované hodnoty: Shockleyho-Queisserovu hranici (**33,77 %** při 1,335 eV
proti 33,7 % při 1,34 eV), limit multiplikace nosičů z vlastní reference [5]
toho preprintu (**44,62 %** proti 44,4 %) a hodnotu téže skupiny pro
multiplikaci zastropovanou na dva nosiče na foton, což je právě to, co dělá
singletní fise (**42,09 %** při 0,94 eV proti 42,0 % při 0,95 eV). Týž kód pak
staví tu architekturu na **41,24 %**, což překonává Shockleyho-Queissera
o **7,5 bodu**. Překročení hranice není to, co je tady špatně.

**Ale 45,9 % je řádek dvoupřechodového tandemu v práci, z níž je to citované.**
Nejlepší, co tahle rodina modelů umí při *jakékoli* dvojici energií, je 42,09 %,
takže na 45,9 % nedosáhne žádný donor ani akceptor. Abstrakt reference [5] dává
33,7 % pro jeden přechod bez multiplikace, **44,4 % pro jeden přechod s ní** a
**45,7 %–47,7 % pro ideální dvoupřechodový tandem** — a 45,9 % padá do rozsahu
toho tandemu. Přitom být jedním přechodem je celá prodejní teze té architektury.

**A vysokoenergetický kanál je nad stropem svého vlastního mechanismu.** Fotony
nad 2,25 eV nesou po jednom elektronu jen **9,76 mA/cm²** náboje, takže uvedených
23,8 mA/cm² potřebuje **2,44 elektronu na absorbovaný foton**; singletní fise dá
nejvýš dva. S vlastními kvantovými účinnostmi preprintu je naměřený J_sc
**43,83 mA/cm²**, ne 52,3, a PCE **29,8 %**, ne 35,6 %. V tom čísle je shoda,
pro kterou se ta práce vyplatila: obyčejný absorbér 1,12 eV s EQE = 1 a vůbec
bez fise sbírá **43,81 mA/cm²** — totéž číslo na 0,1 %. Ta multiplikace zaplatí
za 0,85, za 0,92 a za 0,90 a nic víc, a skutečný zisk té architektury je v tom,
že sbírá křemíkový proud při křemíkovém napětí a ty ztráty přitom pohltí.

## Co je potřeba

```
python3 -m pip install -r requirements.txt   # jen numpy
```

Bez GPU, bez sítě. `data/ASTMG173.csv` je přiložené a před použitím se kontroluje
proti sha256 zapsanému v `constants.py`; [`fetch_data.sh`](fetch_data.sh) ho
znovu odvodí z publikovaného wheelu pvlib a porovná bajt po bajtu, znovu se
dotáže na ty čtyři atomové hladiny v NIST a vytáhne text preprintu pro
`census.py`.

## Reprodukce výsledků

```
./run_all.sh          # všechno, asi deset sekund na jakémkoli CPU
```

| Skript | Co spočítá | Sekce |
|---|---|---|
| [`spectrum.py`](spectrum.py) | spektrum, jeho integrál, obě fotonové hranice a census termalizace / podprahového průchodu, který cituje úvod | §1 |
| [`photocurrent.py`](photocurrent.py) | oba kanály integrálu J_sc proti vlastním účinnostem preprintu; strop každého z nich; odkud by publikované číslo mohlo pocházet; přepočtenou účinnost; jestli 220 nm stačí na oba pásy | §6.2 |
| [`detailed_balance.py`](detailed_balance.py) | model detailní rovnováhy, tři self-checky, vlastní hranici té architektury, tvrzení o 45,9 %, V_oc, implikovaný výtěžek elektroluminiscence a strop plnícího faktoru | §§2.2, 6.2 |
| [`spin.py`](spin.py) | vzorec potlačení, η_PB proti jeho vlastním časům, proměření pohyblivosti, spinově statistickou základní linii, k čemu zavazuje tanh(ΔE/2kT), a exponent Z⁴ měřený proti datům NIST | §§3, 4 |
| [`materials.py`](materials.py) | energetické okénko fise proti proměřeným chromoforům, Néelovu teplotu altermagnetu proti provozní teplotě modulu, specifický výkon stohu z tabulky 1 a rozpočet na sériový odpor | §§2.2, 5, tabulka 1 |
| [`census.py`](census.py) | slovník série v tomhle depositu | forma |
| [`consistency.py`](consistency.py) | veličiny, kterým preprint přiřazuje dvě různé hodnoty, každou přepočtenou z jeho vlastních čísel, a aritmetické kroky, které vychází | §§2, 4, 6.2, tabulky 1 a 2 |

Každá hodnota je v [`constants.py`](constants.py) s **příznakem provenience** —
`[P]` z preprintu, `[V]` ověřeno proti pojmenovanému zdroji, `[A]` předpokládané
a proměřované — a žádný další skript žádnou nedefinuje. Celý výstup jednoho
běhu je v [`results.log`](results.log).

## Klíčová čísla

| co | publikováno | naměřeno / spočítáno |
|---|---|---|
| Shockleyho-Queisserova hranice, jako self-check | 33,7 % při 1,34 eV | **33,77 % při 1,335 eV** |
| limit jednoho přechodu z reference [5], jako self-check | 44,4 % při 0,70 eV | **44,62 %** |
| totéž jen pro zdvojení, jako self-check | 42,0 % při 0,95 eV | **42,09 % při 0,94 eV** |
| tato architektura při jejích vlastních dvou energiích | — | **41,24 %**, o 7,5 bodu nad SQ |
| uvedená hranice | „45,9 %" | **nad stropem 42,09 % toho modelu** |
| kde v referenci [5] 45,9 % je | citováno jako jeden přechod | rozsah **dvoupřechodového tandemu**, 45,7–47,7 % |
| EQE_high = 1,85 × 0,92 × 0,90 | „153 %" | **1,5318, správně** |
| IR kanál, 1,12–2,25 eV, při EQE 0,85 | 28,5 mA/cm² | **28,89, správně na 1,3 %** |
| fotony nad 2,25 eV, po jednom elektronu | — | **9,76 mA/cm²** |
| SF kanál, nad 2,25 eV | 23,8 mA/cm² | **14,95** — tvrzení potřebuje **2,44 e⁻/foton** |
| hranice, která by 23,8 dala | „nad E(S₁) = 2,25 eV" | **1,96 eV / 634 nm**, posun o 294 meV |
| celkem J_sc | 52,3 mA/cm² | **43,83** |
| PCE | „35,58 %" | **29,82 %**; sama aritmetika je konzistentní |
| obyčejný absorbér 1,12 eV, EQE = 1, bez fise | — | **43,81 mA/cm²** — kaskáda vrací totéž na 0,1 % |
| V_oc v radiačním limitu při 1,12 eV | „0,90 V" | **0,8834 V** se zdvojením |
| ΔV_oc,nr z 0,22 V na 0,09 V | tvrzeno | **×158 ve výtěžku elektroluminiscence**, 0,02 % → 3 % |
| plnící faktor | 84,0 % | strop ideální diody **86,2 %** — dosažitelné, jak je uvedeno |
| podíl vlastního radiačního limitu | — | **86,3 %**, proti 92,9 % u c-Si a 59,3 % u dnešní OPV |
| β_eff = β_L(1 − η_PB P²) při 0,85 a 0,95 | „0,314, potlačení 68,6 %" | **správně, jak je napsáno** |
| η_PB z časů téže věty | „0,95" | **0,984–0,996**, tedy 72,0 % — v prospěch preprintu |
| potlačení přes rozsah pohyblivosti | 68,6 % | **39,5 % až 71,8 %**; 20–80 ns chce µ = 3,8e-3 až 1,5e-2 cm²/Vs |
| achirální spinově statistická základní linie | — | **0,250 β_L**, pod chirálními 0,314 β_L |
| rozštěpení, které implikuje P_CISS = 0,85 při 300 K | — | **64,5 meV**, a potlačení pak klesá na 57,3 % při 85 °C |
| ξ_SOC ∝ Z⁴ | tvrzeno | **exponent 1,69** naměřený na halogenových rozštěpeních z NIST |
| E(S₁) ≥ 2E(T₁) s vlastními 2,25 a 1,15 | „must satisfy" | **padá o 50 meV**; ta fise je endotermická o 1,9 kT |
| chromofory splňující E(T₁) ≥ 1,12 a E(S₁) ≥ 2E(T₁) | TIPS-tetracen, DPP | pentacen, tetracen a rubren padají každý na jedné; **rubren míjí o 70 meV** |
| spinové rozštěpení altermagnetického kolektoru | „~0,8 eV" | **0,37–0,80 eV naměřeno pro MnTe: správně** |
| Néelova teplota MnTe proti teplotě modulu | neuvedeno | **267–307 K** proti 318–332 K v provozu |
| specifický výkon stohu z tabulky 1 | „≥ 10 000 W/kg" | **2944 W/kg**, 2815–3087 přes proměření: nižší **3,4×** |
| hmotnost, která nedělá fyziku | — | **97,7 %** — 75 µm polymeru; bylo by potřeba 19 µm |
| rozpočet R_s na jeden bod FF při 52,3 mA/cm² | — | **0,155 Ω·cm²**, o 22 % utaženější než u křemíku |
| slovník ostatních sedmnácti depositů | — | **nulový výskyt**: žádný tensor, hyperkomplex, causal ani GPU |
| ORCID placeholder, autocitace, spoluautor AI | — | **nic z toho** — první deposit z osmnácti se všemi třemi |
| veličiny, kterým preprint sám přiřazuje dvě hodnoty | — | **8**, nejvíc o faktor **12,4**, dvě z nich v jeho prospěch |
| aritmetické kroky, které provede správně | — | **8 z 8** — algebra neselhává nikdy, jen čísla, která se do ní vloží |

## Rozsah

Deposit je krátký preprint pod CC BY 4.0 bez kódu, bez měření a bez obrázků.
§8 textu vypisuje, co se tady neměří — morfologii Dexterova přenosu, jestli se
chirální rozhraní v objemu vyhne námitce, kterou §3.1 vznáší proti elektrodovým
spinovým filtrům, zachování spinu v infračerveném kanálu, chybějící Thomasův
faktor dvě v hamiltoniánu z §3.2 a tunelovou bariéru nad rámec jejího odporového
rozpočtu — a říká proč, místo aby je vydával za vady.

§9 vypisuje hranice. Model detailní rovnováhy dává stropy, což zesiluje nález,
že jedno tvrzení leží nad jedním z nich, a neoslabuje nic na reprodukci tří
publikovaných hodnot. Zaznamenává taky tři chyby nalezené v tomhle vyhodnocení:
divergující Boseho faktor, který vracel 7 × 10¹² %, dokud ho nezachytila tabulka
self-checků; jednotku plošné hmotnosti chybnou o 10³; a počítání referencí, které
počítalo každý číslovaný seznam v těle textu.

Měření starších depositů, na která se tu odkazuje, se tu nereprodukují; verdikty
u referencí žijí
v [`reference-audit`](../reference-audit).

## Doprovodná vyhodnocení

- [`reference-audit`](../reference-audit) — jestli všech 81 citací ve všech 18 depositech říká to, pro co je citovaných
- [`openomega-eval`](../openomega-eval) — openOmega, antimaterie a sedeniony z října 2026
- [`intensional-physics-eval`](../intensional-physics-eval) — Intensional Physics Computing a openQL v1.1 z října 2026
- [`openql-eval`](../openql-eval) — tenzorová maticová architektura openQL / openOL
- [`phytomining-eval`](../phytomining-eval) — matrice kvantové biofortifikace a in-situ phytominingu z října 2026
- [`naion-hfrs-eval`](../naion-hfrs-eval) — dvoušálový signál a nabíjení HFRS z října 2026
- [`hemocyanin-eval`](../hemocyanin-eval) — hemocyaninová fyziologie na měďi z října 2026
- [`cymatic-eval`](../cymatic-eval) — cymatická stimulace průduchů a pulzní osvětlení z října 2026
- [`octonion-mppt-eval`](../octonion-mppt-eval) — oktonionová dvouvrstvá šablona s asociátorem a census Maxwellovy atribuce
- [`xternary-eval`](../xternary-eval) — 2bitový inferenční engine pro LLM
- [`causal-trilogy-eval`](../causal-trilogy-eval) — trilogie CQFT / PCTP / SOTP ze září 2026

## Licence

Kód (všechny `*.py`, `run_all.sh` a `fetch_data.sh`): MIT, viz `LICENSE`.
Text `PAPER.md` a `PAPER.cs.md`: CC BY 4.0.
`data/ASTMG173.csv` je tabulace ASTM G173-03 od NREL, jak ji distribuuje pvlib
(BSD 3-clause); viz [`data/README.md`](data/README.md).
