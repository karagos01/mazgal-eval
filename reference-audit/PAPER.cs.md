# Obhajoba v referencích: audit všech 81 citací v osmnácti preprintech

karagos01, říjen 2026

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`PAPER.md`](PAPER.md).

## Abstrakt

Autor osmnácti preprintů na Zenodu veřejně uvedl, že obhajoba jeho argumentů
je záměrně uložená v referencích a není napsaná v textu, takže analýza omezená
na text ji musí minout. To je testovatelné tvrzení. Tento audit ho testuje tím,
že u každé citace čte, co citovaná práce o daném tvrzení skutečně říká — napříč
všemi 81 externími referencemi ve všech osmnácti záznamech — a tím, že hledá
podporu, ne jen chyby.

Tvrzení se částečně potvrdilo. Ve čtyřech depositech citovaná literatura nese
podporu, kterou preprinty nevyslovují, a v jednom případě lepší odvození, než
je v samotné práci: Fureyová ve své disertaci argumentuje, že kauzalita
a nevratný čas vyplývají ze závorkování algebraického výrazu, což je konceptuální
jádro celé „Causal" série; Baez dodává jak reálně-maticové zakódování
oktonionového násobení, tak cestu k číslu 12 přes sl(3,ℍ) působící na ℝ¹², o němž
sám píše „this is no coincidence!"; poznámka pod čarou č. 22 u Shockleyho
a Queissera pojmenovává multiplikaci nosičů a vědomě ji z výpočtu vyjímá, což je
obhajoba názvu HOS-PV 2.0; a Moreno má vytištěnou tu dvojici sedenionových
dělitelů nuly, na které stojí anihilace v openOmeze.

Dál to nejde, a to ze tří změřených důvodů. Za prvé, 52 z 81 referencí není
připnutých k žádnému tvrzení a tři deposity nemají seznam literatury vůbec,
takže u dvou třetin korpusu neexistuje nosič, který by skrytá obhajoba mohla
použít. Za druhé, tam kde se podpora našla, tytéž stránky vyvracejí mechanismus,
pro který je nabízena: Fureyová, Dixon i Baez řeší neasociativitu přechodem do
asociativní algebry operátorů levého násobení, což je právě ten manévr, na
jehož odmítnutí navrhovaná architektura stojí, a Adlerův centrální výsledek je,
že kvaternionové jednotky z S-matice vypadnou. Za třetí, patnáct tvrzení
vyvracejí jejich vlastní citované zdroje vlastními slovy, včetně těch dvou,
které nesou nejvíc váhy v zemědělském a biomedicínském depositu, a včetně
účinnosti v názvu toho nejnovějšího.

## 1. Co se testuje a co ne

Podnětem k tomuto auditu byla konkrétní a věcná metodická kritika: že ověřit
existenci reference je slabší než přečíst, co říká, a že argument může žít
v bibliografii. Obojí je správně a to první popisuje reálnou slabinu pěti
starších repozitářů v této sérii, které ověřovaly existenci a atribuci
důkladněji než obsah.

Otázka je tedy úzká a zodpověditelná: říká u každé citace ta citovaná práce to,
pro co je citovaná? Z té úzkosti plynou tři věci.

Není to audit toho, zda jsou tvrzení pravdivá. Tvrzení může být správné se
špatnou citací. Kde je aritmetika spočítaná, je v doprovodných repozitářích,
a čísla, která na čtení referencí nezávisejí, se ničím zde nemění.

Kde se práci nepodařilo přečíst, audit to říká místo dohadů. Sekce 3 v
`audit.py` uvádí, že 43 z 69 verdiktových řádků stojí na plném textu; zbytek
stojí na abstraktu, na obsahu knihy, nebo — u dvou nedostupných knih — na
vlastních pracích téhož autora a na jeho vlastním publikovaném souhrnu té knihy,
přičemž substituce je pojmenovaná v poli `source` každého řádku.

A absence klíčového slova se hlásí jako počet, ne jako dojem. Nula v
`refdata.py` znamená, že se termín v získaném textu hledal a není tam. Kde text
pochází z OCR indexu, řádek to říká a absence je silná, ne absolutní evidence.

