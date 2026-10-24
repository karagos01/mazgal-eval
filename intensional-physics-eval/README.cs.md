# Intensional Physics Computing + openQL v1.1 — nezávislé vyhodnocení

Reprodukovatelné vyhodnocení dvou depositů z 8. října 2026: M. Mazgal,
*Intensional Physics Computing: Generating Virtual Reality via Multidimensional
Tensor Core Queries* (DOI
[10.5281/zenodo.23241777](https://doi.org/10.5281/zenodo.23241777)) a
*openQL / openOL … (Version 1.1)* (DOI
[10.5281/zenodo.23241148](https://doi.org/10.5281/zenodo.23241148)), což je
revize originálu z 3. října. Jsou vyhodnocené společně, protože ani jeden
nestojí sám.

Text je v [`PAPER.cs.md`](PAPER.cs.md), anglicky v [`PAPER.md`](PAPER.md).

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`README.md`](README.md) a [`PAPER.md`](PAPER.md).

**Polovina toho hlavního nového tvrzení je správná, a tím je třeba začít.** §5
v IPC tvrdí „millions of physical queries per millisecond" — tedy 10⁹/s. Pro
uzel 4×4 z §3 je svazující strop na kartě, kterou autorovy vlastní preprinty
specifikují, **1,46·10¹⁰/s**, takže se to vejde s **14,6× rezervou** — je to
první numerické hardwarové tvrzení v téhle sérii, které aritmetika podpírá. Pro
uzel 112×112 z téže věty je strop 1,87·10⁷/s, tedy mimo **54×**.

**Ale pro vlastní aplikaci ta rychlost nedostačuje.** §4 dělá z každého kroku
raymarchingu dotaz, takže rozpočet je na pixel na snímek: 10⁹/s koupí **8,0
kroku na pixel** při 1080p60, proti 64–256, které volumetrický raymarching
potřebuje — tedy **4 až 32× nízko**, ještě než který krok udělá nějakou fyziku.

**openQL v1.1 vypustila čtyři tvrzení, která tohle vyhodnocení měřilo**, spolu
se všemi pěti glosami u referencí a klíčovým slovem „octonions" — zatímco
abstrakt pořád transformuje „quaternion and octonion algebra into unified block
matrices". Ta shoda je zaznamenaná; příčinnost se netvrdí, protože revize nemá
changelog. Její jediná nová sekce, §6.1, tvrdí „millions of topologies per day"
na mřížce s milionem uzlů, což nechává **14–140 update sweepů** na kandidáta pro
vázanou multifyzikální účelovou funkci.

## Co je potřeba

```
python3 -m pip install -r requirements.txt   # jen numpy
```

Bez GPU, bez sítě. Hardwarové údaje jsou katalogové specifikace RTX 3090, kterou
preprinty samy jmenují.

## Reprodukce výsledků

```
./run_all.sh          # všechno, asi sekunda na jakémkoli CPU
```

| Skript | Co spočítá | Sekce |
|---|---|---|
| [`queries.py`](queries.py) | uvedená rychlost dotazů proti výpočetnímu a propustnostnímu stropu pro oba uzly; obsazenost dlaždice; rozpočet raymarchingu; co stál NeRF; ta formulace o symplektičnosti | §§2–3 |
| [`bldc.py`](bldc.py) | co stojí jedno vyhodnocení topologie, kolik sweepů nechává „millions per day", co zero-branching skutečně vynáší, a tvrzení o kožním efektu | §4 |
| [`versions.py`](versions.py) | diff v1.0 → v1.1, co bylo vypuštěné a přidané, a co zůstalo | §5 |

`versions.py` je záznam, ne výpočet, a je držený jako skript, aby se ten seznam
objevil v `results.log` vedle aritmetiky. Každá hodnota je
v [`constants.py`](constants.py) s **příznakem provenience** — `[P]`
z preprintů, `[V]` ověřeno proti pojmenovanému zdroji, `[A]` předpokládaný
rozsah, který se proměřuje. Celý výstup jednoho běhu je
v [`results.log`](results.log).

## Klíčová čísla

| co | publikováno | naměřeno / spočítáno |
|---|---|---|
| uvedená rychlost dotazů | „millions of physical queries per millisecond" | 10⁹/s |
| uzel 4×4, svazující strop | — | **1,46·10¹⁰/s — tvrzení se vejde, 14,6×** |
| uzel 112×112, svazující strop | tatáž věta | 1,87·10⁷/s — **mimo 54×** |
| co svazuje v obou případech | „natively processed by Tensor Cores" | propustnost paměti, ne výpočet |
| uzel 4×4 v tensor-core dlaždici 16×16 | jeden uzel na jedno MMA | **6,2 % obsazenost** |
| 112×112 v téže dlaždici | — | 100 % — 112 = 7 × 16 přesně |
| kroků marchingu, které uvedená rychlost koupí při 1080p60 | „absolute real-time" | **8,0 na pixel** |
| co volumetrický raymarching potřebuje | — | 64–256, takže ta rychlost je **4–32× nízká** |
| NeRF, citovaný jako předchůdce | „theoretical predecessor" | 150–200 M dotazů/obrázek, **30 s/snímek** |
| σ(W·S + b) v IPC §3 | „a **symplectic** discrete Hamiltonian operator" | openQL v1.0 říkal „preserves the Lie group symmetries"; výraz je nezměněný a byl vyvrácený v `openql-eval` |
| „symplectic" v pracích citovaných kterýmkoli preprintem | — | **1**, a to o Freudenthalově prostoru pro E₇ |
| stav mřížky v §6.1 v1.1 | „a million-node grid" | 274,7 MiB; jeden sweep 549,3 MiB = 0,615 ms |
| sweepů na kandidáta při „millions per day" | „circumvents this limit" | **14 až 140** — asi jeden multigridový lineární solve |
| co ta účelová funkce musí skutečně pokrýt | — | pole, zvlnění momentu, cogging podle úhlu rotoru, hysterezní ztráty z B–H, vázaná tepelná úloha |
| zero-branching | to, co ten limit obchází | pravda, ale je to ztráta řídkosti: penalta **2× až 100×** proti řídkému solveru |
| „fractal-like winding patterns that minimize skin effect" | tvrzeno | zavedená náprava vodič dělí (Litz); fraktální hranice přidává obvod při konstantním průřezu |
| tvrzení vypuštěná ve v1.1, která tohle vyhodnocení měřilo | — | **4 ze 6 vypuštění** |
| ORCID placeholder v hlavičce PDF | — | pořád nevyplněný, **znovu vygenerovaný česky** |
| tvar 12D uzlu | openQL: 12×12 ze tří bloků 4×4 | IPC §3: „a 4×4 (for 12D macroscopic physics)" |

## Rozsah

Ani jeden deposit nepřikládá kód, měření ani obrázky. §6 textu vypisuje, co se
neměří — intenzionálně-výpočetní rámování je pozice o reprezentaci, ne
kvantitativní tvrzení — a §7 hranice: ty stropy jsou teoretické špičky, což
nálezy „přesahuje kartu" zesiluje a nález „vejde se" oslabuje, byť 14,6× rezervy
přežije jakýkoli reálný koeficient účinnosti.

Měření openQL v1.0, na která se tady odkazuje, se tu nereprodukují; žijí
v [`openql-eval`](https://github.com/karagos01/openql-eval) a verdikty
u referencí v [`reference-audit`](https://github.com/karagos01/reference-audit).

## Doprovodná vyhodnocení

- [`openql-eval`](https://github.com/karagos01/openql-eval) — originál openQL / openOL v1.0, který tyto dva deposity převyprávějí a revidují
- [`reference-audit`](https://github.com/karagos01/reference-audit) — jestli všech 81 citací ve všech 18 depositech říká to, pro co je citovaných
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — matrice kvantové biofortifikace a in-situ phytominingu z října 2026
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — dvoušálový signál a nabíjení HFRS z října 2026
- [`hemocyanin-eval`](https://github.com/karagos01/hemocyanin-eval) — hemocyaninová fyziologie na měďi z října 2026
- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — oktonionová dvouvrstvá šablona s asociátorem a census Maxwellovy atribuce
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — 2bitový inferenční engine pro LLM
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — trilogie CQFT / PCTP / SOTP ze září 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — cymatická stimulace průduchů a pulzní osvětlení z října 2026
- [`openomega-eval`](https://github.com/karagos01/openomega-eval) — openOmega, antimaterie a sedeniony z října 2026
- [`hospv-eval`](https://github.com/karagos01/hospv-eval) — HOS-PV 2.0, singletní fise a spintronická fotovoltaika z října 2026

## Licence

Kód (všechny `*.py` a `run_all.sh`): MIT, viz `LICENSE`.
Text `PAPER.md` a `PAPER.cs.md`: CC BY 4.0.
