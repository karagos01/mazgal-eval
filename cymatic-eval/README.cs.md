# Cymatická stimulace průduchů — nezávislé vyhodnocení

Reprodukovatelné vyhodnocení práce M. Mazgal, *Cymatic Stomatal Stimulation and
Pulsed Optical Assimilation: Scaling from Cybernetic Bioreactors to
Industrial-Scale Acoustic Modulation* (Zenodo, 5. října 2026, DOI
[10.5281/zenodo.23156927](https://doi.org/10.5281/zenodo.23156927)).

Text je v [`PAPER.cs.md`](PAPER.cs.md), anglicky v [`PAPER.md`](PAPER.md).

**Obě frekvence, na kterých návrh stojí, jsou nota B.** 246,91 Hz je rovnoměrně
temperované B3 na 0,22 centu, 61,72 Hz je B1 na 0,43 centu, a optická perioda
50 µs + 4000 µs je 4,050 ms = 246,91 Hz — takže časování odvozené z kinetiky
Calvinova cyklu a frekvence odvozená z mechaniky svěracích buněk jsou jedno číslo.
Při duty cyclu 1,2346 % je střední ozářenost 256 µmol/m²/s, pod saturací světlem pro
každou C3 plodinu, takže zhášení, které návrh obchází, v režimu, který ten návrh
vytváří, téměř není nasazené; a sušina na kilowatthodinu je pod pulzováním
invariantní na 3,6·10⁻¹⁵ — což je právě ta veličina, kterou §5 tvrdí, že redefinuje.
V polním měřítku má třílistá turbína blade-pass frekvenci 0,700 Hz tam, kde se chce
61,72 Hz, celý její širokopásmový výstup je o 22,5 dB pod hladinou, při které
citované review funguje, a jádro transformátoru na 50 Hz nemá žádnou linku na
61,72 Hz, kterou by šlo ladit.

Z autorova hyperkomplexního slovníku tu není nic a je to první deposit s téměř
celou reálnou bibliografií; §1 textu vypisuje, co je správně, ještě než cokoli
dalšího. (§1 dostala 9. 10. opravu: tvrdila prvenství v tom, že ten slovník
chybí, a census nad všemi šestnácti záznamy v
[`reference-audit`](https://github.com/karagos01/reference-audit) to vyvrátil —
COBAR a Momentum Drive ze září ty termíny nemají taky.)

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
./run_all.sh          # všechno, asi 2 sekundy na jakémkoli CPU
```

| Skript | Co spočítá | Sekce |
|---|---|---|
| `frequency.py` | nejbližší rovnoměrně temperovaný tón ke každé publikované frekvenci; optická perioda proti akustické; citované pásmo proti odvozené subharmonické | §§2–3 |
| `light.py` | duty cycle a časově střední fotonový tok proti saturaci C3 světlem; temný interval proti RuBisCO a PQ poolu; invariance g/kWh | §§4–6 |
| `acoustics.py` | blade-pass frekvence, potřebné otáčky a Mach na konci lopatky, výkonová bilance na 100–1000 m, rozestupy ve farmě jako fázované pole, harmonické transformátoru | §§7–8 |
| `water.py` | transpirace přes polední depresi a voda na jednotku uhlíku | §9 |

Každá externí konstanta je se svým zdrojem v [`constants.py`](constants.py) a žádný
skript si nedefinuje vlastní fyzikální konstantu. Celý výstup jednoho běhu je
v [`results.log`](results.log).

## Klíčová čísla

| co | publikováno | naměřeno / spočítáno |
|---|---|---|
| 246,91 Hz, „synthesized to maximize localized guard cell vibration" | — | **B3**, −0,22 centu |
| 61,72 Hz, „calculated" subharmonická | — | **B1**, −0,43 centu |
| optická perioda 50 µs + 4000 µs | z „the Calvin cycle" | **246,91 Hz** — totéž číslo jako akustická, na 1,5·10⁻⁵ |
| citlivé pásmo PAFT | „typically between 50 and 120 Hz" | citované review dává **0,1–1 kHz**; dělení čtyřmi z něj vyvede |
| časově střední ozářenost | „extreme-intensity photon bursts (4500 W/m²)" | **55,6 W/m² = 256 µmol/m²/s**, 0,13× plné slunce |
| ta střední hodnota proti saturaci C3 světlem | obchází NPQ | **1,57× pod** salátem, 5,48× pod pšenicí |
| strop obejití NPQ | „up to 60%" rozptýleno | **2,50×**, z vlastní hodnoty práce |
| temná fáze proti pojmenovanému mechanismu | „perfectly matches … the Calvin cycle" | Calvin **250–500 ms**, 62–125× vedle; PQ pool **2–20 ms** |
| g/kWh přes 81násobný rozsah duty cyclu | „redefine the gram-per-watt limit of CEA" | rozptyl **3,6·10⁻¹⁵** — invariantní |
| g/kWh za předpokladů ve prospěch návrhu | redefinováno | **12,42**, uvnitř komerčního rozsahu 5–10 |
| blade-pass frekvence, 3 lopatky při 14 ot/min | přeladitelná na 61,72 Hz | **0,700 Hz** — 61,72 Hz je 88. harmonická |
| otáčky pro blade pass na 61,72 Hz | dosažené „electromagnetically braking" | **1234 ot/min**, Mach **18,8** na konci, **85 167 g** |
| akustický výkon turbíny proti 70 dB u rostliny | „large-scale agricultural acoustic stimulators" | chybí **22,5 dB (179×)** na 300 m, **33,0 dB (1987×)** na 1 km |
| ztráta, na kterou volba frekvence míří | „minimal atmospheric attenuation" | správně, a je to **0,1 dB** proti **24 dB** rozptýlení |
| větrná farma jako fázované pole | „phased acoustic arrays" | prvky **90–180 λ** od sebe tam, kde je potřeba λ/2; 0,136° úhlu rotoru |
| linky transformátoru dostupné na 50 Hz síti | „tuned to precisely 61.72 Hz" | celé násobky **50 Hz**; nejbližší je o 11,72 Hz vedle |
| „asymmetric DC injection" | ladicí prvek | polocyklová saturace — poruchový režim geomagnetických proudů |
| polední transpirace, když se průduchy drží otevřené | „evapotranspiration rates will rise" | **3,0×**, nezávisle na VPD |
| voda na jednotku uhlíku | — | **1,3–2,5×** pro každou saturující asimilační odezvu |
| 15–18 % přírůstku biomasy | tvrzeno | bez vazby na dávku, dobu, frekvenci nebo plodinu |
| reference | 5 uvedených | **4 z 5** se dohledají přesně; pátou se nepodařilo najít (§10) |

## Rozsah

Deposit je čtyřstránkový preprint pod CC BY 4.0 bez přiloženého kódu, bez měření
a bez obrázků, takže není co testovat; jeho §6 říká, že topologie hardwaru, firmware
pro STM32 a CAD modely „will be maintained in an open-source GitHub repository",
a žádný nejmenuje. Hranice toho, co je tady spočítané, jsou v §11 textu — žádné
rostliny pěstované nebyly a akustický model je hemisférické rozptýlení, kalibrované
proti naměřeným 40–45 dB(A) na 300 m.

## Doprovodná vyhodnocení

- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — oktonionová dvouvrstvá šablona s asociátorem a census Maxwellovy atribuce
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — 2bitový inferenční engine pro LLM
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — trilogie CQFT / PCTP / SOTP ze září 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — tenzorová maticová architektura openQL / openOL z října 2026
- [`reference-audit`](https://github.com/karagos01/reference-audit) — jestli všech 81 citací ve všech 18 depositech říká to, pro co je citovaných
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — matrice kvantové biofortifikace a in-situ phytominingu z října 2026
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — dvoušálový signál a nabíjení HFRS z října 2026
- [`hemocyanin-eval`](https://github.com/karagos01/hemocyanin-eval) — hemocyaninová fyziologie na měďi z října 2026
- [`intensional-physics-eval`](https://github.com/karagos01/intensional-physics-eval) — Intensional Physics Computing a openQL v1.1 z října 2026
- [`openomega-eval`](https://github.com/karagos01/openomega-eval) — openOmega, antimaterie a sedeniony z října 2026
- [`hospv-eval`](https://github.com/karagos01/hospv-eval) — HOS-PV 2.0, singletní fise a spintronická fotovoltaika z října 2026

## Licence

Kód (všechny `*.py` a `run_all.sh`): MIT, viz `LICENSE`.
Text `PAPER.md` a `PAPER.cs.md`: CC BY 4.0.
