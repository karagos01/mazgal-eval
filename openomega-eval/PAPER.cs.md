# Správná algebra pro vlastnost, kterou nepotřebuje: vyhodnocení *openOmega*

karagos01, říjen 2026

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`PAPER.md`](PAPER.md).

## Abstrakt

M. Mazgal, *openOmega: Tensor Matrix Architecture for Matter-Antimatter Symmetry
in ±12D, ±112D, and ±224D Spaces* (Zenodo, 9. října 2026, DOI
[10.5281/zenodo.23263528](https://doi.org/10.5281/zenodo.23263528)) rozšiřuje
engine openQL/openOL na antimaterii. Cayley-Dicksonova konstrukce a sedeniony
mají zdvojit fázový prostor na 224D a přidat „negativní zrcadlovou" polovinu
s Diracovým morem; dělitelé nuly té algebry pak mají nativně provádět anihilaci
materie a antimaterie — „The Tensor Core simply multiplies both matrices. The
result is a zero in the matter register and the release of an absolute tensor
vector into the energy register… natively in a single processor clock cycle."
Abstrakt to nazývá „a unified framework for a Theory of Everything in
computational physics".

**Ta algebra je správná a tento repozitář to potvrzuje od základů, místo aby to
bral na slovo.** Cayley-Dicksonova věž je tu postavená z reálných čísel;
konstrukce reprodukuje učebnicovou klasifikaci přesně — ℍ asociativní,
𝕆 neasociativní ale alternativní, sedeniony ani to — a multiplikativita normy
platí přesně do dimenze 8 a padá na 16, což je právě důvod, proč se tam objeví
dělitelé nuly. Sedenionový dělitel nuly se pak najde hledáním:
**(e₁ + e₁₀) × (e₄ − e₁₅) = 0**, přesně. Moreno (1998), reference [3], je pro to
správný zdroj a je správně připnutý — vedle Fureyové v SOTP je to nejlépe vybraná
citace ze sedmnácti autorových depositů.

**Ale engine ty sedeniony pro tu vlastnost, kterou chce, nepotřebuje.** Vlastní
rovnice §3 je o **maticích**: „there exist non-zero matrices A (positron) and B
(electron)". Dělitelé nuly jsou v každé maticové algebře nad tělem naprosto
běžní — [[1,0],[0,0]]·[[0,0],[0,1]] = 0 je nejmenší případ a **200 ze 200**
náhodně zkonstruovaných nenulových párů reálných matic 224×224 tu dává nulu. Ta
vlastnost je zdarma v každé dimenzi a hardware už v maticové algebře je.

**Z toho součinu energie vypadnout nemůže.** Naměřeno: ‖A‖ = 34,1, ‖B‖ = 221,9,
‖A·B‖ = **4,1·10⁻¹³**. Nulový součin si z operandů neponechá nic, takže v něm
není co uvolnit. Aby engine mohl vyzářit E = mc², musí si obě velikosti přečíst
**před** násobením a pak zaregistrovat, že registr spadl na nulu — což je
porovnání s nulou, tedy právě to `if (collision)`, o kterém §3 říká, že není
potřeba. Ta podmínka se neodstraní, jen se přesune.

**224 v Cayley-Dicksonově věži není.** Věž jsou mocniny dvou; sedeniony jsou
**šestnáctirozměrné**. 224 = 2 × 112 a 112 ve věži taky není — a série pro něj
už ani nenabízí odvození, protože openQL v1.1 tu větu, která ho dávala, vypustila.
Takže „Sedenion architecture (which is the mathematical foundation of the −224D
space)" se nemá k čemu připojit.

**Hardwarové tvrzení v §4 je správné a dědičné.** 224/16 = 14 přesně, takže uzel
kryje WMMA granularitu na 100 % obsazenosti. Ale 112/16 = 7 je taky přesně —
zdvojením násobku šestnácti zůstane násobek šestnácti — a uzel 224D je **196 MMA
operací**, ne jedna. Na kartě, kterou autorovy vlastní preprinty jmenují, je
jeden součin 224×224 **269 taktů celé GPU**, tedy osmkrát horší než ten případ
112D, pro který se tvrdilo totéž.

**A ten roofline výsledek zdvojení přežije.** Maticová forma a stav, který kóduje,
mají na každé vrstvě totožnou aritmetickou intenzitu — 6,0, 56,0 a 112,0
FLOP/bajt pro obojí — zatímco matice stojí **d×** provozu. Zakódovat d čísel jako
matici d×d nekoupí žádnou aritmetickou intenzitu při žádném d, a to je ten
naměřený smysl, v němž je „100 % saturated" pravda a není k ničemu: dlaždice jsou
plné a karta čeká na pamět.

## 1. Co je správně

Tento deposit má víc věcí, které obstojí, než většina v té sérii, a pořadí tady
to odráží.

**Sedeniony dělitele nuly mají a důvod, který práce uvádí, je ten správný.**
`zerodivisors.py` staví Cayley-Dicksonovu věž z reálných čísel podle
(a,b)(c,d) = (ac − d b̄, ā d + c b) a v každé dimenzi měří, jestli je násobení
komutativní, asociativní, alternativní a multiplikativní v normě:

| dim | komutativní | asociativní | alternativní | ‖xy‖ − ‖x‖‖y‖, relativně |
|---|---|---|---|---|
| 1 | ano | ano | ano | 0 |
| 2 | ano | ano | ano | 1,5·10⁻¹⁶ |
| 4 (ℍ) | ne | **ano** | ano | 0 |
| 8 (𝕆) | ne | ne | **ano** | 1,4·10⁻¹⁶ |
| 16 (sedeniony) | ne | ne | **ne** | **1,1·10⁻²** |

To je učebnicová klasifikace reprodukovaná přesně a je to kontrola, že ta
konstrukce je správná, ne jen plausibilní. Selhání multiplikativity normy na 16
je přesně Morenův důvod pro vznik dělitelů nuly a hledání pak najde **168**
párů mezi jednoduchými kombinacemi e_i ± e_j, přičemž první je
**(e₁ + e₁₀) × (e₄ − e₁₅) = 0** s ‖a·b‖ = 0 přesně.

**Reference [3] je výborná.** Moreno, *The zero divisors of the Cayley-Dickson
algebras over the real numbers*, Bol. Soc. Mat. Mexicana (3) 4(1), 13–28 (1998),
arXiv:q-alg/9710013, je přesně o tomhle: o dělitelích nuly od dimenze 16 výš a o
selhání multiplikativity normy, které je umožňuje. Správně vybraná a správně
připnutá. V auditu referencí celého korpusu tenhle standard splnila jen
disertace Fureyové v SOTP.

**Reference [1] je reálná a správně citovaná.** Dirac, *A Theory of Electrons
and Protons*, Proc. R. Soc. Lond. A 126, 360–365 (1930). Teorie děr je
historicky významný model, byť ji nahradil formalismus antičástic v QFT —
citovat ji jako aktuální fyzikální obraz vakua je zastaralé čtení, ne nepravdivé.

**224/16 = 14 přesně.** Tvrzení o zarovnání v §4 je aritmeticky správné a stejně
tak 100% obsazenost, která z něj plyne. §2 níž rozporuje, co to vynáší, ne jestli
to platí.

**Fázová konjugace je reálná.** Optická fázová konjugace skutečně vytváří vlnu,
která se vrací svou cestou aberujícím prostředím, a běžně se popisuje jako časově
obrácená. Rámování vrstvy −12D tedy není vymyšlené, i když „active gravity
shielding" ve stejné odrážce ano.

## 2. Ta algebra pro ten mechanismus není potřeba

§3 formuluje mechanismus maticově:

> „in the 224D node of the openOmega engine, there exist non-zero matrices A
> (positron) and B (electron) for which the following holds: A×B=0"

> „This 'anomaly' is physically perfect. If matter and antimatter collide in the
> virtual grid of the engine, the computational core requires no conditional
> script like 'if (collision) { delete_object }'."

Dělitelé nuly nejsou v maticové algebře anomálie, jsou generické. Jakékoli dvě
singulární matice, u nichž se obraz jedné potká s jádrem druhé, dají nulu.
Nejmenší příklad je

    [[1,0],[0,0]] · [[0,0],[0,1]] = [[0,0],[0,0]]

a ve vlastní dimenzi té práce `zerodivisors.py` zkonstruuje **200 ze 200**
nenulových párů reálných matic 224×224 s A·B = 0, tím že zvolí náhodný rozklad
podprostoru a uloží im(B) do ker(A).

Takže vlastnost, pro kterou §3 sahá do sedenionů, má každá maticová algebra nad
tělem, v každé dimenzi a zdarma. Nic z 224 ani z Cayley-Dicksonova zdvojení není
k získání nenulového páru s nulovým součinem potřeba.

Záleží na tom víc než esteticky, protože se tím mění, co ta sekce tvrdí. Kdyby
dělitelé nuly byli exotičtí a vyhrazení vysokodimenzionálním hyperkomplexním
algebrám, pak by dosažení 224D byl ten umožňující krok. Protože nejsou, ten
umožňující krok chybí — engine to mohl dělat na 2×2.

## 3. Ten součin energii neunese

§3 pokračuje:

> „The Tensor Core simply multiplies both matrices. The result is a zero in the
> matter register and the release of an absolute tensor vector into the energy
> register. The engine executes pure, mathematically perfect E=mc²
> annihilation natively in a single processor clock cycle."

Naměřeno na zarovnaném páru 224×224:

| | hodnota |
|---|---|
| ‖A‖_F | 34,1038 |
| ‖B‖_F | 221,8755 |
| ‖A·B‖_F | **4,06·10⁻¹³** |

Součin si z velikostí operandů neponechá nic — to je, co znamená být nulový.
V tom výsledku nezůstal žádný „absolute tensor vector" k uvolnění do
energetického registru, protože ten výsledek je nulová matice.

Aby engine vyzářil E = mc², musí tedy: přečíst ‖A‖ a ‖B‖ před násobením, někde
si je podržet, provést násobení a pak **otestovat, jestli registr materie spadl
na nulu**, aby věděl, že má ty uložené velikosti přičíst do energetického
registru. Ten test je porovnání s nulou — tedy přesně to `if (collision)`, které
podle té sekce není potřeba. Podmínka se neodstranila, přesunula se zpřed
násobení za něj, a ta evidence, kterou měla nahradit, je pořád potřeba.

Zachování padá i druhým směrem. Nulový součin vznikne z **jakéhokoli** zarovnaného
singulárního páru, takže engine, který vyzáří energii vždy, když registr dojde na
nulu, ji vyzáří pro každý takový pár, bez ohledu na to, jestli ty operandy
představovaly částici a její antičástici. Odlišit fyzikální případ od numerické
shody vyžaduje vědět, co ty matice znamenají, což je další evidence.

## 4. Odkud je 224 a odkud to práce říká

Abstrakt a §2 přisuzují 224 Cayley-Dicksonově konstrukci a „dimensional
doubling". `dimensions.py` to kontroluje:

| | v Cayley-Dicksonově věži? |
|---|---|
| věž | 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 |
| sedeniony, dimenze 16 | **ano** |
| 12 | ne |
| 112 | ne |
| 224 | **ne** |
| 448 | ne |

Cayley-Dicksonovo zdvojení vede algebru dimenze n na algebru dimenze 2n počínaje
jedničkou, což dává mocniny dvou a nic jiného. Vynásobit libovolné číslo dvěma je
jiná operace, která s tím sdílí slovo. 224 = 2 × 112 a 112 ve věži taky není —
a `openql-eval` zaznamenalo, že openQL v1.1 vypustila tu jedinou větu v celé
sérii, která 112 odvozovala, a nenahradila ji. Takže 224 je zdvojení čísla, pro
které série aktuálně žádné odvození nenabízí.

Sedeniony jsou přitom šestnáctirozměrné. „Sedenion architecture (which is the
mathematical foundation of the −224D space)" se tedy nemá k čemu připojit:
algebra je reálná, její dělitelé nuly jsou reální, a dimenze, v níž žije, je 16,
ne 224.

**„Negativní dimenze" jsou nálepka, ne prostor.** Dimenze je mohutnost — počet
souřadnic potřebných k určení bodu — takže vektorový prostor dimenze −224 nad
žádným tělem neexistuje. To, co §2 popisuje, zrcadlovou kopii stavu držící
antičásticový sektor, je obyčejná konstrukce, a je to *víc* dimenzí:

| vrstva | pozitivní | zrcadlo | celkový stav |
|---|---|---|---|
| ±12 | 12 | 12 | 24 |
| ±112 | 112 | 112 | 224 |
| ±224 | 224 | 224 | **448** |

Největší vrstva je 448rozměrný stav, což hardware musí držet a přesouvat, a §5
níž je spočítaná na tom čísle. V té aritmetice je mírná ironie: ±112 už dává 224.

**Dimenze, které citovaná fyzika používá, jsou jiná čísla.** §2 říká „The
positive 224D contains complete string theory and supersymmetry". Kritické
dimenze jsou 10 pro superstruny a 26 pro bosonovou strunu, M-teorie 11, a jsou
dané zrušením anomálií, ne volbou. 224 není ani jedna z nich a sekce nenabízí
žádné vnoření nebo kompaktifikaci, která by ta dvě čísla spojovala.
Zaznamenáno jako nepodložené, ne vyvrácené: není tu žádná konstrukce ke kontrole.

## 5. Co to stojí na hardwaru, který sama specifikuje

**„a single processor clock cycle".** RTX 3090, kterou autorovy vlastní
preprinty jmenují, zvládne 83 529 fp16 FLOP za takt přes celou kartu.

| uzel | FLOP na součin | takty celé GPU |
|---|---|---|
| 12×12 | 3 456 | 0,04 |
| 112×112 | 2 809 856 | 33,6 |
| 224×224 | 22 478 848 | **269,1** |

Takže jedna anihilace je 269 taktů celé karty a osmkrát horší než ten případ
112D, pro který openQL tvrdila totéž — což je, co dělá třetí mocnina dimenze.
Uzel 224D je navíc 196 WMMA instrukcí, každá s latencí několika taktů, ještě
než se natáhnou operandy.

**Nároky na pamět.** Uzel 224×224 fp16 má 98,0 KiB, se zrcadlem 196,0 KiB.
Dvacet čtyři gibibajtů udrží **128 397** párů uzlů, jen stav — tedy krychli
50 uzlů na hranu, bez čehokoli pro pravidlové matice, stav paprsku nebo výstupní
obrázek. Proti tokamakové aplikaci z §5 při jednom uzlu na částici: kubický
milimetr plazmatu o 10²⁰ m⁻³ obsahuje 10¹¹ částic, takže ta mřížka chybí faktorem
**778 834**, tedy asi šest řádů, na jeden kubický milimetr.

**Kroková frekvence.** Pro fixní milionuzlovou mřížku potřebuje ±224D 186,9 GiB
stavu a 373,8 GiB na jeden sweep — na kartu se nevejde vůbec, a ±112D taky ne.
Největší mřížka, která se při ±224D vejde, sweepuje na **18,2 Hz**; real-time je
60.

(Tabulka nad kartou zaplněnou do kapacity by tu byla degenerovaná: zaplnit kartu
a jednou ji přejít jsou asi dva průchody VRAM bez ohledu na velikost uzlu, takže
každá vrstva by vrátila totéž z konstrukce. Místo toho se drží fixní mřížka
a mění vrstva, což je to, co cenu toho zdvojení zviditelní. Dřívější verze
tohohle repozitáře měla tu degenerovanou variantu.)

**Roofline, který zdvojení neposune.**

| vrstva | stav | matice | režie | W·s FLOP/bajt | W·S FLOP/bajt |
|---|---|---|---|---|---|
| ±12 | 24 B | 288 B | 12× | 6,0 | 6,0 |
| ±112 | 224 B | 25 088 B | 112× | 56,0 | 56,0 |
| ±224 | 448 B | 100 352 B | 224× | **112,0** | **112,0** |

Poslední dva sloupce jsou na každé vrstvě shodné. To je výsledek, který
`openql-eval` naměřilo pro 112, a zdvojení ho přežije: maticová forma leží na
roofline přesně ve stejném bodě jako stav, který kóduje, a stojí přitom d× provozu
a d× aritmetiky. Zakódovat d čísel jako matici d×d nekoupí žádnou aritmetickou
intenzitu při žádném d.

To je ten naměřený smysl, v němž je „100 % saturated quantum field simulator"
z §4 pravda a není k ničemu. Dlaždice jsou plné — to je, co 224/16 = 14 přesně
kupuje — a karta čeká na pamět tak jako tak.

**Cena kroku od openQL:** 4× pamět na uzel, 8× aritmetika, 4× dlaždice, a to
ještě než zrcadlo pamět zdvojí znovu. §4 to předkládá jako bezplatné, protože
zarovnání zůstává; zarovnání je o plýtvání uvnitř dlaždice, ne o tom, kolik
dlaždic je.

## 6. Volba, kterou architektura nedělá

Architektura potřebuje WMMA, což je násobení matic, a násobení matic je nad
každým okruhem asociativní. Mechanismus potřebuje sedeniony, které §1 měří jako
ani asociativní, ani alternativní. Obojí nemůže platit zároveň a preprint to
tvrdí v po sobě jdoucích sekcích: §3 vyvozuje dělitele nuly ze sedenionové
matematiky, §4 popisuje uzel jako pole 14 × 14 WMMA bloků.

Je to tentýž strukturální bod, který `openql-eval` naměřilo pro oktoniony, kde
asociátory autorovy vlastní násobicí tabulky vyplnily celou imaginární část
a nechaly 1 z 8 dimenzí, která přežije jakoukoli maticovou formu. Sedeniony jsou
striktně větší verze toho problému.

Audit referencí zjistil, že všichni tři matematici, které tento autor cituje
kvůli hyperkomplexní algebře — Fureyová, Dixon a Baez — to řeší přechodem do
**asociativní** algebry operátorů levého násobení, a každý to říká výslovně.
Ten manévr je k dispozici i tady a je to to, co by architekturu udělalo
koherentní; zároveň by rozpustil ten mechanismus, protože asociativní operátorová
algebra je maticová algebra, kde platí bod z §2 a sedeniony nedělají žádnou práci.

## 7. Co se tady neměří

„A unified framework for a Theory of Everything in computational physics" není
kvantitativní tvrzení a nic tady o něm nerozhoduje. Stejně tak aplikace z §5:
fázově konjugovaný radar „with zero reflection delay", sonoluminiscence „via
vacuum field collapse in the −112D layer", nebo temná hmota simulovaná jako
„manifestations of tensor curvature that do not interact with the positive
spectrum but exert gravitational force". Ani jedno není vysloveno s nějakou
veličinou, takže není co kontrolovat.

Dvě poznámky k té sérii, ne k fyzice. Je to první deposit, který používá frázi
„Theory of Everything". A hyperkomplexní slovník se vrací po šesti depositech:
„octonion" jednou a „sedenion" pětkrát, zatímco „causal" zůstává na nule, kde je
od openQL v1.0 z 3. října.

## 8. Hranice

Žádná GPU nebyla použita. Hardwarové údaje jsou katalogové specifikace a ty
stropy jsou teoretické špičky; reálná implementace dosáhne jejich zlomku, což
nálezy o nákladech zesiluje a na poměrech nic nemění.

Provenience je označená v `constants.py`: `[P]` z preprintu, `[V]` ověřeno proti
pojmenovanému zdroji, `[A]` předpokládaná hodnota nebo volba prezentace.
Velikost mřížky, hustota plazmatu, seed generátoru a numerická tolerance nuly
jsou `[A]`; ta hustota nenese nic nad řád toho chybějícího faktoru.

Cayley-Dicksonova konstrukce tady používá jednu z několika znaménkových konvencí
pro zdvojovací součin. Jiná konvence permutuje bázi a mění, které konkrétní páry
jsou dělitelé nuly, ale nemění dimenzi, v níž se objeví, ani klasifikační tabulku
v §1 — a právě proto je ta tabulka uvedená: je to kontrola, že implementovaná
konvence je správná. Dřívější verze používala chybný vzorec pro druhou složku
a ta tabulka to odhalila tím, že kvaterniony vyšly neasociativní.

Konstrukce dělitelů nuly v 224×224 je přesná až na plovoucí řádovou čárku; ‖A·B‖
řádu 10⁻¹³ proti normám operandů řádu 10² je nula na asi patnáct míst, ne
analyticky nula. Příklad 2×2 i ten sedenionový jsou přesné.

## 9. Data a kód

`constants.py` drží každou hodnotu s příznakem provenience a zdrojem a žádný
další skript žádnou nedefinuje. `dimensions.py` reprodukuje §4,
`zerodivisors.py` §§1–3 a §6, `hardware.py` §5. `run_all.sh` projde všechno
offline za asi dvacet sekund, `results.log` je výstup jednoho běhu. Měření
openQL, na která se tady odkazuje, se tu nereprodukují — žijí
v [`openql-eval`](../openql-eval) a verdikty
u referencí v [`reference-audit`](../reference-audit).

## Reference

Vyhodnocený preprint: M. Mazgal, *openOmega: Tensor Matrix Architecture for
Matter-Antimatter Symmetry in ±12D, ±112D, and ±224D Spaces*, Zenodo,
9. října 2026, DOI 10.5281/zenodo.23263528, CC BY 4.0.

Externí zdroje jsou citované v `constants.py` vedle hodnot, které podpírají:
G. Moreno, *The zero divisors of the Cayley-Dickson algebras over the real
numbers*, Bol. Soc. Mat. Mexicana (3) 4(1), 13–28 (1998), arXiv:q-alg/9710013;
P. A. M. Dirac, *A Theory of Electrons and Protons*, Proc. R. Soc. Lond. A 126,
360–365 (1930); S. Markidis et al., IPDPSW 522–531 (2018), DOI
10.1109/IPDPSW.2018.00091, pro granularitu dlaždice WMMA; a katalogové
specifikace NVIDIA RTX 3090. Citace jsou krátké výňatky použité pro kritiku
a recenzi.
