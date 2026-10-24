# Audit referencí — říkají citace to, pro co jsou citované?

Audit všech **81 externích referencí** ve všech **18 záznamech na Zenodu** od
M. Mazgala, který u každé citace čte, co ta práce o daném tvrzení skutečně říká.

Text je v [`PAPER.cs.md`](PAPER.cs.md), anglicky v [`PAPER.md`](PAPER.md).

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze textu je
> v [`README.md`](README.md) a [`PAPER.md`](PAPER.md).

## Proč to existuje

Autor těchto preprintů veřejně uvedl, že obhajoba jeho argumentů je záměrně
uložená v referencích a není napsaná v textu, takže analýza omezená na text ji
musí minout. To je věcná metodická kritika a testovatelné tvrzení: ověřit, že
reference existuje, je slabší než přečíst, co říká, a pět starších repozitářů
v této sérii dělalo víc toho prvního než toho druhého.

Tento audit proto hledá **podporu**, ne jen chyby. Reference, která tvrzení
skutečně nese, je tady cennější nález, a žebříček toho, co se našlo, je
v [`hidden.py`](hidden.py).

## Výsledek

**Tvrzení se ve čtyřech depositech potvrdilo.** Disertace Fureyové, citovaná
v SOTP, argumentuje, že kauzalita a nevratný čas vyplývají ze závorkování
algebraického výrazu — to je konceptuální jádro celé „Causal" série, je to
recenzované a v samotných preprintech to nikde není. Baez, citovaný v openQL,
dodává jak reálně-maticové zakódování oktonionového násobení přes operátory
levého násobení, tak cestu k číslu 12 přes sl(3,ℍ) působící na ℝ¹², se so(12)
v jeho magickém čtverci a s jeho vlastní poznámkou „this is no coincidence!" —
tedy lepší odvození dvanáctky než obě, která openQL nabízí. Poznámka pod čarou
č. 22 u Shockleyho a Queissera (1961), citovaných v HOS-PV 2.0, pojmenovává
multiplikaci nosičů a vědomě ji z výpočtu vyjímá — to je přesně to povolení,
které název toho depositu potřebuje a nikde se na ně neodvolává. A Moreno
(1998), citovaný v openOmeze, má přímo vytištěnou dvojici sedenionových
dělitelů nuly, na které stojí tamní anihilace — tutéž, kterou `openomega-eval`
našel hrubou silou. To je autorův bod a platí.

**Dál to nejde, a to ze tří změřených důvodů.** 52 z 81 referencí není připnutých
k žádnému tvrzení a tři deposity nemají seznam literatury vůbec, takže u dvou
třetin korpusu neexistuje nosič, který by skrytá obhajoba mohla použít. Tam, kde
se podpora našla, tytéž stránky vyvracejí mechanismus, pro který je nabízena:
Fureyová, Dixon i Baez řeší neasociativitu přechodem do **asociativní** algebry
operátorů levého násobení, což je přesně ten krok, na jehož odmítnutí navrhovaná
architektura stojí; selhání normy, které Morenovy dělitele nuly vůbec umožňuje,
je totéž, co openOmeze bere její „absolutní zachování energie"; a 45,9 %
v HOS-PV 2.0 je řádek dvoupřechodového tandemu z práce, ze které je to číslo
vzaté a jejíž jednopřechodová odpověď je 44,4 %. A patnáct tvrzení vyvracejí
jejich vlastní citované zdroje vlastními slovy.

**HOS-PV 2.0 ze 14. října je místo, kde má autorovo tvrzení nejblíž k tomu být
prostě pravdivé.** Je to první deposit, ve kterém je každá externí reference
připnutá k větě, všech sedm; všech sedm se dohledá přesně tak, jak jsou
vytištěné; žádná sebecitace, žádná AI jako spoluautor, žádný nevyplněný ORCID.
Šest ze sedmi nese část toho, pro co jsou citované. Jeho problémy jsou jiného
druhu než ve zbytku korpusu: ne vymyšlené reference, ale špatný řádek tabulky
v reálné.

## Co je potřeba

```
python3 -m pip install -r requirements.txt   # jen numpy
```

Bez GPU, a pro samotný audit bez sítě. `fetch.sh` je jediný skript, který síť
potřebuje, a jen stahuje deposity, aby se z nich daly přepočítat počty citačních
značek.

## Reprodukce výsledků

