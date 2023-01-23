import serial
import time

ser = serial.Serial('/dev/ttyUSB0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

def checksum(data):
    xorval = 0
    for el in data:
        xorval ^= el
    return 255 - xorval

print ("Öffne Serialport " + ser.port)
ser.flushOutput()
ser.flushInput()


tx_1 = [0x7E,0x81,0x7D,0x5E,0x7E] #Initialisierung
tx_2 = [0x7E,0x91,0x04,0x02,0x68,0x7E]

tx_301 = [0x7E,0x82,0x7D,0x5D,0x7E,]
tx_302 = [0x7E,0x83,0x7C,0x7E,]
tx_303 = [0x7E,0x84,0x7B,0x7E,]
tx_304 = [0x7E,0x85,0x7A,0x7E,]
tx_305 = [0x7E,0x86,0x79,0x7E,]
tx_306 = [0x7E,0x87,0x78,0x7E,]
tx_307 = [0x7E,0x88,0x77,0x7E,]
tx_308 = [0x7E,0x89,0x76,0x7E,]
tx_309 = [0x7E,0x8A,0x75,0x7E,]
tx_310 = [0x7E,0x8B,0x74,0x7E,]
tx_311 = [0x7E,0x8C,0x73,0x7E,]
tx_312 = [0x7E,0x8D,0x72,0x7E,]
tx_313 = [0x7E,0x8E,0x7D,0x5E,0x7E,]
tx_314 = [0x7E,0x81,0x7D,0x5E,0x7E,]

tx_row = [0x7E,0x91,0x24,0x12,0x58,0x7E,] # Als nächstes kommen die Bitmap Rows

row_24 = [0xA1,0x24,0x90,0xAF,0xAA,0x53,0xAA,0xAF,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90, 0x00,0x00, 0x00,0x00, 0x00,0x90,0x00, 0x00,0x00, 0x00,0x00] # Testpattern
row_12 = [0xA1,0x12,0x10,0xF9,0xAA,0x86,0xAA,0xF9,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10, 0x00,0x00, 0x00,0x00, 0x00,0x10,0x00, 0x00,0x00, 0x00,0x00] # Testpattern

row_23 = [0xA1,0x23,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0b10000001,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_11 = [0xA1,0x11,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0b11000011,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern

row_22 = [0xA1,0x22,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0xFF,0x81,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_10 = [0xA1,0x10,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0xFF,0xC3,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern

row_21 = [0xA1,0x21,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_20 = [0xA1,0x20,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_1F = [0xA1,0x1F,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern

row_1E = [0xA1,0x1E,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_1D = [0xA1,0x1D,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_1C = [0xA1,0x1C,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern

row_1B = [0xA1,0x1B,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_1A = [0xA1,0x1A,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_19 = [0xA1,0x19,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern

row_18 = [0xA1,0x18,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_17 = [0xA1,0x17,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_16 = [0xA1,0x16,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern

row_15 = [0xA1,0x15,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_14 = [0xA1,0x14,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_13 = [0xA1,0x13,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00,0x90,0x00,0x00,0x00,0x00,0x00] # Testpattern

row_0F = [0xA1,0x0F,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_0E = [0xA1,0x0E,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_0D = [0xA1,0x0D,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_0C = [0xA1,0x0C,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_0B = [0xA1,0x0B,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_0A = [0xA1,0x0A,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_09 = [0xA1,0x09,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_08 = [0xA1,0x08,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_07 = [0xA1,0x07,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_06 = [0xA1,0x06,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_05 = [0xA1,0x05,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_04 = [0xA1,0x04,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_03 = [0xA1,0x03,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_02 = [0xA1,0x02,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern
row_01 = [0xA1,0x01,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00,0x10,0x00,0x00,0x00,0x00,0x00] # Testpattern



# Initialisierung senden
print ("Sende Initialisierung " + ''.join(format(x, '02x') for x in tx_1))
txData = tx_1
ser.write(serial.to_bytes(txData))


print ("\nWarte auf Antwort ...\n")
#time.sleep(0.007)
ser.flushInput()
step = 1

while 1:
    # Bytes einlesen
    hexData = ser.read(100).hex()
    # Antwort bereinigen
    rxData = hexData.replace(''.join(format(x, '02x') for x in txData), "", 1)

    #Auf Antwort warten
    if (rxData):
        print("\nEmpfange hexData: " + hexData) 
        print("Empfange  rxData: " + rxData)

       
        if (rxData == "7e014c4d01563135ac7e" and step == 1):
            txData = tx_2
            print ("Schritt 2")
            print ("    Sende Antwort 2: " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            step = 3

        elif (rxData == "7e117e" and step == 3):
            print ("Schritt 3")
            print ("    Sende Antwort 301: " + ''.join(format(x, '02x') for x in tx_301))
            ser.write(serial.to_bytes(tx_301))
            time.sleep(0.1)
            print ("    Sende Antwort 302: " + ''.join(format(x, '02x') for x in tx_302))
            ser.write(serial.to_bytes(tx_302))
            time.sleep(0.1)
            print ("    Sende Antwort 303: " + ''.join(format(x, '02x') for x in tx_303))
            ser.write(serial.to_bytes(tx_303))
            time.sleep(0.1)
            print ("    Sende Antwort 304: " + ''.join(format(x, '02x') for x in tx_304))
            ser.write(serial.to_bytes(tx_304))
            time.sleep(0.1)
            print ("    Sende Antwort 305: " + ''.join(format(x, '02x') for x in tx_305))
            ser.write(serial.to_bytes(tx_305))
            time.sleep(0.1)
            print ("    Sende Antwort 306: " + ''.join(format(x, '02x') for x in tx_306))
            ser.write(serial.to_bytes(tx_306))
            time.sleep(0.1)
            print ("    Sende Antwort 307: " + ''.join(format(x, '02x') for x in tx_307))
            ser.write(serial.to_bytes(tx_307))
            time.sleep(0.1)
            print ("    Sende Antwort 308: " + ''.join(format(x, '02x') for x in tx_308))
            ser.write(serial.to_bytes(tx_308))
            time.sleep(0.1)
            print ("    Sende Antwort 309: " + ''.join(format(x, '02x') for x in tx_309))
            ser.write(serial.to_bytes(tx_309))
            time.sleep(0.1)
            print ("    Sende Antwort 310: " + ''.join(format(x, '02x') for x in tx_310))
            ser.write(serial.to_bytes(tx_310))
            time.sleep(0.1)
            print ("    Sende Antwort 311: " + ''.join(format(x, '02x') for x in tx_311))
            ser.write(serial.to_bytes(tx_311))
            time.sleep(0.1)
            print ("    Sende Antwort 312: " + ''.join(format(x, '02x') for x in tx_312))
            ser.write(serial.to_bytes(tx_312))
            time.sleep(0.1)
            print ("    Sende Antwort 313: " + ''.join(format(x, '02x') for x in tx_313))
            ser.write(serial.to_bytes(tx_313))
            time.sleep(0.1)
            print ("    Sende Antwort 314: " + ''.join(format(x, '02x') for x in tx_314))
            txData = tx_314
            ser.write(serial.to_bytes(tx_314))
            step = 4
            ser.flushInput()
    
        elif (rxData == "7e014c4d01563135ac7e" and step == 4):
            print ("Schritt 4")
            print ("    Sende BITMAP Befehl")
            print ("    Sende Antwort tx_row: " + ''.join(format(x, '02x') for x in tx_row))
            ser.write(serial.to_bytes(tx_row))
            ser.flushInput()
            time.sleep(0.22)
      
            row = 0x24
            txData = row_24            
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)   
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))            
            ser.write(serial.to_bytes(txData))
            row -=1
            ser.flushInput()

        elif (rxData == "7e217e" and row == 0x23):
            txData = row_23
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x22):
            txData = row_22
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x21):
            txData = row_21
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x20):
            txData = row_20
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x1F):
            txData = row_1F
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x1E):
            txData = row_1E
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x1D):
            txData = row_1D
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x1C):
            txData = row_1C
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x1B):
            txData = row_1B
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x1A):
            txData = row_1A
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x19):
            txData = row_19
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x18):
            txData = row_18
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x17):
            txData = row_17
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x16):
            txData = row_16
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x15):
            txData = row_15
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x14):
            txData = row_14
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x13):
            txData = row_13
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x12):
            txData = row_12
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1
         
        elif (rxData == "7e217e" and row == 0x11):
            txData = row_11
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x10):
            txData = row_10
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x0F):
            txData = row_0F
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x0E):
            txData = row_0E
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x0D):
            txData = row_0D
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x0C):
            txData = row_0C
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x0B):
            txData = row_0B
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x0A):
            txData = row_0A
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x09):
            txData = row_09
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x08):
            txData = row_08
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x07):
            txData = row_07
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x06):
            txData = row_06
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x05):
            txData = row_05
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x04):
            txData = row_04
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x03):
            txData = row_03
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x02):
            txData = row_02
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x01):
            txData = row_01
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende BITMAP row_" + format(row, '02x') + ": " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            row -= 1

        elif (rxData == "7e217e" and row == 0x00):
            txData = [0x7E, 0x81, 0x7D, 0x5E, 0x7E]
            txData.append(checksum(txData))           
            txData.insert(0,0x7E)           
            txData.append(0x7E)
            print ("    Sende : " + ''.join(format(x, '02x') for x in txData))
            ser.write(serial.to_bytes(txData))
            ser.flushInput()
            step = 5

        elif (rxData == "7e014c4d01563135ac7e" and step == 5):
            print ("Schritt 5")
            
            txData = [0x7E,0x82,0x7D,0x5D,0x7E]
            for x in range(3):
                time.sleep(0.4)
                print ("    Sende : " + ''.join(format(x, '02x') for x in txData))
                ser.write(serial.to_bytes(txData))
                ser.flushInput()
            
            txData = [0x7E,0x83,0x7D,0x7E]
            for x in range(3):
                time.sleep(0.4)
                print ("    Sende : " + ''.join(format(x, '02x') for x in txData))
                ser.write(serial.to_bytes(txData))
                ser.flushInput()

            txData = [0x7E,0x84,0x7B,0x7E]
            for x in range(3):
                time.sleep(0.4)
                print ("    Sende : " + ''.join(format(x, '02x') for x in txData))
                ser.write(serial.to_bytes(txData))
                ser.flushInput()

            txData = [0x7E,0x87,0x78,0x7E]
            for x in range(2):
                time.sleep(0.4)
                print ("    Sende : " + ''.join(format(x, '02x') for x in txData))
                ser.write(serial.to_bytes(txData))
                ser.flushInput()        


        else:
            print ("    Daten unbekannt")

        print ("\nWarte auf Antwort ...")




ser.close()


