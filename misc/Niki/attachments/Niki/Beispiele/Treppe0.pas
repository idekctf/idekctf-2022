Program Treppe0;

Procedure drehe_rechts;
Begin
  drehe_links;
  drehe_links;
  drehe_links;
End;

Procedure stufe_hoch;
Begin
  drehe_links;
  vor;
  drehe_rechts;
  vor;
End;

Procedure stufe_runter;
Begin
  vor;
  drehe_rechts;
  vor;
  drehe_links;
End;

Begin {Hauptprogramm}
  Arbeitsfeld(Treppe0);
  vor;
  vor;
  vor;
  vor;
  stufe_hoch;
  stufe_hoch;
  stufe_hoch;
  nimm_auf;
  stufe_runter;
  stufe_runter;
  stufe_runter;
  vor;
  vor;
  vor;
  stufe_hoch;
  gib_ab;
  drehe_links;
  drehe_links;
  vor;
  drehe_links;
  vor;
  drehe_rechts;
end.  