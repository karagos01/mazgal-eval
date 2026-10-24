# Polovina tvrzení: vyhodnocení *Intensional Physics Computing* a openQL v1.1

karagos01, říjen 2026

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`PAPER.md`](PAPER.md).

## Abstrakt

Dva deposity z 8. října 2026 jsou vyhodnocené společně, protože ani jeden
nestojí sám: M. Mazgal, *Intensional Physics Computing: Generating Virtual
Reality via Multidimensional Tensor Core Queries* (DOI
[10.5281/zenodo.23241777](https://doi.org/10.5281/zenodo.23241777)) převypráví
sekce openQL jako samostatnou práci a *openQL / openOL … (Version 1.1)* (DOI
[10.5281/zenodo.23241148](https://doi.org/10.5281/zenodo.23241148)) reviduje
originál z 3. října.

**Polovina toho hlavního nového tvrzení je správná, a tím je třeba začít.** §5
v IPC tvrdí „millions of physical queries per millisecond" — tedy 10⁹/s. Pro
uzel 4×4, který §3 přiřazuje 12D vrstvě, je svazující strop na kartě, kterou
autorovy vlastní preprinty specifikují, **1,46·10¹⁰ dotazů/s**, takže se to
tvrzení vejde s 14,6× rezervou. Pro uzel 112×112 z téže věty je strop
**1,87·10⁷/s**, tedy mimo **54×**. §5 to tvrdí pro oba zároveň.

**Ale pro aplikaci, pro kterou je to číslo uvedené, nedostačuje.** §4 dělá
z raymarchingu mechanismus, kterým scéna vůbec existuje, takže rozhodující
rozpočet je dotazů na pixel na snímek: 10⁹/s koupí **8,0 kroku na pixel** při
1080p60. Volumetrický raymarching obvykle chce 64–256, takže uvedená rychlost je
**4 až 32× nízká** — ještě než který krok udělá nějakou fyziku. Vlastní
renderovací reference té práce, NeRF, potřebovala 150–200 milionů dotazů na
obrázek při **30 sekundách na snímek**; její počet dotazů se s tímto výpočtem
shoduje, což je bod ve prospěch architektury, a její čas na snímek je opakem
„absolute real-time".

**IPC navíc zesiluje tvrzení, které už bylo vyvrácené.** §3 nazývá
σ(W_PINN ⊗ S(t) + b) „a symplectic discrete Hamiltonian operator", zatímco
openQL v1.0 říkal jen, že to „preserves the Lie group symmetries". Ten výraz je
nezměněný. Bylo to naměřené v `openql-eval/symplectic.py`: se σ = tanh ujede
harmonický oscilátor na 2·10⁻⁵ × E(0) za 10⁵ kroků a nafitované kyvadlo dojde na
10,2 × E(0), zatímco leapfrog drží 1,0000 × E(0) bez trénování. „Symplectic" se
vyskytuje v přesně jedné práci citované kterýmkoli z těch preprintů, a to
o Freudenthalově prostoru pro E₇, ne o časovém kroku.

**openQL v1.1 vypustila čtyři tvrzení, která tohle vyhodnocení měřilo.**
Odvození 112, „Tensor Core load in the efficient 15-20% range", „the memory
footprint of a single node reaches tens of kilobytes" a „without requiring
floating-point correction loops" jsou pryč, spolu se všemi pěti glosami
u referencí a klíčovým slovem „octonions" — přičemž abstrakt pořád říká, že
architektura funguje „By transforming quaternion and octonion algebra into
unified block matrices", což je ta polovina vyloučená teorémem. Ta shoda je
zaznamenaná; příčinnost se netvrdí, protože revize nemá žádný changelog.

**Její jediná substančně nová sekce je §6.1**, případová studie motoru BLDC
tvrdící „millions of organically mutated topologies per day" na mřížce
s milionem uzlů. To nechává **14 až 140 update sweepů** na kandidáta — tedy asi
jeden multigridový lineární solve — pro účelovou funkci, která musí pokrýt
magnetostatické pole, zvlnění momentu přes elektrický cyklus, polohově závislé
cogging, hysterezní ztráty potřebující historii B–H a vázaný tepelný ustálený
stav. A argument o zero-branchingu, na kterém to stojí, je správný, ale obrácený:
bezpodmínečnost znamená, že na prázdném prostoru není žádná úspora, což je
**2× až 100× penalta** proti řídkému solveru na převážně vzdušné mřížce motoru,
ne výhoda.

## 1. Co je správně

**Ta rychlost dotazů pro 4×4 je dosažitelná**, s 14,6× rezervou na propustnosti.
Je to první numerické hardwarové tvrzení v téhle sérii, které aritmetika
podpírá, místo aby ho vyvracela, a zaslouží si to být řečeno bez výhrad.

**Počet dotazů u NeRF je správného řádu.** Model z §4 — paprsek dotazující se
každého uzlu, kterým prochází — implikuje asi 10⁸ dotazů na obrázek při
použitelném vzorkování, a NeRF naměřil 150–200 milionů. Takže odhad
architektury, kolik práce volumetrický snímek stojí, je správný. Co je špatně,
je rychlost, jakou se ta práce dá udělat.

**Zero-branching je reálná vlastnost MMA pipeline.** „Computing empty space
takes the exact same nanosecond fraction as computing a highly complex,
asymmetric copper coil" je pravda. §4 níž rozporuje, co to vynáší, ne jestli to
platí.

**Rozdíl intenze a extenze je v logice reálný** a analogie s uložením pravidel
místo vyjmenovaného stavu je jako rámec legitimní. Signed distance fields
a procedurální generování ten prostor obývají už dnes, což je precedens, na který
se ta práce mohla odvolat.

**112 = 7 × 16 přesně**, takže uzel 112×112 kryje tensor-core granularitu 16×16
na 100 %. Je to shoda okolností, ne návrhové rozhodnutí, protože práce odvozuje
112 odjinud a ne z hardwaru, ale platí to.

## 2. Rychlost dotazů, oběma směry

IPC §5: „the hardware stops rendering hollow shells and begins acting as
a particle micro-accelerator, evaluating millions of physical queries per
millisecond". Při nejmírnějším čtení „miliony za milisekundu" je to 10⁹ dotazů
za sekundu. §3 definuje dvě velikosti uzlu: 4×4 pro „12D macroscopic physics"
a 112×112 pro „quantum-level physics".

| uzel | na jedno MMA | výpočetní strop | strop propustnosti | svazující | proti tvrzení |
|---|---|---|---|---|---|
| 4×4 | 32 B, 128 FLOP | 1,11·10¹² /s | 1,46·10¹⁰ /s | propustnost | **14,62× — vejde se** |
| 112×112 | 25 088 B, 2,81·10⁶ FLOP | 5,05·10⁷ /s | 1,87·10⁷ /s | propustnost | **0,02× — přesahuje** |

Oba jsou svázané propustností, což je tentýž závěr, ke kterému pro tuhle
architekturu došlo `openql-eval/roofline.py` jinou cestou. Malý uzel se vejde
pohodlně, velký je mimo 54×. Ta věta tvrdí tu rychlost pro architekturu jako
celek, takže polovina z ní platí.

Jedna výhrada ve prospěch práce a jedna proti. Proti: uzel 4×4 obsadí jednu
šestnáctinu dlaždice 16×16, takže výpočetní strop výše je optimistický, pokud se
do jedné dlaždice nenapakuje víc uzlů — což možné je, ale je to jiný algoritmus
než model jeden-uzel-jedno-MMA, který §3 popisuje. Ve prospěch: pro 112 je to
dlaždicování přesné.

## 3. Ta rychlost nedostačuje pro svou vlastní aplikaci

§4 výslovně dělá z dotazování způsob, jakým se scéna vůbec pozoruje: „When
a virtual camera casts a photon (a ray) into the tensor grid, the photon travels
through the matrices and interrogates them. At each step, the ray asks the local
node". Takže každý krok marchingu je dotaz a rozhodující rozpočet je na pixel na
snímek.

| kroků na pixel | potřeba dotazů/s | proti tvrzení |
|---|---|---|
| 32 | 3,98·10⁹ | 3,98× |
| 64 | 7,96·10⁹ | 7,96× |
| 128 | 1,59·10¹⁰ | 15,93× |
| 256 | 3,19·10¹⁰ | 31,85× |

Uvedená rychlost koupí **8,0 kroku marchingu na pixel** při 1080p60.
Volumetrický raymarching skrz zúčastněné médium obvykle chce 64–256 vzorků na
paprsek a s osmi je výsledkem výrazné pruhování na každém gradientu. A to ještě
než krok udělá jakoukoli fyziku, přečte stav paprsku nebo zapíše výsledek —
strop spočítaný v §2 předpokládá, že se nedotýká ničeho kromě samotného uzlu.

Takže ta rychlost je zároveň v abstraktu dosažitelná a čtyři až třicetdvakrát
nízká pro účel, pro který je uvedená. Poctivé čtení je, že to číslo není
chybné, odpovídá na jinou otázku, než jakou §4 klade.

NeRF říká totéž z druhé strany: 150–200 milionů dotazů na obrázek, 30 sekund na
snímek na V100, 1–2 dny tréninku. Citovaný v obou preprintech jako „theoretical
predecessor" pro real-time volumetrickou syntézu běžel na 0,03 snímku za
sekundu.

## 4. openQL v1.1 §6.1, jediná nová sekce

§6.1 tvrdí, že genetický algoritmus nad 12D enginem „circumvents" kombinatorickou
explozi a dokáže „simulate millions of organically mutated topologies per day" na
mřížce s milionem uzlů.

Uzel 12×12 fp16 má 288 B, takže stav mřížky je 274,7 MiB a jeden update sweep
přesune 549,3 MiB — 0,615 ms při 936 GB/s, svázané propustností. To dává:

| topologií/den | čas na jednu | dostupné sweepy |
|---|---|---|
| 1 000 000 | 86,400 ms | 140,4 |
| 5 000 000 | 17,280 ms | 28,1 |
| 10 000 000 | 8,640 ms | 14,0 |

Tedy 14 až 140 sweepů celé mřížky na jeden kandidátní návrh. Multigridový
Poissonův solve na 100³ je v tom rozsahu pro **jeden** lineární solve. Účelová
funkce, kterou §6.1 popisuje, není jeden lineární solve; aby mohla řadit
topologie motoru, musí vyhodnotit minimálně magnetostatické pole vinutí, moment
a jeho zvlnění přes celý elektrický cyklus, cogging jako funkci polohy rotoru,
hysterezní ztráty vyžadující historii B–H v každém uzlu, a tepelný ustálený
stav, který bere pole ztrát jako vstup. Několik z nich je vázaných a ty polohově
závislé potřebují pole přepočítané pro mnoho úhlů rotoru. Na celé tohle je
k dispozici rozpočet jednoho solve.

**A argument o zero-branchingu je obrácený.** Je pravda, že MMA pipeline stojí
pro vzduch stejně jako pro měď. Ale to je tvrzení, že na prázdném prostoru není
žádná úspora, a hlavní ekonomika konvenčního solveru na mřížce motoru je právě
to, že většina objemu je vzduch:

| mřížka prázdná | řídký solver udělá | hustý udělá | penalta |
|---|---|---|---|
| 50 % | 50 % | 100 % | 2,0× |
| 90 % | 10 % | 100 % | 10,0× |
| 99 % | 1 % | 100 % | 100,0× |

Zero-branching je cena té architektury, ne její výhoda, a §6.1 předkládá absenci
úspory jako to, co ten limit obchází.

Třetí bod: ta exploze, kterou §6.1 jmenuje, je v prostoru hledání topologií, ne
v ceně jednoho vyhodnocení. Genetický algoritmus ji řeší tím, že vyhodnotí málo
kandidátů dobře, takže potřebuje levnou a přesnou účelovou funkci — a to je přesně
to, co ten rozpočet sweepů omezuje. Tím, že se každé vyhodnocení udělá
bezpodmínečné, se počet kandidátů nezmenší, a počet kandidátů je ta veličina,
která se nazývá nepřekonatelnou. Sekce uvádí jako vstupy objem prostoru a limit
48 V, bez jakékoli parametrizace vinutí, takže dimenze toho prostoru není daná
a nedá se tu zkontrolovat.

Jediné nové fyzikální tvrzení §6.1 je „fractal-like winding patterns that
minimize skin effect". Kožní efekt je vytlačování proudu k povrchu vodiče a
zavedenou nápravou je rozdělit vodič na vlákna tenčí než hloubka vniku
a transponovat je — tedy Litzův drát. Fraktální hranice zvětšuje obvod při
konstantním průřezu, což dává víc měďi do oblasti s vysokou proudovou hustotou.
Fraktální geometrie mají reálné použití v RF antenách, kde je cílem dlouhá
elektrická cesta v malém objemu; to je jiná účelová funkce a §6.1 nedává žádný
mechanismus, který by je spojoval. Zaznamenávám to jako nepodložené, ne jako
naměřené, protože ta sekce neudává žádnou geometrii vinutí, proti které by se
dalo počítat.

## 5. Diff verzí a co ukazuje a neukazuje

Ve v1.1 je vypuštěných šest věcí a čtyři z nich jsou tvrzení, která
`openql-eval` měřilo:

- odvození 112 — „derived from the necessary degrees of freedom to encapsulate
  the macroscopic 12D gauge groups alongside the microstate variables of
  crystallography, spin configurations, and valence orbital interactions"
  ← měřeno
- „keeps Tensor Core load in the efficient 15-20% range when simulating
  environments with millions of nodes" ← měřeno
- „the memory footprint of a single node reaches tens of kilobytes" ← měřeno
- „without requiring floating-point correction loops" ← měřeno
- všech pět glos u referencí
- klíčová slova „octonions" a „dimensional reduction"

Ta shoda je celá evidence. Revize nemá changelog a neuvádí důvod k žádné
úpravě, takže se tu žádná příčinnost netvrdí a žádná se do toho nemá vkládat.

Dvě věci jsou nápadně nezměněné. Abstrakt pořád říká, že architektura funguje
„By transforming quaternion and octonion algebra into unified block matrices",
zatímco „octonions" zmizelo z klíčových slov — a oktonionová polovina té věty je
ta vyloučená teorémem, naměřená v `openql-eval/octonion.py`. A ORCID placeholder
v hlavičce PDF je pořád nevyplněný: v1.0 měla `[ORCID: enter-your-orcid]`, v1.1
má `[ORCID: Zadejte-svůj-ORCID]`. Nebyl vyplněný, byl znovu vygenerovaný česky.
Autorovo skutečné ORCID je v metadatech záznamu na Zenodu od 3. října, takže ten
identifikátor existuje a zastaralá je jen šablona PDF.

Jedna nekonzistence mezi těmi dvěma deposity z téhož dne: openQL dává 12 dimenzí
do uzlu 12×12 postaveného ze tří zřetězených kvaternionových bloků 4×4, zatímco
IPC §3 popisuje uzel pro tutéž vrstvu jako matici „4×4 (for 12D macroscopic
physics)" — 16 slotů pro 12 čísel, v jiném uspořádání, než jaké openQL
specifikuje.

## 6. Co se tady neměří

Intenzionálně-výpočetní rámování IPC §§1–2 a §4 je filozofická pozice
o reprezentaci, ne kvantitativní tvrzení, a nic tady o ní nerozhoduje. Ukládat
pravidla a generovat stav na vyžádání je reálná technika s reálnými precedenty.

Tvrzení, že CPU „fail at this task because they rely on branching logic", se tu
taky neměří, byť dvě věci o jeho formě stojí za zmínku: CPU mají taky SIMD
a bezpodmínečný kód, a raymarcher je inherentně podmíněný v bodě ukončení
paprsku — a právě proto vlastní návrh v §4 předává mezi CUDA jádry a tensor
cores, a to předání je podmínka.

Pět referencí IPC bylo obsahově přečteno v
[`reference-audit`](https://github.com/karagos01/reference-audit); čtyři jsou
společné s openQL a pátá je Fittingova položka ve Stanfordské encyklopedii
o intenzionální logice, v níž mají „tensor", „GPU", „matrix" a „quantum" nula
výskytů každé a jejíž §4.5 se jmenuje „Algorithms Need Not Be Effective".

## 7. Hranice

Žádná GPU nebyla použita. Hardwarové údaje jsou katalogové specifikace RTX 3090,
kterou autorovy vlastní preprinty jmenují, a spočítané stropy jsou teoretické
špičky — reálná implementace dosáhne jejich zlomku, což nálezy typu „přesahuje
kartu" zesiluje a nález „vejde se" oslabuje. Rezerva 14,6× u uzlu 4×4 je dost
velká, aby přežila jakýkoli reálný koeficient účinnosti.

Provenience je označená v `constants.py`: `[P]` z preprintů, `[V]` ověřeno proti
pojmenovanému zdroji, `[A]` předpokládaný rozsah, který se proměřuje místo
tvrzení. Rozlišení obrazovky, snímková frekvence, počet kroků marchingu a podíl
prázdné mřížky jsou všechno `[A]`.

Nejmíň pevný předpoklad je rozsah 64–256 kroků. Techniky, jak ho snížit,
existují — přeskakování prázdného prostoru, adaptivní a importance vzorkování —
ale přeskakování prázdného prostoru je právě to, čeho se návrh se
zero-branchingem z §6.1 vzdává, takže ta architektura má těch možností méně než
konvenční renderer, ne víc.

Počet sweepů v §4 je odvozený z toho tvrzení, ne předpokládaný, a srovnání
s multigridovým solvem je řádové; závěr je, že rozpočet jednoho solve musí
pokrýt multifyzikální účelovou funkci, a to na přesné konstantě nezávisí.

## 8. Data a kód

`constants.py` drží každou hodnotu s příznakem provenience a zdrojem a žádný
další skript žádnou nedefinuje. `queries.py` reprodukuje §§2–3 a tu poznámku
o symplektičnosti, `bldc.py` §4 a `versions.py` §5; `versions.py` je záznam, ne
výpočet, a je držený jako skript, aby se objevil v `results.log`. `run_all.sh`
projde všechno offline za asi sekundu.

Měření openQL v1.0, na která se tady odkazuje, se tu nereprodukují. Žijí
v [`openql-eval`](https://github.com/karagos01/openql-eval) a verdikty
u referencí v
[`reference-audit`](https://github.com/karagos01/reference-audit).

## Reference

Vyhodnocené preprinty: M. Mazgal, *Intensional Physics Computing*, Zenodo,
8. října 2026, DOI 10.5281/zenodo.23241777; a *openQL / openOL: Tensor Matrix
Architecture for Unified Simulation of Physical Fields in 12D and 112D via GPU
Tensor Cores (Version 1.1)*, Zenodo, 8. října 2026, DOI
10.5281/zenodo.23241148. Obojí CC BY 4.0.

Externí zdroje jsou citované v `constants.py` vedle hodnot, které podpírají:
katalogové specifikace NVIDIA RTX 3090; Markidis, S. et al., IPDPSW 522–531
(2018), DOI 10.1109/IPDPSW.2018.00091, pro granularitu dlaždice WMMA a varování
o přesnosti; a Mildenhall, B. et al., ECCV (2020), arXiv:2003.08934, pro počet
dotazů a čas na snímek u NeRF. Citace jsou krátké výňatky použité pro kritiku
a recenzi.
