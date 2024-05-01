RHYODIN
=======
La quest consiste nel riportare nella dimensione reale la zona di Rhyodin.
In origine era necessario trovare una serie di oggetti per **Valik** al fine
di ottenere una chiave per aprire un portale, ora è possibile usare **doorbash** e
saltare questa parte. Vedi :doc:`/equipaggiamento/oggetti_rhyodin` per gli oggetti
che è possibile forgiare con gli ingredienti che si trovano in questa quest.

.. note::

    Prima di iniziare la quest guardare l'ora (``time``), tra le 22:00 e le 5:00
    ci sono i fantasmi ed è più pericoloso. Alle 5:00 i fantasmi si dissolvono
    *"nella luce del mattino"*

.. note::

    Durante l'ora dei fantasmi **Lattimore** si nasconde sotto il letto, è **hide**
    ne *Gli Alloggi Militari*, attenzione a non ucciderlo con attacchi ad area.
    Viene fuori alle 6:00 e si mette a dormire

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
* oggetti Ryhodin

Inizio
------
* ``astral;u;n;w;w;enter spe`` per arrivare al *Fiume delle Anime Perdute*
* ``w;w;w;u;w;w;s;w;w;s;s;s;e;e;push teschio``
* andare agli *Alloggi Militari*: ``s;e;s;w;u;e;n;n;e;e;e``
* qui dovrebbe esserci **Lattimore** che dorme. Dare 5 pagnotte a **Lattimore** e precederlo 
  in *Sala Riunioni*: ``w;w;w;s;s;w;u;n;e``
* aspettare **Lattimore** per ricevere la chiave
* | andare al *Portale d'ingresso*, dalla *Sala Riunioni*: ``w;s;d;e;n;n;e;e;s;s;e``
  | **NB** il path per il *Portale d'ingresso* dalla locazione dove si apre il teschio è: ``s;e;s;w;u;e;n;n;e;e;s;s;e``
* ``ulock ea;open ea;e;s;s;s`` fino a *I Cancelli di Rhyodin*
* invece di reperire gli oggetti da **Valik** è possibile fare ``doorbash so``
* ``s;pick bauletto;open bauletto;get all bauletto``, andare tutto a nord: ``run n`` e scavare: ``dig tunnel``
* ``n;n;unlock porta;open porta;w;get sigillo;e;n;n``
* a est c'è: *La grotta del terrore*, sbloccare magicamente ad est (**bacchetta di quercia**) e aprire

La Corsa per la Quest
---------------------
* andare a est, uccidere i MOB e raccogliere i **glifo di Interdizione** fino a trovarne uno **indistruttibile** (la chiave),
  attenzione, solo nel proprio inventario si vede la differenza, finchè non vengono raccolti tutti i glifi sembrano
  indistruttibili. Tra i vari scheletri guardiani c'è la **Regina degli Scheletri** che è più forte
* trovata la chiave andare a sud fino a un'uscita chiusa *In trappola!*: ``unlock so;open so;s``

Le Prime due Chiavi
-------------------
* scatta una teleport, poi ci si trova in un'area con molti mob e due locazioni *Il cumulo di ossa*, una a est una a ovest
  i cumuli sono le uniche stanze gain
* in particolare ci sono due MOB:

  - **Luogotenente Fantasma** ha la **chiave Spettrale**
  - **Generale Fantasma** ha la **chiave Eterea**

  uccidere i due MOB e recuperare le chiavi

* i guerrieri hanno addosso un **ectoplasma**, uno di questi contiene la **chiave Fantasma** che va recuperata, quando
  si droppa l'ectoplasma vuoto, questo scompare automaticamente, quindi si puo' usare la stringa
  ``open ecto;get all ecto;drop ecto``

La Tomba Nascosta del Generale
------------------------------
* andare nord del cumulo a est, c'è un passaggio segreto down
* ``unlock barriera; open barriera;d`` (serve **chiave Eterea**)
* ``unlock sarcofago; open sarcofago;get all sarcofago`` (serve **chiave Spettrale**) per ottenere **chiave ossea**

La Tomba Nascosta del Re
------------------------
* andare a west del cumulo a ovest: ``unlock coperchio;open coperchio;d;unlock barriera;open barriera``
* andare down: sconfiggerre **Re Fantasma** e **Regina Fantasma** (con 4x **guardia del corpo**) e prendere la
  **chiave distorta**

Una Intensa Luce
----------------
* ``unlock pulsante;open pulsante;down``
* aspettare la teleport: ``unlock forziere;open forziere;get all forziere;unlock scrigno;open scrigno;get all scrigno``
