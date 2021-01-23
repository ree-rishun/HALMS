#include <Wire.h>
 
void setup()
{
    Serial.begin(9600);
    Wire.begin(); // マスターに設定
}
 
void loop()
{
    //スレーブ（0x1E）から1byteのデータを取得
    Wire.requestFrom(0x1E, 1); 
 
    while(Wire.available())
    { 
        byte num = Wire.read(); // 1バイト受信
        Serial.println(num);
    }
 
    delay(500);
}
