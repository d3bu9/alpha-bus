# alpha-bus

CU5

Betriebsspannung: 24 VDC

Alpha-Bus für Anzeige
1 weiss  24V DOT Anzeige
2 braun  GND
3 grün   DATA
4 gelb   8V Slave Board

• Datenübertragung mit 19200 Bit/s bidirektional auf einer Leitung (DATA) 8 Datenbits, 2 Stopbits, Parität: keine
• Spannungshub der seriellen Datenübertragung: 24V (idle)

Bedienung

Parameter
H+/Z+/E+ 3 Sekunden drücken

Display Testmode
H-/Z-/E- 3 Sekunden drücken

Texteingabe
T+/T- 3 Sekunden drücken

Serial Dump

Reset CU5 (ohne Anzeige angeschlossen)
0x7E, 0x81, 0x7D, 0x5E, 0x7E
Pause 400ms
0x7E, 0x81, 0x7D, 0x5E, 0x7E

Reset CU5 (mit Anzeige angeschlossen)
CU5: 0x7E, 0x81, 0x7D, 0x5E, 0x7E
1,2 ms Pause
Anzeige: 0x7E, 0x01, 0x4C, 0x4D, 0x01, 0x56, 0x31, 0x35, 0xAC, 0x7E 
420us Pause
CU5?: 0x7E, 0x91, 0x04, 0x02, 0x68, 0x7E
379us Pause
0x7E, 0x11, 0x7E
19ms Pause