## 2. Existuje vůbec nosič?

Aby reference nějaké tvrzení hájila, musí ji text k tomu tvrzení připojit.
Spočítat ta připojení je první měření a rozhoduje o tom, kolik z korpusu je
vůbec testovatelné.

| | počet | podíl |
|---|---|---|
| externích referencí, 18 záznamů | 81 | |
| připnutých k větě značkou v textu | **14** | 17,3 % |
| nesoucích jen glosu v seznamu literatury | 15 | 18,5 % |
| **bez vysloveného vztahu k čemukoli** | **52** | **64,2 %** |
| sebecitace | 4 | |

Externí práci v těle textu citují tři deposity: *Acoustic Projector*, který
označuje pět ze svých šesti — Putland je uvedený, ale nikde necitovaný — SOTP,
který označuje dvě z pěti pomocí `[3, 4]` na jedné větě, a HOS-PV 2.0 ze
14. října, který označuje **všech sedm ze sedmi** a je prvním depositem
v korpusu, kde nezůstala nepřipnutá ani jedna reference. Tři deposity — MPPT v1.0, MPPT v1.1 a CQFT — nemají seznam literatury
vůbec, takže se tam obhajoba nemá kde schovat. Další tři glosují každou
referenci poznámkou, co dokládá, a to je nejpřímější testovatelná forma toho
tvrzení, protože mapování vyslovuje autor sám.

Zbývá 29 referencí v šesti depositech, kde je vazba vyslovená. Tam se skrytá
obhajoba dala najít, a tam se taky našla.

## 3. Co hledání podpory našlo

Pět nálezů je podstatných a první je nejsilnější výsledek tohoto repozitáře.

**Fureyová (2016), kapitola 2**, citovaná v SOTP jako `[3]`, argumentuje přesně
to, co trilogie potřebuje a nikde neříká:

> „Taking multiplication to be the propagation along an edge, and addition to
> be the joining of two edges at a vertex, it can be seen that this unevaluated
> algebraic expression gives a causal set."

> „In the case of an algebra, an event is a calculation. … an event can be seen
> to be irreversible, it cannot 'unhappen'. … Time, then, is simply a sequence
> of calculations, and is clearly irreversible."

Její abstrakt: „we argue that physical concepts such as particles, causality,
and irreversible time may result from the algebra acting on itself." Z komplexních
oktonionů také skutečně dostává su(3)_c a u(1)_em a neasociativitu nazývá „not
a impediment, but instead a gift". Ta in-text citace v SOTP je substančně
podložená, byť „isomorphism" je volné: Fureyová pracuje s minimálními levými
ideály a stabilizátorovými podgrupami, ne s izomorfismem 𝕆 a grupy symetrie.

**Baez (2002)**, citovaný v openQL v1.0 jako `[5]` pod glosou o „12D/112D
spatial mappings", která padá sama — „112" ani „12-dimensional" se u Baeze
nevyskytuje — přesto obsahuje dvě věci, které práce potřebuje. Sekce 2.3 dává
reálné matice oktonionového násobení přes operátory levého násobení, z nichž
Baez odvozuje reprezentaci Cliffordovy algebry. A sekce 3.3 dává sl(m,𝕂)
působící na 𝕂^m, takže sl(3,ℍ) na ℍ³ ≅ ℝ¹² jsou reálné operátory 12×12, se
so(12) v poli (ℍ,ℍ) jeho magického čtverce a s jeho vlastní poznámkou, že
„the numbers 9, 10, 12 and 16 are 8 more than the dimensions of ℝ, ℂ, ℍ and 𝕆.
As usual, this is no coincidence!" To je lepší odvození dvanáctky než obě, která
openQL nabízí, a práce na něj neukazuje.

Existuje i slabší kandidát na 112, který je třeba zaznamenat: 2 × 56, přes
56rozměrný Freudenthalův prostor pro E₇, který Baez skutečně vybavuje
symplektickou strukturou. Číslo 112 nikde nepíše a ta symplektická forma je
bilineární forma zachovávaná E₇₍₋₂₅₎, nikoli vlastnost update kroku, takže je to
stopa, ne výsledek.

