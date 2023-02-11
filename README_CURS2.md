Obiective Întâlnire 2

● Să cunoști tipurile principale de operatori:
○ De atribuire;
○ Aritmetici;
○ De comparare;
○ Logici.
● Să înțelegi cum se folosește condiționalul if else (flow control):
○ If simplu;
○ If / else;
○ If / else if / else.

Operatori de atribuire

Operatori aritmetici

Operatori de comparare

Operatori logici

if...

● În engleză acest principiu se numește ‘flow control’ - controlăm pe unde curge codul
● Un if simplu e ca o ușă: daca ușa e deschisă (true), se va executa codul din spate. Dacă ușa
(condiția) e închisă (false), python nu va afla ce e în spatele ușii. Pentru Python, acea zona
de cod e inaccesibilă, nu există.
● După cele: ale unei ramuri, când apăsăm ‘Enter’ se vor pune automat 4 spații sau un TAB
Acest lucru se numește indentare. Indentarea are scopul de a-i transmite lui python de unde până
unde ține blocul de cod corespunzător acelei condiții. Sau, altfel spus, marchează pereții camerei
din spatele ușii.

- E ok logica codului?
- Găsește ‘bug-ul’.

If... else

● Dacă (condiție) atunci (executăm codul).
● Are tot timpul fix 2 ramuri.
● If are condiție urmată de:
● Else nu mai are nevoie de condiție, deoarece înseamnă în celălat caz.

○ Ex: Un număr dacă nu e par, e automat impar.

If... else if... else

● Se folosește când avem mai mult de 2 situații posibile.
● Condițiile se evaluează de sus în jos.
● Se execută codul aferent primei condiții adevărate.
● După ce s-a găsit cu true, nu se mai verifică ce a mai rămas mai jos.

● Un singur if la început.
● Oricâte elif-uri sunt necesare.
● Un singur else la final.
● Dacă nu găsește niciun true mai sus,
else se vă executa automat (e ca un default).

Întrebări & curiozități?
j Întrebări de interviu:
➢ Ce reprezintă operatorii logici?
➢ Ce reprezintă operatorii aritmetici?
➢ Când folosim condiționalul if?