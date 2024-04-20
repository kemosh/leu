Evoluzione del Personaggio
==========================

Primi Passi
-----------

* XP per raggiungere il livello 50

* reincarnazione: è possibile reincarnarsi in ul altra razza per ottenere 
  abilità, resistenze e immunità, consulta l'help per i dettagli. Per reincarnarni
  è necessarion procurarsi un **cristallo della forma** e darlo a un MOB, specifico
  per ogni razza:

  * **spettro**: consegnare il cristallo a uno ``spettro-anello``, è portalabile

* aumentare la statistiche naturali: è necessario un cristallo specifico per ogni
  statistica. I cristalli possono essere comprati ad Allania e lo stesso vale per il
  servizio di icremento statistica

* **edit** e **over edit** sul personaggio: costano **gemme**, possono essere fatti ad Allania,
  usare i comandi ``showres`` e ``showedit`` per verificare lo stato

* **edit leggendari**: come i precedenti ma costano **gemme** e **lingotti**, andranno
  fatti mano a mano che si trovano i lingotti

Equipaggiamento Accademia Astrale
---------------------------------
Con i dungeon è possibile procursi equipaggiamento di ottima qualità che può essere potenziato
usando **astralite**

Scintilla
---------
Oggetto molto potente che può essere comprato con le gemme. Vedi ``help scintilla``

Cozza
-----
Con 10 **scaglie di drago** è possibile comprare un'armatura con **resistenza all'impatto**.
Spendendo altri ingredienti è possibile potenziarla fino a una versione che ha rarità **COMUNE**

Guanti degli Inferi
-------------------
Con 10 **artigli del diavolo**

Edit
----
Oggetti come l'armatura o i guanti sono editabili, è possibile andare da i mob di *Allania* per
mettere vari effetti sugli slot liberi

Edit Leggendari
---------------
E' possibile potenziare armatura e guanti con edit speciali che costano **gemme**, **mdc** e
**lingotti**.

* ``help leggendari minori``
* ``help leggendari superiori``

Cristalli
---------
I cristalli possono essere applicati su tutti gli oggetti NOEDIT, ecco gli effetti:

.. table::
   :align: left
   :widths: auto

   ============================ ================= =======
   Cristallo                    Effetto           Max                                    
   ============================ ================= =======
   flessibile                   +2 mana regain    +10
   tagliente                    +1 redu slash     +2
   brillante                    +1 HIT&SP         +1
   concentrato                  +1 focus          +3
   fluorescente                 +6 mana           +30
   frastagliato                 +1 HIT&DAM        +1
   pungente                     +1 redu pierce    +2
   luminoso                     +1 SP             +1
   affilato                     +1 HIT            +2
   appuntito                    +1 DAM            +1
   contundente                  +1 redu blunt     +2
   irrequieto                   +1 extra attack   +3
   rigenerante                  +4 hit regain     +20
   robusto                      +5 HP             +45
   ============================ ================= =======

Simboli e Armi Invasioni
------------------------
Possono essere forgiati da Thor con **sfere colorate**, **monili** e **ethereum**.
Ecco le ricette:

.. table::
   :align: left
   :widths: auto

   =========================== ======== ================================
   Oggetto                     Monili   Sfere
   =========================== ======== ================================
   Simbolo Benem (caster)      3        4 amaranto, 2 smeraldo
   Simbolo Hansolo (tank)      3        4 indaco, 2 ambra
   Moonshatter (arma caster)   3        3 ambra, 1 smeralo, 2 indaco
   Moonschyte (arma slash)     3        3 amaranto, 2 smeraldo, 1 indaco
   Moonthunder (arma blunt)    3        3 indaco, 2 amaranto, 1 ambra
   Moonspear (arma pierce)     3        3 smeraldo, 2 ambra, 1 amaranto
   =========================== ======== ================================

Hanno uno slot fisso e gli altri slot random, sia come tipologia che come valore,
ecco i possibili slot e valori:

.. table::
   :align: left
   :widths: auto

   ============================ ========== ==========
   Slot                         Min        Max                                    
   ============================ ========== ==========
   HIT&DAM                      2          4
   HIT&SP                       2          4
   MANA                         20         40
   MANA REGAIN                  15         30
   HITROLL                      3          6
   SPELL POWER                  2          5
   DAMROLL                      2          5
   HIT POINTS                   60         100
   REDUCTION BLUNT              2          4
   REDUCTION PIERCE             2          4
   REDUCTION SLASH              2          4
   EXTRA ATTACK                 6          15
   SPELL FOCUS                  6          15
   SPELL FAIL                   -20        -60      
   ============================ ========== ==========

Si hanno a disposizione un numero limitato di reroll gratis, poi il reroll avrà un costo
incrementale fino a un max di **25K eth**. Per effettuare il reroll basta consegnare
l'oggetto **Vitalik**, è possibile fissare alcuni slot, rirollando solo gli altri, ma
questo avrà un costo di un **monile triangolare dorato** per ogni slot che si vuole
fissare, va fatto ad ogni reroll. Il comando è: ``use monile OGGETTO SLOT`` con
``SLOT = 2, ..., 5``, dato che il primo slot è fisso.