**Adler (1995)**, citovaný v PCTP jako `[1]`, podporuje premisu. Selhání
obyčejného tenzorového součinu nad ℍ je reálné a dlouho známé — Horwitz: „there
is an essential destruction of linearity, i.e., f q ⊗ g ≠ (f ⊗ g)q"; Baez
a Huerta: „the tensor product of quaternionic Hilbert spaces is not naturally
a quaternionic Hilbert space."

**Shockley a Queisser (1961)**, citovaní v HOS-PV 2.0 jako `[1]`, hájí název
toho depositu z poznámky pod čarou. Celá práce stojí na tom, že jeden přechod
může překonat 33,7 %, protože singletní fise posílá do obvodu dva nosiče za
jeden foton. Poznámka č. 22 v práci, která tu hranici stanovila:

> „Once a photon exceeds about three times the energy gap [E_g], the
> probability of producing two or more hole-electron pairs becomes
> appreciable"

> „the data can be well fitted up to quantum yields greater than two … This
> effect would slightly increase the possible quantum efficiency; however, **we
> shall not consider it further in this article**."

Autoři té hranice multiplikaci vyňali vědomě, takže překonat ji tudy je
legitimní a deposit má v tomhle pravdu — aniž by kdekoli řekl, odkud to
povolení bere. Výhrada je velikost toho zisku a je v referenci [5] téhož
depositu: jeden přechod s multiplikací dává 44,4 %, ne tvrzených 45,9 %,
a 45,9 % padá do tandemového rozsahu té práce.

**Moreno (1998)**, citovaný v openOmeze jako `[3]`, má vytištěný mechanismus,
na kterém ten deposit běží. Jeho anihilační krok potřebuje dva nenulové
sedeniony, jejichž součin je přesně nula, a úvod citované práce jednu takovou
dvojici dává:

> „for n ≥ 4 this norm-preserving formula is not true in general and this opens
> the possibility of the existence of zero divisors in A_n for n ≥ 4 i.e. x and
> y non-zero elements in A_n such that xy = 0 e.g. let **x = e₁ + e₁₀ and
> y = e₁₅ − e₄** in ℝ¹⁶ = A₄"

To je přesně dvojice, kterou doprovodný repozitář `openomega-eval` našel hrubou
silou přes kombinace bázových prvků — uvádí (e₁ + e₁₀) × (e₄ − e₁₅) = 0, tutéž
dvojici s obráceným znaménkem u y — a v referenci byla celou dobu vytištěná.
Z týchž dvou stránek plynou dvě výhrady. Dělitelé nuly existují *proto*, že nad
dimenzí 8 selhává ‖xy‖ = ‖x‖‖y‖, takže v jediné operaci, kterou deposit provádí
„s absolutním zachováním energie", je norma zničena. A Morenův vlastní bod 2)
odstraňuje potřebu sedenionů v maticové formulaci, kterou deposit sám používá:
„in an associative (alternative) context as in M_n(ℝ) … 0 ≠ A is a zero divisor
if and only if det A = 0."

Pět menších nálezů je ve prospěch autora a jsou v `hidden.py`: Bi et al.
skutečně demonstrují monolitickou nereciprocitu na čipu, kterou PCTP potřebuje
k vynucení pořadí; Lehmannův abstrakt skutečně podpírá biochar „as inoculant
carriers", což je koncept smart-peletu; Teslův patent skutečně učí tu
distribuovanou kapacitu, kterou z něj COBAR bere; tabulka III u Šmejkala,
Sinovy a Jungwirtha dává altermagnetickému kolektoru v HOS-PV 2.0 **větší**
spinové rozštěpení, než o jaké deposit žádá, 1,1–1,4 eV proti tvrzeným
0,5–1,0 eV; a Rao et al. podporují tripletový odtok, kvůli kterému ten deposit
vznikl, přesně slovy vět, které předcházejí značce.

## 4. Manévr, který mají všichni tři společný