```
./run_all.sh                        # všechno, offline, asi sekunda
./fetch.sh corpus                   # volitelně: stáhnout znovu 18 depositů
python3 keywords.py corpus          #   a přepočítat z nich počty značek
```

| Skript | Co dělá |
|---|---|
| [`refdata.py`](refdata.py) | data: každá reference, verdikt, doslovná citace, na níž verdikt stojí, a jak daleko se tu práci podařilo přečíst |
| [`carrier.py`](carrier.py) | kolik referencí je vůbec k nějakému tvrzení připnutých |
| [`audit.py`](audit.py) | součty verdiktů, rozpad podle dostupnosti, počty klíčových slov, citace, které se v uvedené podobě nedohledají |
| [`hidden.py`](hidden.py) | nalezená podpora, seřazená, s výhradou, která každou omezuje |
| [`keywords.py`](keywords.py) | přepočítá počty citačních značek z depositů; offline vypíše zaznamenané hodnoty |
| [`fetch.sh`](fetch.sh) | stáhne 18 depositů ze Zenoda a převede je na text |

Celý výstup jednoho běhu je v [`results.log`](results.log).

## Klíčová čísla

| co | naměřeno |
|---|---|
| auditovaných záznamů na Zenodu | 18 (16 různých prací; openQL a MPPT mají dvě verze) |
| externích referencí | **81** |
| připnutých k větě značkou v textu | **14 (17,3 %)** — jen *Acoustic Projector*, SOTP a HOS-PV 2.0 |
| nesoucích jen glosu v seznamu literatury | 15 (18,5 %) — openQL v1.0, fytomining, hemocyanin |
| **bez vysloveného vztahu k čemukoli** | **52 (64,2 %)** |
| deposity bez seznamu literatury vůbec | **3** — MPPT v1.0, MPPT v1.1, CQFT |
| deposity, kde je připnutá každá reference | **1** — HOS-PV 2.0, 7 ze 7 |
| sebecitace | 4, dvě z nich uvedené jako „Mazgal, M., & Gemini AI" |
| verdikt SUPPORTS | 4 |
| verdikt PARTIAL | 25 |
| verdikt NO SUPPORT | 24 |
| verdikt REFUTES (zdroj tvrdí opak) | **15** |
| verdikt UNRESOLVED (reference nedohledána) | 1 |
| verdiktových řádků stojících na plném textu | **43 z 69 (62 %)** |
| citací, které se v uvedené podobě nedohledají | **7**, jedna z nich chiméra ze tří zdrojů |
| míst, kde se našla reálná podpora | **10**, seřazeno v `hidden.py` |
| tvrzení bez nosiče kdekoli v těch 81 referencích | 19 |

## Auditované deposity

