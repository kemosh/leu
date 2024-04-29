RHYODIN
=======
La quest consiste nel riportare nella dimensione reale la zona di Rhyodin.
In origine era necessario trovare una serie di oggetti per **Valik** al fine
di ottenere una chiave per aprire un portale, ora è possibile usare **doorbash** e
saltare questa parte.

.. note::

    Prima di iniziare la quest guardare l'ora (``time``), tra le 22:00 e le 5:00
    ci sono i fantasmi ed è più pericoloso.

Requisiti
---------
* **doorbash**
* **picklock**
* **pala** o oggetto/arma con flag **dig**
* **bachetta di quercia** o altro metodo di sblocco magico
* 5x **pagnotta** da dare a **Latimore**

Premi
-----
* **400 eth**
* ingredienti per equipaggiamento Rhyodin

Inizio
------
* ``astral;u;n;w;w;enter spe`` per arrivare al *Fiume delle Anime Perdute*
* ``w;w;w;u;w;w;s;w;w;s;s;s;e;e;push teschio``
* andare agli *Alloggi Militari*: ``s;e;s;w;u;e;n;n;e;e;e``
* qui dovrebbe esserci **Lattimore** che dorme. Seguire **Lattimore** e dargli 5 pagnotte
* lattimore si muoverà fino alla *Sala Riuninoni* e consegnerà una chiave (si sposterà w;w;w;s;s;w;u;n;e)
* | andare al *Portale d'ingresso*, dalla *Sala Riunioni*: ``w;s;d;e;n;n;e;e;s;s;e``
  | **NB** il path per il *Portale d'ingresso* dalla locazione dove si apre il teschio è: ``s;e;s;w;u;e;n;n;e;e;s;s;e``
* ``ulock ea;open ea;e;s;s;s`` fino a *I Cancelli di Rhyodin*
* invece di reperire gli oggetti da **Valik** è possibile fare ``doorbash so``
* ``s;picklock bauletto;get all bauletto``, andare tutto a nord: ``run n`` e scavare: ``dig tunnel``
* ``n;n;unlock porta;open porta;w;get sigillo;e;n;n``
* a est c'è: *La grotta del terrore*, sbloccare magicamente ad est (**bacchetta di quercia**) e aprire

La Corsa per la Quest
---------------------
* andare a est, uccidere i MOB e raccogliere i **glifo di Interdizione** fino a trovarne uno **indistruttibile** (la chiave)
* trovata la chiave andare a sud fino a un'uscita chiusa *In trappola!*: ``unlock so;open so;s``

Le Prime due Chiavi
-------------------
* scatta una teleport, poi ci si trova in un'area con molti mob e due locazioni *Il cumulo di ossa*, una a est una a ovest
  i cumuli sono le uniche stanze gain
* in particolare ci sono due MOB:

  - **Luogotenente Fantasma**
  - **Generale Fantasma**

  uccidere il **Generale Fantasma** e recuperare la **chiave Eterea** dal suo corpo

* i guerrieri hanno addosso un **ectoplasma**, uno di questi contiene la **chiave Fantasma** che va recuperata


La Tomba Nascosta del Generale
------------------------------
* andare nord del cumulo a est, c'è un passaggio segreto down
* usare la **chiave Eterea** per aprire il sarcofago: ``unlock sarcofago;open sarcofago``

La Tomba Nascosta del Re
------------------------
* andare a west del cumulo a ovest: ``unlock coperchio;open coperchio;unlock barriera;open barriera``
* andare down: sconfiggerre **Re Fantasma** e **Regina Fantasma** (con 4x **guardia del corpo**) e prendere la
  **chiave distorta** e la **chiave spettrale**
* aprire usando la chiave trovata nel sarcofago: ``unlock pulsante;open pulsante``
