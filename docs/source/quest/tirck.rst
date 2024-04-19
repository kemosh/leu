TIRCK
=====
La quest consiste nel trovare 4 cubetti colorati per aprire una serie di porte
e raggiungere *La Cupola*. Qui si dovranno affrontare una serie di mob:
**mano gigante**, **occhio gigante** e **cervello gigante** che rappresentano gli
attributi che servono a un mago e hanno un totale di 6 **frammento di mithril**
che servono per comporre una chiave (**piramide di mithril**).

Requisiti
---------

* **pick lock**
* **pala** o arma/oggetto con flag **dig**
* **falcetto** o arma/oggetto con flag **cut**

Premi
-----
* oggetti vendibili per un totale di 200-250 mdc
* lingotti: soprattutto fasce B, C, meno probabili D, E, frammenti A sui mob 
* sacchetti: fino a **oro**
* sesterzio di bronzo

Inizio
------
Si trova a nord di Talonia (dal centro della piazza andare tutto North, arrivati 
alla prateria cercare la locazione con la P grande e proseguire verso quell’uscita. 
Fare lift ramo e proseguire verso .2n push cancello .4ws), ma ci si può arrivare
anche portalando su **Cane Briciola**.

- portal cane-briciola
- andare nella *Scuola di Tirck*: ``e;open south;s``
- impugnare la pala: ``turn tempo;d;dig passaggio;d``
- uccidere il **Guardiano**
- ``get armatura guardiano;unlock down;open down;d;d``

Cubetto GIALLO
--------------
- da dove scendi (guardiano) vai down fino a *Un corridoio di marmo*
- ``n;w;n;n;pull natura;w``
- scassina nord e poi: ``n;get cubetto buchetto``
- torna al corridoio principale: ``s;e;s;s;e;s``

Cubetto BLU
-----------
- vai alla stanza prima dell'ingresso dell bibliotece: ``n;run w;e``
- ``unlock s;s;kill topo-biblio;get all.chiav cad``
- ``open imbottitura;get cubetto imbottitura``
- ``s;unlock ea;unlock we;open we;w;get chiave gancio;unlock w;open w;w;open m3415;get chiav m3415;e;e;n``
- torna al corridoio principale: ``n``

Cubetto ROSSO
-------------
Attenzione alla **Matrice di Evocazione** ne *La sala di evocazione*,
se si viene presi mentre si passa la matrice inizierà a evocare mob.

- vai tutto west
- ``unlock n;open n;n;get chiave disco;unlock passaggio;open passaggio``
- impugnare il falcetto, la prossima stringa tenterà di saltare la
  **Matrice di Evocazione**
- ``n;cut nebbia;turn vortice;d;get cube ucis;u;u``
- ``s;e;e;n;open alchimia;n;e``

Cubetto VERDE
-------------
- pick/doorbash nord, vai a nord e uccidi grosso fantasma
- ``pull cordicella;w;open luce;w;get cubetto mensola``
- ``e;e;s;w;unlock serratura;open serratura;w``
- ``unlock no;open no;n``
- ``unlock ea;open ea;e``
- ``unlock so;open so;s``
- ``unlock we;open we;w``

Cupola
------
Si parte dalla *Cupola* che è una stanza safe, è possibile tornare alla Cupola
da qualunque locazione con: ``run s;run e;n;e``

- cercarere 6 **frammenti di mithril** procedendo per colonne (w, tutto sud o
  nord, ancora w e tutto nord o sud, etc), uccidendo i mob e recuperando i 
  frammenti dai cadaveri
- tornare alla *Cupola*: ``run s;run e;n;e``

Stanza Finale con Premio
------------------------
- ``w;w;w;lift occhi;u``
- ``join framm-occhio framm-mano``
- ``join framm-mano framm-cervello``
- ``join framm-cervello framm-occhio``
- ``join piramide 2.piramide 3.piramide``
- ``unlock baule;open baule``

Uscita
------
- impugnare la pala
- ``d;s;u;u;dig parete;w;dig passaggio;u;turn stalla;n``