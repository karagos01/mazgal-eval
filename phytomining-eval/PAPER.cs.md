# Jedna věta, dvě hustoty: vyhodnocení *Quantum Biofortification and In-Situ Phytomining*

karagos01, říjen 2026

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`PAPER.md`](PAPER.md).

## Abstrakt

M. Mazgal, *Quantum Biofortification and In-Situ Phytomining: Design of an
Autonomous Closed-Loop Nanometallic Agricultural Matrix* (Zenodo, 6. října 2026,
DOI [10.5281/zenodo.23174932](https://doi.org/10.5281/zenodo.23174932)) navrhuje
zapravit 25 t/ha pelet z biocharu a bentonitu s extrémofilními bakteriemi, 5 kg
zlata na 30 ha a profil „stabilních izotopů s nenulovým jáderným spinem", aby
plodiny a lidé i zvířata, kteří je jedí, získali „absolute structural immunity"
a „the theoretical blockade of natural biological aging processes".

Čtyři měření. §4 uvádí v jedné větě objemovou hustotu, počet na metr kvadrátní
a hmotnost na hektar, jako by to bylo totéž; při uvedené hloubce orby je první
údaj **24×** vyšší než druhý, a celý nacenený návrh práce stojí na druhém. §3.3
nazývá ¹³⁸La stabilním izotopem: je to **primordiální radionuklid** s poločasem
1,03·10¹¹ let, rozpadající se 65,5 % β⁺ a 34,5 % β⁻. Premisa §3.3 ale u lanthanu
padá ještě dřív, než na tom záleží, protože ¹³⁹La — 99,91 % veškerého lanthanu —
**už spin 7/2 má**, takže není co vybírat. A při přírodním izotopovém složení
zvedne matrice lanthan v poli **asi o pětinu** proti tomu, co tam už je, a podíl
¹³⁸La nechá přesně tam, kde byl — takže z „nejradikálnější inovace matrice" je
přidání obyčejné zeminy.

Vlastní seznam literatury práce obrací tři její nosná tvrzení. Citovaný autor
magnetického izotopového efektu měří pro přesně tu trojici izotopů, kterou práce
cituje pro akceleraci, **3–5× potlačení** syntézy DNA a navrhuje je jako
cytostatikum; citovaná práce o zlatě má zlato oxidační stres **vyvolávající**
a buňkou vyváděné, kde práce má biogenní zlato, které ho „entirely blocking";
a citovaná phytominingová recenze je o **odnímání** kovu z půdy a jeho tavení.
Všechny tři jsou s doslovnou evidencí v doprovodném repozitáři
[`reference-audit`](../reference-audit) a v §6 tady.

Dva nálezy jdou naopak. Premisa §1 — 30–50 % dodaného dusíku využito první
plodinou — je správná. A přidaný ¹³⁸La je radiologicky zanedbatelný, čtyři až
pět řádů pod kaliem-40, které v té půdě už je, takže označit ho za stabilní je
chyba o nuklidu, ne bezpečnostní problém návrhu.

## 1. Co je správně

**Úvodní premisa obstojí.** §1 říká, že rostlina využije „only 30% to 50% of the
supplied nutrients in real-time". Využití dusíku z hnojiva první plodinou je
30–50 %, takže práce vychází z reálného a dobře kvantifikovaného problému
a vyplavování, které popisuje, je jeho standardní důvod.

**Biochar jako nosič bakteriálního inokula je reálný precedens**, ne výmysl té
práce, a citovaná Lehmannova recenze ho podpírá ve vlastním abstraktu — „as
inoculant carriers". Fyzický koncept lisované pelety se zpožděným uvolňováním
a sporami v porech je normální materiálové inženýrství a nic tady proti němu
nemluví.

**Všechny jáderné spiny jsou uvedené správně.** ¹³⁸La má I = 5, ²⁵Mg a ⁶⁷Zn
I = 5/2, ⁴³Ca I = 7/2. Jsou nenulové ze správného důvodu a kontrast, na kterém
práce staví — že hojné izotopy magnesia, zinku a kalcia jsou sudo-sudé a mají
tedy I = 0 přesně — je v pořádku. Magnetický izotopový efekt, na který se
odvolává, je reálná fyzika s reálnou literaturou.

**Hyperkomplexní slovník tam není.** Spočítáno nad extrahovaným textem:
„Maxwell", „octonion", „quaternion", „hypercomplex", „non-associative", „tensor"
a „causal" mají nula výskytů. Tento deposit je jeden ze šesti z autorových
šestnácti, který ten slovník nenese; census je v
[`reference-audit`](../reference-audit).

## 2. Jedna věta uvádí dvě hustoty, které jsou 24× vedle

§4, doslova:

> „Densification to the level of 1 pellet per 5 cm³ of soil (at a plowing depth
> of 30 cm) equates to approximately 2,500 pellets per 1 m², or 25 tons of
> matrix per 1 hectare."

Při hloubce 30 cm je pod metrem kvadrátním 300 000 cm³ zeminy. Jedna peleta na
5 cm³ je tedy **60 000 pelet/m²**, ne 2 500. Opačně: 2 500 pelet/m² je jedna
peleta na **120 cm³**.

Kterou z těch dvou práce používá? Rozhodne to hmotnost: 25 t/ha je 2,5 kg/m²,
což při 2 500 peletách/m² je přesně **1 g na peletu** — rozumná peleta. Při
60 000/m² by to bylo 0,042 g. Takže hmotnostní rozpočet, požadavek 750 tun
i miliondolarová případová studie stojí na těch 2 500, a „5 cm³" je ten údaj,
který nesedí.

A záleží na tom, protože těch 5 cm³ není dekorace. Věta hned před nimi je
odůvodnění: kořen „must not 'search' for distant deposits via fungi; it must be
in constant physical contact with the nanomatrix." Když se ten požadavek vezme
vážně, při vlastní 1g peletě:

| | když se drží 1 na 5 cm³ | údaj práce |
|---|---|---|
| matrice | **600 t/ha** | 25 t/ha |
| na 30 ha | **18 000 t** | 750 t |
| při téže ceně za tunu | **$24 000 000** | $1 000 000 |

Takže požadavek fyzického kontaktu a nacenený návrh nejsou tentýž návrh a jsou
od sebe faktorem 24. Je to jedno aritmetické klopýtnutí v jedné větě, ne vada
konceptu — ale je to ta věta, která spojuje biologickou motivaci s ekonomikou,
a to je spoj, na kterém celá případová studie visí.

Mimochodem ani jedna z těch hustot není kontakt. Na kubické mříži dává
2 500/m² přes 0,3 m střední rozestup 4,93 cm, takže kořen není nikdy dál než
2,5 cm od pelety; při 60 000/m² je to 1,71 cm a 0,9 cm. Obojí je vzdálenost,
kterou kořen musí prorůst, a práce neudává žádnou délkovou hustotu kořenů, proti
které by se to dalo poměřit.

## 3. ¹³⁸La není stabilní izotop

Abstrakt říká „a precisely defined profile of **stable isotopes** (including
elements with non-zero nuclear spin such as 138La, 43Ca, and 25Mg)". §3.3 říká
„the selection of rare, **stable** isotopes". Klíčová slova na Zenodu obsahují
„Stable Isotopes".

¹³⁸La je **primordiální radionuklid**: poločas 1,03(1)·10¹¹ let, rozpad β⁺
65,5 % na ¹³⁸Ba a β⁻ 34,5 % na ¹³⁸Ce, přírodní zastoupení 8,881(71)·10⁻⁴. Je to
jeden z několika mála lichých-lichých nuklidů, které přežívají od vzniku Země,
a právě proto je vzácný. Ta vzácnost, pro kterou si ho práce vybírá, a ta
nestabilita, kterou přehlíží, jsou tentýž fakt o tomtéž nuklidu.

Je to tvrdá, dohledatelná chyba a je v abstraktu, v textu i v metadatech. Není
to ale bezpečnostní problém — viz §7.

## 4. Premisa u lanthanu padá ještě dřív, než na stabilitě záleží

§3.3 nazývá „Quantum Circuit" svou nejradikálnější inovací a pravidlo výběru je
„rare, stable isotopes with a non-zero (and often asymmetric) nuclear spin".

**¹³⁹La, které je 99,91 % veškerého lanthanu, má spin 7/2.** Nenulový, a větší
než nic. Takže u lanthanu se výběrem vzácného izotopu žádný spin nezíská —
ten běžný ho už má.

U magnesia, zinku a kalcia ta logika funguje: ²⁴Mg, ²⁶Mg, ⁶⁴/⁶⁶/⁶⁸/⁷⁰Zn a ⁴⁰Ca
jsou sudo-sudé a mají I = 0 přesně, takže tam volba lichého izotopu magnetické
prostředí skutečně mění, a to je základ reálného magnetického izotopového
efektu. Lanthan je jediný prvek v tom seznamu, pro který to pravidlo nemá co
vybrat, a je to prvek, kolem kterého je ta sekce postavená — ¹³⁸La jako
„magnetický gyroskop" v synapsi je nejkonkrétnější mechanistické tvrzení celé
práce.

## 5. Při přírodním zastoupení přidá matrice méně, než v poli už je

Práce nikde neříká, že jsou izotopy obohacené, a její rozpočet — 1 t oxidu
lanthanu plus 3 t stopových prvků v položce za $146 000 — odpovídá běžnému
komerčnímu materiálu. Vezměme ji za slovo a spočítejme, co matrice změní.

Jedna tuna La₂O₃ je 853 kg lanthanu, což na 30 ha dává 2,84 g/m². Orniční vrstva
už lanthan obsahuje, při krustálním obsahu 31 ppm:

| objemová hmotnost | zemina pod 1 m² | La už přítomný | matrice přidá | nový obsah |
|---|---|---|---|---|
| 1,1 g/cm³ | 330 kg | 10,23 g/m² | +27,8 % | 39,6 ppm |
| 1,4 g/cm³ | 420 kg | 13,02 g/m² | +21,8 % | 37,8 ppm |
| 1,6 g/cm³ | 480 kg | 14,88 g/m² | +19,1 % | 36,9 ppm |

Takže ta nejradikálnější inovace zvedne lanthan v poli asi o pětinu — a při
přírodním izotopovém složení nechá podíl ¹³⁸La přesně tam, kde byl, na 0,0888 %.
**Přírodní izotopový poměr není něco, v čem může mít půda deficit.**

U dalších dvou to platí ještě silněji. ²⁵Mg je 10,00 % veškerého magnesia
a magnesium je hlavní půdní prvek: přes proměřovaný rozsah 0,2–3 % hmotnosti má
orniční vrstva už **84 až 1260 g/m² ²⁵Mg**. ⁶⁷Zn je 4,10 % veškerého zinku, tedy
0,34–2,07 g/m² už přítomných. Chlorofyl už obsahuje ²⁵Mg na 10,00 % svého
magnesia a zinkové fingery ⁶⁷Zn na 4,10 % svého zinku. Jakou velikost magnetický
izotopový efekt má, v tom poli už běží, a matrice ten poměr neposune.

Alternativní čtení taky k dispozici není. Získat tunu ¹³⁸La při jeho přírodním
zastoupení by vyžadovalo asi **1 126 tun** přírodního lanthanu jako vsázku, ještě
před náklady na separaci. Neobohacené: Quantum Circuit nepřidá nic. Obohacené:
rozpočet je o řády mimo. Práce potřebuje jedno z těch dvou čtení a nenacenila
ani jedno.

## 6. Reference obracejí tři nosná tvrzení

Všech šest referencí tohoto depositu bylo obsahově přečteno v doprovodném
repozitáři [`reference-audit`](../reference-audit),
kde je doslovná evidence i záznam, jak daleko se každou práci podařilo přečíst.
Tři výsledky se týkají přímo tvrzení výše.

**Buchačenko o magnetickém izotopovém efektu.** Práce ho cituje pro ²⁵Mg a ⁶⁷Zn,
které „accelerate the chemical kinetics of DNA transcription and ATP synthesis".
Jeho vlastní výsledek pro přesně tu trojici:

> „The substitution of these catalyzing ions in polymerases by the ions ²⁵Mg²⁺,
> ⁴³Ca²⁺, and ⁶⁷Zn²⁺ with magnetic nuclei was shown to produce a huge isotope
> effects: nuclear magnetic ions **by 3–5 times suppress DNA synthesis**"

> „A new **anti-cancer strategy** is suggested based on the using of the nuclear
> magnetic ions of magnesium, calcium, and zinc as a powerful and universal
> means to **selectively kill** only cancer cells."

Reparace je taky 1,5× pomalejší. Přežívá jen tvrzení o ATP — a to jen pro ²⁵Mg
při obohacení 99,9 % dodané injikovatelnou nanočásticí, a nereplikovalo se
v PNAS v roce 2012, což práce neuvádí. Zinková polovina glosy je navíc
anachronismus: Buchačenkova biologická práce o zinku je z roku 2013, čtyři roky
po citované knize z 2009.

**Reith et al. o zlatě.** Práce má biogenní nanozlato jako „ultimate scavengers
of reactive oxygen species (ROS), entirely blocking cellular corrosion".
Citovaná práce: „Au detoxification is mediated by a combination of **efflux**,
reduction, and possibly methylation", a „one major toxic effect of Au(III) … is
the **induction of oxidative stress**", s minimální inhibiční koncentrací 2 µM.
Buňka zlato vyváží, aby přežila, a zlato vyvolává právě ty částice, které podle
práce vychytává. Citace se navíc v uvedené podobě nedohledá: skutečná práce je
Reith et al. (2009), PNAS 106(42), 17757–17762.

**Sheoran et al. o phytominingu.** Phytomining je v té recenzi „a … technology
of **phytoremediation**", kde se plodina sklidí jako „bio-ore" a „smelted, and
recovered" — kov se z půdy **odnímá** a prodá. Práce to cituje jako základ pro
**dodávání** zlata, lanthanu a vanadu do poživatelné biomasy a pro jejich
udržení v systému. Opačný směr toku hmoty a opačný účel.

Dva další rozpory jsou menší. Práce říká, že biochar „provides massive cation
exchange capacity"; Lehmann říká, že biochary „typically have **initially low**
cation exchange capacities (CEC)" a že vyšší pyrolýzní teplota ji dál snižuje.
A Wright & Upadhyaya je glosováno pro „mechanics of glomalin production and its
role in … water retention", ale je to survey 37 vzorků s jediným výstupem
v podobě regrese, voda se v něm objevuje jen jako destrukční agens při mokrém
sítování, a tělo práce glomalin ani mykorhizu nezmiňuje jinak než proto, aby je
obešlo.

## 7. Ekonomika, a jedna věc, která je naopak uklidňující

**Položka za zlato je zastaralá, ne metodicky chybná.** $417 000 za 5 kg
implikuje $83,40/g, tedy $2 594 za troyskou unci. Spot v den depositu byl
$4 168,80/oz, čili $134,03/g, takže 5 kg stálo $670 150 — ta položka chybí
o $253 150 a celkový součet je $1 253 150.

**Návratnost vyžaduje trvalou diskontní sazbu nejvýš 2,5 %.** Proti $25 000/rok
tvrzených úspor má $1 000 000 jednoduchou návratnost **40 let** a současná
hodnota té úspory navěky se rovná kapitálu právě při 2,50 % ročně. Nad tím je
čistá současná hodnota negativní. Práce tomu říká „permanent capital", což je
správný rámec pro ten argument — ale ten rámec pak vyžaduje, aby ten inventář
skutečně byl permanentní.

**Uzavřená smyčka vyžaduje roční ztráty pod 1,72 %.** Aby do čtyřicetileté
návratnosti přežila víc než polovina inventáře kovů, musí celková roční ztráta
zůstat pod tím číslem — a musí pokrýt odvoz sklizní po odečtení vráceného hnoje,
vyplavování, erozi i odtok současně. Práce předpokládá, že návratový podíl je
přesně 1, a neudává číslo pro žádnou jeho složku. Phytomining funguje
koncentrováním kovu do biomasy a biomasa z pole odchází, takže tady mechanismus
té práce pracuje proti premise její vlastní smyčky.

**A radiologie je v pořádku, což je třeba říct naplno.** Jedna tuna přírodního
La₂O₃ obsahuje 757 g ¹³⁸La, celkem 705 kBq rozprostřených na 30 ha, tedy
2,35 Bq/m². Kalium-40, které v té orniční vrstvě už je, dává 42 000–294 000
Bq/m². Ten přírůstek je **čtyři až pět řádů** pod přírodním pozadím v každém
bodě rozsahu. Označit ¹³⁸La za stabilní je chyba o nuklidu, ne riziko v návrhu,
a to jsou dvě různé věci.

## 8. Co tady změřit nejde

§3.1–3.3 a §5 obsahují tvrzení, na která aritmetika nedosáhne: „absolute
structural immunity", „entirely blocking cellular corrosion", „immediate repair
of DNA strand breaks", synapse, které „theoretically exhibit quantum coherence
and extreme acceleration of cognitive transmission", společenství „impervious to
degenerative cellular diseases" a „the theoretical blockade of natural
biological aging processes".

Tady se neměří a ani se o to nepokouším. Dvě poznámky k jejich formě, což je
všechno, co je k dispozici. Ani jedno není vysloveno s dávkou, dobou,
endpointem nebo srovnávací skupinou, takže ani jedno není tak, jak je napsané,
falzifikovatelné. A to nejblíž mechanismu — ¹³⁸La v synapsi — nemá v seznamu
literatury vůbec nosič: jediná lanthanoidová citace práce obsahuje slova neuron,
synapse, brain, nuclear spin, quantum, coherence a aging nulakrát každé,
a konkrétně zpochybňuje tu substituci kalcia, na které mechanismus stojí („REs
are not perfect mimics of Ca … may not play a general role as Ca substitutes in
Ca-dependent proteins").

Tento deposit je taky bod, kde série začíná navrhovat intervence na lidech,
ne na hardwaru — biomasu z této matrice mají po generace jíst „animals and
humans". To je změna povahy proti ostatním depositům a zaznamenávám ji jako
takovou, bez dalšího komentáře.

## 9. Hranice

Žádná půda nebyla upravena, žádná plodina pěstována a žádný izotop měřen.
Všechno tady je aritmetika nad vlastními parametry preprintu a nad publikovanými
konstantami, protože deposit nepřikládá žádný kód, žádná měření a žádné obrázky.

Provenience je označená v `constants.py`. `[P]` značí vlastní hodnoty preprintu,
`[V]` hodnoty ověřené proti pojmenovanému zdroji při psaní tohoto a `[A]`
**předpokládané rozsahy, které se proměřují přes celý rozsah, netvrdí se** — objemová hmotnost
zeminy, půdní magnesium a zinek, krustální zlato, půdní kalium-40 a diskontní
a ztrátové sazby. Každý závěr z hodnoty `[A]` je spočítaný přes celý její rozsah
a vysloven jen tam, kde platí všude. Tohle značení existuje proto, že audit
referencí zjistil, že citování plausibilního čísla z hlavy je přesně způsob,
jakým se bibliografie pokazí; dvě konstanty použité v dřívější verzi této práce
byly degradovány na `[A]`, když se je tady nepodařilo ověřit proti primárnímu
zdroji.

Krustální lanthan je jediná externí hodnota, která nese závěr, a je `[V]`:
31 ppm, Rudnick & Gao, *Composition of the Continental Crust*. Půdní magnesium
a zinek jsou `[A]`, takže tvrzení, které podpírají, je ta slabší verze, co
přežije celý rozsah.

Rozestupy v §2 předpokládají kubickou mříž, takže jsou nejlepším případem;
reálné rozmetání a zaorání je méně uniformní, což střední vzdálenost k nejbližší
peletě zvětšuje, ne zmenšuje.

## 10. Data a kód

`constants.py` drží každou konstantu s příznakem provenience a zdrojem a žádný
další skript žádnou nedefinuje. `density.py`, `isotopes.py` a `economics.py`
reprodukují §§2–5 a §7. `run_all.sh` projde všechno offline za asi sekundu,
`results.log` je výstup jednoho běhu. Verdikty u referencí tady nejsou
duplikované — žijí se svou evidencí v
[`reference-audit`](../reference-audit).

## Reference

Vyhodnocený preprint: M. Mazgal, *Quantum Biofortification and In-Situ
Phytomining*, Zenodo, 6. října 2026, DOI 10.5281/zenodo.23174932, CC BY 4.0.

Použité externí zdroje, každý označený `[V]` v `constants.py` se svou citací:
tabulka izotopů lanthanu na Wikipedii zkřížená s CIAAW pro jaderná data ¹³⁸La
a ¹³⁹La; WebElements a NMR tabulky Hebrejské univerzity pro spiny a zastoupení
²⁵Mg, ⁶⁷Zn a ⁴³Ca; standardní atomové hmotnosti IUPAC 2021; definující konstanty
SI 2019; Rudnick & Gao, *Composition of the Continental Crust*, Treatise on
Geochemistry (2. vyd. 2014, DOI 10.1016/B978-0-08-095975-7.00301-6) pro
krustální lanthan; Kitco pro cenu zlata 6. října 2026; a IFA,
*Nutrient/fertilizer use efficiency*, kap. 1 (2014) pro využití dusíku první
plodinou.

Práce citované v §6 jsou celé uvedené, se svými DOI a s poznámkou, jak byla
každá získaná, v `refdata.py` repozitáře `reference-audit`. Citace jsou krátké
výňatky použité pro kritiku a recenzi.
