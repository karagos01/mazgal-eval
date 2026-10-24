# Pásmo, ve kterém nic není: vyhodnocení *Dual-Scale Waveform Optimization and HFRS*

karagos01, říjen 2026

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`PAPER.md`](PAPER.md).

## Abstrakt

M. Mazgal, *Dual-Scale Waveform Optimization and Hysteretic-Fractal Resonant
Stimulation (HFRS) for Minimizing Transport Resistance in Na-ion Lattices*
(Zenodo, 6. října 2026, DOI
[10.5281/zenodo.23186884](https://doi.org/10.5281/zenodo.23186884)) navrhuje
nabíjet sodíkoiontové články superpozicí V(t) = W_macro(t) + F_micro(t), kde
F_micro je „high-frequency fractal modulation (kHz to MHz range)", která má
„induce phonon-assisted tunneling and lower activation barriers".

Tři měření, všechna poměrová. Nejnižší Ramanovsky aktivní mřížková linie
naměřená ve vrstevnaté oxidové katodě je 144 cm⁻¹, tedy **4,32 THz** — mezi
**6,6 a 9,6 řádu** nad pásmem F_micro, takže v tom pásmu není žádný fonon, kterému
by se dalo asistovat. Energeticky je hf při 1 MHz rovno 4,1·10⁻⁹ eV, což je
**6,3 milionu×** pod kT při 300 K a sedm až osm řádů pod migrační bariérou
sodíku 0,10–0,64 eV, kterou má snižovat. A pásmo, v němž má článek vůbec
faradaickou odezvu — půlkružnice přenosu náboje asi 1 Hz–1 kHz — se s F_micro
**nepřekrývá**: nad ním je naměřená odezva ohmická a induktivní, takže proud
teče dvojvrstvou kapacitou a disipuje v sériovém odporu. To je Jouleovo teplo,
tedy ztráta, kvůli které §1 celý návrh existuje.

§2.2 má v nadpisu negativní diferenciální odpor a v těle definuje
podproporcionální tepelnou odezvu; to jsou různé veličiny a pro nabíjený článek
je dV/dI = R_i > 0 vždy. Hůř: kritérium, jak je napsané, splní článek, který se
jen ohřívá — Arrheniovsky s aparentní aktivační energií 0,20–0,50 eV sníží
ohřev o 20 K teplo I²R **1,6–3,0×**. §5 ten konfound sama pojmenovává
a předepisuje izotermickou kalorimetrii, což je té práci ke cti — ale §2.2 je
místo, kde se definuje účelová funkce, a tak, jak je definovaná, by optimalizátor
našel teplé články.

Hledání v §3 je svázané elektrochemií, ne GPU: 8 článků při 1C dá **96
vyhodnocení/den** a celá užitečná životnost vzorků dá nejvýš **24 000**
vyhodnocení, což je spodní okraj rozsahu, který roj potřebuje na
„hyperdimenzionálním" prostoru z §3. §6 vyjmenovává Gerber soubory, CUDA kernely
a DAQ logy jako „Provided Data"; deposit obsahuje **jeden soubor**, to
čtyřstránkové PDF.

Dva nálezy jdou naopak. **§5 je nejlépe argumentovaná sekce v kterémkoli ze
sedmnácti autorových depositů** — pojmenovává dva reálné konfoundy, aniž by ji
o to někdo požádal, a předepisuje na oba správné nástroje. A její závěr o MHz
signálech je správný, jen z jiného důvodu než ten kožní efekt, který cituje: při
1 MHz je hloubka vniku v aluminiu 82 µm proti folii 12–20 µm.

## 1. Co je správně

**§5 dělá práci, kterou by udělal recenzent.** Doslova: komerční vinuté články
„present massive parasitic inductance and capacitance", takže „Phase 1 of
experimental validation must strictly utilize planar coin-cell geometries";
a „Differentiating between standard thermal agitation (which naturally lowers
R_i as the cell heats up) and genuine electro-kinetic field enhancement requires
highly precise isothermal calorimetry during the GPU-driven search phase."
Obojí jsou reálné konfoundy, obojí je vysloveno bez vyzvání a obojí přichází se
správnou nápravou. Nic jiného v téhle sérii to nedělá.

**W_macro je reálná a podložená myšlenka.** Nízkofrekvenční makroskopická
obálka, která mezi pulzy nechá zrelaxovat koncentrační gradienty, je přesně to,
co analyzuje vlastní pulzní citace té práce, a tam to funguje.

**Hardware je obyčejný a postavitelný.** GaN synchronní stupeň na izolovaném
kovovém substrátu se STM32 nebo Zynqem, který loguje v mikrosekundách, je normální
výkonová elektronika. Nic v §4 nevyžaduje nic, co by neexistovalo.

**Slovník tam není.** „Maxwell", „octonion", „quaternion", „hypercomplex",
„non-associative", „tensor" a „causal" mají nula výskytů.

## 2. V tom pásmu není žádný fonon

§2.1 klade F_micro do „kHz to MHz range" a říká, že indukuje „phonon-assisted
tunneling". Ramanovská spektroskopie vrstevnaté oxidové katody měří linie na
144, 189 a 324 cm⁻¹ — 4,32, 5,67 a 9,71 THz. Vrstevnatý LiMO₂ krystalizuje ve
struktuře α-NaFeO₂, tedy ve stejné strukturní rodině jako sodíkové vrstevnaté
katody, o které jde.

| | frekvence | poměr k horní hranici F_micro (1 MHz) |
|---|---|---|
| nejnižší naměřená linie | 4,32 THz | **4 317 011×** (6,6 řádu) |
| totéž proti 1 kHz | — | 4,3·10⁹× (9,6 řádu) |

V pásmu kHz–MHz v tom materiálu nic nevibruje, takže tam není mód, na který by se
modulace mohla navázat. Slovo „fraktální" to nemění: sebepodobný signál, jehož
nejvyšší složka je 1 MHz, nemá na 4 THz žádný výkon.

Energeticky čte tatáž mezera ostřeji, protože to je forma, ve které se tunelovací
argumenty dělají:

| | hodnota |
|---|---|
| hf při 1 MHz | 4,136·10⁻⁹ eV |
| kT při 300 K | 0,02585 eV |
| poměr | **6 250 986×** |
| migrační bariéra Na | 0,10–0,64 eV |
| E_a / hf(1 MHz) | 2,4·10⁷ až 1,5·10⁸ |

Kvantum navrhované stimulace je šest milionů krát menší než tepelná energie,
kterou ty ionty už mají. Ion za pokojové teploty je neustále bombardovaný kT;
kvantum pole o devět řádů nižší mu nepomůže přes bariéru o osm řádů vyšší.

Čestná výhrada: silné *klasické* pole samozřejmě iony hýbat umí, driftovým
členem, a to dělá každá nabíječka. Měří se tady to konkrétní mechanistické
tvrzení — fononová asistence a snižování bariéry — a jsou to právě ty poměry,
které vyvracejí tohle, ne myšlenku, že střídavá složka něco dělá.

## 3. V tom pásmu nemá článek ani faradaickou odezvu

I kdybychom mřížku nechali stranou, článek sám v pásmu F_micro faradaicky
neodpovídá. V impedanční spektroskopii se přenos náboje objevuje jako půlkružnice
v rozsahu asi **1 Hz až 1 kHz**; nad asi 1 kHz je naměřená odezva ohmický odpor
plus indukčnost — elektrolyt, kolektory, konektory a přívody.

F_micro je specifikované jako 10³–10⁶ Hz. Ta dvě pásma se potkávají v bodě a jejich
překryv je **nulový**. Takže v celém rozsahu F_micro teče proud vstupující do
článku dvojvrstvou kapacitou paralelně s větví přenosu náboje a sériovou
indukčností — nabíjí a vybíjí rozhraní, aniž by ho překročil. Kapacitní proud
žádný sodík neinterkaluje. Co dělá, je disipace v sériovém odporu, tedy ohřev
I²R: právě ta ztráta, jejímž pojmenováním §1 začíná.

Tohle je nález, který přežije i vlastní nápravu z §5. §5 předepisuje planární
coin-cell, aby zmizely parazitní prvky jelly-rollu, a pro indukčnost je to
správný krok — ale dvojvrstvý zkrat je vlastnost elektrodového rozhraní, ne
geometrie vinutí, takže v coin-cell je taky.

## 4. §2.2 definuje dvě různá kritéria a to, které definuje, je konfoundované

Nadpis říká „Anomaly Criterion (Negative Differential Resistance)". Tělo říká
Z_diff = dV/dI a definuje anomálii jako „incremental increase in the integral
power delivered by V(t)", která dává „sub-proportional thermal response".

To nejsou totožná tvrzení. NDR znamená dV/dI < 0. Pro nabíjený článek při
pevném stavu nabití je V = OCV(SoC) + I·R_i s R_i > 0, takže dV/dI = R_i > 0
bezpodmínečně — veličina z nadpisu nemůže nastat. Podproporcionální teplo na
jednotku výkonu je tvrzení o účinnosti a nastat může. Sekce nedává žádný způsob,
jak poznat, které z nich optimalizátor hledá. (dV/dI má navíc jednotku ohm, takže
je to diferenciální *odpor*; „differential impedance" je komplexní veličina
měřená proti frekvenci.)

A to kritérium, které tělo definuje, splní ohřívající se článek. Vnitřní odpor
klesá s teplotou; s aparentní aktivační energií 0,20–0,50 eV vynásobí ohřev
o 20 K teplo I²R při stejném proudu faktorem 0,61 až 0,29 — tedy sníží teplo na
jednotku proudu **1,6× až 3,0×**, což je přesně ta signatura, kterou §2.2 čte
jako „the onset of coherent, low-friction ion intercalation".

**§5 ten konfound sama pojmenovává**, a proto je tohle kritika §2.2, ne
povědomí té práce. Ale §2.2 je místo, kde žije účelová funkce, a osmičlánkový roj
optimalizující tuhle funkci by zkonvergoval na té kombinaci parametrů, která
články ohřívá nejrychleji.

## 5. Hledání je svázané elektrochemií a vzorky umřou dřív

§3 mapuje jednu GPU na jeden fyzický článek a navrhuje „find the optimal 'Key'
in real physical time". Jedno vyhodnocení kandidátního signálu je minimálně
jedno nabití plus vybití, které článek vrátí do známého stavu:

| C-rate | nabití + vybití | vyhodnocení/den na 8 článcích |
|---|---|---|
| C/2 | 4,0 h | 48 |
| 1C | 2,0 h | **96** |
| 2C | 1,0 h | 192 |

Proti tomu je coin-cell použitelná jako testovací nosič snad 500–3000 cyklů,
takže jedna sada osmi dá **4 000 až 24 000 vyhodnocení celkem**, dosažených po
42 až 250 dnech nepřetržitého cyklování. Particle swarm optimization na prostoru
o 10–30 dimenzích obvykle chce 10⁴–10⁵ vyhodnocení a §3 svůj vlastní prostor
nazývá „hyperdimensional". Celý životní rozpočet té aparatury je na spodním
okraji toho rozsahu.

A je tam konfound, který §3 nezmiňuje a na který kalorimetrie z §5 nedosáhne.
Účelová funkce je vnitřní odpor a vnitřní odpor s počtem cyklů roste. Takže
veličina, která se minimalizuje, driftuje nahoru přesně v časovém měřítku toho
hledání, a to o hodnotu, která závisí na tom, kolik vyhodnocení už který článek
odsloužil. Roj, který mezi uzly rozesílá svůj nejlepší parametrický vektor,
porovnává články různého věku, a každé zlepšení nalezené dřív je konfoundované
s tím, že vzorky byly novější. Odpověď §3 — „Dynamic Key Trajectory
parameterized by the State of Charge" — řeší drift v rámci cyklu; stárnutí je
drift přes cykly a není funkcí SoC.

A konečně, §3 a §4 popisují různé stroje. §3 má každou GPU streamovat DDS data
do svého článku; při 10–100 MSa/s a 16 bitech je to 20–200 MB/s na článek, tedy
přenos dat bez výpočetního obsahu a bez čehokoli, co by GPU zaměstnalo mezi
vyhodnoceními dvě hodiny od sebe. §4 pak říká, že lokální „DSP or FPGA (e.g.
STM32/Zynq architectures)" je „acting as the local generative engine" — a v tom
případě GPU signál negeneruje a mapování 1:1 nemá co dělat.

## 6. §6 popisuje data, která v depositu nejsou

§6 má nadpis „Structure of Provided Data (Zenodo Repository)" a vyjmenovává
v přítomném čase `/Hardware` s „Gerber, BOM, 3D STEP", `/Software` s „CUDA
kernels for the distributed arbitrary waveform search, PSO synchronization
scripts, and DDS streaming code" a `/Datasets` s „High-speed Data Acquisition
(DAQ) logs comparing isothermal calorimetry and voltage curves".

Deposit obsahuje jeden soubor: to čtyřstránkové PDF, 97 786 bajtů. Hlavička PDF
navíc navrhuje „CC BY 4.0 for text and data, CERN-OHL-S for hardware"; záznam na
Zenodu nese jen CC BY 4.0.

Je to tentýž vzorec jako §6 cymatické práce, která slibuje GitHub repozitář
a žádný nejmenuje — ale v budoucím čase. Tady jsou data popsaná jako poskytnutá.

## 7. Co místo toho říká vlastní citace té práce

Purushothaman & Landau (2006), jediná pulzní reference preprintu, identifikuje
limitující mechanismus jako **difuzi v pevné fázi**: koncentrace lithia „reaches
saturation at the graphite/electrolyte interface after about 1 h under
conventional constant current charging". Jejich analyzovaný protokol je **pulz
3 s a klid 1 s** — 75 % střída, 0,25 Hz. A jejich nejlepší výsledek není pulz
vůbec: „A nonlinearly decreasing current density profile … was shown to provide
complete charging in less than 3/4 of an hour, faster than any other
pulse-charging profile studied."

Takže jediný zdroj citovaný pro pulzování podporuje W_macro, při čtvrt hertzu,
a dává přednost spojité rampě před jakýmkoli pulzem. Žádné výhodné kHz pásmo
neidentifikuje a obsahový audit všech šesti referencí tohoto depositu
v [`reference-audit`](https://github.com/karagos01/reference-audit) nenašel
žádnou, která by ho identifikovala. Dva další citační posuny jsou zaznamenané
tam: Tarascon & Armand je Nature 414(**6861**) a „Macdonald (2005)" je Barsoukov
& Macdonald jako editoři druhého vydání, přičemž Macdonald sám editoval jinak
nazvané první vydání z roku 1987.

## 8. Hranice

Žádný článek nebyl postavený, nabitý ani měřený. Všechno tady je aritmetika nad
vlastními parametry preprintu a nad publikovanými hodnotami, protože deposit
nepřikládá kód, měření ani obrázky.

Provenience je označená v `constants.py`: `[P]` vlastní hodnoty preprintu, `[V]`
ověřeno proti pojmenovanému zdroji, `[A]` předpokládaný rozsah, který se
proměřuje místo tvrzení. Životnost coin-cell, tloušťka folie, Arrheniova
aktivační energie, rozpočet vyhodnocení pro PSO a vzorkovací rychlost DDS jsou
všechno `[A]` a každý závěr z nich je spočítaný přes celý rozsah.

Ramanovská čísla jsou z lithiové NMC katody, ne ze sodíkové. Jsou použitá proto,
že vrstevnatý LiMO₂ a sodíkové vrstevnaté oxidy mají společnou strukturu
α-NaFeO₂, takže frekvence módů jsou správného řádu; sodíkově specifické měření
by je posunulo o desítky procent a ne o šest řádů, což je velikost té mezery,
o kterou jde.

Pásmo EIS je citované jako „approximately 1 Hz to 1 kHz", kde se půlkružnice
přenosu náboje konvenčně nachází. Reálné články se liší chemií, teplotou
a stavem nabití a článek s neobvykle rychlou kinetikou by ten zlom posunul výš.
Musel by ho posunout o tři řády, aby dosáhl horní hranice F_micro.

Tvrzení v §4, že naměřená aparentní aktivační energie pro R_i odpovídá jedinému
procesu, je zjednodušení; R_i agreguje vodivost elektrolytu, transport SEI
a přenos náboje, každý s vlastní teplotní závislostí. Proměřovaný rozsah to má
pokrýt a závěr — že ta signatura vznikne už samotným ohřevem — platí ve všech
jeho bodech.

## 9. Data a kód

`constants.py` drží každou konstantu s příznakem provenience a zdrojem a žádný
další skript žádnou nedefinuje. `frequency.py`, `anomaly.py` a `throughput.py`
reprodukují §§2–6. `run_all.sh` projde všechno offline za asi sekundu,
`results.log` je výstup jednoho běhu. Verdikty u referencí se tady neduplikují —
žijí se svou evidencí v
[`reference-audit`](https://github.com/karagos01/reference-audit).

## Reference

Vyhodnocený preprint: M. Mazgal, *Dual-Scale Waveform Optimization and
Hysteretic-Fractal Resonant Stimulation (HFRS) for Minimizing Transport
Resistance in Na-ion Lattices*, Zenodo, 6. října 2026, DOI
10.5281/zenodo.23186884, CC BY 4.0.

Externí zdroje jsou citované v `constants.py` vedle hodnot, které podpírají:
Raman and Infrared Spectroscopy of Materials for Lithium-Ion Batteries,
*Int. J. Mol. Sci.* 26(24), 11879 (2025), DOI 10.3390/ijms262411879, pro
mřížkové módy katody; literatura o migračních bariérách v NaFeO₂ a NaFePO₄,
včetně *Materials* 12(19), 3243 (2019), DOI 10.3390/ma12193243; standardní praxe
EIS pro pásmo přenosu náboje; rezistivity z CRC; definující konstanty SI 2019;
a Purushothaman, B. K. & Landau, U., *J. Electrochem. Soc.* 153(3), A533 (2006),
DOI 10.1149/1.2161580. Citace jsou krátké výňatky použité pro kritiku a recenzi.
