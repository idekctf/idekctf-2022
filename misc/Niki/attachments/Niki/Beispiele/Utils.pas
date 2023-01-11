unit Utils;

interface

procedure drehe_rechts;
procedure drehe_um;

implementation

procedure drehe_rechts;
begin
  drehe_links;
  drehe_links;
  drehe_links;
end;

procedure drehe_um;
begin
  drehe_links;
  drehe_links;
end;

end.