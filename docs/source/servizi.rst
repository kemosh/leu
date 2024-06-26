Servizi
=======

Rent
----
Ogni personoggio deve affittare una camera e pagare l'affitto. L'affitto base è fissato a 10 monete d'oro 
al giorno (tempo reale), alcuni oggetti hanno un costo di rent ed incrementato il conto, alcuni oggetti
sono **NORENT** e scompariranno dall'inventario del personaggio in caso di disconnessione per un tempo
prolungato. **Giulietta** offre questo servizio ad Alma, presso la *Reception* della *Taberna Viatoris*,
ma non è l'unica.

- preventivo: ``offer``
- affitta camera: ``rent``

Banca
-----
Qui è possibile depositare soldi e ingredienti:

- path da *Alma Civitas*: ``s;e;e;e;s``
- bilancio: ``balance``
- deposita: ``deposit``
- ritira: ``withdraw``
- visualizza cassetta (ingredienti): ``cassetta`` oppure ``cassetta NUMERO`` 
  per una specifica pagina, con ``NUMERO = 1, ..., 5``

Bottega dei Ricordi perduti
---------------------------
È fatta da 3 stanze, nella prima c'è il venditore/rottamatore **Hamlin** e l'assicuratore **lloyd**,
nelle altre 2 stanze i venditori **Triddit** e **Linette**. Dando un oggetto all'assicuratore è
possibile abilitare/disabilitare la protezione contro transizioni involontarie. Qui è possibile
comprare ``spada-coraggio``, ``martello-coraggio``, ``anello-coraggio`` e ``baule-eroe``,
molto utili nelle fasi iniziali:

- path da *Alma Civitas*: ``s;s;e;e;s;s;open we;w``

Maestri Abilità Secondarie
--------------------------
Insegnano abilità secondarie comuni a tutte le classi, molti sono raggiunginili tramite portal
e la key è tra parentesi:

- **Maestro Ninja** (``maestro-ninja``):

  - cavalcare
  - sfondare porte
  - scassinare
  - spy

- **Marinaio di Alma** (``marinaio-alma``):

  - nuotare

- **Cacciatore** (``cacciatore``)

  - cacciare
  - primo soccorso

- **Occhio di Falco** (``occhio-falco``):

  - spot

- **Saggio di Mordilnia** (``11.saggio``):

  - cerca
  - leggere il magico
  - linguaggio dei segni
  - linguaggi vari
  - lore
 
Maestri Gilde
-------------
In *Via delle Gilde* si trovano i maestri per i bassi livelli. Altri maestri di alto livello:

* **Grenetta** per i maghi: ``astral u;n;w;n;enter spe;n;n;e;e;d;s;s;s;s;w;w;w;w;n;n;open w;w;open d;d;open d;d;open ea;e;s;s;e;e;e;open s;s``
* **Ibn Sina** per i chierici: ``astral n;u;u;n;w;w;n;u;enter spe;e;n;e;s;u;e;e;d;w``

Identificazione Equipaggiamento
-------------------------------
Questo servizio è offerto ad Alma da **Gnosh**.

* path da *Alma Civitas*: ``s;e;e;s;s``
* comando: ``give OGGETTO gnosh``

Riparazione Equipaggiamento
---------------------------

* path per **Iwaldur** da *Alma Civitas* (oggetti di basso livello):
  ``s;e;e;n``
* path per **Plutarco** da *Alma Civitas* (ripara tutto):
  
  - andata: ``astral;u;n;w;w;n;u;w;u;u;enter spe;e;d;d;d;n;n;e;e;e;u;u;open masso;e;e;n;e;s;d;d;w;w``
  - ritorno: ``e;e;n``

.. _locate_object:

Localizzazione Oggetti
----------------------
**Ekkhae, la gitana** offre il servizio di **locate object**:

* path da *Alma Civitas*: ``s;s;e;e;e``
* comando: ``whisper gitana OGGETTO``

Localizzazione Lingotti
-----------------------
I lingotti (incluse le pietre) si trovano nei tesori delle quest e in alcune
**scatole nere laccate** che appaiono a caso addosso ad alcuni mob. È possibile
individuare quali mob hanno la scatola chidendo al **vacchietto**:

* path da *Alma Civitas*: ``s;s;e;e;s``
* comando: ``ask vecchietto ingredienti``

Allania
-------
Allania offre diversi servizi di edit sul personaggio e sugli oggetti, inoltre
è possibile comprare oggetti quest, ingredienti e fare varie conversioni.

* path per andare e tornare da *Un'intersezione tra le gallerie*:

  - andata: ``astral;u;n;w;w;n;u;w;u;u;w;d;w;s;s;s;s;w;w;w;w;d;d``
  - ritorno: ``w;s;s;e;s;enter portale``

* per esaminare i servizi, una volta arrivati a *Un'intersezione tra le gallerie*:
  ``exa NUMERO``, con ``NUMERO = prima, ..., quinta``

Path per i venditori (``exa NUMERO``) relativi a *Un'intersezione tra le gallerie*:

* path per **Tarr** (vende il **cristallo della crono-traslazione**):

  - andata: ``n;e;e;n;u;u;e;e;e;n``
  - ritorno: ``s;w;w;w;d;d;s;w;w;s``

