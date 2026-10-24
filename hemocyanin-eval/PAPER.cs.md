# Čtyři a půl objemového procenta: vyhodnocení *Copper-Based Hemocyanin Physiology in Hominids*

karagos01, říjen 2026

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`PAPER.md`](PAPER.md).

## Abstrakt

M. Mazgal, *Theoretical Framework for Copper-Based Hemocyanin Physiology in
Hominids* (Zenodo, 7. října 2026, DOI
[10.5281/zenodo.23209266](https://doi.org/10.5281/zenodo.23209266)) tvrdí, že
hemoglobin na železe je „oxidační daň", jejíž Fentonova chemie žene stárnutí, že
lidé nesou latentní geny pro hemocyanin na měďi, a že krmení izolované populace
po generace biomasou z půdy přesycené kovy by je epigeneticky přepnulo — s tím,
že výsledkem je život po stovky let, supravodivý nervový systém a biologický
kvantový počítač se synapsemi dopovanými ¹³⁸La.

Otázku rozhoduje jedna veličina a **neuvádí ji ani ta práce, ani žádná z jejích
pěti referencí**. Lidská arteriální krev nese asi **20 obj. %** kyslíku.
Hemocyanin nese 1,37 až 3,44 obj. % u naměřených druhů a u hlavonožců obecně
„never exceeds 4.5 vols%" — tedy **4,4 až 14,6× méně**. Zkoncentrovat se to
nedá, a to z důvodu, který uvádí spoluautor právě té práce, kterou první citace
preprintu komolí: pigment rozpuštěný v hemolymfě v koncentraci dostatečné pro
transport „will yield an unbearably high osmotic pressure".

Důsledek je spočitatelný. Sedmdesátikilový dospělý v klidu spotřebuje 245 ml
O₂/min, což při normálním srdečním výdeji 4–6 l/min vyžaduje arteriovenózní
rozdíl **4,1–6,1 obj. %** — číslo, které reprodukuje ~5 obj. % skutečně
naměřených u člověka, takže je ta aritmetika kalibrovaná. S hemocyaninem na
publikovaném strop hlavonožců a při velkorysé 75% extrakci potřebuje tentýž
člověk **7,3 l/min v klidu**; při naměřené kapacitě *Octopus vulgaris* je to
**24–72 l/min**, proti maximálnímu lidskému srdečnímu výdeji kolem 20–25 l/min
u trénovaného sportovce. Návrh padá, když se jen sedí.

Genetická cesta padá na předpokladu, ne na míře. Epigenetický přepínač zapne
existující gen; **obratlovci hemocyaninový gen nemají** — InterPro IPR013788
nevrací ve Vertebrata ani v Chordata nic, a tři lidské geny s tyrosinázovou
doménou jsou TYR, TYRP1 a DCT, z nichž TYRP1 má v aktivním místě zinek, ne měď.
Jediný konkrétní molekulární most té práce vyvrací její vlastní citovaný
abstrakt: ceruloplasmin „plays no essential role in the transport or metabolism
of" měďi a je to **ferroxidáza** regulující výtok železa. A její čtvrtá
reference přisuzuje měďi „the generation of superoxide and **hydroxyl
radicals**" — tedy ty částice, podle kterých se Fentonova reakce jmenuje a kvůli
kterým se železo zavrhuje.

Jeden nález jde naopak a je dost silný, aby stál napřed. **Záměna třídy pigmentu
se v živočišné linii skutečně stala** — plži z rodiny Planorbidae nahradili
původní hemocyanin sekundárně vzniklým hemoglobinem. Práce to necituje. Běží to
opačným směrem, publikovaný důvod je „possibly to replace a less-efficient
hemocyanin", a je to jednosměrné: „Once lost, hemocyanin was not regained."

## 1. Co je správně a co tohle vyhodnocení nedělá

**Chemie železa opravdu je zdrojem oxidačního poškození.** Fentonova reakce je
reálná, ferroptóza je reálná a přetížení železem je reálná patologie. Výchozí
pozorování té práce není vymyšlené.

**Hemocyanin opravdu je respirační pigment na měďi**, který funguje u měkkýšů
a členovců, a opravdu má vlastnosti, které hemoglobin nemá, včetně teplotně
adaptované afinity a kooperativity. Práce nepopisuje fiktivní protein.

**Živočichové s hemocyaninem opravdu dosahují savčích metabolických rychlostí
na jednotku hmotnosti.** Epipelagické olihně mají teplotně korigované
metabolické rychlosti nad savci podobné velikosti. To je nejsilnější argument,
který je návrhu k dispozici, a §4 níž ho bere vážně, místo aby ho smetl.

Co tohle vyhodnocení nedělá, je rozhodovat o tvrzeních o stárnutí. „Život po
stovky let", „supravodivý nervový systém" a „biologický kvantový počítač" se
tady neměří; §6 říká, co se o jejich formě říct dá, a tím končí. Ten kyslíkový
výpočet si vystačí sám a je první, protože nepotřebuje, aby byla kterákoli
z těch těžších otázek rozhodnutá.

Poznámka k počítání: práce používá „epigenetic" a jeho formy **osmkrát**,
zatímco „methylation", „histone" a „chromatin" mají každé **nula** výskytů,
a neuvádí **žádnou měřenou veličinu** — jediná čísla v ní jsou čísla sekcí,
roky, rozsahy stran referencí, verze licence a „138".

## 2. Číslo, které práce neuvádí

| médium | obj. % O₂ | proti člověku |
|---|---|---|
| lidská arteriální krev | **20,00** | 1,00× |
| *Cancer magister* | 3,44 | 5,8× |
| *Octopus dofleini* | 3,06 | 6,5× |
| *Nautilus pompilius* | 2,30 | 8,7× |
| *Octopus vulgaris* | 1,37 | 14,6× |
| hlavonožci, publikovaný strop | 4,50 | 4,4× |

Čtyři až patnáctkrát méně kyslíku na jednotku objemu. A ta mezera je
strukturální, ne věcí formulace. Hemoglobin je zabalený v erytrocytech při
330–340 mg/ml, kde nepřispívá k osmolaritě plazmy; hemocyanin je rozpuštěný
v hemolymfě, takže jeho koncentraci omezuje koloidní osmotický tlak a viskozita.
Z van Holde, Miller & Decker (2001) — což je práce, na kterou první citace
preprintu míří názvem venue, zatímco autorem a rokem míří na jinou:

> „a low molecular weight monomeric protein dissolved in the hemolymph is not
> efficient for oxygen transport. If its concentration in the hemolymph is high
> enough to transport a significant amount of oxygen, it will yield an
> unbearably high osmotic pressure."

To je mechanismus té mezery, vyslovený spoluautorem práce, kterou preprint
cituje pro „efficiency, and thermodynamic stability" hemocyaninu — dvě fráze,
které se v práci, k níž ta citace skutečně vede, nevyskytují ani jednou.

## 3. Co to stojí krevní oběh

Sedmdesátikilový dospělý při jednom metabolickém ekvivalentu spotřebuje
3,5 ml O₂/kg/min = **245 ml O₂/min**. Při klidovém srdečním výdeji 4–6 l/min
musí krev vydat:

| srdeční výdej | potřebný a-v rozdíl |
|---|---|
| 4,0 l/min | 6,12 obj. % |
| 6,0 l/min | 4,08 obj. % |

Lidská arteriální krev je 20 obj. % a venózní asi 15, takže naměřený
arteriovenózní rozdíl v klidu je okolo 5 obj. %. Výpočet to reprodukuje, což je
kontrola, že ta aritmetika popisuje soustavu, o které tvrdí, že ji popisuje.

Teď nahradíme hemocyaninem. Extrakce nemůže být úplná — vyložení potřebuje
tlakový gradient — takže ji proměřím:

| kapacita | extrakce | vydáno | potřebný srdeční výdej |
|---|---|---|---|
| 4,50 | 75 % | 3,38 obj. % | **7,3 l/min** |
| 4,50 | 25 % | 1,12 obj. % | 21,8 l/min |
| 1,37 | 75 % | 1,03 obj. % | 23,8 l/min |
| 1,37 | 25 % | 0,34 obj. % | **71,5 l/min** |

Při nejvelkorysejší publikované kapacitě a nejvelkorysejší reálné extrakci musí
klidový srdeční výdej vystoupit nad normální klidové rozmezí. Při naměřené
kapacitě chobotnice musí dosáhnout 24–72 l/min, což přesahuje maximální lidský
srdeční výdej. A námaha ten požadavek násobí 8 až 20×: na stropě potřebuje 8×
klid **58 l/min** a 20× klid **145 l/min**.

Takže návrh nepadá na okrajích. Padá v klidu, faktorem větším než jedna, ještě
než se vůbec dojde k tvrzením o stárnutí nebo poznávání.

## 4. Proč olihně nejsou protipříklad

Epipelagické olihně skutečně dosahují metabolických rychlostí nad podobně
velkými savci, a to je fakt, po kterém by obhájce tohohle návrhu měl sáhnout.
Dělají to tím, že přesunou mnohem víc tekutiny mnohem rychleji, a lidé, kteří to
naměřili, tu cenu pojmenovávají:

> „The constraint on power output in squids is clearly not oxygen uptake, but
> **oxygen transport in the blood**"

Tedy: limitem olihně je přesně ta veličina, kterou preprint navrhuje lidem
převzít. Podpůrná fyziologie je adekvátně extrémní: Bohrův koeficient −1,2 až
−2,3 proti lidským −0,35 až −0,5, venózní saturace kolem 14 %, prakticky nulový
aerobní rozsah a život na hranici kyslíkového limitu. Největší živočich
s hemocyaninem, oliheň *Mesonychoteuthis* s téměř 500 kg, je přepadový predátor,
jehož metabolická rychlost je o řády pod aktivní olihní téhož kladu — hmotnost
je živočichům s hemocyaninem k dispozici, trvalý aerobní výkon ne.

Mechanistická poznámka pod čarou, označená `[A]` a nabízená jako vysvětlení, ne
jako evidence: hemoglobin nese čtyři O₂ na tetramer 64,5 kDa, tedy asi 16 kDa
proteinu na O₂, zatímco hemocyanin nese jeden O₂ na binukleární centrum typu 3
v podjednotce řádu 50–100 kDa. To je 3–6× víc proteinové hmoty na kyslík, tedy
stejný rozsah jako naměřená mezera v kapacitě, což je přesně to, co by se dalo
čekat, kdyby ten rozdíl byl převážně stechiometrický a částečně osmotický.
Evidencí jsou měření kapacity v §2; tohle je jen důvod.

## 5. Genetická cesta padá na předpokladu

Epigenetický mechanismus mění, které geny organismu jsou exprimované. Nemůže
exprimovat gen, který ta linie nemá. Takže ten návrh má předpoklad, který je
věcí záznamu:

| dotaz | výsledek |
|---|---|
| hemocyaninová rodina IPR013788 ve Vertebrata (7742) | **0** |
| totéž omezené na Chordata (7711) | **0** |
| lidské geny s tyrosinázovou doménou, z níž hemocyaniny vznikly | TYR, TYRP1, DCT |
| kov v aktivním místě TYRP1 | **zinek**, ne měď |

Není co odemknout. TYRP1 není ani latentní vazač kyslíku — „Because zinc ions,
in contrast to copper ions, are not redox-active".

Jediný konkrétní molekulární most té práce je ceruloplasmin, který nazývá „the
fundamental human protein for copper transport in the blood", „structurally
related to invertebrate hemocyanins". Její vlastní citovaná recenze začíná:

> „Ceruloplasmin is a serum ferroxidase … Despite the need for copper in
> ceruloplasmin function, **this protein plays no essential role in the
> transport or metabolism of this metal.**"

28 ze 112 referencí té recenze je o železe a žádná o hemocyaninu; její strukturní
srovnání vedou k askorbát oxidáze, lakáze, Fet3p a hefaestinu. Databáze souhlasí:
ceruloplasmin je multikuprooxidáza s cupredoxinovým foldem, hemocyaniny mají
tyrosinázové binukleární centrum typu 3, a průnik domén je prázdný. Jiná
nadrodina, jiný fold, jiná třída měďného centra — a fyziologická role, která vede
přes výtok železa, tedy opačným směrem, než je potřeba.

A premisu, že měď je ten jemnější kov, vyvrací čtvrtá reference preprintu:

> „it is this property of copper that also makes it potentially toxic because
> the transitions between Cu(II) and Cu(I) can result in the generation of
> superoxide and **hydroxyl radicals**."

Hydroxylové radikály jsou to, podle čeho se Fentonova reakce jmenuje. Oba kovy
jsou redoxní páry, a právě proto umí oba nést kyslík a právě proto není inertní
ani jeden. Tatáž recenze nezmiňuje epigenetiku vůbec — „epigenet" má v ní nula
výskytů, proti glose, která ji nazývá „baseline framework for understanding the
epigenetic adaptation of organisms to extreme environmental metal
concentrations".

## 6. Skutečný precedens a tři nálezy, které práce mohla použít

Tato sekce existuje proto, že obsahový audit referencí tohoto depositu hledal
podporu, ne jen chyby, a nějakou našel — a nic z toho práce necituje.

**Záměna třídy pigmentu se skutečně stala.** Planorbidae „have replaced the
ancestral (blue) hemocyanin as an oxygen-carrier with secondarily evolved
hemoglobin". Takže myšlenka, že linie může změnit respirační pigment, není
fantazie. Tři problémy: směr je hemocyanin → hemoglobin; publikovaný důvod je
„possibly to replace a less-efficient hemocyanin", což je vlastní nález tohoto
repozitáře přicházející z druhé strany; a je to jednosměrné — „Once lost,
hemocyanin was not regained."

**Hemocyaninové geny po záměně přetrvávají.** *Biomphalaria glabrata*, která
používá hemoglobin, má pořád dva hemocyaninu podobné geny, a tentýž typ buňky —
rhogocyt — vyrábí hemocyanin u modrokrevných plžů a hemoglobin u červenokrevných.
To je nejbližší reálná analogie k „latentním genům" z preprintu a platí uvnitř
měkkýšů, kde ten gen existuje, aby se dal zachovat.

**Exprese hemocyaninu je regulovaná prostředím.** Embryonální hemocyanin je
„highly upregulated by ambient O₂ deprivation, up to 10-fold" a u některých
insektů je exprese omezená na embryo. Takže regulace právě tohoto pigmentu
podle kyslíku v prostředí je doložená — u živočichů, kteří ten gen mají.

Ani jeden ze tří nedosáhne na linii, která hemocyaninový gen nemá vůbec,
a ani jeden nemění tu kapacitní aritmetiku. Ale je to to, co by obhájce měl
citovat, a stojí za zaznamenání, že to existuje a že to ta práce nepoužívá.

Celý obsahový audit všech pěti referencí, s doslovnou evidencí a se záznamem,
jak daleko se každou práci podařilo přečíst, je v
[`reference-audit`](https://github.com/karagos01/reference-audit). Dvě z pěti
preprint aktivně vyvracejí, jedna se v uvedené podobě nedohledá vůbec a pátá je
sebecitace, jejíž cíl ten mechanismus, pro který je citovaná, neobsahuje: slovo
„copper" se ve fytominingovém preprintu vyskytuje jednou, v nadpisu odrážky,
jejíž tělo je celé o zlatě, a měď není v žádné položce jeho materiálového
rozpočtu — zato železo tam je.

## 7. Co se tady neměří

„Život po stovky let", „supravodivý nervový systém", termoregulační nezávislost,
„biologický kvantový počítač" se synapsemi dopovanými ¹³⁸La, a rámování „modré
krve aristokracie" jako reálné biochemie místo společenského obratu — nic z toho
se neměří a ani se o to nepokouším.

Dvě poznámky k jejich formě, což je všechno, co je k dispozici. Ani jedno není
vysloveno s endpointem, časovou škálou nebo srovnáním, takže ani jedno není tak,
jak je napsané, falzifikovatelné. A ani jedno nemá v seznamu literatury nosič:
ani jedna z pěti referencí se netýká neurofyziologie, vodivosti tkání ani délky
života.

Tento deposit a jeho předchůdce jsou taky ta dvě místa ze sedmnácti autorových,
kde je návrh intervencí na lidech — tady izolovaná lidská populace krmená po
generace plodinami nabitými kovy s cílem změnit jim krev. To je rozdíl v povaze
proti regulátoru motoru nebo renderovací architektuře a zaznamenávám to jako
takový, bez dalšího komentáře.

## 8. Hranice

Žádná krev nebyla odebraná, žádný gen sekvenovaný a žádný organismus studovaný.
Kapacitní čísla jsou z publikované literatury o čtyřech druzích plus strop
z recenze, a liší se mezi druhy, s teplotou a s nutričním stavem; závěr je
vyslovený přes celý naměřený rozptyl, ne při jedné hodnotě.

Provenience je označená v `constants.py`: `[P]` vlastní tvrzení preprintu, `[V]`
ověřeno proti pojmenovanému zdroji, `[A]` předpokládaný rozsah, který se
proměřuje místo tvrzení. Srdeční výdej, extrakční podíl, násobek VO₂max
a proteinové hmotnosti na kyslík jsou všechno `[A]`.

Nejmíň pevný předpoklad je ten extrakční podíl. Tkáně neextrahují fixní podíl;
extrakce roste s nárokem a klesá s průtokem, a oběh na hemocyaninu by se
pravděpodobně vyvíjel k vyššímu konci. Proměřuje se až k 75 %, což je nad
lidskou klidovou hodnotou kolem 25 %, takže ten výpočet je k návrhu už
velkorysý — a i tak padá v klidu.

Výsledky k TYRP1 a InterPro jsou databázové dotazy udělané při psaní tohohle.
Negativní databázový výsledek je slabší než důkaz absence: ukazuje, že žádný
obratlovčí hemocyaninový gen není anotovaný, ne že žádný nemůže existovat. Když
α-subklasa, z níž měkkýší hemocyaniny vycházejí, u chordátů chybí, obě linie
evidence se shodují — ale to tvrzení je omezené na to, co anotace ukazuje.

## 9. Data a kód

`constants.py` drží každou hodnotu s příznakem provenience a zdrojem a žádný
další skript žádnou nedefinuje. `oxygen.py` reprodukuje §§2–4 a `genetics.py`
§5 a část §6; `genetics.py` je záznam databázových výsledků a citací, ne
výpočet, a je držený jako skript, aby se objevil v `results.log` vedle té
aritmetiky. `run_all.sh` projde všechno offline za asi sekundu.

## Reference

Vyhodnocený preprint: M. Mazgal, *Theoretical Framework for Copper-Based
Hemocyanin Physiology in Hominids*, Zenodo, 7. října 2026, DOI
10.5281/zenodo.23209266, CC BY 4.0.

Externí zdroje jsou citované v `constants.py` vedle hodnot, které podpírají:
Collins et al., *Breathe* 11(3), DOI 10.1183/20734735.001415, pro obsah kyslíku
v lidské arteriální krvi; Johansen et al. (1970) DOI 10.1007/BF00299532, Lenfant
& Johansen (1965) DOI 10.1152/ajplegacy.1965.209.5.991, Johansen (1978) DOI
10.1002/jez.1402050105 a Oellermann et al. (2015) DOI 10.1186/s12983-015-0097-x
pro kapacity druhů; Wells & Smith (1987) DOI 10.1007/BF02143577 pro strop
hlavonožců; van Holde, Miller & Decker (2001) DOI 10.1074/jbc.R100010200 pro
osmotický argument; Jetté et al. (1990) DOI 10.1002/clc.4960130809 pro
metabolický ekvivalent; O'Dor & Webber (1991) DOI 10.1242/jeb.160.1.93 pro limit
olihní; Hellman & Gitlin (2002) DOI 10.1146/annurev.nutr.22.012502.114457
a Tchounwou et al. (2012) DOI 10.1007/978-3-7643-8340-4_6, obojí citované
preprintem; Peña & Adema (2016) DOI 10.1371/journal.pone.0168665, Lieb et al.
(2006) DOI 10.1073/pnas.0601861103 a Burmester (2015) DOI 10.1093/icb/icv079 pro
záměnu u Planorbidae; Lai et al. (2020) DOI 10.3390/ijms21030915 pro aktivní
místo TYRP1; a InterPro s Pfam pro přiřazení domén. Citace jsou krátké výňatky
použité pro kritiku a recenzi.
