PROGRAM german;

PROCEDURE turn_left;
BEGIN
drehe_links;
END;

PROCEDURE turn;
BEGIN
drehe_links;
drehe_links;
drehe_links;
END;

PROCEDURE move;
BEGIN
vor;
END;

PROCEDURE deposit;
BEGIN
gib_ab;
END;

PROCEDURE pick_up;
BEGIN
nimm_auf;
END;

PROCEDURE l;
BEGIN
move; deposit; turn_left; move; deposit; move; deposit; move; deposit; 
turn_left; move; deposit; turn; turn; move; move; deposit;
END;

PROCEDURE u;
BEGIN
deposit; move; deposit; move; deposit;
turn; turn ; move; turn;
move; deposit; move; deposit; move;
deposit; turn; move; deposit; turn; turn; move; move; deposit; turn; turn; 
END;

PROCEDURE v;
BEGIN
deposit; move; deposit; move; deposit;
turn_left; move; move; move; deposit; turn_left;
move; deposit; move; deposit; turn_left;
move; deposit; turn_left; move; deposit;
turn; turn; move; turn_left; move; deposit; turn_left; move; deposit;
END;

PROCEDURE p;
BEGIN
deposit; move; move; deposit; turn_left;
move; move; move; deposit; turn_left; move; turn_left; move; move; deposit; turn; 
move; deposit; turn; move; deposit; move; deposit; turn; move; move; turn; move; deposit; 
END;

PROCEDURE brackl;
BEGIN
move; deposit; turn_left; move; turn_left; move; deposit;
turn; move; deposit; move; turn; move; deposit;
END;

PROCEDURE q;
BEGIN
deposit; move; deposit; move; turn_left;
move; deposit ; move; deposit;
move; turn_left; move; deposit; move; deposit; turn_left;
move; deposit; move; deposit; turn_left; 
END;

PROCEDURE o;
BEGIN
deposit; move; deposit; move; deposit; turn_left;
move; turn_left; move; deposit; turn; move; turn_left;
move; deposit; turn; move; deposit; turn; move; deposit; move; deposit;
END;

PROCEDURE h;
BEGIN
deposit; turn_left; move; deposit; move; deposit; move; deposit; turn; move; deposit; move; deposit;
turn; move; deposit; move; deposit; turn; move; deposit;
END;

PROCEDURE a;
BEGIN
deposit; move; deposit; move; deposit;
turn_left; move; deposit; move; deposit; move; deposit;
turn_left; move; deposit; move; deposit;
turn_left; move; deposit; move; deposit;
END;

PROCEDURE zero;
BEGIN
move; deposit; move; turn_left;
move; deposit; move; deposit; move; turn_left; move; deposit; move; 
turn_left; move; deposit; move; deposit; turn_left; 
END;


PROCEDURE brackr;
BEGIN
deposit; move; turn_left; move; deposit; move; deposit;
turn_left; move; turn; move; deposit; 
END;

BEGIN
move; move; move; turn; move; move; move; turn_left;
move; move; turn; move; turn_left; move;
h;
o;
brackl;
a;
v;
move;
turn; move; move; move; turn_left; move;
move; move; turn_left; move;
u;
turn; turn; move; move; turn; move; turn_left;
brackr;
turn; move; move; move; turn_left; move;
turn_left; move; move; move; move; turn_left;
q;
turn; move; move; move; turn_left; move;
turn_left; move; move; turn; move; turn_left; move;
p;
move; turn; move; turn_left; move;
WHILE vorne_frei DO move; turn; turn;
l;
END.