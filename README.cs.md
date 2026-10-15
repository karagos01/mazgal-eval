# openOmega — nezávislé vyhodnocení

Reprodukovatelné vyhodnocení práce M. Mazgal, *openOmega: Tensor Matrix
Architecture for Matter-Antimatter Symmetry in ±12D, ±112D, and ±224D Spaces*
(Zenodo, 9. října 2026, DOI
[10.5281/zenodo.23263528](https://doi.org/10.5281/zenodo.23263528)).

Text je v [`PAPER.cs.md`](PAPER.cs.md), anglicky v [`PAPER.md`](PAPER.md).

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`README.md`](README.md) a [`PAPER.md`](PAPER.md).

**Ta algebra je správná a tento repozitář to potvrzuje od základů.**
Cayley-Dicksonova věž je tu postavená z reálných čísel; konstrukce reprodukuje
učebnicovou klasifikaci přesně — ℍ asociativní, 𝕆 neasociativní ale alternativní,
sedeniony ani to — a multiplikativita normy platí do dimenze 8 a padá na 16, což
je právě důvod, proč se tam objeví dělitelé nuly. Sedenionový dělitel nuly se pak
najde hledáním: **(e₁ + e₁₀) × (e₄ − e₁₅) = 0**, přesně. Moreno (1998), reference
[3], je správný zdroj a je správně připnutý — vedle Fureyové v SOTP je to nejlépe
vybraná citace ze sedmnácti autorových depositů.

**Ale engine ty sedeniony pro tu vlastnost, kterou chce, nepotřebuje.** Vlastní
rovnice §3 je o **maticích** a dělitelé nuly jsou v každé maticové algebře nad
tělem naprosto běžní: [[1,0],[0,0]]·[[0,0],[0,1]] = 0 je nejmenší případ
a **200 ze 200** náhodně zkonstruovaných nenulových párů 224×224 tu dává nulu.
**A z toho součinu energie vypadnout nemůže** — ‖A‖ = 34,1, ‖B‖ = 221,9,
‖A·B‖ = **4,1·10⁻¹³**. Aby engine vyzářil E = mc², musí si obě velikosti přečíst
před násobením a pak registr porovnat s nulou, což je právě to `if (collision)`,
o kterém §3 říká, že není potřeba: ta podmínka se přesune, neodstraní.

**224 v Cayley-Dicksonově věži není** (ta jsou mocniny dvou, sedeniony jsou
šestnáctirozměrné), **jeden součin 224×224 je 269 taktů celé GPU** a ne jeden,
a **roofline výsledek zdvojení přežije** — maticová forma a kódovaný stav mají na
každé vrstvě totožnou aritmetickou intenzitu, zatímco matice stojí d× provozu.

## Co je potřeba

```
python3 -m pip install -r requirements.txt   # jen numpy
```

Bez GPU, bez sítě. Algebra se staví od nuly; hardwarové údaje jsou katalogové
specifikace RTX 3090, kterou jmenuje vlastní série preprintů.

## Reprodukce výsledků

```
./run_all.sh          # všechno, asi 20 sekund na jakémkoli CPU
```

| Skript | Co spočítá | Sekce |
|---|---|---|
| [`dimensions.py`](dimensions.py) | jestli je 224 v Cayley-Dicksonově věži; tvrzení o násobku šestnácti, dlaždice a obsazenost; „negativní dimenze" jako mohutnost; kritické dimenze, které citovaná fyzika používá | §4 |
| [`zerodivisors.py`](zerodivisors.py) | Cayley-Dicksonova věž postavená z reálných čísel a zkontrolovaná proti učebnicové klasifikaci; sedenionový dělitel nuly nalezený hledáním; dělitelé nuly v maticových algebrách; jestli ten součin zachovává energii; asociativita, kterou architektura potřebuje | §§1–3, 6 |
| [`hardware.py`](hardware.py) | tvrzení o „jednom taktu"; nároky na pamět a rezidentní uzly; kroková frekvence pro fixní mřížku; roofline; co to zdvojení stojí proti openQL | §5 |

Každá hodnota je v [`constants.py`](constants.py) s **příznakem provenience** —
`[P]` z preprintu, `[V]` ověřeno proti pojmenovanému zdroji, `[A]` předpokládaná
hodnota nebo volba prezentace — a žádný další skript žádnou nedefinuje. Celý
výstup jednoho běhu je v [`results.log`](results.log).

## Klíčová čísla

| co | publikováno | naměřeno / spočítáno |
|---|---|---|
| sedeniony mají dělitele nuly | „so-called zero divisors emerge" | **správně** — 168 párů nalezeno mezi e_i ± e_j |
| první nalezený | — | **(e₁ + e₁₀) × (e₄ − e₁₅) = 0**, přesně |
| proč se objeví na 16 a ne níž | — | multiplikativita normy přesná do dim 8, **1,1·10⁻²** na 16 |
| vlastní kontrola té konstrukce | — | ℍ asociativní, 𝕆 alternativní, sedeniony ani to — učebnicová klasifikace reprodukovaná |
| reference [3], Moreno 1998 | citován pro dělitele nuly | **přesná a správně připnutá** |
| jsou dělitelé nuly exotičtí? | „This 'anomaly'" | ne — **200 ze 200** nenulových párů 224×224 s A·B = 0 |
| nejmenší příklad téže vlastnosti | — | [[1,0],[0,0]] · [[0,0],[0,1]] = 0 |
| unese ten součin energii? | „release of an absolute tensor vector into the energy register" | ‖A‖ = 34,1, ‖B‖ = 221,9, **‖A·B‖ = 4,1·10⁻¹³** |
| je ta podmínka odstraněná? | „requires no conditional script like `if (collision)`" | ne — test registru proti nule **je** ta podmínka |
| 224 v Cayley-Dicksonově věži | „By introducing the Cayley-Dickson construction" | **ne** — věž je 1, 2, 4, 8, 16, 32, … |
| dimenze sedenionů | „the mathematical foundation of the −224D space" | **16** |
| odkud 224 skutečně je | „dimensional doubling" | 2 × 112, a 112 už v sérii nemá přežívající odvození |
| 224 / 16 | „a perfect multiple of 16 (224 ÷ 16 = 14)" | **správně**, 14 přesně, 100% obsazenost dlaždic |
| 112 / 16 | — | 7 taky přesně — to zarovnání je **dědičné**, ne získané |
| MMA operací na uzel 224D | „a single processor clock cycle" | **196 dlaždic** |
| takty pro jeden součin 224×224 | „a single processor clock cycle" | **269,1 taktu celé GPU** |
| totéž na 112D | openQL tvrdila totožně | 33,6 — takže 224 je **8× horší** |
| uzel ±224D se zrcadlem | — | **196,0 KiB**; do 24 GiB se vejde 128 397 párů, krychle 50 uzlů |
| proti tokamaku z §5, 1 mm³ při 10²⁰ m⁻³ | „exact plasma behavior" | chybí **778 834×** (5,9 řádu) |
| milionuzlová mřížka při ±224D | — | 186,9 GiB — **na kartu se nevejde** |
| největší mřížka, která se vejde, kroková frekvence | — | **18,2 Hz**; real-time je 60 |
| maticová forma proti kódovanému stavu | „natively processed by Tensor Cores" | totožný FLOP/bajt na každé vrstvě: 6,0, 56,0, **112,0** |
| cena kroku od openQL | předložena jako bezplatná | **4×** pamět, **8×** aritmetika, **4×** dlaždice, a pak zrcadlo pamět zdvojí znovu |
| „negativní dimenze" | ±12D, ±112D, ±224D | dimenze je mohutnost; největší vrstva je **448**rozměrný stav |
| 224 proti kritickým dimenzím | „contains complete string theory" | superstruny 10, bosonová 26, M-teorie 11 — **ani jedna není 224** |
| co potřebuje architektura proti tomu, co potřebuje mechanismus | tvrzeno v po sobě jdoucích sekcích | WMMA je **asociativní**; sedeniony nejsou ani alternativní |
| hyperkomplexní slovník | — | vrací se po šesti depositech: octonion 1, **sedenion 5**; „causal" pořád 0 |
| „Theory of Everything" | v abstraktu | první výskyt v celé sérii |

## Rozsah

Deposit je krátký preprint pod CC BY 4.0 bez kódu, bez měření a bez obrázků.
§7 textu vypisuje, co se neměří — tvrzení o Theory of Everything, fázově
konjugovaný radar, sonoluminiscence a aplikace na temnou hmotu — a říká proč,
místo aby je vydával za vady.

§8 vypisuje hranice. Cayley-Dicksonova konstrukce používá jednu z několika
znaménkových konvencí; jiná permutuje, které konkrétní páry jsou dělitelé nuly,
ale ne dimenzi, v níž se objeví, a právě proto je ta klasifikační tabulka
uvedená jako kontrola. Dřívější verze tohoto repozitáře měla chybný vzorec pro
druhou složku a ta tabulka to odhalila tím, že kvaterniony vyšly neasociativní.
Dřívější verze měla taky degenerovanou tabulku krokové frekvence, zaplněnou do
kapacity karty, kde každá vrstva vracela totéž z konstrukce; teď se počítá nad
fixní mřížkou.

Měření openQL, na která se tady odkazuje, se tu nereprodukují; žijí
v [`openql-eval`](https://github.com/karagos01/openql-eval) a verdikty
u referencí v [`reference-audit`](https://github.com/karagos01/reference-audit).

## Doprovodná vyhodnocení

- [`openql-eval`](https://github.com/karagos01/openql-eval) — originál openQL / openOL, který tento deposit rozšiřuje
- [`intensional-physics-eval`](https://github.com/karagos01/intensional-physics-eval) — Intensional Physics Computing a openQL v1.1 z října 2026
- [`reference-audit`](https://github.com/karagos01/reference-audit) — jestli všech 81 citací ve všech 18 depositech říká to, pro co je citovaných
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — matrice kvantové biofortifikace a in-situ phytominingu z října 2026
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — dvoušálový signál a nabíjení HFRS z října 2026
- [`hemocyanin-eval`](https://github.com/karagos01/hemocyanin-eval) — hemocyaninová fyziologie na měďi z října 2026
- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — oktonionová dvouvrstvá šablona s asociátorem a census Maxwellovy atribuce
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — 2bitový inferenční engine pro LLM
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — trilogie CQFT / PCTP / SOTP ze září 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — cymatická stimulace průduchů a pulzní osvětlení z října 2026
- [`hospv-eval`](https://github.com/karagos01/hospv-eval) — HOS-PV 2.0, singletní fise a spintronická fotovoltaika z října 2026

## Licence

Kód (všechny `*.py` a `run_all.sh`): MIT, viz `LICENSE`.
Text `PAPER.md` a `PAPER.cs.md`: CC BY 4.0.
