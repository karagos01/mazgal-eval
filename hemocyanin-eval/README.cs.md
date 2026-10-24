# Copper-Based Hemocyanin Physiology in Hominids — nezávislé vyhodnocení

Reprodukovatelné vyhodnocení práce M. Mazgal, *Theoretical Framework for
Copper-Based Hemocyanin Physiology in Hominids* (Zenodo, 7. října 2026, DOI
[10.5281/zenodo.23209266](https://doi.org/10.5281/zenodo.23209266)).

Text je v [`PAPER.cs.md`](PAPER.cs.md), anglicky v [`PAPER.md`](PAPER.md).

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`README.md`](README.md) a [`PAPER.md`](PAPER.md).

**Číslo, které o tom rozhoduje, není ani v té práci, ani v žádné z jejích pěti
referencí**, takže jsem ho dohledal samostatně. Lidská arteriální krev nese asi
**20 obj. %** kyslíku; hemocyanin nese 1,37–3,44 obj. % u naměřených druhů a u
hlavonožců „never exceeds 4.5 vols%" — tedy **4,4 až 14,6× méně**. A
zkoncentrovat ho nejde, z důvodu, který uvádí spoluautor té práce, kterou první
citace preprintu komolí: rozpuštěný v hemolymfě v koncentraci dostatečné pro
transport „will yield an unbearably high osmotic pressure".

Důsledek je aritmetika. Sedmdesátikilový dospělý v klidu potřebuje 245 ml
O₂/min, což při srdečním výdeji 4–6 l/min znamená arteriovenózní rozdíl
4,1–6,1 obj. % — čímž se reprodukuje ~5 obj. % skutečně naměřených, takže je ten
výpočet kalibrovaný. S hemocyaninem na publikovaném stropu a při velkorysé 75%
extrakci potřebuje tentýž člověk **7,3 l/min v klidu** a při naměřené kapacitě
*Octopus vulgaris* **24–72 l/min**, proti maximálnímu lidskému srdečnímu výdeji
asi 20–25 l/min. **Návrh padá, když se jen sedí.**

Genetická cesta padá na předpokladu: epigenetický přepínač zapne existující gen
a **obratlovci hemocyaninový gen nemají** — InterPro IPR013788 nevrací ve
Vertebrata ani v Chordata nic.

Jeden nález jde naopak a §6 textu ho dává prominentně. **Záměna třídy pigmentu
se skutečně stala** — plži Planorbidae nahradili původní hemocyanin
hemoglobinem. Práce to necituje, běží to opačným směrem a publikovaný důvod je
„possibly to replace a less-efficient hemocyanin".

## Co je potřeba

```
python3 -m pip install -r requirements.txt   # jen numpy
```

Bez GPU, bez sítě. Deposit neuvádí žádnou měřenou veličinu, takže každá hodnota
tady je buď ověřená z literatury, nebo předpokládaný rozsah, který se proměřuje.

## Reprodukce výsledků

```
./run_all.sh          # všechno, asi sekunda na jakémkoli CPU
```

| Skript | Co spočítá | Sekce |
|---|---|---|
| [`oxygen.py`](oxygen.py) | kapacita pro kyslík proti lidské krvi; co klidový lidský metabolismus vyžaduje od oběhu; tentýž požadavek s hemocyaninem při proměřované extrakci; námaha; proč olihně nejsou protipříklad; proteinová hmota na O₂ | §§2–4 |
| [`genetics.py`](genetics.py) | jestli je co zapnout; jak práce používá slovo „epigenetic"; ceruloplasminový most proti vlastnímu citovanému abstraktu; vlastní redoxní toxicita měďi; jediný skutečný precedens záměny pigmentu | §§5–6 |

`genetics.py` je záznam databázových výsledků a citací, ne výpočet, a je držený
jako skript, aby se objevil v `results.log` vedle aritmetiky. Každá hodnota je
v [`constants.py`](constants.py) s **příznakem provenience** — `[P]` z preprintu,
`[V]` ověřeno proti pojmenovanému zdroji, `[A]` předpokládaný rozsah, který se
proměřuje, netvrdí se. Celý výstup jednoho běhu je v
[`results.log`](results.log).

## Klíčová čísla

| co | publikováno | naměřeno / spočítáno |
|---|---|---|
| kapacita navrhovaného pigmentu pro kyslík | „highly efficient and thermodynamically stable" | **4,4–14,6× pod lidskou krví** |
| lidská arteriální krev | — | 20,00 obj. % |
| *Cancer magister* / *O. dofleini* / *Nautilus* / *O. vulgaris* | — | 3,44 / 3,06 / 2,30 / 1,37 obj. % |
| strop hlavonožců | — | „never exceeds **4.5 vols%**" |
| proč to nejde zkoncentrovat | — | „unbearably high osmotic pressure" — z vlastní zkomolené citace preprintu |
| klidová spotřeba kyslíku, 70 kg | neuvedeno | 245 ml O₂/min (1 MET) |
| jaký a-v rozdíl to vyžaduje | neuvedeno | **4,1–6,1 obj. %** — reprodukuje těch ~5 naměřených |
| potřebný srdeční výdej, hemocyanin na stropu, 75% extrakce | neuvedeno | **7,3 l/min v klidu** |
| totéž při naměřené kapacitě *O. vulgaris* | neuvedeno | **24–72 l/min** proti ~20–25 maximálním |
| totéž při 8× a 20× klidovém metabolismu | „thermoregulatory independence" | 58 a **145 l/min** |
| co limituje olihně, nejlepší protipříklad | — | „not oxygen uptake, but **oxygen transport in the blood**" |
| hemocyaninové geny ve Vertebrata / Chordata | „latentní geny" | **0 / 0** |
| lidské geny s tyrosinázovou doménou | — | TYR, TYRP1, DCT; aktivní místo TYRP1 má **zinek** |
| ceruloplasmin | „fundamental human protein for copper transport" | **ferroxidáza**; „plays no essential role in the transport or metabolism of this metal" |
| průnik domén ceruloplasmin ∩ hemocyanin | „structurally related" | **prázdný** — cupredoxinový fold proti tyrosinázovému binukleárnímu typu 3 |
| redoxní chování měďi podle vlastní reference práce | „absence of the Fenton reaction" | „generation of superoxide and **hydroxyl radicals**" |
| „epigenetic" v preprintu | mechanismus celého přepnutí | **8 výskytů**; methylation, histone, chromatin: **0 každé** |
| „epigenet" v referenci glosované pro epigenetickou adaptaci | — | **0** |
| měřené veličiny uvedené kdekoli v preprintu | — | **0** |
| skutečný precedens záměny pigmentu | necitován | hemocyanin → hemoglobin, „possibly to replace a less-efficient hemocyanin"; „Once lost, hemocyanin was not regained" |

## Rozsah

Deposit je krátký preprint pod CC BY 4.0 bez kódu, bez měření a bez obrázků.
§7 textu vypisuje, co se tady neměří — tvrzení o životě po stovky let,
supravodivém nervovém systému a biologickém kvantovém počítači — a říká proč,
místo aby je vydával za vady. Taky zaznamenává, že tento deposit a jeho
předchůdce jsou ta dvě místa ze sedmnácti autorových, kde je návrh intervencí na
lidech.

§8 vypisuje hranice. Nejmíň pevný předpoklad je extrakční podíl a proměřuje se
až k 75 %, což je výrazně nad lidskou klidovou hodnotou, takže ten výpočet je
k návrhu už velkorysý — a i tak padá v klidu. Negativní databázový výsledek je
slabší než důkaz absence a to tvrzení je omezené na to, co anotace ukazuje.

Všech pět referencí bylo obsahově přečteno v
[`reference-audit`](https://github.com/karagos01/reference-audit), kde je
doslovná evidence; §§5–6 to shrnují a neduplikují.

## Doprovodná vyhodnocení

- [`reference-audit`](https://github.com/karagos01/reference-audit) — jestli všech 81 citací ve všech 18 depositech říká to, pro co je citovaných
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — matrice kvantové biofortifikace a in-situ phytominingu z října 2026, kterou tento deposit sebecituje
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — dvoušálový signál a nabíjení HFRS z října 2026
- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — oktonionová dvouvrstvá šablona s asociátorem a census Maxwellovy atribuce
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — 2bitový inferenční engine pro LLM
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — trilogie CQFT / PCTP / SOTP ze září 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — tenzorová maticová architektura openQL / openOL z října 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — cymatická stimulace průduchů a pulzní osvětlení z října 2026
- [`intensional-physics-eval`](https://github.com/karagos01/intensional-physics-eval) — Intensional Physics Computing a openQL v1.1 z října 2026
- [`openomega-eval`](https://github.com/karagos01/openomega-eval) — openOmega, antimaterie a sedeniony z října 2026
- [`hospv-eval`](https://github.com/karagos01/hospv-eval) — HOS-PV 2.0, singletní fise a spintronická fotovoltaika z října 2026

## Licence

Kód (všechny `*.py` a `run_all.sh`): MIT, viz `LICENSE`.
Text `PAPER.md` a `PAPER.cs.md`: CC BY 4.0.
