# Správný mechanismus, špatný řádek tabulky

Nezávislé vyhodnocení práce M. Mazgal, *HOS-PV 2.0: Exceeding the
Shockley-Queisser Limit via Chiral-Induced Spin Selectivity, Dexter-Sensitized
Singlet Fission, and Altermagnetic Carrier Extraction* (Zenodo, 14. října 2026,
DOI [10.5281/zenodo.23364732](https://doi.org/10.5281/zenodo.23364732)).

Každé číslo níž vyrábějí skripty v tomto repozitáři z referenčního spektra
ASTM G173-03 a z publikovaných měření, bez GPU a bez sítě. Jeden běh
`./run_all.sh` je zaznamenaný v [`results.log`](results.log).

> Komentáře v kódu a výpisy skriptů jsou anglicky.

## 1. Ten mechanismus je v pořádku a ta hranice se skutečně posouvá

Hlavní tvrzení té architektury je, že jeden přechod může překonat
Shockleyho-Queisserovu hranici tak, že jeden absorbér rozdělí vysokoenergetické
singlety na páry tripletů a předá je druhému, úzkopásmovému absorbéru, který
určuje napětí. To je správně a tento repozitář to potvrzuje od základů, ne na
autorovo slovo.

Výpočet detailní rovnováhy v [`detailed_balance.py`](detailed_balance.py) je
postavený ze spektra a Planckova zákona. Než se obrátí na ten preprint,
reprodukuje tři publikované hodnoty:

| model | naměřeno zde | publikováno |
|---|---|---|
| Shockley-Queisser, jeden nosič na foton | **33,77 %** při 1,335 eV | 33,7 % při 1,34 eV |
| multiplikace nosičů, QY = floor(E/E_g) | **44,62 %** při 0,70 eV | 44,4 % při 0,70 eV |
| multiplikace zastropovaná na dva na foton | **42,09 %** při 0,94 eV | 42,0 % při 0,95 eV |

Druhý a třetí řádek jsou z reference [5] toho preprintu a z průvodní zprávy téže
skupiny. Všechny tři sedí do 0,3 procentního bodu, třetí do 0,1 bodu a 10 meV —
a to je to, co opravňuje všechno ostatní.

Aplikováno na tu architekturu — jeden elektron na foton mezi 1,12 eV a 2,25 eV,
dva nad 2,25 eV, všechno odebírané při 1,12 eV — dává týž kód:

| | hranice |
|---|---|
| obyčejný jeden přechod při 1,12 eV | 33,48 % |
| Shockleyho-Queisserovo optimum, 1,34 eV | 33,76 % |
| **tato architektura, při jejích vlastních dvou energiích** | **41,24 %** |

Takže ta myšlenka funguje. Architektura překonává Shockleyho-Queissera
o **7,5 procentního bodu**, se zkratovým proudem 53,6 mA/cm² a napětím
naprázdno 0,883 V v radiačním limitu. Překročení hranice není to, co je na
tomhle preprintu špatně.

Správně je v něm i řada dalších věcí, a je třeba to říct natvrdo, protože
zbytek tohoto textu je kritický:

* Převody vlnových délek jsou přesné: 2,25 eV → 551,0 nm, 1,12 eV → 1107,0 nm,
  oba jak jsou vytištěné.
* `EQE_high = η_SF × η_DET × EQE_BHJ = 1,85 × 0,92 × 0,90 = 1,5318`, vytištěno
  jako 153 %. Správně.
* `β_eff = β_L(1 − η_PB P²) = 1 − 0,95 × 0,85² = 0,3136`, vytištěno jako 0,314
  a 68,6 % potlačení. Správně.
* `PCE = 52,3 × 0,81 × 0,840 / 100 = 0,3558`, vytištěno jako 35,58 %. Vnitřně
  konzistentní aritmetika; padá ten proud, který do ní vstupuje.
* Uvedený plnící faktor 84,0 % je pod stropem ideální diody, který je
  **86,2 %** při V_oc = 0,81 V, takže na rozdíl od ostatních hlavních čísel je
  dosažitelný tak, jak je uvedený.
* Spinové rozštěpení přisouzené altermagnetickému kolektoru, ~0,8 eV, je
  naměřená hodnota pro MnTe: fotoemise s rozlišením úhlu uvádí 0,37 eV a
  0,80 eV ve dvou nezávislých studiích.
* Symetrický argument §5.1 — že kolineární antiferomagnet, jehož podmříže jsou
  spojené inverzí nebo translací, má spinově degenerované pásy, zatímco ten
  spojený rotací ne — je formulovaný správně a reference [7] je pro něj správná
  citace.
* Reference [3], Rao a spol. 2013, je správně identifikovaná jako to měření
  spinové kinetiky, které zakládá tripletový odtok.

## 2. 45,9 % je řádek dvoupřechodového tandemu

Abstrakt tvrdí, že architektura „elevates the single-junction thermodynamic
limit to 45.9 %", s citací reference [5]: M. C. Hanna a A. J. Nozik,
*J. Appl. Phys.* **100**, 074510 (2006).

Nejlepší, co tahle rodina modelů umí, při jakékoli dvojici energií vůbec a se
zdvojením tak dokonalým, jak jen singletní fise umí, je **42,09 %**. Při těch
dvou energiích, které preprint skutečně specifikuje, je to **41,24 %**. Takže
45,9 % není jen optimistické: je to nad stropem modelu, z něhož je to vzaté, a
žádná volba donoru ani akceptoru toho nedosáhne.

Odkud to je, se dá vidět ve zdroji. Abstrakt reference [5] uvádí:

| [5] uvádí | hodnota |
|---|---|
| jeden přechod, bez multiplikace | 33,7 % |
| jeden přechod, s multiplikací | 44,4 % |
| ideální **dvoupřechodový tandem**, bez a s CM absorbéry | **45,7 % → 47,7 %** |

45,9 % není řádek jednoho přechodu. Padá do rozsahu dvoupřechodového tandemu.
A hodnota pro jeden přechod je v citované práci 44,4 % pro *neomezenou*
multiplikaci; pro to zdvojení, které singletní fise skutečně dělá, uvádí táž
skupina 42,0 % — číslo reprodukované v §1 výš.

Tohle váží víc než obvyklý přepis, protože být jedním přechodem je celá prodejní
teze té architektury. §1 argumentuje proti III-V tandemům vyrobitelností; číslo
dovezené na to, aby je překonalo, je číslo tandemu.

## 3. Fotoproud: jeden kanál správně, druhý nad svým vlastním stropem

§6.2 píše J_sc jako dva integrály, uvádí pro každý kvantovou účinnost a pro
každý hlásí hodnotu. Oba integrály jsou v [`photocurrent.py`](photocurrent.py)
vyhodnocené proti skutečnému spektru s vlastními účinnostmi preprintu:

| kanál | publikováno | naměřeno |
|---|---|---|
| IR, 1,12–2,25 eV, při EQE = 0,85 | 28,5 | **28,89** |
| SF, nad 2,25 eV, při EQE = 1,53 | 23,8 | **14,95** |
| celkem J_sc, mA/cm² | 52,3 | **43,83** |

Infračervený kanál je správný na 1,3 %, což je v rámci přesnosti odečtení
spektra z grafu.

Vysokoenergetický kanál ne. Fotony nad 2,25 eV nesou **9,76 mA/cm²** náboje,
pokud každý jediný z nich dá jeden elektron. Dosáhnout 23,8 mA/cm² proto
vyžaduje

    EQE_high = 23,8 / 9,76 = 244 %,

tedy **2,44 elektronu na absorbovaný foton**. Singletní fise dává nejvýš dva.
Tvrzení překračuje strop svého vlastního mechanismu o 22 % a překračuje těch
153 %, které uvádí tatáž věta, o 59 %.

Ta aritmetika se dá zpětně dohledat: 23,8 mA/cm² při EQE_high = 1,53 je proud
všech fotonů nad **1,96 eV (634 nm)**, ne nad 2,25 eV / 551 nm, které tatáž
věta specifikuje — posun o 294 meV. Nad 2,25 eV leží ze spektra AM1.5G jen
9,8 mA/cm², a to je ta veličina, kterou architektura musí násobit.

Dotaženo do konce se publikovaný pracovní bod stává:

| | J_sc | PCE |
|---|---|---|
| jak publikováno | 52,30 | 35,58 % |
| s J_sc z vlastních účinností preprintu | **43,83** | **29,82 %** |
| s dokonalou fisí, přenosem a sběrem | 53,50 | 36,40 % |

Je tu jedna shoda, kterou je třeba vypíchnout, protože je to nejčistší vyjádření
toho, co ta architektura přináší a co ne. Obyčejný absorbér 1,12 eV s EQE = 1 a
vůbec bez fise sbírá **43,81 mA/cm²**. Celá kaskáda fise plus Dexter, při
vlastních kvantových účinnostech preprintu, vrací **43,83 mA/cm²** — totéž
číslo na 0,1 %. Ta multiplikace zaplatí za 0,85, za 0,92 a za 0,90, a nic víc.
Skutečný zisk té architektury proti křemíku není v proudu vůbec; je v tom, že se
ten proud sbírá při napětí daném pásem 1,12 eV, zatímco ty sběrné ztráty pohltí
zdvojení. To je opravdový a zajímavý výsledek — a není to výsledek, který ten
preprint tvrdí.

Dvě další kontroly pracovního bodu:

* **V_oc.** Radiační limit při E_g = 1,12 eV je **0,8782 V** pro obyčejný pás a
  **0,8834 V** se zdvojením. §6.2 uvádí 0,90 V, o 17 mV vyšší. Jeho 0,81 V pak
  plyne z jeho vlastních 0,90 V minus 0,09 V; z naměřeného limitu by to bylo
  0,793 V.
* **Neradiační ztráta.** Posun ΔV_oc,nr z 0,22 V, které §6.2 označuje za
  typické, na 0,09 V, které tvrdí, je podle reciprocitního vztahu
  ΔV_nr = −(kT/q) ln EQE_EL krokem v kvantové účinnosti elektroluminiscence
  z 1,9 × 10⁻⁴ na 3,0 × 10⁻², tedy **faktor 158**.

A pro měřítko, jak náročný je uvedený pracovní bod vzhledem ke svému vlastnímu
radiačnímu limitu:

| | podíl limitu |
|---|---|
| HOS-PV 2.0 proti naměřenému limitu | **86,3 %** |
| rekord c-Si proti Augerovu limitu | 92,9 % |
| nejlepší dnešní OPV proti Shockley-Queisserovi | 59,3 % |

Ta projekce žádá od neuspořádané organické směsi, aby dosáhla většího podílu
svého radiačního limitu než krystalický křemík za padesát let — a to z 59 %,
kde organika dnes stojí.

## 4. Spinový mechanismus: správná aritmetika, dva nekonzistentní vstupy

Výraz z §4.1 i jeho dopočítaná hodnota jsou správné, jak je uvedeno v §1.
Problém jsou vstupy a oba omyly jsou poučné.

**η_PB = 0,95 je nekonzistentní s jeho vlastními časy, a to v jeho prospěch.**
Ta sekce definuje η_PB = exp(−τ_ext/τ_s) a v téže větě uvádí τ_ext = 20–80 ns
a τ_s = 5 µs. Z těch hodnot vychází η_PB = 0,984 až 0,996, ne 0,95 — a tedy
potlačení **72,0 %**, ne 68,6 %. Uvedených 0,95 odpovídá τ_ext = 256 ns. Tahle
oprava výsledek preprintu zlepšuje a je tu zaznamenaná právě proto.

**Sám τ_ext je dán pohyblivostí, a preprint argumentuje oběma jejími konci.**
§4.1 definuje τ_ext = d²/(2 µ V_int). S aktivní vrstvou 220 nm z tabulky 1 je
doba přeletu taková, jakou ji udělá pohyblivost — a §1 uvádí organické směsi
jejich „low carrier mobilities" bez čísla. Proměřeno ([`spin.py`](spin.py)):

| µ (cm²/Vs) | τ_ext | η_PB | β_eff/β_L | potlačení |
|---|---|---|---|---|
| 1,0 × 10⁻⁴ | 3025 ns | 0,546 | 0,606 | **39,5 %** |
| 1,0 × 10⁻³ | 302 ns | 0,941 | 0,320 | 68,0 % |
| 1,0 × 10⁻² | 30 ns | 0,994 | 0,282 | **71,8 %** |

Uvedených 20–80 ns vyžaduje µ = 1,5 × 10⁻² až 3,8 × 10⁻³ cm²/Vs, tedy o jeden
až dva řády výš než neuspořádaná objemová heteropřechodová směs a na úrovni
nejlepších uspořádaných organických filmů nebo nad nimi. Na dolním konci
rozsahu je doba přeletu 3,0 µs, tedy srovnatelná s 5 µs spinové doby života,
ne zanedbatelná proti ní, a celý efekt klesá na 39,5 %. Rezerva toho
mechanismu, τ_ext ≪ τ_s, je reálná při vysoké pohyblivosti a zmizelá při
nízké — a preprint tvrdí ten horní konec, zatímco jeho úvod argumentuje tím
dolním.

**To potlačení se měří proti špatné základní linii.** §1 uvádí, že
nekorelovaná setkání tvoří 25 % singletů a 75 % tripletů; §4.1 tripletový kanál
blokuje. Když je tripletový kanál zablokovaný, zbývá singletní podíl,
β_eff = 0,250 β_L. Chirální výsledek §4.1 je 0,314 β_L — tedy *vyšší* z těch
dvou. Pokud se β_L nečte jako spinově slepý Langevinův koeficient — v kterémžto
případě by obyčejná achirální směs už měla ukazovat 0,250 — ten výraz
nezlepšuje statistiku, kterou nahrazuje. Vlastní reference [3] toho preprintu
je měřením právě téhle spinové kontroly v achirálních součástkách.

**P_CISS = tanh(ΔE/2kT) je testovatelný závazek.** Čtená, jak je napsaná, je ta
polarizace poměrem termálních populací, takže polarizace naměřená při 300 K
připíná rozštěpení: 0,75 potřebuje 50,0 meV, 0,85 potřebuje 64,5 meV, 0,90
potřebuje 75,7 meV. Při pevných 64,5 meV pak týž vzorec předpovídá teplotní
chování celého mechanismu — a solární článek neběží na 25 °C:

| T | P_CISS | potlačení |
|---|---|---|
| 0 °C | 0,879 | 72,7 % |
| 25 °C | 0,850 | 68,0 % |
| 45 °C | 0,827 | 64,3 % |
| 59 °C | 0,810 | 61,8 % |
| 85 °C | 0,780 | 57,3 % |

Je to falzifikovatelná předpověď a čistší experimentální signatura než srovnání
racemátu s homochirálním vzorkem, které navrhuje §7 — a doplňuje ji.

**ξ_SOC ∝ Z⁴ je zákon pro vodíkupodobný atom, ne pro valenci.** §1 zdůvodňuje
slabou spin-orbitální interakci uhlíku škálováním Z⁴. Z⁴ je škálování jemné
struktury pro elektron v neodstíněném jádrovém potenciálu; elektrony, které
v konjugovaném polymeru nesou spin, jsou odstíněné valenční p elektrony. Ten
exponent se dá změřit, protože rozštěpení základního termu halogenů je jedna
valenční np vrstva stupňovaná dolů sloupcem periodické tabulky (NIST ASD):

| | Z | ²P₃⁄₂–²P₁⁄₂ (cm⁻¹) |
|---|---|---|
| F | 9 | 404,141 |
| Cl | 17 | 882,352 |
| Br | 35 | 3685,24 |
| I | 53 | 7602,976 |

Metoda nejmenších kvadrátů na ln(rozštěpení) proti ln Z dává exponent **1,69**
(nejhorší reziduum 20 %, takže ta mocninná závislost je sama jen přibližná) —
tedy pod i tím Z², které přehledová literatura uvádí pro nejvnějšnější
elektrony, a daleko od 4. Od uhlíku k olovu dává naměřený trend pořád faktor
83, proti 187 pro Z² a 34 886 pro Z⁴. Výhoda uhlíku je reálná při každém
z nich. Špatná je jen její velikost a zákon, který se pro ni uvádí.

## 5. Materiály

**Fisní donor nesplňuje vlastní řazení preprintu.** §2.1 požaduje
E(S₁) ≥ 2E(T₁). §2.2 specifikuje E(S₁) = 2,25 eV a E(T₁) = 1,15 eV, takže
2E(T₁) = 2,30 eV a ta podmínka **padá o 50 meV** — fise, na níž stojí celá
architektura, je endotermická o 1,9 kT při 25 °C. Zbytek řetězu,
2E(T₁) ≥ 2E_g(IR), platí s rezervou 60 meV.

Endotermická fise sama není smrtelná; tetracen je endotermický a přesto
účinný. Ale §2.1 taky požaduje 1/k_SF pod 100 fs, a fise pod 100 fs je to, co
umí *exotermické* chromofory. Ty dva požadavky táhnou opačnými směry a ten
klinec je strukturální, ne přepsání. Řazení vyžaduje současně E(T₁) ≥ 1,12 eV
*a* E(S₁) ≥ 2E(T₁) ≥ 2,24 eV:

| | E(S₁) | E(T₁) | 2T₁−S₁ | T₁ ≥ 1,12? | S₁ ≥ 2T₁? |
|---|---|---|---|---|---|
| pentacen | 2,20 | 0,86 | −0,48 | **ne** | ano |
| tetracen | 2,32 | 1,25 | +0,18 | ano | **ne** |
| rubren | 2,21 | 1,14 | +0,07 | ano | **ne** |
| ten preprint | 2,25 | 1,15 | +0,05 | ano | **ne** |

Každý z těch tří proměřených chromoforů padá na jedné z těch dvou podmínek — a
padají na ní i vlastní čísla preprintu. Pentacen, ten, který fisuje za 80 fs,
má triplety na 0,86 eV a akceptor s 1,12 eV nemůže nakrmit vůbec. Rubren je
nejblíž a míjí o 70 meV. Donor jmenovaný v tabulce 1, TIPS-tetracen, je
tetracen: endotermický, pikosekundy. To okénko je úzké, ne prázdné — a nic
z preprintu v něm není proměřené.

**Vrstva 6 se uspořádává pod teplotou, na které článek běží.** Spinové
rozštěpení přisouzené altermagnetickému kolektoru je publikovaná hodnota (§1).
Co uvedené není, je, kde to přestává:

| | T (K) |
|---|---|
| Néelova teplota MnTe, naměřená | **267 – 307** |
| standardní testovací podmínky | 298,15 |
| typický NOCT modulu | 318,15 |
| naměřený NOCT, tenkovrstvý modul | 332,15 |
| horní kvalifikační hranice IEC 61215 | 358,15 |

Modul v provozu běží nad teplotou uspořádání MnTe podle obou publikovaných
hodnot. Při 332 K naměřených pro tenkovrstvý modul metodou IEC 61215 je ten
kolektor 25 až 65 K ve své paramagnetické fázi, kde je spinové rozštěpení,
pro které vrstva 6 existuje, nulové. I standardní testovací podmínky leží na
nebo nad nižší publikovanou hodnotou.

Alternativa jmenovaná jako první, RuO₂, má opačný problém: jeho teplota
uspořádání je výrazně nad pokojovou, ale jestli je vůbec magneticky
uspořádaný, je od roku 2024 předmětem sporu. Rotace spinu muonu a neutronová
difrakce kladou objemový moment pod 1,4 × 10⁻⁴ µ_B/Ru, přičemž nesouhlas
přichází z tenkých vrstev a povrchů — a to je forma, kterou tabulka 1
specifikuje, takže pro tenhle návrh je ta otázka otevřená, ne uzavřená proti
němu. Tak či tak, ty dva materiály nabídnuté pro vrstvu 6 jsou ten, o jehož
magnetismu se vede spor, a ten, který se uspořádává pod provozní teplotou
článku.

**Specifický výkon je 3,4× nižší.** Tabulka 2 tvrdí ≥ 10 000 W/kg. Tabulka 1
dává každou tlouštku kromě zadního reflektoru, který se proměřuje přes
100–200 nm, a plošná hmotnost z toho plyne ([`materials.py`](materials.py)):

| vrstva | g/m² | podíl |
|---|---|---|
| 1 substrát, 50 µm PEN | 68,000 | 56,3 % |
| 7 zapouzdření, 25 µm | 50,000 | 41,4 % |
| všechno ostatní | 2,84 | 2,3 % |
| **celkem** | **120,8** | |

Při uvedených 35,6 % je to **2944 W/kg** a přes všechny krajní kombinace těch
tří proměřovaných předpokladů 2815–3087 W/kg. Tvrzení je nižší o faktor
**3,4**. Těch 75 µm polymeru, které nedělají žádnou fyziku, je 97,7 %
hmotnosti; funkční část váží 2,84 g/m² a sama by dala přes 100 000 W/kg.
Dosáhnout 10 000 W/kg při uvedené účinnosti znamená celkem 35,6 g/m², což je
asi **19 µm** obalu, ne 75 µm. To číslo je dosažitelné pro samonosný
ultratenký článek — odkud taky hodnoty 5 000–10 000 W/kg v témž sloupci
pocházejí — ale ne pro stoh z tabulky 1.

**Vysoký proud utahuje rozpočet na sériový odpor.** Udržet uvedený FF na jeden
bod vyžaduje R_s pod **0,155 Ω·cm²** při 52,3 mA/cm², proti 0,189 Ω·cm² pro
křemíkový článek s 42,8 mA/cm² v téže tabulce — o 22 % utaženější, a to při
přidání chirální monovrstvy 1,5 nm a bariéry MgO 1,2 nm do série, které
křemíkový článek nemá. Nic tady neříká, že to nejde splnit; je to podmínka,
kterou preprint neuvádí.

## 6. Forma: tenhle deposit proti sérii

Měřeno v [`census.py`](census.py), tohle je první z osmnácti autorových
zenodových depositů, který neobsahuje nic ze slovníku, který ostatních
sedmnáct sdílí:

| | počet |
|---|---|
| tensor, Tensor Core | 0 |
| octonion, quaternion, sedenion, hypercomplex | 0 |
| non-associative, associator, zero divisor | 0 |
| causal, intensional | 0 |
| Maxwell | 0 |
| GPU, CUDA, RTX, clock cycle | 0 |
| Theory of Everything | 0 |
| Gemini | 0 |

Místo toho: spin 70, chiral 30, CISS 21, altermagnet 18, triplet 18, exciton
11, singlet fission 10, Dexter 10, AM1.5G 9. Hlavička PDF nenese nevyplněný
ORCID placeholder, který nese každý starší deposit; žádný spoluautor není
přiznán umělé inteligenci; nejsou tu žádné autocitace; a všech sedm referencí
je externích, skutečných a připnutých k tvrzením, která podpírají — což,
měřeno přes celou sérii v repozitáři
[`reference-audit`](../reference-audit), není
obvyklý stav.

Tohle je nejkonvenčněji postavený deposit z osmnácti. Jeho centrální chyba je
jiného druhu než obvyklá chyba série: ne tvrzení bez zdroje, ale správně
citovaný zdroj odečtený ze špatného řádku.

## 7. Táž veličina dvakrát

Nálezy v §§2–6 jsou dvojího druhu. Některé porovnávají tvrzení s vnějším světem:
se spektrem, s proměřeným chromoforem, s Néelovou teplotou, se sloupcem
periodické tabulky. Jiné ten dokument vůbec neopustí — veličina má na jednom
místě jednu hodnotu a na druhém jinou, nebo je hodnota uvedená ve větě, jejíž
vlastní ostatní čísla dávají jinou. [`consistency.py`](consistency.py) sbírá ten
druhý druh, protože k rozhodnutí nepotřebuje žádný model ani důvěru v žádný
zdroj: obě hodnoty jsou preprintu vlastní a aritmetika mezi nimi taky.

| veličina | uvedeno | co dávají jeho vlastní čísla | rozdíl |
|---|---|---|---|
| absorpční hrana fisního donoru | 2,25 eV (551 nm), §2.2 | **1,96 eV (634 nm)**, z jeho vlastních 23,8 mA/cm² při jeho vlastní EQE_high, §6.2 | **294 meV** |
| E(S₁) donoru | 2,25 eV, §2.2 | **aspoň 2,30 eV**, z E(S₁) ≥ 2E(T₁), §2.1 | 50 meV, 1,9 kT |
| elektronů na pohlcený foton | 1,53, napsáno „153 %“, §6.2 | **2,44**, z jeho vlastních 23,8 mA/cm² proti 9,76, které spektrum nad 2,25 eV nese | 59 % a **22 % nad stropem, který má fise sama — dva** |
| τ_ext | 20–80 ns, §4.1 | **256 ns**, z jeho vlastního η_PB = 0,95 přes jeho vlastní η_PB = exp(−τ_ext/τ_s) | ×3,2 až ×12,8 |
| η_PB | 0,95, §4.1 | **0,984–0,996**, ze dvou časů v té samé větě | 2,5 bodu potlačení |
| pohyblivost nosičů | „low carrier mobilities“, bez čísla, §1 preprintu | **3,8 × 10⁻³ až 1,5 × 10⁻² cm²/Vs**, z jeho vlastních 20–80 ns přes τ_ext = d²/(2μV) a 220 nm z tabulky 1 | jeden až dva řády |
| spinové rozštěpení, na němž mechanismus stojí | ~0,8 eV, tabulka 1; 0,5–1,0 eV, §5.1 | **64,5 meV**, z jeho vlastního P_CISS = 0,85 přes jeho vlastní P_CISS = tanh(ΔE/2kT) | **×12,4** |
| specifický výkon | aspoň 10 000 W/kg, tabulka 2 | **2944 W/kg**, z jeho vlastních sedmi tlouštěk při jeho vlastní PCE | ×3,4 |

Dva z těch osmi jsou v prospěch preprintu a zaznamenávají se proto, stejně jako
je zaznamenává §4: obě možná čtení páru η_PB / τ_ext potlačení zvyšují.

Když se ten samý test použije na každou další veličinu, kterou preprint uvádí
dvakrát, vyjde komplement — a má stejnou cenu jako tabulka výš:

| veličina | přepočteno | jak publikováno |
|---|---|---|
| EQE_high = 1,85 × 0,92 × 0,90 | 1,5318 | 153 % (§6.2) |
| 1 − η_PB P_CISS² | 0,3136 | 0,314 (§4.1) |
| potlačení, které z toho plyne | 68,6 % | 68,6 % (§4.1) |
| P_CISS dopočítaného příkladu | 0,85 | uvnitř 0,75–0,90 (§3.2) |
| rozštěpení z tabulky 1 | 0,8 eV | uvnitř 0,5–1,0 eV (§5.1) |
| V_oc = 0,90 V − 0,09 V | 0,81 V | 0,81 V (§6.2) |
| PCE = J_sc V_oc FF / P_in | 35,58 % | 35,58 % (§6.2) |
| 2E(T₁) ≥ 2E_g(IR), druhý článek řetězu | 2,30 ≥ 2,24 eV | požaduje §2.2 |

Osm z osmi. **Každý aritmetický krok, který ten preprint provede, provede
správně.** Všechny vzorce jsou standardní a správně upravené, jednotky souhlasí
a jediný součin provedený do konce — PCE v §6.2 — je přesný na čtyři cifry. Co
nesouhlasí, není nikdy algebra; jsou to vždycky čísla, která se do ní vloží, a
v šesti z osmi řádků výš leží ty dvě hodnoty v různých sekcích. Ten dokument
je lokálně v pořádku a globálně nekonzistentní.

**Jeden řádek není nekonzistence, ale vyloučení.** Ostatních sedm by se dalo
spravit tím, že se jedna z dvojice hodnot zvolí a druhá opraví. První ne,
protože termodynamické řazení, které si §2.2 sama stanoví,

    E(S₁_D) ≥ 2E(T₁_D) ≥ 2E_CT ≥ 2E_g(IR)

určuje, která z těch dvou hodnot je přípustná. 2E_g(IR) = 2,24 eV, takže ten
řetěz zakazuje jakýkoli donor, jehož S₁ leží níž — a hrana 1,96 eV, kterou
jeho vlastní fotoproud potřebuje, je **284 meV pod tím dnem**. Obráceně:
donor s E(S₁) = 1,96 eV smí mít E(T₁) nejvýš 0,98 eV, což je 142 meV *pod*
zakázaným pásem 1,12 eV toho akceptoru, který má krmit, takový Dexterův krok
z §2.2 by běžel do kopce a ta kaskáda by neexistovala.

Buď ten vysokoenergetický kanál nese 14,95 mA/cm² a ne 23,8, nebo je
energetická kaskáda, na které celá ta architektura stojí, termodynamicky
zakázaná. K tomuhle závěru není potřeba nic zvenčí toho preprintu.

## 8. Co se tady neměří

* Rychlost Dexterova přenosu. Výraz v §2.2 je standardní Dexterova forma; jestli
  je η_DET ≥ 0,90 dosažitelné při požadovaném R_DA < 1 nm a přitom s donorovými
  domény 5–10 nm, což je konkurence, kterou identifikuje fáze I v §7, je otázka
  morfologie a nemodeluje se tu.
* Jestli CISS umí polarizovat nosiče, aniž by zahodil odmítnutou spinovou
  populaci. §3.1 namítá proti elektrodovým spinovým filtrům právě to, že
  odrážejí polovinu proudu; jestli se chirální rozhraní v objemu vyhne vlastní
  námitce, je otázka o mechanismu, ne výpočet, a zůstává tu otevřená. Totéž
  platí pro zachování spinu v infračerveném kanálu, jehož nosiče vznikají ze
  singletních excitonů a nemohou tvořit páry |↑↑⟩ argumentem, který §4.1
  používá pro fisní kanál.
* Thomasův faktor. Spin-orbitální hamiltonián v §3.2 je napsaný
  s koeficientem eℏ/2m²c²; standardní redukce Diracovy rovnice dává eℏ/4m²c².
  Je to faktor dvě v členu, jehož velikost se nikde v preprintu numericky
  nepoužívá, takže to nic nemění a je to zaznamenané jen pro úplnost.
* Tunelová bariéra MgO 1,2 nm, nad rámec rozpočtu na sériový odpor v §5.
* Zkratový odpor, hustoty pastí a režim nízkého osvětlení z §4.2.
* Aplikace typu sonoluminiscence v tomhle depositu chybí; na rozdíl od
  starších zůstává celou dobu ve svém oboru.

## 9. Hranice tohoto vyhodnocení a tři chyby, které se v něm našly

Model detailní rovnováhy je standardní: jen radiační rekombinace, jednotková
absorptivita nad hranicí, bez sériového a zkratového odporu, emise z přední
strany s dokonalým zadním reflektorem a kvantový výtěžek vstupující do emise
stejně jako do absorpce. Dává tedy *stropy*. To nález §2 zesiluje, protože tam
tvrzení leží nad stropem, a v §1 to neoslabuje nic, protože tam se ten strop
reprodukuje proti třem publikovaným hodnotám.

Ty tři self-checky v §1 jsou v repozitáři právě proto a své místo si
vysloužily: první verze `detailed_balance.py` nechala Boseho faktor
divergovat, když chemický potenciál dosáhl energie fotonu, což vracelo
nekonečna a tiše proměnilo prohledávání účinností v nesmysl — 7 × 10¹² % při
„optimu" 1,52 eV. Tabulka self-checků to zachytila při prvním běhu, protože
Shockleyho-Queisserova hranice nevyšla 33,7 %. Argument je teď omezený na malou
pozitivní hodnotu a důvod je v komentáři v kódu.

Další dvě chyby v tomhle vyhodnocení, obě zachycené vytištěnými mezivýsledky,
ne čtením:

* `materials.py` počítal plošnou hmotnost s faktorem 10³ tam, kde 1 g/cm³ na
  metru tlouštky potřebuje 10⁶, což dávalo specifický výkon tři miliony W/kg,
  „zkrácení faktorem 0,0" a obalový rozpočet 10 588 µm. Tabulka vrstvu po
  vrstvě se tiskne, a ne jen celek, právě proto, aby takováhle chyba měla kde
  vylézt.
* `census.py` počítal jako referenci každý číslovaný seznam v těle textu a
  hlásil jich 25 místo 7. Teď počítá až za poslední hlavičkou „References".

Čtvrtá změna nebyla chyba: hledání V_oc bylo skalární bisekcí a celý skript
běžel 2 min 21 s, což je nahrazené třemi zjemněními vektorizovaného
64bodového intervalu a teď to trvá 8 s. Čísla jsou nezměněná.

Předpokládané hodnoty — rozsah pohyblivosti, vnitřní pole, objemový podíl
absorbéru, hustoty obalu, tlouštka zadního reflektoru — se
v [`constants.py`](constants.py) proměřují, ne tvrdí, a každý závěr výš je
uvedený přes celý rozsah každé z nich. Verdikty u referencí ostatních
sedmnácti depositů se tady neopakují; žijí
v [`reference-audit`](../reference-audit).

---

*Kód: MIT. Tento text: CC BY 4.0. Měření `karagos01`, 14. října 2026.*
