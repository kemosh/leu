Oggetti Invasioni
=================

Cristalli
---------
I cristalli possono essere applicati su tutti gli oggetti NOEDIT, ecco gli effetti:

.. table::
   :align: left
   :widths: auto

   ============================ ================= =======
   Cristallo                    Effetto           Max                                    
   ============================ ================= =======
   affilato                     +1 HIT            +2
   appuntito                    +1 DAM            +1
   luminoso                     +1 SP             +1
   frastagliato                 +1 HIT&DAM        +1
   brillante                    +1 HIT&SP         +1
   rigenerante                  +4 hit regain     +20
   flessibile                   +2 mana regain    +10
   irrequieto                   +1 extra attack   +3
   concentrato                  +1 focus          +3
   tagliente                    +1 redu slash     +2
   pungente                     +1 redu pierce    +2
   contundente                  +1 redu blunt     +2
   fluorescente                 +6 mana           +30
   robusto                      +5 HP             +45
   ============================ ================= =======

.. note::

   Se un oggetto ha più slot dello stesso tipo, il cristallo sarà applicato solo
   al primo slot. Quindi, in questo senso, è più conveniente avere oggetti con
   slot diversi. Se si usa un cristallo su un oggetto con uno slot libero e il
   cristallo è di un tipo diverso dagli effetti negli slot occupati, allora il
   bonus andrà nel primo slot libero.

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

Si hanno a disposizione **4 reroll gratis**, poi ogni ulteriore reroll avrà un costo
di **25K eth**. Per effettuare il reroll basta consegnare l'oggetto **Vitalik**,
è possibile **bloccare** alcuni slot, facendo il reroll solo degli altri, ma
questo avrà un costo di un **monile triangolare dorato** per ogni slot che si vuole
fissare e va fatto prima di ogni reroll. Il comando è: ``use monile OGGETTO SLOT`` con
``SLOT = 2, ..., 5``, dato che il primo slot è fisso.