Tři matematici citovaní kvůli oktonionům řeší neasociativitu stejně a každý to
říká naplno:

> Fureyová: „As the composition of maps is always associative, ℂ⊗𝕆⃖ is an
> associative algebra" … „faithfully represents the 64-complex-dimensional
> Clifford algebra Cl(6)"

> Dixon: „𝕆_L ≃ ℝ(8) ≃ CL(0,6) … **(Note: 𝕆_L is trivially associative.)**"

> Baez: „multiplication in this group is given by composition of real-linear
> operators, **which is associative even for 𝕂 = 𝕆**"

Přechod do asociativní algebry operátorů levého násobení je právě ten krok, na
jehož odmítnutí navrhovaná architektura stojí, protože jejím prodejním
argumentem je nenulový asociátor vykonávaný jako hardwarová observabla.
Fureyová tu brzdu dodává vlastním hlasem: „It is at this early stage only
a conjecture that any **(associative)** algebraic expression gives a causal set."

Adlerova brzda má stejný tvar a je stejně rozhodující: „the S-matrix is always
a complex matrix with no dependence on the quaternionic units j, k … Hence the
asymptotic dynamics for quaternionic quantum mechanics is always an effective
complex theory", a „noncommutative dynamics hides itself beneath effective
complex quantum mechanical structures." Procesor, jehož výstup se měří, nemůže
ve svém in/out chování vykázat nekomutativitu, pro kterou existuje.

Skrytá obhajoba je tedy reálná pro motivaci těch prací a vyvrací jejich
mechanismus, z týchž stránek. Doprovodné `openql-eval` tu hranici už měří —
operátory levého násobení dávají 1,8·10⁻¹⁵ pro ℍ a 29,5 pro 𝕆 — ale
nepřipisovalo Baezovi, že tu konstrukci dodal. Tuhle atribuci audit dluží
staršímu repozitáři, ne preprintu.

## 5. Glosy, které citovaná práce vyvrací

Kde autor říká, co reference dokládá, se to dá zkontrolovat přímo. Pět z
patnácti glos citovaná práce vyvrací a ve třech případech je ten rozpor
v citovaném abstraktu.

**Raissi et al.**, glosováno jako základ pro „encoding physical laws into
neural weights", říká: „the resulting pair u(t,x;W,b) and f(t,x;W,b) must
satisfy the Burgers equation **regardless of the choice of the weights W and
bias b**." Fyzika je v loss funkci a v automatické diferenciaci vůči vstupním
souřadnicím. „Symplectic" se v práci nevyskytuje.

**Hellman & Gitlin**, glosováno pro „human copper transport" a „structural
relationship … to invertebrate hemocyanins", začíná: „Ceruloplasmin is a serum
ferroxidase … **Despite the need for copper in ceruloplasmin function, this
protein plays no essential role in the transport or metabolism of this
metal.**" 28 ze 112 jejích referencí je o železe a žádná o hemocyaninu; její
strukturní srovnání vedou k askorbát oxidáze, lakáze, Fet3p a hefaestinu.
Domén­ové databáze souhlasí: ceruloplasmin je multikuprooxidáza s cupredoxinovým
foldem, hemocyaniny mají tyrosinázové binukleární centrum typu 3, a průnik je
prázdný. Je to jediný konkrétní molekulární most mezi člověkem a hemocyaninem,
který ta práce má.

**Tchounwou et al.**, glosováno pro „epigenetic adaptation", obsahuje řetězec
„epigenet" **nulakrát** a měďi přisuzuje „the generation of superoxide and
**hydroxyl radicals**" — tentýž radikál, kvůli kterému práce odmítá železo.

**Wright & Upadhyaya**, glosováno pro „mechanics of glomalin production"
a „water retention", je průřezový survey 37 vzorků, jehož výstupem je jediná
regrese; produkce je jeho premisa, voda se objevuje jen jako destrukční agens
při mokrém sítování a slovo „permanent" tam není. Citace je navíc osiřelá:
preprint mykorhizu zmiňuje jen proto, aby ji obešel — „The plant root must not
'search' for distant deposits via fungi."

