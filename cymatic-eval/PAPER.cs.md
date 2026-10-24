# Nota B dělená čtyřmi: vyhodnocení práce *Cymatic Stomatal Stimulation and Pulsed Optical Assimilation*

karagos01, říjen 2026

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`PAPER.md`](PAPER.md).

## Abstrakt

Práce M. Mazgala *Cymatic Stomatal Stimulation and Pulsed Optical Assimilation*
(Zenodo, 5. října 2026) navrhuje cylindrický fotobioreaktor, který dodává
4500 W/m² v pulzech po 50 µs se temnou fází 4000 µs, synchronizovaných s akustickou
vlnou 246,91 Hz, která má držet průduchy otevřené, a pak navrhuje reprodukovat
akustickou polovinu téhož v polním měřítku tím, že se přes SCADA firmware přeladí
hluk větrných turbín a vysokonapěťových transformátorů na 61,72 Hz. Je to první
z jedenácti autorových depositů, ve kterém není žádná hyperkomplexní algebra,
a první, jehož reference jsou téměř všechny reálné a citované správně.

Fyzika pulzního osvětlení je v hrubých obrysech v pořádku a temná fáze 4 ms je
řádově to, co ten návrh potřebuje. Všechno nad tím je tady naměřeno jako selhávající,
a selhává na aritmetice, ne na biologii.

Obě publikované frekvence jsou rovnoměrně temperované tóny: 246,91 Hz je B3 na
0,22 centu a 61,72 Hz je B1 na 0,43 centu, tedy pod hranicí, kde cvičený posluchač
rozdíl slyší. Optická perioda 50 µs + 4000 µs je 4,050 ms, což je 246,91 Hz — takže
časování, které má vyplývat z kinetiky Calvinova cyklu, a frekvence, která má
vyplývat z mechaniky svěracích buněk, jsou jedno číslo, a to číslo je nota B.
Dělení čtyřmi je zdůvodněno tím, že výsledek padne do „empiricky prokázaného PAFT
pásma"; měřeno proti pásmu review, které je pro to citované, tedy 0,1–1 kHz, dělení
frekvenci z toho pásma vyvádí — a 246,91 Hz v něm už bylo.

Při duty cyclu 1,2346 % je časově střední ozářenost 55,6 W/m² = 256 µmol/m²/s, což
je 1,57× pod saturačním bodem salátu a 5,5× pod saturačním bodem pšenice — takže
nefotochemické zhášení, ztráta, kterou má návrh obcházet, v režimu, který ten návrh
vytváří, téměř není nasazené. Sušina na kilowatthodinu je pod pulzováním
invariantní na 3,6·10⁻¹⁵ přes 81násobný rozsah duty cyclu, protože pulzování dělí
výnos i energii týmž činitelem; tvrzení, že se „redefinuje gram-per-watt limit CEA",
je tvrzení právě o té jedné veličině, se kterou to schéma nemůže hýbat. Interval
4 ms odpovídá reoxidaci plastochinolu na cytochromu *b₆f* (2–20 ms), ne Calvinovu
cyklu, kterému je připisován (250–500 ms, 62–125× pomalejší).

Polní polovina je ještě dál. Blade-pass frekvence třílisté turbíny při 14 ot/min je
0,700 Hz; na 61,72 Hz by bylo potřeba 1234 ot/min, Mach 18,8 na konci lopatky
a 85 000 g dostředivého zrychlení — a práce navrhuje toho dosáhnout *bržděním*.
I kdyby ten tón existoval, celý deklarovaný akustický výkon turbíny 105 dB re 1 pW
je o 22,5 dB — tedy 179× ve výkonu — pod 70 dB u rostliny, které generátory
z citovaného review dodávají z 30–60 m, a na kilometru je to 33 dB; a tou ztrátou je
geometrické rozptýlení, ne atmosférická absorpce, kvůli které byla ta frekvence
vybraná. Jako fázované pole má větrná farma prvky 90–180 vlnových délek od sebe
tam, kde se vyžaduje λ/2. Jádro transformátoru svázané s 50 Hz sítí vyzařuje linky
na celých násobcích 50 Hz a 61,72 Hz mezi ně nepatří, takže žádné nastavení firmwaru
tam energii nedostane; „asymmetric DC injection" je polocyklová saturace, poruchový
mechanismus. A konečně: potlačení polední deprese průduchů znásobuje transpiraci
listu přesně 3,0× nezávisle na sytostním doplňku vzduchu a stojí 1,3–2,5× více vody
na jednotku uhlíku pro každou saturující asimilační odezvu — což je cena, kterou
preprint sám uvádí, pro otevřená pole ozimé pšenice, cukrovky a brambor.

