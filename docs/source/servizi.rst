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
  ``astral;u;n;w;w;n;u;w;u;u;enter spe;e;d;d;d;n;n;e;e;e;u;u;open masso;e;e;n;e;s;d;d;w;w``

Localizzazione Oggetti
----------------------

* path da *Alma Civitas*: ``s;s;e;e;e``
* comando: ``whisper gitana OGGETTO``

Localizzazione Lingotti
-----------------------
I lingotti (incluse le pietre) si trovano nei tesori delle quest e in alcune
**scatole nere laccata** che appaiono a caso addosso ad alcuni mob. È possibile
individuare quali mob hanno la scatola chidendo al **vacchietto**:

* path da *Alma Civitas*: ``s;s;e;e;s``
* comando: ``ask vecchietto ingredienti``

Allania
-------
Allania offre diversi servizi di edit sul personaggio e sugli oggetti, inoltre
è possibile comprare oggetti quest, ingredienti e fare varie conversioni.

* path per andare a *Un'intersezione tra le gallerie*:
  ``astral;u;n;w;w;n;u;w;u;u;w;d;w;s;s;s;s;w;w;w;w;d;d``
* path per tornare da *Un'intersezione tra le gallerie*:
  ``w;s;s;e;s;enter portale``
* per esaminare i servizi, una volta arrivati a *Un'intersezione tra le gallerie*:
  ``exa NUMERO``, con ``NUMERO = prima, ..., quinta``
* path per **Tarr** (vende il **cristallo crono-traslazione**), da
  *Un'intersezione tra le gallerie*: ``n;e;e;n;u;u;e;e;e;n``
* path per **Viaggiatori** (oggetti speciali), bisogna avere 
  il cristallo della crono-traslazione in inventario,
  poi da *Un'intersezione tra le gallerie*:
  ``n;e;e;n;u;u;e;e;e;e;unlock parete;twist parete;e``

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

Sanctuary
---------
È molto importante avere a disposizione l'incantesimo **sanctuary** anche se non fa
parte delle abilità della propria classe, ecco come procurarselo:

* **Scettro di Ravenloft**, ha 6 cariche, quando usato lancia sanctuary su tutti i
  mob/giocatori nella stanza
  - andare ad *Allania*, all'intersezione delle gallerie
  - andare da **Arren**: ``n;e;e;n;u;u;e;e;n``
  - comprare lo scettro: ``buy 7``, costa **350 mdc** e, una volta scarico, può essere 
    rivenduto per **70 mdc**
  - tornare: ``s;w;w;d;d;s;w;w;s``

* **Scudo di Silver**, lancia sanctuary a piacere, ha un cooldown di 2 RockHound
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

- portal ``topo-deserto`` e down fino a *La Base della Piramide*
- ``n;n;n;e;e;e;e;e;u;u;u;e;d;e;e``
- uccidere **RockHound** e poi ``get chiave-pietra cad``
- ``unlock fessura;open fessura;e;pull stalagmite;n``
- attendere teleport
- ``say raido``

A questo punto ci si trova davanti a **Thor**, per il processo di creazione:

- ``ask thor sfere``, **Thor** dirà di mettere le sfere nella fornace
- mettere gli ingredienti nella ``fornace``
- ``nod thor``

Ricette Invasioni:

- Simbolo di **Benem**: 4 amaranto, 2 smeraldo, 3 monili
- Simbolo di **Hansolo**: 4 indaco, 2 ambra, 3 monili