**Decker et al. (2007)** se v uvedené podobě nedohledá vůbec. Je to chiméra:
název venue patří k van Holde, Miller & Decker (2001) v JBC, autor s rokem
k Decker et al. (2007) v *Integrative and Comparative Biology*. Ani
„efficiency", ani „thermodynamic stability" — dvě slova, která glosa tvrdí —
se v práci, k níž to vede, nevyskytují; ta místo toho uvádí „a low to moderate
oxygen affinity".

## 6. Vyvrácení vlastními slovy zdrojů

Patnáct řádků nese verdikt REFUTES, tedy citovaná práce tvrdí opak. Sedm stojí
za vypsáním.

**Buchačenko o magnetických izotopech.** Fytominingový preprint tvrdí, že ²⁵Mg
a ⁶⁷Zn „accelerate the chemical kinetics of DNA transcription and ATP
synthesis". Výsledek citovaného autora pro přesně tu trojici izotopů, kterou
práce jmenuje:

> „The substitution of these catalyzing ions in polymerases by the ions ²⁵Mg²⁺,
> ⁴³Ca²⁺, and ⁶⁷Zn²⁺ with magnetic nuclei was shown to produce a huge isotope
> effects: nuclear magnetic ions **by 3–5 times suppress DNA synthesis**"

> „A new **anti-cancer strategy** is suggested based on the using of the nuclear
> magnetic ions of magnesium, calcium, and zinc as a powerful and universal
> means to **selectively kill** only cancer cells."

Reparace je taky pomalejší, 1,5×. Přežívá jen tvrzení o ATP, a to jen pro ²⁵Mg
při obohacení 99,9 % dodané injikovatelnou nanočásticí — a nereplikovalo se
v PNAS v roce 2012, což preprint neuvádí. Zinková polovina glosy je
anachronismus: Buchačenkova biologická práce o zinku je z roku 2013, čtyři roky
po citované knize.

**Reith et al. o zlatě.** Preprint má biogenní nanozlato „entirely blocking"
reaktivní formy kyslíku. Zdroj: „Au detoxification is mediated by a combination
of **efflux**, reduction, and possibly methylation", a „one major toxic effect
of Au(III) … is the **induction of oxidative stress**", s minimální inhibiční
koncentrací 2 µM. Buňka zlato vyváží, aby přežila, a zlato vyvolává právě ty
částice, které podle práce vychytává.

**NVIDIA o 2bitové aritmetice.** Whitepaper: „FP8, FP16, BF16, TF32, FP64, and
INT8 MMA data types are supported." Úplný výčet operandů `wgmma.mma_async`
přidává jen `b1` s `.and`+`.popc`; `.s4`/`.u4` chybí a `.u2`/`.s2` existují jen
jako konverzní typy. Nativní 2bitový ani ternární tensor-core typ na Hopperu
není a není na žádné generaci.

**Manchon et al. o disipaci.** SOTP tvrdí, že čisté spinové proudy odstraňují
I²R úplně. Recenze: čistý spinový proud se indukuje „transverse to the direction
of **the applied electrical current**", při 10⁷–10⁸ A/cm² a asi 100 fJ na bit.
Rashbovo a Dresselhausovo pole navíc klade do téže roviny, lišící se smyslem
rotace, takže to nejsou ortogonální spinové osy, jaké jim práce přiřazuje.

**Demokritov o magnonových kondenzátech.** Pohon potřebuje magnonový BEC za
pokojové teploty držený milisekundy, jehož fázový posun posune mříž rotoru.
Z pozdější práce téhož autora: „the magnon BEC is doubly degenerate: two
condensate components are simultaneously formed in the two spectral minima at
k_BEC = ±k_min", a „the group velocity at these spectral points is zero.
Therefore, **the created condensate clouds do not move**." Čistá hybnost je
nulová symetrií, měřené životnosti jsou 175–230 ns proti předpokládaným 3 ms,
a rovnovážný magnonový BEC nemůže existovat vůbec, protože chemický potenciál
je v rovnováze nulový.

