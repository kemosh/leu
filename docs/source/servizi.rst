Servizi
=======

Rent
----
Ogni personoggio deve affittare una camera e pagare l'affitto. L'affitto base è fissato a 10 monete d'oro 
al giorno (tempo reale), alcuni oggetti hanno un costo di rent ed incrementato il conto, alcuni oggetti
sono **NO RENT** e scompariranno dall'inventario del personaggio in caso di disconnessione per un tempo
prolungato. **Giulietta** offre questo servizio ad Alma, presso la *Reception* della *Taberna Viatoris*,
ma non è l'unica.

- preventivo: ``offer``
- affitta camera: ``rent``

Astral e Portal
---------------
Sono due metodi di viaggio veloce, questi servizi sono offerti da **Zryon** nella *Gilda dei Viaggiatori*:

- path da *Alma Civitas*: ``s;s;e;e;n``
- astral: ``ask Zryon astral``
- portal: ``ask Zryon portal nome_mob``

Banca
-----
Qui è possibile depositare soldi e ingredienti:

- path da *Alma Civitas*: ``s;e;e;e;s``
- bilancio: ``balance``
- deposita: ``deposit``
- ritira: ``withdraw``
- visualizza cassetta (ingredienti): ``cassetta`` oppure ``cassetta NUMERO`` 
  per una specifica pagina (inserire un numero da 1 a 5)

Maestri Abilità Secondarie
--------------------------
Insegnano abilità secondarie comuni a tutte le classi, molti sono raggiunginili tramite portal:

- **Maestro Ninja** (``maestro-ninja``):

  - cavalcare
  - sfondare porte
  - scassinare

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
In *Via delle Gilde* si trovano i maestri per i bassi livelli.

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
  ``astral;u;n;w;w;n;u;w;u;u;enter spe;``

Localizzazione oggetti
----------------------

* path da *Alma Civitas*: ``s;s;e;e;e``
* comando: ``whisper gitana OGGETTO``

Allania
-------
Allania offre diversi servizi di edit sul personaggio e sugli oggetti, inoltre
è possibile comprare oggetti quest, ingredienti e fare varie conversioni.

* path per andare all'intersezione delle gallerie:
  ``astral;u;n;w;w;n;u;w;u;u;w;d;w;s;s;s;s;w;w;w;w;d;d``
* path per tornare dall'intersezione delle gallerie:
  ``w;s;s;e;s;enter portale``
* per esaminare i servizi, dall'intersezione delle gallerie:
  ``exa prima | seconda | ... | quinta``
* path per **Tarr** (vende il **cristallo crono-traslazione**), dall'intersezione
  delle gallerie: ``n;e;e;n;u;u;e;e;e;n``
* path per **Viaggiatori** (oggetti speciali), bisogna avere 
  il cristallo della crono-traslazione in inventario,
  poi dall'intersezione delle gallerie:
  ``n;e;e;n;u;u;e;e;e;e;unlock parete;twist parete;e``