| záznam | DOI | zkráceně |
|---|---|---|
| 22876757 | [10.5281/zenodo.22876757](https://doi.org/10.5281/zenodo.22876757) | Acoustic Projector |
| 22877345 | [10.5281/zenodo.22877345](https://doi.org/10.5281/zenodo.22877345) | X-Ternary |
| 22877912 | [10.5281/zenodo.22877912](https://doi.org/10.5281/zenodo.22877912) | MPPT v1.0 |
| 22914238 | [10.5281/zenodo.22914238](https://doi.org/10.5281/zenodo.22914238) | MPPT v1.1 |
| 22923154 | [10.5281/zenodo.22923154](https://doi.org/10.5281/zenodo.22923154) | COBAR |
| 22934058 | [10.5281/zenodo.22934058](https://doi.org/10.5281/zenodo.22934058) | Topological Momentum Drive |
| 22959886 | [10.5281/zenodo.22959886](https://doi.org/10.5281/zenodo.22959886) | CQFT |
| 22962188 | [10.5281/zenodo.22962188](https://doi.org/10.5281/zenodo.22962188) | PCTP |
| 22962557 | [10.5281/zenodo.22962557](https://doi.org/10.5281/zenodo.22962557) | SOTP |
| 23112560 | [10.5281/zenodo.23112560](https://doi.org/10.5281/zenodo.23112560) | openQL / openOL v1.0 |
| 23156927 | [10.5281/zenodo.23156927](https://doi.org/10.5281/zenodo.23156927) | cymatická stimulace průduchů |
| 23174932 | [10.5281/zenodo.23174932](https://doi.org/10.5281/zenodo.23174932) | kvantová biofortifikace / fytomining |
| 23186884 | [10.5281/zenodo.23186884](https://doi.org/10.5281/zenodo.23186884) | Na-ion HFRS |
| 23209266 | [10.5281/zenodo.23209266](https://doi.org/10.5281/zenodo.23209266) | hemocyaninová fyziologie |
| 23241148 | [10.5281/zenodo.23241148](https://doi.org/10.5281/zenodo.23241148) | openQL / openOL v1.1 |
| 23241777 | [10.5281/zenodo.23241777](https://doi.org/10.5281/zenodo.23241777) | Intensional Physics Computing |
| 23263528 | [10.5281/zenodo.23263528](https://doi.org/10.5281/zenodo.23263528) | openOmega |
| 23364732 | [10.5281/zenodo.23364732](https://doi.org/10.5281/zenodo.23364732) | HOS-PV 2.0 |

Poslední dva přibyly 15. října 2026. openOmega vyšel 9. října, tedy přesně
v den, kdy tenhle audit běžel poprvé, a HOS-PV 2.0 14. října; `keywords.py`
přepočítal počty citačních značek všech osmnácti přímo z depositů a proti
hodnotám zaznamenaným v říjnu nevznikl žádný rozpor.

## Rozsah

Není to audit toho, zda jsou tvrzení pravdivá — tvrzení může být správné se
špatnou citací. Kde je aritmetika spočítaná, je v doprovodných repozitářích níž
a nic zde ji nemění.

Hranice jsou v §8 textu. 26 z 69 verdiktových řádků nestojí na plném textu
a každý říká, jaká substituce se použila; dvě knihy byly nedostupné a nahradily
je vlastní práce a publikované souhrny jejich autorů; jednu referenci se
nepodařilo dohledat vůbec, což je negativní evidence, ne důkaz neexistence.
Počty klíčových slov se hlásí jako počty: nula znamená, že se termín hledal
a není tam.

Tři opravy, které tento audit dluží jinam, jsou v něm zaznamenané. Teslův patent
železné jádro **nepresuponuje**, proti výchozímu předpokladu tohoto auditu,
a citace Griffithse je správná — chyba, kterou jsem tu předpokládal, neexistuje.
`openql-eval` už Baezovu konstrukci levého násobení měřilo, aniž by Baezovi
připsalo, že ji dodal. A census slovníku v `keywords.py`, spuštěný nad všemi
osmnácti záznamy místo deseti, vyvrátil nárok na prvenství v `cymatic-eval`:
„causal" bylo nulové poprvé už v openQL v1.0 z 3. října a všech sedm sledovaných
termínů chybí v COBARu z 23. září a v Momentum Drive z 24. září, takže ten
slovník přichází ve dvou proložených skupinách, nemizí v čase. Ta oprava je teď
zaznamenaná v §1 repozitáře `cymatic-eval`.

## Doprovodná vyhodnocení

- [`octonion-mppt-eval`](../octonion-mppt-eval) — oktonionová dvouvrstvá šablona s asociátorem a census Maxwellovy atribuce
- [`xternary-eval`](../xternary-eval) — 2bitový inferenční engine pro LLM
- [`causal-trilogy-eval`](../causal-trilogy-eval) — trilogie CQFT / PCTP / SOTP ze září 2026
- [`openql-eval`](../openql-eval) — tenzorová maticová architektura openQL / openOL z října 2026
- [`cymatic-eval`](../cymatic-eval) — cymatická stimulace průduchů a pulzní osvětlení z října 2026
- [`phytomining-eval`](../phytomining-eval) — matrice kvantové biofortifikace a in-situ phytominingu z října 2026
- [`naion-hfrs-eval`](../naion-hfrs-eval) — dvoušálový signál a nabíjení HFRS z října 2026
- [`hemocyanin-eval`](../hemocyanin-eval) — hemocyaninová fyziologie na měďi z října 2026
- [`intensional-physics-eval`](../intensional-physics-eval) — Intensional Physics Computing a openQL v1.1 z října 2026
- [`openomega-eval`](../openomega-eval) — openOmega, antimaterie a sedeniony z října 2026
- [`hospv-eval`](../hospv-eval) — HOS-PV 2.0, singletní fise a spintronická fotovoltaika z října 2026

## Licence

Kód (všechny `*.py`, `run_all.sh`, `fetch.sh`): MIT, viz `LICENSE`.
Text `PAPER.md` a `PAPER.cs.md`: CC BY 4.0.
Citace z prací třetích stran jsou krátké výňatky použité pro kritiku a recenzi,
každá je ve `refdata.py` přiřazená ke svému zdroji.
