# Korpus preprintů M. Mazgala — nezávislá vyhodnocení

Dvanáct reprodukovatelných vyhodnocení zenodových depositů M. Mazgala, která
pokrývají **všech 18 záznamů** (16 odlišných prací) publikovaných mezi září
a říjnem 2026, plus audit **všech 81 externích referencí** v nich.

Každá podsložka je samostatná: má vlastní `README.md` / `README.cs.md`, text
v `PAPER.md` / `PAPER.cs.md`, vlastní skripty, `requirements.txt`, `run_all.sh`
a zacommitovaný `results.log` z jednoho běhu. Do 24. října 2026 byla každá
publikovaná jako samostatné repo a celá commitová historie všech dvanácti je tu
zachovaná.

> Komentáře v kódu a výpisy skriptů jsou anglicky. Anglická verze je
> v [`README.md`](README.md).

## Těch dvanáct vyhodnocení

| | deposit | datum | co měření zjistilo |
|---|---|---|---|
| [`octonion-mppt-eval`](octonion-mppt-eval) | *Intensional Maxwellian Formalism in Power Electronics* ([v1.0](https://doi.org/10.5281/zenodo.22877912), [v1.1](https://doi.org/10.5281/zenodo.22914238)) | 22. 9. | asociátor, na kterém ten regulátor stojí, je **identicky nulový** přesně na těch sedmi trojicích Fanovy roviny; `e0`, složka, kterou publikovaný kód počítá, je pro libovolný vstup identicky nulová; prohledáno dalších 20 000 konfigurací a **žádná nepřekonala Perturb & Observe** |
| [`xternary-eval`](xternary-eval) | *X-Ternary: A Deterministic Causal 2-Bit Inference Engine* ([22877345](https://doi.org/10.5281/zenodo.22877345)) | 22. 9. | 1,26 bitu na váhu uložené ve 2,25 — o 20 % méně informace než BitNet b1.58 ve 42 % více bitů; 60 tok/s je nad pamětovým stropem jmenované karty; sčítání floatů na GPU **už asociativní není u 31,9 %** náhodných trojic, a právě to je ten nedeterminismus, který článek léčí přidáním nonasociativity; ternární KV cache stojí ×5 001 na perplexitě |
| [`causal-trilogy-eval`](causal-trilogy-eval) | CQFT ([22959886](https://doi.org/10.5281/zenodo.22959886)), PCTP ([22962188](https://doi.org/10.5281/zenodo.22962188)), SOTP ([22962557](https://doi.org/10.5281/zenodo.22962557)) | 25. 9. | **algebra je správná** — orientovaná Fanova rovina v SOTP rov. (3) je jedna z pouhých 16 ze 128 orientací, které dávají normovanou divizní algebru — a všechny vady jsou v přechodu od algebry k hardwaru |
| [`openql-eval`](openql-eval) | *openQL / openOL* ([23112560](https://doi.org/10.5281/zenodo.23112560)) | 3. 10. | matice 4×4 z §2.1 **je** levá regulární reprezentace ℍ, na 1,8·10⁻¹⁵; oktonionová polovina téže věty je **vyloučená teorémem**, protože násobení matic je asociativní a z homomorfismu zůstane 1 z 8 dimenzí |
| [`cymatic-eval`](cymatic-eval) | *Cymatic Stomatal Stimulation and Pulsed Optical Assimilation* ([23156927](https://doi.org/10.5281/zenodo.23156927)) | 5. 10. | **obě frekvence, na kterých návrh stojí, jsou nota B** (B3 na 0,22 centu, B1 na 0,43 centu); sušina na kWh je pod pulzováním invariantní na 3,6·10⁻¹⁵ — a to je právě ta veličina, kterou §5 tvrdí, že redefinuje |
| [`naion-hfrs-eval`](naion-hfrs-eval) | *Dual-Scale Waveform Optimization and HFRS* ([23186884](https://doi.org/10.5281/zenodo.23186884)) | 6. 10. | **v tom pásmu nic není** — `F_micro` leží 6,6 až 9,6 řádu pod nejnižší Ramanovsky aktivní mřížkovou linií a s faradaickým pásmem se nepřekrývá vůbec; ale §5 je **nejlépe argumentovaná sekce v celém korpusu** |
| [`phytomining-eval`](phytomining-eval) | *Quantum Biofortification and In-Situ Phytomining* ([23174932](https://doi.org/10.5281/zenodo.23174932)) | 6. 10. | jedna věta §4 uvádí **dvě hustoty 24× od sebe**; §3.3 nazývá ¹³⁸La stabilním izotopem a ¹³⁹La už spin 7/2 má, takže není co vybírat; citovaný autor magnetického izotopového efektu měří pro přesně tu trojici, která je citovaná pro akceleraci, **3–5× potlačení** |
| [`hemocyanin-eval`](hemocyanin-eval) | *Copper-Based Hemocyanin Physiology in Hominids* ([23209266](https://doi.org/10.5281/zenodo.23209266)) | 7. 10. | hemocyanin nese **4,4 až 14,6× méně** kyslíku než lidská krev, takže návrh potřebuje **7,3 l/min srdečního výdeje v klidu** a **padá, když se jen sedí**; a obratlovci žádný hemocyaninový gen, který by ten epigenetický spínač zapnul, nemají |
| [`intensional-physics-eval`](intensional-physics-eval) | IPC ([23241777](https://doi.org/10.5281/zenodo.23241777)) + openQL v1.1 ([23241148](https://doi.org/10.5281/zenodo.23241148)) | 8. 10. | **první numerické hardwarové tvrzení, které aritmetika podpírá** — 10⁹ dotazů/s proti stropu 1,46·10¹⁰/s, tedy 14,6× rezerva na uzlu 4×4 — na 112×112 mimo 54× a pro raymarching vlastní §4 o 4 až 32× nízko |
| [`openomega-eval`](openomega-eval) | *openOmega: ±12D, ±112D, ±224D* ([23263528](https://doi.org/10.5281/zenodo.23263528)) | 9. 10. | algebra je správná a je tu **ověřená od základů** — (e₁+e₁₀)×(e₄−e₁₅) = 0 přesně — ale sedeniony na to potřeba nejsou (200 ze 200 náhodných párů 224×224 dělá totéž), **ze součinu s normou 4,1·10⁻¹³ žádná energie nevypadne** a `if (collision)` se přesune, neodstraní |
| [`hospv-eval`](hospv-eval) | *HOS-PV 2.0* ([23364732](https://doi.org/10.5281/zenodo.23364732)) | 14. 10. | **mechanismus je v pořádku a ta hranice se skutečně posouvá**: 41,24 % proti 33,7 % Shockleyho-Queissera, potvrzeno ze spektra ASTM G173-03 po třech publikovaných kontrolách. Ale 45,9 % je **řádek dvoupřechodového tandemu** v práci, z níž je to citované, a vysokoenergetický kanál potřebuje 2,44 e⁻/foton proti stropu singletní fise, který je dva |
| [`reference-audit`](reference-audit) | všech 18 záznamů, 81 referencí | 9. 10. | **14 z 81 referencí (17,3 %) je připnutých k nějakému tvrzení**, 15 nese jen glosu, **52 (64,2 %) nemá vyslovený vztah k ničemu** a tři deposity nemají seznam literatury vůbec. Verdikty: SUPPORTS 4, PARTIAL 25, NO SUPPORT 24, **REFUTES 15**, UNRESOLVED 1 |

## Co těch dvanáct měří dohromady

**To, co je vypůjčené, je většinou správně. To, co je postavené, padá na jednom
švu, pořád tomtéž: na přechodu od algebry k hardwaru.** Hardware je asociativní
a každý stroj v tom korpusu stojí na tom, že nonasociativita je fyzicky
k dispozici.

| co si vzal | kde to zemřelo |
|---|---|
| oktonionový asociátor jako „nenulová hardwarová observabla" | identicky nulový přesně na těch sedmi trojicích Fanovy roviny, ze kterých je pole hradel postavené |
| 𝕆 → reálné matice 12×12 | násobení matic je asociativní; přežije 1 z 8 dimenzí |
| sedenionoví dělitelé nuly jako anihilace | WMMA je asociativní a sedeniony nejsou ani alternativní; ‖A·B‖ = 4,1·10⁻¹³ žádnou energii nenese |
| nonasociativita jako lék na nedeterminismus GPU | ten nedeterminismus **je** nonasociativita sčítání floatů, u 31,9 % náhodných trojic |

Šest věcí drží a každé vyhodnocení jimi začíná: HOS-PV je fyzikálně reálný směr
a Shockleyho-Queisserova hranice se skutečně posouvá (+7,5 bodu); dotazovací
rychlost z IPC §5 na malém uzlu projde roofline; HFRS §5 se čte jako posudek
recenzenta; vypůjčená algebra je v průběhu série postupně správnější
(kvaterniony na 1,8·10⁻¹⁵, jedna z 16 platných orientací Fanovy roviny, 168
sedenionových dělitelů nuly); autorovo vlastní tvrzení, že obhajoba leží
v referencích, se ve čtyřech depositech potvrdilo (Fureyová, Baez, poznámka pod
čarou č. 22 u Shockleyho a Queissera, Moreno); a tři premisy mimo algebru jsou
uvedené správně.

Tam, kde je podpora skutečná, tytéž stránky vyvracejí mechanismus, pro který je
nabízena: Fureyová, Dixon i Baez řeší neasociativitu přechodem do
**asociativní** algebry operátorů levého násobení, což je přesně ten krok, na
jehož odmítnutí navrhovaná architektura stojí, a selhání normy, které Morenovy
dělitele nuly vytváří, je totéž, co openOmeze bere „absolutní zachování
energie".

## Jak to spustit

Každá podsložka stojí sama:

```
cd openomega-eval
python3 -m pip install -r requirements.txt
./run_all.sh
```

nebo odtud všechna vyhodnocení po sobě:

```
./run_all.sh            # asi 25 minut, z toho téměř všechno octonion-mppt-eval
```

Všechno je čistě na CPU a bez sítě, se dvěma výjimkami: `octonion-mppt-eval`
trvá ~20 min a používá 16 procesů a `xternary-eval` potřebuje jednu CUDA GPU na
všechno kromě `bits.py`. Sjednocení všech závislostí je v kořenovém
[`requirements.txt`](requirements.txt); soubory v jednotlivých složkách jsou
užší a jsou to ty, které očekává tamní `run_all.sh`.

Každá hodnota v každé podsložce je definovaná právě jednou, v tamním
`constants.py`, kde ho ta složka má, a s **příznakem provenience** — `[P]`
z preprintu, `[V]` ověřeno proti pojmenovanému zdroji, `[A]` předpokládaná
hodnota.

## Licence

Kód (všechny `*.py`, `*.sh`): MIT, viz [`LICENSE`](LICENSE).
Všechny `PAPER.md`, `PAPER.cs.md`, `README.md` a `README.cs.md`: CC BY 4.0.
`hospv-eval/data/ASTMG173.csv` je tabulace ASTM G173-03 od NREL tak, jak se
distribuuje s pvlib (BSD 3-clause); `xternary-eval/vendor/` si drží svou
původní licenci.

Vyhodnocované preprinty jsou dílem svého autora a tady obsažené nejsou; jsou
otevřeně přístupné pod CC BY 4.0 na uvedených DOI.
