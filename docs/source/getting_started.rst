Getting Started
===============

.. _connessione:

Come Connettersi
----------------

Per accedere al gioco è necessrio connettersi con un client telnet all'indirizzo: 

.. code-block:: console

   mclmud.mclink.it:6000

È possibile usare un qualunque client telnet, ma per migliorare sensibilmente l'esperienza ludica
è caldamente consigliato usare un client dedicato come `Mudlet <https://www.mudlet.org/it/>`_,
uno dei pochi attivamente mantenuto e sviluppato.

.. _configurazione_mudlet:

Configurazione Mudlet
---------------------

Bisogna creare un profilo dedicato, fare attenzione ad alcune opzioni come il separatore di riga che di
default è ``;;``, mentre alcuni preferiscono ``;``, questa opzione può essere configurata a piacere. 

.. _configurazione_leu:

Configurazione LeU
------------------

Ci sono alcune importanti configurazioni che vanno impostate nel gioco:

- **Prompt**, è fondamentale per avere informazioni in tempo reale durante la battaglia
  (consultare ``help prompt``) per i dettagli, ecco alcune configurazioni consigliate:

  - buon prompt di default: ``set prompt 19``
  - | prompt per monaci, ranger, ladri e psionici (mostra i punti energia: ``%e/%E``): 
    | ``set prompt |$c0115%bH2| |$c0415%bM2| |$c0615%bV2| $c0011%g $c0008%x $c0005%e/%E $c0007%n/%c - %N/%C %S``

  da notare che i colori si specificano usando ``$cXXYY`` dove XX è il colore di sfondo e YY è il colore
  del testo. Il testo normale, grigio su sfondo nero, corriponde a ``$cXXYY``, vedi: ``help color``

- | **Colori**, abilitare i colori con il comando:
  | ``set ansi on``

- | **Autoexits**, impostare la visualizzazione automatica delle uscite con il comando:
  | ``set autoexits on``

- | **Compact Combat**, permette di ridurre lo scroll raggruppando gli attacchi fisici:
  | ``set compact enable``

Scopo del Gioco
---------------
LeU è un gioco persistente, si crea un personaggio, scegliendo tra le molte opzioni
possibili, per poi farlo crescere e diventare sempre più potente in modo da affrontare
e sconfiggere creature leggendarie, sempre più forti. Idealmente per ogni combattimento
vinto si guadagna qualcosa (**punti esperienza**, **equipaggiamento**, **gemme**, etc.)
che può essere utile a personalizzare e potenziare il proprio alter ego, i potenziamenti
permetteranno di affrontare nuove sfide in aree prima inaccessibili, riuscendo a 
battere creature che prima era impensabile solo avvicinare.
Inevitabilmente a volte il proprio personaggio sarà sconfitto e la morte porterà a una
perdita di risorse (punti esperienze e danneggiamento dell'equipaggiamento), che
comunque sarà facile recuperare.
Oltre alla libera eplorazione, ci sono eventi particolari, come le quest, che saranno
disponibili a intervalli regolari o riappariranno dopo un certo tempo dall'ultimo
completamento.
Tutte le fide possono essere affrontate in solitaria e in gruppo.
**La crescita e il potenziamento del proprio personaggio è l'elemento cardine del
gioco** e gran parte del potenziamento sarà legato al reperimento e allo sviluppo
dell'equipaggiamento.
Vedi le meccaniche di gioco.
