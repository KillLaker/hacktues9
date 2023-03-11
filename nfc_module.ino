#include <SoftwareSerial.h>
#include <PN532_SWHSU.h>
#include <PN532.h>
SoftwareSerial SWSerial( 3, 2 );

#define R 9
#define G 10
#define B 11
 
PN532_SWHSU pn532swhsu( SWSerial );
PN532 nfc( pn532swhsu );
String tagId = "None", dispTag = "None";
byte nuidPICC[4];
 
void setup(void)
{
  Serial.begin(9600);

  nfc.begin();
  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata)
  {
    while (1);
  }
  
  nfc.SAMConfig();
}
 
 
void loop()
{
  readNFC();
}
 
 
void readNFC()
{
  boolean success;
  uint8_t uid[] = { 0, 0, 0, 0, 0, 0, 0 }; 
  uint8_t uidLength;                       
  success = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A, &uid[0], &uidLength);
  if (success)
  {
    for (uint8_t i = 0; i < uidLength; i++)
    {
      nuidPICC[i] = uid[i];
    }
    tagId = tagToString(nuidPICC);
    dispTag = tagId;
    delay(1000);

    if(tagId == "144.8.60.33") {
       Serial.println(1);
    } else {
      Serial.println(0);
    }
  }
  delay(2000);
}

String tagToString(byte id[4])
{
  String tagId = "";
  for (byte i = 0; i < 4; i++)
  {
    if (i < 3) tagId += String(id[i]) + ".";
    else tagId += String(id[i]);
  }
  return tagId;
}
