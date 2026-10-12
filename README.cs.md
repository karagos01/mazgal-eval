# Quantum Biofortification / In-Situ Phytomining — nezávislé vyhodnocení

Reprodukovatelné vyhodnocení práce M. Mazgal, *Quantum Biofortification and
In-Situ Phytomining: Design of an Autonomous Closed-Loop Nanometallic
Agricultural Matrix* (Zenodo, 6. října 2026, DOI
[10.5281/zenodo.23174932](https://doi.org/10.5281/zenodo.23174932)).

Text je v [`PAPER.cs.md`](PAPER.cs.md), anglicky v [`PAPER.md`](PAPER.md).

**Jedna věta v §4 uvádí dvě hustoty, které jsou 24× od sebe.** Při uvedené
hloubce orby 30 cm je „1 pellet per 5 cm³" rovno 60 000 peletám/m², ne 2 500,
které stojí v téže větě — a hmotnostní rozpočet, požadavek 750 tun
i miliondolarová případová studie stojí na těch 2 500, zatímco na těch 5 cm³ je
postavený požadavek „constant physical contact". **§3.3 nazývá ¹³⁸La stabilním
izotopem**; je to primordiální radionuklid s poločasem 1,03·10¹¹ let. Premisa
§3.3 ale u lanthanu padá ještě dřív, protože **¹³⁹La — 99,91 % veškerého
lanthanu — už spin 7/2 má**, takže není co vybírat; a při přírodním izotopovém
složení zvedne matrice lanthan v poli **asi o pětinu** proti tomu, co tam už je,
a podíl ¹³⁸La nechá nezměněný. Vlastní reference práce obracejí tři nosná
tvrzení: citovaný autor magnetického izotopového efektu měří pro přesně tu
trojici, která je citovaná pro akceleraci, **3–5× potlačení** syntézy DNA
a navrhuje je jako cytostatikum.

Dva nálezy jdou naopak a §1 textu je vypisuje jako první: premisa o 30–50 %
využití dusíku je správná a přidaný ¹³⁸La je čtyři až pět řádů pod kaliem-40,
které v té půdě už je, takže označit ho za stabilní je chyba o nuklidu, ne
riziko v návrhu.

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`README.md`](README.md) a [`PAPER.md`](PAPER.md).

## Co je potřeba

```
python3 -m pip install -r requirements.txt   # jen numpy
```

Bez GPU, bez sítě. Všechno je aritmetika nad vlastními parametry preprintu a nad
publikovanými konstantami, protože deposit nepřikládá žádný kód, žádná měření
a žádné obrázky.

## Reprodukce výsledků

```
./run_all.sh          # všechno, asi sekunda na jakémkoli CPU
```

| Skript | Co spočítá | Sekce |
|---|---|---|
| [`density.py`](density.py) | dvě hustoty z §4, kterou z nich používá ekonomika, co by stálo držet tu druhou, a na co vyjde „constant physical contact" | §§2, 4 |
| [`isotopes.py`](isotopes.py) | spiny, které má práce správně; jaderná data ¹³⁸La; spin ¹³⁹La; přidaný inventář proti tomu, co orniční vrstva už drží; alternativa s obohacením; radiologické srovnání | §3.3 |
| [`economics.py`](economics.py) | položka za zlato proti spotu v den depositu, návratnost a její break-even sazba, a kolik ztrát „uzavřená smyčka" snese | §4 |

Každá konstanta je v [`constants.py`](constants.py) s **příznakem provenience** —
`[P]` z preprintu, `[V]` ověřeno proti pojmenovanému zdroji, `[A]` předpokládaný
rozsah, který se proměřuje, netvrdí se — a žádný další skript žádnou
nedefinuje. Celý výstup jednoho běhu je v [`results.log`](results.log).

## Klíčová čísla

| co | publikováno | naměřeno / spočítáno |
|---|---|---|
| zemina pod 1 m² při uvedené hloubce orby | — | 300 000 cm³ |
| „1 pellet per 5 cm³" | „approximately 2,500 pellets per 1 m²" | **60 000 pelet/m²** — tatáž věta, **24× vedle** |
| kterou hodnotu používá ekonomika | — | těch 2 500, při přesně **1 g na peletu** |
| kdyby se držely ty 5 cm³ | 750 t, $1 000 000 | **18 000 t, $24 000 000** |
| „constant physical contact" | požadováno | střední rozestup **4,93 cm**, kořen do 2,5 cm |
| ¹³⁸La | „stable isotope" (abstrakt, §3.3, klíčová slova) | **primordiální radionuklid**, T½ 1,03·10¹¹ let, β⁺ 65,5 % / β⁻ 34,5 % |
| jáderný spin ¹³⁸La | „I = 5" | **správně** |
| ¹³⁹La, 99,91 % veškerého lanthanu | — | spin **7/2** — nenulový, takže není co vybírat |
| lanthan přidaný 1 t La₂O₃ na 30 ha | „the most radical innovation" | 2,84 g/m² proti **10,2–14,9 g/m², které tam už jsou** → **+19 až +28 %** |
| podíl ¹³⁸La po aplikaci | „precisely defined profile" | **nezměněný, 0,0888 %** |
| ²⁵Mg už v orniční vrstvě | — | **84–1260 g/m²** (10,00 % veškerého Mg) |
| ⁶⁷Zn už v orniční vrstvě | — | 0,34–2,07 g/m² (4,10 % veškerého Zn) |
| vsázka na 1 t obohaceného ¹³⁸La | nezmíněno | **≈1 126 t** přírodního lanthanu |
| aktivita přidaného ¹³⁸La | — | celkem 705 kBq, **2,35 Bq/m²** |
| proti půdnímu kaliu-40 | — | **4 až 5 řádů pod** — není to riziko |
| položka za zlato v rozpočtu | $417 000 za 5 kg = $83,40/g | spot v den depositu **$134,03/g** → chybí **$253 150** |
| jednoduchá návratnost | „permanent capital" | **40 let**; break-even jen při ≤ **2,50 % p. a.** navěky |
| ztráty, které „uzavřená smyčka" snese | předpokládány nulové | **< 1,72 % ročně**, aby do návratnosti zůstala polovina |
| 30–50 % využití živin | tvrzeno v §1 | **správně** pro dusík a první plodinu |
| Buchačenko, citován pro zrychlenou syntézu DNA | „accelerate … DNA transcription" | **3–5× potlačení**, navrženo jako protinádorové cytostatikum |
| Reith et al., citováni pro zlato blokující ROS | „entirely blocking" | zlato oxidační stres **vyvolává**; buňka ho vyváží |
| Sheoran et al., citováni pro dodávání kovu | dodávání do biomasy | phytomining kov **odnímá** a taví |
| reference dohledatelné v uvedené podobě | 6 uvedených | **4 ze 6**; Reith je 2009 PNAS 106(42) a Buchačenkova kniha má v titulu *Biochemistry* |

## Rozsah

Deposit je čtyřstránkový preprint pod CC BY 4.0 bez kódu, bez měření a bez
obrázků, takže není co benchmarkovat. §8 textu vypisuje tvrzení, na která
aritmetika nedosáhne — „absolute structural immunity", „entirely blocking
cellular corrosion", „the theoretical blockade of natural biological aging
processes" — a říká, proč se neměří, místo aby je vydával za vady.

Všech šest referencí bylo obsahově přečteno v
[`reference-audit`](https://github.com/karagos01/reference-audit), kde je
doslovná evidence i záznam, jak daleko se každou práci podařilo přečíst;
verdikty jsou shrnuté v §6 tady a neduplikují se.

§9 vypisuje hranice. Příznaky `[A]` v `constants.py` označují hodnoty, které se
tady nepodařilo ověřit proti primárnímu zdroji, a proto se proměřují, přičemž
každý závěr z nich je spočítaný přes celý rozsah — dvě konstanty použité
v dřívější verzi byly na tomto základě degradovány na `[A]`. Rozestupy
předpokládají kubickou mříž, což je nejlepší případ.

## Doprovodná vyhodnocení

- [`reference-audit`](https://github.com/karagos01/reference-audit) — jestli všech 69 citací ve všech 16 depositech říká to, pro co je citovaných
- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — oktonionová dvouvrstvá šablona s asociátorem a census Maxwellovy atribuce
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — 2bitový inferenční engine pro LLM
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — trilogie CQFT / PCTP / SOTP ze září 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — tenzorová maticová architektura openQL / openOL z října 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — cymatická stimulace průduchů a pulzní osvětlení z října 2026
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — dvoušálový signál a nabíjení HFRS z října 2026
- [`hemocyanin-eval`](https://github.com/karagos01/hemocyanin-eval) — hemocyaninová fyziologie na měďi z října 2026
- [`intensional-physics-eval`](https://github.com/karagos01/intensional-physics-eval) — Intensional Physics Computing a openQL v1.1 z října 2026

## Licence

Kód (všechny `*.py` a `run_all.sh`): MIT, viz `LICENSE`.
Text `PAPER.md` a `PAPER.cs.md`: CC BY 4.0.
