# Dual-Scale Waveform Optimization / HFRS — nezávislé vyhodnocení

Reprodukovatelné vyhodnocení práce M. Mazgal, *Dual-Scale Waveform Optimization
and Hysteretic-Fractal Resonant Stimulation (HFRS) for Minimizing Transport
Resistance in Na-ion Lattices* (Zenodo, 6. října 2026, DOI
[10.5281/zenodo.23186884](https://doi.org/10.5281/zenodo.23186884)).

Text je v [`PAPER.cs.md`](PAPER.cs.md), anglicky v [`PAPER.md`](PAPER.md).

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`README.md`](README.md) a [`PAPER.md`](PAPER.md).

**V tom pásmu nic není.** `F_micro` je specifikované jako „kHz to MHz" a má
„induce phonon-assisted tunneling"; nejnižší Ramanovsky aktivní mřížková linie
naměřená ve vrstevnaté oxidové katodě je 144 cm⁻¹ = **4,32 THz**, tedy mezi
**6,6 a 9,6 řádu** nad ním. Energeticky je hf při 1 MHz **6,3 milionu×** pod kT
při 300 K a sedm až osm řádů pod migrační bariérou sodíku 0,10–0,64 eV. A pásmo,
kde má článek vůbec faradaickou odezvu — půlkružnice přenosu náboje asi
1 Hz–1 kHz — se s `F_micro` **nepřekrývá vůbec**, takže proud tam teče
dvojvrstvou kapacitou a disipuje v sériovém odporu, což je právě to Jouleovo
teplo, kvůli kterému §1 existuje.

**Ale §5 je nejlépe argumentovaná sekce v kterémkoli ze sedmnácti autorových
depositů** a §1 textu to říká jako první: pojmenovává parazitní prvky
jelly-rollu i konfound teplo-versus-kinetika bez vyzvání a předepisuje planární
coin-cell a izotermickou kalorimetrii. To je přesně to, co by napsal recenzent.

## Co je potřeba

```
python3 -m pip install -r requirements.txt   # jen numpy
```

Bez GPU, bez sítě. Všechno je aritmetika nad vlastními parametry preprintu a nad
publikovanými hodnotami, protože deposit nepřikládá kód, měření ani obrázky.

## Reprodukce výsledků

```
./run_all.sh          # všechno, asi sekunda na jakémkoli CPU
```

| Skript | Co spočítá | Sekce |
|---|---|---|
| [`frequency.py`](frequency.py) | pásmo `F_micro` proti naměřeným mřížkovým módům, proti kT a migrační bariéře, proti pásmu přenosu náboje, a hloubka vniku, kterou §5 uvádí | §§2–3 |
| [`anomaly.py`](anomaly.py) | nadpis §2.2 proti jejímu tělu, jestli to kritérium přežije ohřev článku, a co našla vlastní pulzní citace práce | §4, §7 |
| [`throughput.py`](throughput.py) | vyhodnocení za den, strop daný životností vzorků, konfound stárnutí, datový tok DDS, a §6 proti skutečnému obsahu depositu | §§5–6 |

Každá konstanta je v [`constants.py`](constants.py) s **příznakem provenience** —
`[P]` z preprintu, `[V]` ověřeno proti pojmenovanému zdroji, `[A]` předpokládaný
rozsah, který se proměřuje, netvrdí se — a žádný další skript žádnou
nedefinuje. Celý výstup jednoho běhu je v [`results.log`](results.log).

## Klíčová čísla

| co | publikováno | naměřeno / spočítáno |
|---|---|---|
| pásmo `F_micro` | „kHz to MHz range" | 10³–10⁶ Hz |
| nejnižší naměřený mřížkový mód ve vrstevnaté oxidové katodě | „phonon-assisted tunneling" | 144 cm⁻¹ = **4,32 THz** |
| mezera na horní hranici pásma | — | **4 317 011×** (6,6 řádu) |
| mezera na dolní hranici pásma | — | 4,3·10⁹× (9,6 řádu) |
| hf při 1 MHz | — | 4,136·10⁻⁹ eV |
| kT při 300 K | — | 0,02585 eV, tedy **6 250 986×** víc |
| migrační bariéra Na | „lower activation barriers" | 0,10–0,64 eV, tedy **2,4·10⁷ až 1,5·10⁸×** kvantum |
| pásmo přenosu náboje v EIS | — | ~1 Hz – 1 kHz |
| překryv s `F_micro` | — | **0 Hz** |
| co v tom pásmu teče místo toho | „coherent ion intercalation" | posuvný proud dvojvrstvy, disipující jako I²R |
| nadpis §2.2 proti tělu | „Negative Differential Resistance" | dV/dI = R_i > 0 pro nabíjený článek vždy; tělo místo toho definuje kritérium účinnosti |
| ohřev I²R při vzestupu o 20 K | — | klesne **1,6–3,0×**, což je ta signatura, kterou §2.2 čte jako anomálii |
| hloubka vniku v aluminiu při 1 MHz | „skin-effect reflections" | **82 µm** proti folii 12–20 µm — správný závěr, nesprávný mechanismus |
| vyhodnocení/den, 8 článků při 1C | „in real physical time" | **96** |
| vyhodnocení z jedné sady vzorků | — | **4 000–24 000 celkem**, po 42–250 dnech |
| co obvykle potřebuje PSO | „hyperdimensional" prostor | 10⁴–10⁵ |
| DDS stream na článek | generovaný GPU | 20–200 MB/s — přenos dat, žádný floating point |
| §3 proti §4 o tom, kde se generuje | GPU / „local generative engine" | ty dvě sekce popisují různé stroje |
| §6 „Structure of Provided Data" | /Hardware, /Software, /Datasets | **1 soubor, 97 786 bajtů** — to PDF |
| licence | „CERN-OHL-S for hardware" v PDF | záznam nese jen CC BY 4.0 |
| jediná pulzní citace práce | citovaná vedle `F_micro` | identifikuje difuzi v pevné fázi, **0,25 Hz**, a dává přednost **spojité** rampě |
| hyperkomplexní slovník | — | Maxwell, octonion, quaternion, hypercomplex, non-associative, tensor, causal: **všechno 0** |

## Rozsah

Deposit je čtyřstránkový preprint pod CC BY 4.0 bez kódu, bez měření a bez
obrázků, takže není co benchmarkovat. §8 textu vypisuje hranice: Ramanovská
čísla jsou z lithiové NMC katody, ne ze sodíkové, a jsou použitá proto, že obojí
krystalizuje ve struktuře α-NaFeO₂; sodíkově specifické měření by je posunulo
o desítky procent a ne o těch šest řádů, o které jde. Příznaky `[A]` označují
hodnoty, které se tady nepodařilo ověřit proti primárnímu zdroji, a proto se
proměřují.

Všech šest referencí bylo obsahově přečteno v
[`reference-audit`](https://github.com/karagos01/reference-audit), kde je
doslovná evidence; §7 shrnuje, co ta pulzní citace skutečně říká, a zbytek
neduplikuje.

## Doprovodná vyhodnocení

- [`reference-audit`](https://github.com/karagos01/reference-audit) — jestli všech 69 citací ve všech 16 depositech říká to, pro co je citovaných
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — matrice kvantové biofortifikace a in-situ phytominingu z října 2026
- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — oktonionová dvouvrstvá šablona s asociátorem a census Maxwellovy atribuce
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — 2bitový inferenční engine pro LLM
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — trilogie CQFT / PCTP / SOTP ze září 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — tenzorová maticová architektura openQL / openOL z října 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — cymatická stimulace průduchů a pulzní osvětlení z října 2026

## Licence

Kód (všechny `*.py` a `run_all.sh`): MIT, viz `LICENSE`.
Text `PAPER.md` a `PAPER.cs.md`: CC BY 4.0.