**Purushothaman & Landau o pulzním nabíjení.** Jediná pulzní citace
sodíkoiontové práce identifikuje jako limit difuzi v pevné fázi, pracuje
s pulzem 3 s a klidem 1 s — asi 0,25 Hz — a svůj nejlepší výsledek dostává se
**spojitě** klesajícím profilem proudu, ne s pulzem. Podporuje nízkofrekvenční
obálku a vyvrací tu kHz–MHz složku, vedle níž je citovaná.

**Hanna a Nozik o 45,9 %.** Abstrakt HOS-PV 2.0 i jeho sekce 2.2 tvrdí, že
architektura zvedá jednopřechodovou hranici „from 33.7% (SQ limit) to 45.9%",
a mají u toho tuhle referenci. Ta reference je správná — detailní rovnováha
pod 1 sluncem AM1.5G, se singletní fisí jako multiplikačním absorbérem — a její
abstrakt dává pro přesně tu konfiguraci jiné číslo:

> „for single gap photovoltaic (PV) devices the maximum efficiency increases
> from 33.7% for cells with no carrier multiplication to **44.4%** for cells
> with carrier multiplication"

> „the maximum efficiency of an ideal two gap tandem PV device increases from
> **45.7% to 47.7%**"

45,9 % padá do tandemového rozsahu, a přitom je jediným prodejním argumentem té
architektury právě to, že je jednopřechodová. Doprovodný repozitář `hospv-eval`
staví ten model znovu ze spektra ASTM G173-03 a reprodukuje všechny tři
publikované hodnoty té skupiny — 33,77 %, 44,62 % a 42,09 % při 0,94 eV pro
multiplikaci zastropovanou na dva nosiče na foton, což je přesně to, co dělá
singletní fise, proti jejich publikovaným 42,0 % při 0,95 eV. 45,9 % je nad tím
stropem při jakékoli dvojici energií.

## 7. Co je správně

Čtyři verdikty jsou SUPPORTS a dva další nálezy je třeba říct naplno, protože
opravují tento audit, ne preprinty.

Sedm Fanových trojic v SOTP tu bylo strojově zkontrolováno a tvoří **platnou
Fanovu rovinu**: všech 21 párů sedmi imaginárních jednotek je pokryto právě
jednou. Definice asociátoru i pravidlo ε jsou Baezovy doslovné. Jones et al.
a Kennedy & Eberhart se dohledají přesně a podporují to, vedle čeho jsou,
a Moreno je přesně o těch dělitelích nuly, na kterých openOmega stojí.

HOS-PV 2.0 je podle všech formálních měřítek, která se tu berou, nejčistší
deposit korpusu. Všech sedm referencí je reálných, všech sedm se dohledá přesně
tak, jak jsou vytištěné, všech sedm je připnutých k větě, žádná není sebecitace,
není tam AI jako spoluautor ani nevyplněný ORCID — první deposit z osmnácti,
kde platí všechno najednou. Šest ze sedmi nese část toho, pro co jsou citované.
Jeho problémy jsou jiného druhu než ve zbytku korpusu: ne vymyšlené reference,
ale špatný řádek tabulky v reálné.

