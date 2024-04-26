Oggetti Accademia Astrale
=========================
Si dividono in due categorie: **SET** e **NOSET**. I pezzi **SET** fanno parte
di uno dei set dei piani (**Guaritore**, **Manipolatore**, **Difensore**
e **Distruttore**), hanno livello massimo 25 e se ne possono indossare fino
a 5. Inoltre indossando più pezzi di uno stesso set si ottengono bonus
speciali (vedi ``help set piani``), usando il comando ``info set`` si vede
quali di questi bonus sono attivi. I pezzi **NOSET** hanno un cap al livello
che può essere alzato fino a 20 usando i **frammenti entropici** e
fino a 25 usando i **frammenti entropici maggiori**, l'operazione costa
**ethereum**, consultare :doc:`/accademia_astrale` per i dettagli.
Tutti gli slot seguono la seguente tabella di evoluzione, a seconda
del livello di infusione, vedi ``help infusione``:

======= ===  ======= ====== === === ====== === ==== ====
Livello AC   HP/Mana SP/DAM Red HIT Ea/Foc TS  SF   Reg
======= ===  ======= ====== === === ====== === ==== ====
 1      5    20      1      1   1   1      -2  -4   0
 2      5    22      1      1   1   1      -2  -4   2 
 3      6    24      1      1   1   1      -2  -6   2
 4      6    26      1      1   1   2      -3  -6   4
 5      7    28      2      1   2   2      -3  -10  4
 6      7    30      2      1   2   2      -3  -10  6
 7      8    32      2      1   2   3      -4  -10  6
 8      8    34      2      1   3   3      -4  -14  8
 9      9    36      2      1   3   3      -5  -14  8
10      9    38      2      1   3   3      -5  -14  10
11      9    40      2      1   4   4      -6  -18  12
12      10   42      2      2   4   4      -6  -18  14 
13      10   44      2      2   5   5      -7  -18  18 
14      10   46      3      2   5   5      -7  -22  22
15      11   48      3      2   5   5      -7  -22  26
16      11   52      3      2   6   6      -8  -22  30
17      11   56      3      2   6   6      -8  -26  34
18      12   60      4      3   6   7      -8  -26  38
19      12   64      4      3   7   7      -9  -26  42
20      12   70      4      3   7   8      -9  -30  46
21      13   80      5      4   8   10     -10 -30  50
22      14   90      5      4   9   12     -12 -45  54
23      15   100     6      5   9   14     -14 -45  58
24      16   110     6      5   10  16     -16 -45  60
25      20   130     7      6   12  18     -20 -60  70
======= ===  ======= ====== === === ====== === ==== ====

.. note::

   I pezzi tank (set Difensore e oggetti di ferro) hanno un bonus del
   75% ai punti ferita, quindi il massimo al 25° livello è **227 HP**

Il livello di rarità di tutti gli oggetti (**SET** e **NOSET**) dipende dal livello,
secondo la seguente tabella:

======== ==========  ============
Livello  Rarità      Punti Rarità
======== ==========  ============
1-10     COMUNE      0
11-15    NON COMUNE  1
16-20    RARO        2
21-25    RELIQUIA    3
======== ==========  ============

.. note::

   La key ``pendente`` è usata sia per alcuni orecchini (per esempio ``pendente-oro``),
   sia per alcune collane (per esempio ``pendente-argento``), attenzione a non spendere
   risorse in un pezzo che non si può indossare!

Set Guaritore dei Piani
-----------------------

============ ==== ====== ==== ====== ======== ======= ======= ====
Pezzo        HP   HIT    Mana HP Reg Mana Reg SP      Focus   TS
============ ==== ====== ==== ====== ======== ======= ======= ====
elmo         130                     70       7       18%     -20
occhio       130         130                  7       18%     -20
spallacci                130                  **14**  18%     -20
cintura      130  12                          7       18%     -20
stivali      130                              7       **36%** -20
orecchino                     70     70       7       18%     -20
============ ==== ====== ==== ====== ======== ======= ======= ====

