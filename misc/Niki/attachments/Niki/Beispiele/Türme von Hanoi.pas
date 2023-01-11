Program Hanoi;

{ entnommen  Alfred Kn\'fclle-Wenzel, Hans-J\'f6rg Himmerr\'f6der
                    ROBI der Roboter
                    Westermann Verlag 1989 }
                    
{ Achtung: Unter 
   Start-Optionen-Compiler Syntax umschalten!! }

  Procedure umdrehen;
  begin
    drehelinks;
    drehelinks;
  end;

  Procedure zurueck;
  begin
    umdrehen; vor; umdrehen;
  end;

  Procedure dreherechts;
  begin
     drehelinks; drehelinks; drehelinks
  end;

  Function true;
  begin
    Return vornefrei or not vornefrei
  end;

  Function false;
  begin
    Return vornefrei and not vornefrei
  end;

  Procedure geheweiter;
  begin
     if vornefrei 
        then vor
        else begin
                 umdrehen;
                 vor;
                 vor;
                 umdrehen;
              end;
  end;

  function naechster_frei;
  begin
     geheweiter;
     return not platzbelegt;
     geheweiter;
     geheweiter;
  end;

  function ueber_naechster_frei;
  begin
     geheweiter;
     geheweiter;
     return not platzbelegt;
     geheweiter;
  end;

  function zweifrei;
  begin
     return naechster_frei and ueber_naechster_frei
  end;

  function vorne_platzbelegt;
  begin
     vor;
     return platzbelegt;
     zurueck;
  end;

  procedure geherauf;
  begin
     drehelinks;
     while vorne_platzbelegt do vor;
     dreherechts
  end;

  procedure geherunter;
  begin
     dreherechts;
     while vornefrei do vor;
     drehelinks;
   end;

  Procedure hole_oberste_Scheibe;
  begin
     geherauf;
     while platzbelegt do nimmauf;
     geherunter;
  end;

  Procedure lege_Scheibe_ab;
  begin
     drehelinks;
     while Platzbelegt do vor;
     while hatVorrat do gibab;
     dreherechts;
     geherunter;
  end;

  Procedure setze_kleinste_Scheibe_weiter;
  begin
     geheweiter;
     geheweiter;
     hole_oberste_Scheibe;
     geheweiter;
     lege_Scheibe_ab;
  end;

  Procedure lege_andere_Scheibe_um;
  
     Function Haufen_gefunden;
     begin
        if vornefrei
           then return vorne_platzbelegt
           else return true
     end;

     Procedure Schiebe_Scheibe_runter;
     begin
         While platzbelegt do nimmauf;
         dreherechts;
         while not Haufen_gefunden do vor;
         While hatvorrat do gibab;
         umdrehen;
         while vornefrei do vor;
         dreherechts;
     end;

     Procedure gehe_zur_anderen;
     begin
        geheweiter;
        umdrehen;
     end;

     function hier_ist_kleiner_als_da;
     begin
        if platzbelegt then
           begin
              nimmauf;
              gehe_zur_anderen;
              Return not hier_ist_kleiner_als_da;
              gehe_zur_anderen;
              gibab;
           end
        else return true;
    end;

    Procedure Schiebe_oberste_Scheibe_hoch;
    begin
        geherauf;
        while platzbelegt do nimmauf;
        drehelinks;
        while vornefrei do vor;
        while hatvorrat do gibab;
        dreherechts;
    end;

    Function hier_kleiner_naechste;
    begin
      schiebe_oberste_Scheibe_hoch;
      geherunter;
      geheweiter;
      schiebe_oberste_Scheibe_hoch;
      geheweiter;geheweiter;
      Return hier_ist_kleiner_als_da;
      schiebe_Scheibe_runter;
      geheweiter;
      schiebe_Scheibe_runter;
      geheweiter; geheweiter;
      geherunter
    end;

    Procedure lege_oberste_Scheibe_weiter;
    begin
      hole_oberste_Scheibe;
      geheweiter;
      lege_Scheibe_ab;
      geheweiter;geheweiter;
    end;
 
    Procedure hole_naechste_Scheibe;
    begin
      geheweiter;
      hole_oberste_Scheibe;
      geheweiter;
      geheweiter;
      lege_Scheibe_ab;
    end;

    begin  (* lege_andere_Scheibe_um *)
       geheweiter;
       if not platzbelegt 
         then hole_naechste_Scheibe
         else if naechster_frei
                    then lege_oberste_Scheibe_weiter
                    else if hier_kleiner_naechste
                             then lege_oberste_Scheibe_weiter
                             else hole_naechste_Scheibe
    end;

  begin
    Arbeitsfeld(Hanoi);
    setze_kleinste_Scheibe_weiter;
    While not zweifrei do
       begin
          lege_andere_Scheibe_um;
          setze_kleinste_Scheibe_weiter;
       end;
    geheweiter;        
 end.