Teslův patent **nepresuponuje** železné jádro — je výslovně agnostický („any
conductor") — takže ho nelze citovat pro ani proti bezjádrové konstrukci;
předpoklad opaku byl tohoto auditu, ne preprintu. A citace Griffithse je
správná: Cambridge University Press čtvrté vydání v roce 2017 skutečně znovu
vydalo, ISBN 9781108420419, takže chyba, kterou jsem tu předpokládal, neexistuje.

Třetí oprava patří staršímu repozitáři v této sérii, ne preprintu. Census
slovníku v `keywords.py` spuštěný nad všemi osmnácti záznamy místo deseti, které
byly k dispozici, když vznikalo `cymatic-eval`, vyvrátil nárok na prvenství,
který tam stojí: „causal" je nulové poprvé už v openQL v1.0 z 3. října a všech
sedm sledovaných termínů chybí v COBARu z 23. září a v Topological Momentum Drive
z 24. září, což jsou oba inženýrská tvrzení. Sedm z osmnácti záznamů ten
hyperkomplexní slovník nenese vůbec a jedenáct ho nese hustě, a ty dvě skupiny se střídají, nejdou
po sobě — není tam tedy žádný trend ke čtení. Samotné počty byly správné; špatně
byl ten nárok na prvenství, který na nich stál, a byl to artefakt srovnání proti
části korpusu. V §1 repozitáře `cymatic-eval` je to teď opravené.

## 8. Hranice

Audit poprvé běžel 9. října 2026 nad šestnácti záznamy. openOmega vyšel týž den
a HOS-PV 2.0 o pět dní později; oba byly doplněny 15. října stejným postupem
a `keywords.py` přepočítal počty citačních značek všech osmnácti přímo
z depositů, bez jediného rozporu proti hodnotám zaznamenaným v říjnu.

Dvacet šest z 69 verdiktových řádků nestojí na plném textu a každý říká, jaká
substituce se použila. Dvě knihy byly nedostupné: Adlerova, nahrazená jeho
vlastním publikovaným souhrnem a dvěma primárními přehledy, a Dixonova,
nahrazená jeho vlastní arXiv přednáškou odkazující zpět na knihu. Interiér
Beranek & Mellow se nepodařilo otevřít, takže ten verdikt stojí na ověřeném
seznamu kapitol; vzorec účinnosti jí přisuzovaný je čtený ze sekundárního
zdroje a je tak v `refdata.py` označený. Sheoran et al. a Wright & Upadhyaya
jsou potvrzeně closed access. Hledání klíčových slov u Griffithse proběhlo nad
třetím vydáním se strukturou čtvrtého ověřenou z katalogizačního záznamu. Ze
sedmi řádků doplněných pro HOS-PV 2.0 stojí tři na abstraktu: Shockley
a Queisser, z nichž se podařilo získat jen s. 510–512 jako OCR soudní přílohy;
Dediu et al., za paywallem a bez kopie v repozitáři; a Naaman s Waldeckem,
doplnění vlastním open-access textem týchž autorů, kde je těch 85 %. Přehled
Smithe a Michla z roku 2010 je za paywallem a nahradil ho vlastní přehled týchž
dvou autorů z roku 2013, takže u toho řádku nejsou žádné počty klíčových slov.

Jedna reference, Putland (1993), se nedohledala; AES e-library je za Cloudflare
a není archivovaná. Nepřímá evidence proti ní je silná, ale je to negativní
evidence, což je slabší než ukázat, že práce neexistuje.

Pět referencí cymatického depositu bylo na existenci ověřeno v doprovodném
repozitáři a na obsah jen jedna, takže ten deposit je proti ostatním
nedoauditovaný.

A nakonec režim selhání, který stojí za zaznamenáním, protože je to právě ten,
o němž se vede řeč. Při hledání Sheoranova textu webový summarizer opakovaně
vyrobil „zjištění ze Sheorana" — jmenované druhy, konkrétní čísla — která v té
práci nejsou a byla smíchaná z jiných článků ve výsledcích. Byla zahozena
a řádek je označen jako stojící na abstraktu. Tatáž disciplína je důvodem, proč
byly ze starší práce v této sérii dvě reference vyhozeny místo citování
z hlavy.

## 9. Data a kód

`refdata.py` drží každý verdikt s doslovnou evidencí, zdrojem a tím, jak daleko
se citovanou práci podařilo přečíst. `carrier.py`, `audit.py` a `hidden.py` to
tabelují; `fetch.sh` reprodukuje osmnáct depositů ze Zenoda a `keywords.py`
z nich přepočítává počty citačních značek. `run_all.sh` projde všechno offline
za asi sekundu, `results.log` je výstup jednoho běhu.

## Reference

Osmnáct auditovaných depositů je se svými DOI v [`README.cs.md`](README.cs.md).
Každá práce citovaná v tomto textu je celá uvedená v `refdata.py`, s DOI nebo
URL a s poznámkou, jak byla získaná. Citace jsou krátké výňatky použité pro
kritiku a recenzi.