Set Manipolatore dei Piani
--------------------------

============ ==== ====== ==== ====== ======== ======= ======= ====
Pezzo        HP   HIT    Mana HP Reg Mana Reg SP      Focus   TS
============ ==== ====== ==== ====== ======== ======= ======= ====
elmo              12                 70       7       18%     -20
occhio       130  **24**                      7               -20
spallacci    130  12                          7       18%     -20
mantello     130  12                          7       18%     -20
stivali           12     130                  **14**          -20
paraschiena                   70     70       7       18%     -20
============ ==== ====== ==== ====== ======== ======= ======= ====

Set Difensore dei Piani
-----------------------

============ ==== ====== ====== ====== ===== ===== ======= ======= ====
Pezzo        HP   HIT    HP Reg redBL  redSL redPR DAM     ExAtt   TS
============ ==== ====== ====== ====== ===== ===== ======= ======= ====
elmo                            
occhio       227                6            6     7               -20
gambali                  70     6      6     6                     -20
mantello     227                       6     6     7               -20
stivali 
pavese       227                **12**             7               -20 
============ ==== ====== ====== ====== ===== ===== ======= ======= ====

Set Distruttore dei Piani
-------------------------

============ ==== ====== ====== ====== ===== ===== ======= ======= ====
Pezzo        HP   HIT    HP Reg redBL  redSL redPR DAM     ExAtt   TS
============ ==== ====== ====== ====== ===== ===== ======= ======= ====
orecchino    130  12                               7       18%     -20                             
============ ==== ====== ====== ====== ===== ===== ======= ======= ====

NOSET Equivalenti
-----------------
Alcuni oggetti NOSET hanno le stesse caratteristiche di corrispettivi pezzi SET,
ecco la tabella:

================ ============= =======================
Pezzo SET        Set           Pezzo NOSET Equivalente
================ ============= =======================
cintura          guaritore     cintura stoffa
================ ============= =======================

NOSET Unici
-----------
Pezzi **NOSET** per cui non c'è un corrispettivo **SET**. Alcuni oggetti
con nome diverse si equivalgono (per esempio maschera e occhiali):

* | Oggetto '**pendente oro**', Tipo: ARMATURA
  | Oggetto '**gioiello oro**', Tipo: ARMATURA
  | L'oggetto e`: RESISTENTE NO-EDIT 
  | Puo' essere indossato su : INVENTARIO PERSONAL-EQ ORECCHIO 

  1. HP (max 130)
  2. mana (max 130)
  3. SP (max 7)
  4. HIT (max 12)
  5. TS (max -20)

* | Oggetto '**scudo dei passati**', Tipo: ARMATURA
  | L'oggetto e`: RESISTENTE NO-EDIT 
  | Puo' essere indossato su : INVENTARIO PERSONAL-EQ SCHIENA 

  1. mana (max 130)
  2. SP (max 7)
  3. SP (max 7)
  4. SP (max 7)
  5. TS (max -20)

* | Oggetto '**maschera argento**', Tipo: ARMATURA
  | Oggetto '**occhiali argento**', Tipo: ARMATURA
  | L'oggetto e`: RESISTENTE NO-EDIT 
  | Puo' essere indossato su : INVENTARIO PERSONAL-EQ OCCHI 

  1. HP (max 130)
  2. SP (max 7)
  3. focus (max 18)
  4. focus (max 18)
  5. TS (max -20)

* | Oggetto '**maschera oro**', Tipo: ARMATURA
  | Oggetto '**occhiali oro**', Tipo: ARMATURA
  | L'oggetto e`: RESISTENTE NO-EDIT 
  | Puo' essere indossato su : INVENTARIO PERSONAL-EQ OCCHI 

  1. HP (max 130)
  2. SP (max 7)
  3. SP (max 7)
  4. HIT (max 12)
  5. TS (max -20)