Všechno tady spočítají čtyři skripty bez přístupu k síti a bez GPU. Každá externí
konstanta je v `constants.py` se svým zdrojem.

## 1. Co je správně

Víc než v kterémkoli předchozím depositu tohoto autora, a vyplatí se být konkrétní.

**Nejsou tam oktoniony ani Maxwell.** Vzorec zdokumentovaný přes ostatních deset
depositů — správný algebraický fakt, k němuž je přilepený jeden vyloučený teorémem,
a historická atribuce Maxwellovi, která se objevuje přesně tam, kde jsou oktoniony —
tady chybí. Spočítáno nad extrahovaným textem: „Maxwell" nulakrát, „octonion"
nulakrát, „quaternion" nulakrát, „hypercomplex" nulakrát, „non-associative"
nulakrát, „tensor" nulakrát a „causal" nulakrát. Celý ten slovník tam chybí, není přeznačený.
Co je tady špatně, je špatně normálním způsobem.

> **Oprava, 9. 10. 2026.** Tato sekce původně tvrdila, že „causal" je tady na nule
> „poprvé v jedenácti depositech". To bylo špatně dvakrát a odhalil to census nad
> všemi šestnácti záznamy v doprovodném repozitáři
> [`reference-audit`](https://github.com/karagos01/reference-audit).
>
> „causal" bylo nulové už v openQL / openOL v1.0 z 3. října, dva dny před tímto
> depositem. A všech sedm výše počítaných termínů je nulových v **COBARu**
> (23. 9.) a v **Topological Momentum Drive** (24. 9.), což jsou oba inženýrská
> tvrzení — takže tento deposit není ani první s nulovým „causal", ani první bez
> hyperkomplexního slovníku.
>
> Správné čtení není vývoj v čase, ale dvě proložené skupiny. Šest ze šestnácti
> záznamů nenese ani jeden z těch termínů — COBAR, Momentum Drive, tento,
> fytomining, Na-ion HFRS a hemocyanin — zbylých deset je nese hustě, a ty dvě
> skupiny se střídají, nejdou po sobě. Počty pro tento deposit se nemění; špatně
> byl ten nárok na prvenství, který na nich stál, a byl to artefakt srovnání proti
> deseti depositům místo proti všem.

**Bibliografie je reálná.** Čtyři z pěti referencí se dohledají přesně, jak jsou
vytištěné: Müller, Li a Niyogi 2001 v *Plant Physiology* 125(4) 1558–1566;
Hassanien, Hou, Li a Li 2014 v *Journal of Integrative Agriculture* 13(2) 335–348;
Oerlemans, Sijtsma a Méndez López 2007 v *Journal of Sound and Vibration*
299(4–5) 869–883; Farquhar a Sharkey 1982 v *Annual Review of Plant Physiology*
33 317–345. Všechny čtyři jsou správný zdroj pro to tvrzení, ke kterému jsou
připnuté. Pátá je v §10.

**Pulzní světlo skutečně umí obejít NPQ.** Tohle není okraj. Energeticky závislé
zhášení (qE) se indukuje během sekund až minut přes acidifikaci lumenu; pulz 50 µs
je na jeho rozvinutí mnohem příliš krátký, takže vlak mikrosekundových pulzů opravdu
může dodávat fotony okamžitou rychlostí, která by pod spojitým světlem zhášení
spustila, a nespustit ho. Mechanismus pojmenovaný v §1 preprintu — přesycení
plastochinonového poolu — je navíc ten správný mechanismus, který je potřeba
odlehčit.

**Temný interval 4 ms je dobře zvolené číslo.** Je to správný řád pro reoxidaci
poolu (§5). Zdůvodnění, které je pro něj uvedené, je špatné, ale to číslo ne.

**Nízké frekvence se opravdu šíří s malou absorpcí.** §3 říká, že subharmonická
61,72 Hz „experiences minimal atmospheric attenuation over long distances". Při
63 Hz dává ISO 9613-1 asi 0,1 dB/km. To je správně.

**Zvuk na průduchy působí.** PAFT je reálná, byť sporná literatura, citované review
je rozumný vstup do ní a výnosové přírůstky, které tam jsou uvedené (5,7 % u rýže
až 37,1 % u okurky), obkládají těch 15–18 %, která preprint tvrdí.

**Hardware v malém měřítku je obyčejný a postavitelný.** STM32 řídící GaN
půlmůstky a I²S audio cesta, s kondenzátorovými bankami na špičku při 1,2 % duty, je
normální embedded návrh. Při 4500 W/m² špičkově a duty cyclu 1,2346 % je střední
optická zátěž 55,6 W/m², tedy asi 111 W/m² elektricky při 50% účinnosti —
nenáročné. Na tom bioreaktoru není nic obtížně proveditelného.

Dál následuje to, kde měření s prací nesouhlasí.

## 2. Obě publikované frekvence jsou nota B

Návrh nesou dvě frekvence: 246,91 Hz v reaktoru (§2.3) a 61,72 Hz v poli (§3).
O první se říká, že byla „synthesized to maximize localized guard cell vibration";
o druhé, že byla „calculated" jako čtvrtá subharmonická.

`frequency.py` porovná každou s rovnoměrně temperovanou chromatickou stupnicí na
A4 = 440 Hz:

| publikováno | nejbližší tón 12-TET | přesně | odchylka | centů |
|---|---|---|---|---|
| 246,910 Hz, §2.3 reaktor | **B3** | 246,942 Hz | −0,032 Hz | **−0,22** |
| 61,720 Hz, §3 pole | **B1** | 61,735 Hz | −0,015 Hz | **−0,43** |

Cent je stotina půltónu a nejmenší rozdíl výšky, který cvičený posluchač rozliší, je
kolem 5 centů. Obě čísla jsou nota B tak, jak by ji nastavila kytarová ladička,
s odchylkou na pětinu hranice lidské rozlišovací schopnosti. Že je polní frekvence
dvě oktávy pod reaktorovou, není nezávislý fakt: B1 je z konstrukce B3 dělené čtyřmi.

A pak optické časování:

| | |
|---|---|
| pulz, §2.2 | 50 µs |
| temná fáze, §2.2 | 4000 µs |
| perioda | 4,050 ms |
| repetiční frekvence | **246,91 Hz** |
| cymatická frekvence, §2.3 | **246,91 Hz** |
| rozdíl | 3,6·10⁻³ Hz, relativně 1,5·10⁻⁵ |

§2.2 odvozuje optické hradlování z „the enzymatic turnover rate of the Calvin
cycle". §2.3 odvozuje akustickou frekvenci z mechaniky svěracích buněk. Souhlasí na
jednu část z 10⁵, což je zaokrouhlení 246,91 Hz na dvě desetiny. Nejsou to dva
parametry, které jsou spolu náhodou souměřitelné; je to jeden parametr uvedený dvakrát se
dvěma různými odvozeními, a „synchronizes the acoustic pressure waves with the
optical pulses at a microsecond resolution" z §2.3 je potom triviálně splnitelné,
protože není co synchronizovat.

Nejde jen o uklizenost. Kdyby optickou periodu určovala kinetika přenosu elektronů,
byla by to biologická veličina s obhajitelnou hodnotou. Pokud ji určuje hudební
výška, pak to jedno číslo, na kterém stojí celý návrh v malém měřítku, nemá v práci
žádné biologické odvození, a souhlas v §2.3 je artefakt toho, že se dvakrát vybrala
stejná nota.

## 3. Citované pásmo vylučuje frekvenci, která byla odvozena, aby do něj padla

§3 uvádí, že mechanoreceptory rostlin reagují na nízkofrekvenční vibrace „typically
between 50 and 120 Hz", a dělí 246,91 Hz čtyřmi, aby výsledek „falls perfectly
within the empirically proven PAFT sensitive band".

Review citované pro PAFT je Hassanien et al. 2014. Pásmo v té práci je
**0,1–1 kHz**, při **70 ± 5 dB** SPL, dodávané z 30–60 m dedikovaným generátorem.

| frekvence | v pásmu preprintu 50–120 Hz | v citovaném pásmu 100–1000 Hz |
|---|---|---|
| 246,91 Hz, reaktor | ne | **ano** |
| 61,72 Hz, pole | ano | **ne** |

Takže to odvození běží obráceně. Reaktorová frekvence už v pásmu, které citované
review podporuje, byla; dělení čtyřmi ji z něj vyvede. Pásmo uvedené v §3 není
pásmo zdroje, na který se §3 opírá, a dělení je zdůvodněné právě tím rozporem.

Nic z toho neříká, že 61,72 Hz nemůže fungovat — jen že vlastní citace práce to
nepodporuje a že uvedený důvod pro tu volbu je opak toho, co ta citace říká.

## 4. Duty cycle položí střední hodnotu pod režim, na který je návrh cílený

§2.2 nahrazuje spojité světlo „extreme-intensity photon bursts (4500 W/m²)"
o 50 µs s následnou temnotou 4000 µs a tvrdí, že to „completely bypass[es] the NPQ
trigger". §2.1 dodává, že cylindrická geometrie nechá „photon capture efficiency
approach the theoretical maximum of 100%".

`light.py` spočítá, co to dodá:

| | |
|---|---|
| duty cycle | **1,2346 %** (1 : 81,0) |
| špičková ozářenost | 4500 W/m² = 20 700 µmol/m²/s = **10,35× plné slunce** |
| časově střední ozářenost | **55,6 W/m² = 256 µmol/m²/s = 0,13× plné slunce** |

při 4,6 µmol/J, což je standardní přepočet PAR. Pokud je těch 4500 W/m² celková
a ne PAR ozářenost, je fotonový tok ještě nižší; tohle bere tu hodnotu v její
nejpříznivější podobě.

Uhlík zafixovaný za den určuje střední tok, ne špička: pulz trvá 50 µs a karboxylace
integruje přes stovky milisekund. A střední hodnota, která tady vyjde, je pod
saturací světlem pro každou C3 plodinu:

| | µmol/m²/s | poměr ke dodané střední hodnotě |
|---|---|---|
| saturace světlem, salát | 400 | 1,57× nad |
| saturace světlem, pšenice | 1400 | 5,48× nad |
| **toto schéma, středně** | **256** | — |

Tím se ten argument obrací. NPQ je ztráta saturačního režimu: existuje proto, že
absorbované fotony přesáhnou to, co karboxylace stihne spotřebovat. Při
256 µmol/m²/s není rostlina pod *spojitým* světlem téže střední intenzity saturovaná
také, a tedy zháší málo. Mechanismus, kvůli jehož obejití je návrh postavený,
v režimu, který ten návrh vytváří, není silně aktivní. §1 porovnává proti
„continuous high-intensity irradiation", které tohle schéma ve středu nedodává —
dodává 13 % plného slunce.

A i tam, kde je NPQ plně nasazené, je zisk ohraničený číslem, které dodává sám
preprint: §1 uvádí ztrátu „up to 60% of absorbed photons", takže získat ji celou je
činitel 1/(1−0,6) = **2,50×**. Ohraničené, a daleko od „redefinování" limitu.

K tvrzení o 100 % záchytu fotonů: PAR absorptance jednoho zeleného listu je
0,84–0,90, takže jeden průchod to překročit nemůže. Zavřená odrazná dutina může být
lepší díky vícenásobným průchodům, takže 100 % není vyloučené natvrdo — ale strop pak
určuje odrazivost stěny krytu, kde jsou právě LED, a žádná odrazivost uvedená není.
Tohle je zaznamenáno jako nekvantifikované tvrzení, ne jako vada.

## 5. Interval 4 ms odpovídá jinému mechanismu, než který je pojmenovaný

§2.2: „The burst duration is tightly constrained to 50 µs, followed by a 4000 µs
dark phase. This temporal gating perfectly matches the enzymatic turnover rate of
the Calvin cycle, preventing PQ pool saturation."

| proces | časová škála | zdroj |
|---|---|---|
| temná fáze, §2.2 | **4,00 ms** | preprint |
| obrat RuBisCO, 1/k_cat při k_cat = 2–4 s⁻¹ | **250–500 ms** | von Caemmerer 2000 |
| oxidace plastochinolu na cytochromu *b₆f* | **2–20 ms** | Haehnel 1984 |

Calvinův cyklus je **62–125× pomalejší** než zvolený interval. Ten interval je
nicméně správný řád pro reoxidaci plastochinonového poolu — což je přesně to, co §1
identifikuje jako věc, kterou je třeba odlehčit, a co druhá polovina téže věty říká,
že to hradlování dosahuje.

Takže inženýrství je správné a citace uvnitř té věty špatná. Je to menší vada než
ostatní a v časopise by to byla redakční oprava, ale vyplatí se ji oddělit od §4:
temný interval je obhajitelný, střední tok, který produkuje, ne.

## 6. Gramy na kilowatthodinu jsou pod pulzováním invariantní

§5: „the cybernetic bioreactor achieves conversion ratios that redefine the
gram-per-watt limit of CEA". Ta figura of merit je sušina na jednotku elektrické
energie a `light.py` ukazuje, že s ní návrh hýbat nemůže.

| schéma | g/m²/den | W/m² | **g/kWh** |
|---|---|---|---|
| pulzně, duty 1,23 %, NPQ plně obejité | 33,1 | 111,1 | **12,42** |
| spojitě při téže střední hodnotě, bez NPQ | 33,1 | 111,1 | **12,42** |
| totéž, kdyby tady NPQ stálo publikovaných 60 % | 13,2 | 111,1 | 4,97 |
| spojitě při plném slunci, NPQ na publikovaných 60 % | 103,7 | 869,6 | 4,97 |

Řádky 1 a 2 jsou identické, a jsou identické strukturálně, ne číselně: pulzování
dělí sušinu i elektrický příkon týmž duty cyclem, takže jejich podíl je fixní.
Projetí duty cyclu přes celý rozsah při konstantní špičce to potvrdí:

| duty % | stř. µmol/m²/s | g/m²/den | W/m² | g/kWh |
|---|---|---|---|---|
| 1,235 | 256 | 33,1 | 111,1 | 12,42 |
| 5,000 | 1035 | 134,1 | 450,0 | 12,42 |
| 10,000 | 2070 | 268,3 | 900,0 | 12,42 (*) |
| 25,000 | 5175 | 670,7 | 2250,0 | 12,42 (*) |
| 100,000 | 20700 | 2682,7 | 9000,0 | 12,42 (*) |

(*) za saturací světlem, kde lineární model kvantového výtěžku výnos nadhodnocuje —
takže skutečné g/kWh by tam klesalo, nikdy nerostlo. Rozptyl přes 81násobný rozsah
duty cyclu je **3,6·10⁻¹⁵**, tedy plovoucí řádová tečka.

Výnos na jednotku plochy s duty cyclem roste. Výnos na jednotku *energie* se nemění
vůbec. Jediná páka na něj je v tomhle modelu kvantový výtěžek, který g/kWh škáluje
přesně lineárně (0,02 → 4,97, 0,04 → 9,94, 0,08 → 19,87 g/kWh), a nejvíc, co k němu
obejití NPQ může přidat, je strop 2,50× z §4 — v režimu, kde, jak je naměřeno, NPQ
téměř není nasazené.

Absolutní hodnota, 12,42 g sušiny na kWh za předpokladů vybraných ve prospěch toho
návrhu, padne do rozsahu 5–10 g/kWh, kde komerční vertikální farmaření už funguje.
Není co redefinovat a pulzování je špatná páka na pojmenovanou veličinu.

Je to týž tvar vady jako roofline výsledek v doprovodném vyhodnocení *openQL /
openOL*: restrukturalizace, která znásobí cenu a poměr, který má zlepšit, nechá
přesně tam, kde byl.

## 7. Větrná turbína nemůže vyzařovat 61,72 Hz, a kdyby mohla, nebylo by to slyšet

§4.1 navrhuje udělat z turbín „phased acoustic arrays" změnami v SCADA: „Pitch
Tuning", které má posunout „the blade-pass frequency noise to the target
subharmonic", a „RPM Lock: Electromagnetically braking the rotor via the grid
inverter forces the turbine to maintain exact rotational speeds irrespective of wind
gusts, ensuring a phase-stable 61.72 Hz emission."

**Frekvence.** Blade-pass frekvence je lopatky × ot/min / 60:

| otáčky rotoru | blade-pass frekvence | 61,72 Hz jako její harmonická |
|---|---|---|
| 9,0 | 0,450 Hz | 137. |
| 14,0 (jmenovité) | **0,700 Hz** | **88.** |
| 18,0 | 0,900 Hz | 69. |

Aby byl sám blade pass na 61,72 Hz, musí se rotor otáčet **1234,4 ot/min**, tedy
88× jmenovitých:

| poloměr lopatky | rychlost konce | Mach | zrychlení na konci |
|---|---|---|---|
| 40 m | 5171 m/s | 15,1 | 68 133 g |
| 50 m | **6463 m/s** | **18,8** | **85 167 g** |
| 60 m | 7756 m/s | 22,6 | 102 200 g |

Ta věta o to žádá *bržděním*, které otáčky zvýšit nemůže. Vzato místo toho jako 88.
harmonická blade passu, není nabídnutý žádný mechanismus, jak tam dostat energii;
a „Pitch Tuning: Dynamically adjusting the blade pitch by a fraction of a degree
induces controlled boundary-layer separation (micro-stall)" popisuje širokopásmový
hluk odtržení, který nemá žádnou linkovou strukturu, kterou by šlo položit na
vybranou frekvenci.

**Hladina.** Generátory PAFT z citovaného review dodávají u rostliny 70 ± 5 dB SPL
z 30–60 m. Deklarovaný ekvivalentní akustický výkon turbíny 2–3 MW je 100–110 dB
re 1 pW — 31,6 mW akustického výkonu při 105 dB, širokopásmově. Při
hemisférickém rozptýlení nad odraznou zemí:

| vzdálenost | SPL turbíny | L_w potřebné pro 70 dB | chybí | ve výkonu |
|---|---|---|---|---|
| 100 m | 57,0 dB | 118,0 dB | 13,0 dB | 20× |
| 300 m | 47,5 dB | 127,5 dB | **22,5 dB** | **179×** |
| 500 m | 43,0 dB | 132,0 dB | 27,0 dB | 497× |
| 1000 m | 37,0 dB | 138,0 dB | **33,0 dB** | **1987×** |

Model dává 47,5 dB na 300 m proti 40–45 dB(A), které se v té vzdálenosti od turbíny
této třídy typicky naměří, takže je kalibrovaný a k tomu návrhu spíš vlídný. Změna deklarovaného akustického výkonu přes celou třídu posune
nedostatek na 300 m z 17,5 dB (57×) při 110 dB re 1 pW na 27,5 dB (565×) při
100 dB. Závěr na té volbě nestojí.

A to porovnává **celý širokopásmový výstup** turbíny proti požadavku v jednom úzkém
pásmu, takže skutečný nedostatek je větší, než ta tabulka říká.

**Ztrátový mechanismus je ten nesprávný.** §3 vybrala nízkou frekvenci částečně
proto, že „experiences minimal atmospheric attenuation over long distances", což je
správně: asi 0,1 dB/km při 63 Hz. Ale od 60 m do 1 km stojí geometrické rozptýlení
24 dB a absorpce 0,1 dB. Ta volba frekvence optimalizuje člen, který se na ztrátě
podílí čtvrtinou procenta.

**Pole.** Při 61,72 Hz je λ = 5,56 m, takže tvarování svazku bez mřížkových lalůčků
potřebuje prvky do 2,78 m od sebe. Rozestupy ve větrné farmě jsou 5–10 průměrů
rotoru:

| rozestup | vzdálenost | ve vlnových délkách | proti λ/2 |
|---|---|---|---|
| 5 D | 500 m | 90,0 | 180× příliš daleko |
| 10 D | 1000 m | 179,9 | 360× příliš daleko |

Nezávisle na tom: držet fázovou chybu pod λ/10 přes takové pole vyžaduje stabilitu
časování blade passu na 1,62 ms. Jedna otáčka při 14 ot/min trvá 4,29 s, takže je to
**0,136° úhlu rotoru**, drženo proti poryvům, současně na každé turbíně ve farmě.
„Irrespective of wind gusts" je v té větě ta těžká část, ne ta lehká.

## 8. Jádro transformátoru svázané se sítí nemá linku na 61,72 Hz

§4.2: „High-voltage transformers naturally emit magnetostriction hum. Through
asymmetric DC injection or smart-grid inverter modulation, this hum can be tuned to
precisely 61.72 Hz, turning substations into stationary acoustic stimulators."

Magnetostrikční deformace závisí na |B|, takže jádro na 50 Hz lince je budí na
dvojnásobku síťové frekvence a jejích harmonických: 100, 200, 300, 400 Hz.
Stejnosměrná složka saturuje střídavé polovlny a přidá nepárové linky: 50, 150,
250 Hz. Každá linka, kterou jádro svázané se sítí může vyzářit, je celý násobek
**50 Hz**.

| | |
|---|---|
| síťová frekvence | 50,00 Hz, ± 0,05 Hz (kontinentální oblast ENTSO-E) |
| cíl | **61,72 Hz** = 1,2344 × f_sítě |
| nejbližší dostupná linka | 50,00 Hz, vedle o **11,72 Hz** |

61,72 Hz není harmonická, subharmonická ani intermodulační produkt 50 Hz. Žádné
nastavení firmwaru nevytvoří spektrální linku na frekvenci, kterou budicí signál
neobsahuje; vyrobit ji vyžaduje nezávislý zdroj na té frekvenci, což je reproduktor
a ne „smart-grid inverter modulation". Slovo „precisely" v citované větě dělá opak
toho, co to vypadá, že dělá: je to precizita o frekvenci, na kterou ten mechanismus
vůbec nedosáhne.

Nezávisle na tom je „asymmetric DC injection" polocyklová saturace — poruchový režim
známý z geomagneticky indukovaných proudů, který zvyšuje magnetizační proud, ztráty,
teplotu horkého místa a slyšitelný hluk. Síťové kodexy proto omezují injektovaný
stejnosměrný proud na jednotky ampér. Je to mechanismus poškození, ne ladicí prvek,
a navrhovat ho pro rozvodny ve veřejné síti je návrh degradovat síťová aktiva.

## 9. Hydrologické znaménko

§5 je o směru otevřená: „Because the acoustic stimulation artificially maintains
stomatal aperture, evapotranspiration rates will rise. Therefore, large-scale
deployment must be paired with continuous soil moisture monitoring and sufficient
irrigation buffers."

`water.py` tomu dá velikost. Transpirace listu je E = g_s · VPD / P:

| stav | g_s mol/m²/s | VPD kPa | E mmol/m²/s |
|---|---|---|---|
| ráno, průduchy otevřené | 0,30 | 1,0 | 2,96 |
| poledne, přirozená deprese | 0,10 | 3,0 | **2,96** |
| poledne, drženo otevřené dle návrhu | 0,30 | 3,0 | **8,88** |

Deprese téměř přesně vyruší vzestup sytostního doplňku — na to ta odezva je.
Potlačit ji znásobuje polední transpiraci **3,0×**, a ten činitel je
g_s(drženo)/g_s(deprese), nezávislý na VPD, takže přežije jakoukoli volbu polední
hodnoty (2,0 až 5,0 kPa dávají všechny 3,0×).

Asimilace také roste, ale saturuje ve vodivosti průduchů, zatímco transpirace v ní
zůstává lineární, takže voda na jednotku uhlíku roste pro každý saturující tvar
odezvy:

| poloviční saturace K | zisk asimilace | voda na jednotku uhlíku |
|---|---|---|
| 0,03 | 1,18× | **2,54×** |
| 0,10 | 1,50× | **2,00×** |
| 0,50 | 2,25× | 1,33× |
| lineární (bez saturace) | 3,00× | 1,00× |

Jen přesně lineární odezva vyjde na nulu, a asimilace ve vodivosti lineární není.
K je tady zvolený tvarový parametr, ne měřená konstanta; jde o to, že znaménko na
něm nezávisí.

§1 preprintu uvádí tu biologii správně: polední zavření, „while this prevents lethal
dehydration, abruptly halts CO₂ assimilation". Návrh pak je ten mechanismus porazit
na otevřených polích ozimé pšenice, cukrovky a brambor — u plodin a na zeměpisné
šířce, kde je vázající podmínkou půdní voda, ne světlo, a v hodinách, kdy váže
nejvíc. Ten zavlažovací rezervoár není detail nasazení; to je ten návrh.

Tvrzených 15–18 % přírůstku biomasy je uvedeno bez odvození a bez vazby na dávku,
dobu, frekvenci nebo plodinu. Ten rozsah je věrohodný *pro expozici z citovaného
review* — a právě ta expozice je to, o čem §7 ukazuje, že není k dispozici.

## 10. Reference a prezentace

Čtyři z pěti referencí se dohledají přesně, jak jsou vytištěné, a jsou správným
zdrojem pro své tvrzení (§1). Pátá ne:

> Meng, Q. W., et al. (2012). Plant acoustics: sound-induced stomatal opening and
> the underlying mechanotransduction pathway. *Acoustics Research*, 18(1), 45-53.

Žádný článek s tímto názvem se nepodařilo najít a žádný časopis toho jména se
v prohledaných indexech neobjevuje. Práce Menga a kolegů z roku 2012 o plant
acoustic frequency technology existuje a v PAFT literatuře se cituje, ale v *Hubei
Agricultural Sciences*. Autor a rok vypadají reálně, název, časopis, ročník a strany
ne. Je to zároveň ta reference, která nese jediné kvantitativní biologické tvrzení
v §3 — mechanoreceptorové pásmo — což je zároveň to tvrzení, které §3 uvádí v rozporu
s review, které cituje správně (§3 výše).

K prezentaci: zenodový záznam nese autorovo skutečné ORCID 0009-0000-6842-2187.
Deposit je čtyřstránkový preprint pod CC BY 4.0 bez přiloženého kódu, bez měření
a bez obrázků; §6 uvádí, že topologie hardwaru, firmware pro STM32 a CAD modely
„will be maintained in an open-source GitHub repository associated with this
publication", a žádný repozitář není pojmenovaný ani odkázaný.

## 11. Omezení

Tohle je aritmetika nad publikovanými parametry, ne experiment. Konkrétně:

- **Žádné rostliny nebyly pěstované.** §§4–6 a 9 jsou radiační a výměnná bilance se
  standardními konstantami, ne měření výnosu. Skutečný bioreaktor se od té bilance
  může odchýlit v obou směrech; co ta bilance omezuje, je poměr v §6, a ten je
  strukturální.
- **Kvantový výtěžek 0,05 mol CO₂/mol fotonů a účinnost LED 0,50 jsou
  předpoklady.** §6 ukazuje, že invariance na ani jednom z nich nestojí, a absolutní
  hodnota g/kWh stojí; je uvedená jako jedna hodnota za uvedených předpokladů.
- **Akustický model je hemisférické rozptýlení nad odraznou rovinou** bez vlivu
  země, atmosférické refrakce, střihu větru a směrovosti turbíny. Dává
  47,5 dB na 300 m proti naměřeným 40–45 dB(A) a ty nedostatky jsou 13–33 dB,
  daleko za tím, čím ta dopřesnění hýbou.
- **Argument o transformátoru je spektrální, ne experimentální.** Říká, že budicí
  signál svázaný se sítí neobsahuje složku 61,72 Hz, ne že rozvodnu nelze přinutit
  61,72 Hz vyzařovat jinými prostředky.
- **Netvrdí se, že 61,72 Hz je biologicky neúčinná.** §3 tohoto textu ukazuje, že to
  vlastní citace preprintu nepodporuje; to je jiné tvrzení než ukázat, že ta
  frekvence nefunguje.
- **Shoda s hudební výškou v §2 je fakt o těch číslech, ne o autorově záměru.** Co
  zakládá, je to, že jeden parametr, na kterém návrh v malém měřítku stojí, nemá
  v práci biologické odvození — ne proč.
- **Kontrola referencí je negativní evidence.** §10 uvádí, že se článek nepodařilo
  najít, což je slabší než ukázat, že neexistuje.

## 12. Dostupnost dat a kódu

Všechno v tomto textu produkují `frequency.py`, `light.py`, `acoustics.py`
a `water.py` v tomto repozitáři; `./run_all.sh` to celé zreprodukuje asi ve dvou
sekundách na jakémkoli CPU, bez přístupu k síti a bez GPU. Každá externí konstanta
je se svým zdrojem v `constants.py` a žádný skript si nedefinuje vlastní fyzikální
konstantu. Celý výstup jednoho běhu je v `results.log`.

Vyhodnocovaný preprint je otevřeně dostupný na
[10.5281/zenodo.23156927](https://doi.org/10.5281/zenodo.23156927) pod CC BY 4.0
a není tu reprodukovaný.

## Reference

1. M. Mazgal, *Cymatic Stomatal Stimulation and Pulsed Optical Assimilation:
   Scaling from Cybernetic Bioreactors to Industrial-Scale Acoustic Modulation*,
   Zenodo, 5. října 2026. DOI
   [10.5281/zenodo.23156927](https://doi.org/10.5281/zenodo.23156927).
2. R. H. Hassanien, T. Z. Hou, Y. F. Li, B. M. Li, *Advances in Effects of Sound
   Waves on Plants*, Journal of Integrative Agriculture **13**(2) (2014) 335–348.
3. P. Müller, X.-P. Li, K. K. Niyogi, *Non-photochemical quenching. A response to
   excess light energy*, Plant Physiology **125**(4) (2001) 1558–1566.
4. G. D. Farquhar, T. D. Sharkey, *Stomatal conductance and photosynthesis*, Annual
   Review of Plant Physiology **33** (1982) 317–345.
5. S. Oerlemans, P. Sijtsma, B. Méndez López, *Location and quantification of noise
   sources on a wind turbine*, Journal of Sound and Vibration **299**(4–5) (2007)
   869–883.
6. K. J. McCree, *The action spectrum, absorptance and quantum yield of
   photosynthesis in crop plants*, Agricultural Meteorology **9** (1971) 191–216.
7. W. Haehnel, *Photosynthetic electron transport in higher plants*, Annual Review
   of Plant Physiology **35** (1984) 659–693.
8. S. von Caemmerer, *Biochemical Models of Leaf Photosynthesis*, CSIRO Publishing,
   2000.
9. ISO 9613-1:1993, *Acoustics — Attenuation of sound during propagation outdoors —
   Part 1: Calculation of the absorption of sound by the atmosphere*.
10. IEC 61400-11, *Wind turbines — Part 11: Acoustic noise measurement techniques*.
11. Doprovodná vyhodnocení ostatních depositů téhož autora:
    [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval),
    [`xternary-eval`](https://github.com/karagos01/xternary-eval),
    [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval),
    [`openql-eval`](https://github.com/karagos01/openql-eval).
