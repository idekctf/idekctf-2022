 (*LSW Soest: Lehrerfortbildung; Informatik in der gymnasialen Oberstufe*)

PROGRAM lager_umraeumen;   {Arbeitsfeld: CONTUMR.ROB}

  PROCEDURE drehe_um;
  BEGIN
    drehe_links;
    drehe_links;
  END;

  PROCEDURE drehe_rechts;
  BEGIN
    drehe_um;
    drehe_links;
  END;

  PROCEDURE gehe_zur_halle;
  BEGIN
    drehe_links;          {vorher:  Position (1/1) Ost}
    vor;                  {nachher: Position (2/2) Ost}
    drehe_rechts;
    vor
  END;

  PROCEDURE gehe_zur_naechsten_oberen_box;
  BEGIN
    vor;                   {vorher:  Position (x/2)    Ost}
    drehe_links;           {nachher: Position (x+1/3) Nord}
    vor
  END;

  PROCEDURE leere_die_box;
  BEGIN
    WHILE platz_belegt DO
      nimm_auf
  END;

  PROCEDURE gehe_zur_unteren_box;
  BEGIN
    drehe_um;               {vorher:  Position (x/3) Nord}
    vor;                    {nachher: Position (x/1) S'fcd}
    vor
  END;

  PROCEDURE lege_alle_container_ab;
  BEGIN
    WHILE hat_vorrat DO
       gib_ab
  END;

  PROCEDURE gehe_zum_mittelgang;
  BEGIN
    drehe_um;                 {vorher:  Position (x/1) S'fcd}
    vor;                      {nachher: Position (x/2) Ost}
    drehe_rechts
  END;

  PROCEDURE kehre_zurueck;
  BEGIN
    drehe_um;                  {vorher : Position (10/2) Ost}
    WHILE vorne_frei DO        {nachher: Position (1/1)  Ost}
    vor;
    drehe_links;
    vor;
    drehe_links
  END;

BEGIN   {lager_umraeumen}
  Arbeitsfeld(CONTUMR);
  gehe_zur_halle;
  REPEAT
    gehe_zur_naechsten_oberen_box;
    leere_die_box;
    gehe_zur_unteren_box;
    lege_alle_container_ab;
    gehe_zum_mittelgang;
  UNTIL NOT vorne_frei;
  kehre_zurueck;
  abschalten;
END.