* path per **Arren** (oggetti *Ravenloft*): 

  - andata: ``n;e;e;n;u;u;e;e;n``
  - ritorno: ``s;w;w;d;d;s;w;w;s``

* path per **Ulrick** (oggetti *Abisso*): 

  - andata: ``n;e;e;n;u;u;e;e;s``
  - ritorno: ``n;w;w;d;d;s;w;w;s``

* path per **Grok** (oggetti *Bosco Verde*):

  - andtata: n;e;e;n;u;u;e;n
  - ritorno: s;w;d;d;s;w;w;s

* path per **Kallia** (oggetti *El Quebbar*):

  - andata: ``n;e;e;n;u;u;e;e;e;e``
  - ritorno: ``w;w;w;w;d;d;s;w;w;s``

* path per **Silvius** (conversione lingotti, vedi ``help conversione ingredienti``):

  - andata: ``n;e;e;n;u;u;e;e;e;s``
  - ritorno: ``n;w;w;w;d;d;;s;w;w;s``

* path per **Viaggiatori** (oggetti **leggentari superiori**), bisogna avere il
  **cristallo della cronotraslazione** in inventario per sbloccare la parete:

  - andata: ``n;e;e;n;u;u;e;e;e;e;unlock parete;twist parete;e``
  - ritorno: ``enter realta;w;w;w;w;d;d;s;w;w;s``

.. note::

   Per comprare gli oggetti dai **Viaggiatori** è necessario avere un
   **cristallo della cronotraslazione** in inventario che verrà 
   consumato durante l'acquisto

.. note::
   
   È possibile chiedere ai venditori di identificare gli oggetti prima di comprarli
   con il comando: ``ask MOB identifica NUMERO``, dove ``NUMERO`` è il numero
   associato all'oggetto, mostrato dal comando ``list``. Il numero può essere
   usato anche in fase di acquisto con: ``buy NUMERO``. I venditori di vecchia
   concezione potrebbero non supportare questa funzionalità.

Pick Lock
---------
Comprare la **bacchetta di quercia** da **Elvira** al costo di 28750 monete d'oro

* path per **Elvira**: ``portal turista;e;n``

Disarm Traps
------------
Bisogna prima essere in grado di individuare le trappole e poi poterle disarmare,
servono 2 oggetti:

* **pergamena translucida**, da recitare per individuare il nome della trappola
  
  - path per venditore, da *Allania*: ``...``
  
* **attrezzi da scasso**, per disarmare, il disarm costa 5000 monete d'oro e lagga

  - path per venditore (**Heimslan** a *Mordilnia*): ``portal 11.saggio;w;w;w;w;;s;e``
  - gli attrezzi da scasso hanno un costo di rent non riducibile di 500 monete d'oro

Sanctuary
---------
È molto importante avere a disposizione l'incantesimo **sanctuary** anche se non fa
parte delle abilità della propria classe, ecco come procurarselo:

* **Scettro di Ravenloft**, ha 6 cariche e quando usato lancia sanctuary su tutti i
  presenti. Costa **350 mdc** e, una volta scarico, può essere rivenduto per **70 mdc**.
  Può essere comprato ad *Allania* da **Arren**

* **Scudo di Silver**, lancia sanctuary a piacere, ha un cooldown di 2 round:

  - andare ad **Allania** e poi dai **Viaggiatori**, andare 2 volte a nord
  - comprare lo scudo e indossarlo
  - usare il comando: ``silver``
  - per costo e dettagli: ``help scudi supremi``


Astral e Portal
---------------
Sono due metodi di viaggio veloce, questi servizi sono offerti da **Zryon** nella
*Gilda dei Viaggiatori*:

- path da *Alma Civitas*: ``s;s;e;e;n``
- astral: ``ask Zryon astral``
- portal: ``ask Zryon portal nome_mob``

Aviani Elfici
-------------
È un metodo di trasporto, si aspettano gli aviani, si sale e si scende alla fermata
desiderata.

- path da *Alma Civitas*: ``s;e;e;e;e;e;e;e;s;u``

.. _forgia_di_thor:

Thor: la Forgia degli Dei
-------------------------
Nella forgia di **Thor** è possibile creare vari oggetti. Come raggiungere la forgia:

- portal ``topo-deserto`` e down fino a *Alla base della Piramide*
- ``n;n;n;e;e;e;e;e;u;u;u;e;d;e;e``
- uccidere **RockHound** e poi ``get chiave-pietra cad``
- ``unlock fessura;open fessura;e;pull stalagmite;n``
- attendere teleport
- ``say raido``

A questo punto ci si trova davanti a **Thor**, per il processo di creazione:

- ``ask thor sfere``, **Thor** dirà di mettere le sfere nella ``fornace``
- mettere gli ingredienti nella ``fornace``
- ``nod thor``

Per gli oggetti che si possono forgiare vedi:

- :doc:`equipaggiamento/oggetti_drow`
- :doc:`equipaggiamento/oggetti_rhyodin`
- :doc:`equipaggiamento/oggetti_invasioni`
