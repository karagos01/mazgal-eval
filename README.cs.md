# Audit referencí — říkají citace to, pro co jsou citované?

Audit všech **69 externích referencí** ve všech **16 záznamech na Zenodu** od
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

**Tvrzení se ve dvou depositech potvrdilo.** Disertace Fureyové, citovaná
v SOTP, argumentuje, že kauzalita a nevratný čas vyplývají ze závorkování
algebraického výrazu — to je konceptuální jádro celé „Causal" série, je to
recenzované a v samotných preprintech to nikde není. A Baez, citovaný v openQL,
dodává jak reálně-maticové zakódování oktonionového násobení přes operátory
levého násobení, tak cestu k číslu 12 přes sl(3,ℍ) působící na ℝ¹², se so(12)
v jeho magickém čtverci a s jeho vlastní poznámkou „this is no coincidence!" —
tedy lepší odvození dvanáctky než obě, která openQL nabízí. To je autorův bod
a platí.

**Dál to nejde, a to ze tří změřených důvodů.** 47 z 69 referencí není připnutých
k žádnému tvrzení a tři deposity nemají seznam literatury vůbec, takže u dvou
třetin korpusu neexistuje nosič, který by skrytá obhajoba mohla použít. Tam, kde
se podpora našla, tytéž stránky vyvracejí mechanismus, pro který je nabízena:
Fureyová, Dixon i Baez řeší neasociativitu přechodem do **asociativní** algebry
operátorů levého násobení, což je přesně ten krok, na jehož odmítnutí navrhovaná
architektura stojí. A čtrnáct tvrzení vyvracejí jejich vlastní citované zdroje
vlastními slovy.

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
./fetch.sh corpus                   # volitelně: stáhnout znovu 16 depositů
python3 keywords.py corpus          #   a přepočítat z nich počty značek
```

| Skript | Co dělá |
|---|---|
| [`refdata.py`](refdata.py) | data: každá reference, verdikt, doslovná citace, na níž verdikt stojí, a jak daleko se tu práci podařilo přečíst |
| [`carrier.py`](carrier.py) | kolik referencí je vůbec k nějakému tvrzení připnutých |
| [`audit.py`](audit.py) | součty verdiktů, rozpad podle dostupnosti, počty klíčových slov, citace, které se v uvedené podobě nedohledají |
| [`hidden.py`](hidden.py) | nalezená podpora, seřazená, s výhradou, která každou omezuje |
| [`keywords.py`](keywords.py) | přepočítá počty citačních značek z depositů; offline vypíše zaznamenané hodnoty |
| [`fetch.sh`](fetch.sh) | stáhne 16 depositů ze Zenoda a převede je na text |

Celý výstup jednoho běhu je v [`results.log`](results.log).

## Klíčová čísla

| co | naměřeno |
|---|---|
| auditovaných záznamů na Zenodu | 16 (14 různých prací; openQL a MPPT mají dvě verze) |
| externích referencí | **69** |
| připnutých k větě značkou v textu | **7 (10,1 %)** — jen *Acoustic Projector* a SOTP |
| nesoucích jen glosu v seznamu literatury | 15 (21,7 %) — openQL v1.0, fytomining, hemocyanin |
| **bez vysloveného vztahu k čemukoli** | **47 (68,1 %)** |
| deposity bez seznamu literatury vůbec | **3** — MPPT v1.0, MPPT v1.1, CQFT |
| sebecitace | 4, dvě z nich uvedené jako „Mazgal, M., & Gemini AI" |
| verdikt SUPPORTS | 3 |
| verdikt PARTIAL | 18 |
| verdikt NO SUPPORT | 23 |
| verdikt REFUTES (zdroj tvrdí opak) | **14** |
| verdikt UNRESOLVED (reference nedohledána) | 1 |
| verdiktových řádků stojících na plném textu | **38 z 59 (64 %)** |
| citací, které se v uvedené podobě nedohledají | **7**, jedna z nich chiméra ze tří zdrojů |
| míst, kde se našla reálná podpora | **6**, seřazeno v `hidden.py` |
| tvrzení bez nosiče kdekoli v těch 69 referencích | 13 |

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

## Rozsah

Není to audit toho, zda jsou tvrzení pravdivá — tvrzení může být správné se
špatnou citací. Kde je aritmetika spočítaná, je v doprovodných repozitářích níž
a nic zde ji nemění.

Hranice jsou v §8 textu. 21 z 59 verdiktových řádků nestojí na plném textu
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
šestnácti záznamy místo deseti, vyvrátil nárok na prvenství v `cymatic-eval`:
„causal" bylo nulové poprvé už v openQL v1.0 z 3. října a všech sedm sledovaných
termínů chybí v COBARu z 23. září a v Momentum Drive z 24. září, takže ten
slovník přichází ve dvou proložených skupinách, nemizí v čase. Ta oprava je teď
zaznamenaná v §1 repozitáře `cymatic-eval`.

## Doprovodná vyhodnocení

- [`octonion-mppt-eval`](https://github.com/karagos01/octonion-mppt-eval) — oktonionová dvouvrstvá šablona s asociátorem a census Maxwellovy atribuce
- [`xternary-eval`](https://github.com/karagos01/xternary-eval) — 2bitový inferenční engine pro LLM
- [`causal-trilogy-eval`](https://github.com/karagos01/causal-trilogy-eval) — trilogie CQFT / PCTP / SOTP ze září 2026
- [`openql-eval`](https://github.com/karagos01/openql-eval) — tenzorová maticová architektura openQL / openOL z října 2026
- [`cymatic-eval`](https://github.com/karagos01/cymatic-eval) — cymatická stimulace průduchů a pulzní osvětlení z října 2026
- [`phytomining-eval`](https://github.com/karagos01/phytomining-eval) — matrice kvantové biofortifikace a in-situ phytominingu z října 2026
- [`naion-hfrs-eval`](https://github.com/karagos01/naion-hfrs-eval) — dvoušálový signál a nabíjení HFRS z října 2026
- [`hemocyanin-eval`](https://github.com/karagos01/hemocyanin-eval) — hemocyaninová fyziologie na měďi z října 2026
- [`intensional-physics-eval`](https://github.com/karagos01/intensional-physics-eval) — Intensional Physics Computing a openQL v1.1 z října 2026

## Licence

Kód (všechny `*.py`, `run_all.sh`, `fetch.sh`): MIT, viz `LICENSE`.
Text `PAPER.md` a `PAPER.cs.md`: CC BY 4.0.
Citace z prací třetích stran jsou krátké výňatky použité pro kritiku a recenzi,
každá je ve `refdata.py` přiřazená ke svému zdroji.
