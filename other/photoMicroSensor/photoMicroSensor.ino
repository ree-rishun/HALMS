#include <Wire.h>

#define SENSOR_PIN  3

void setup()
{
  // 自身のアドレスを指定
  Wire.begin(0x31);
  Serial.begin(115200);
  
  // マスターからのリクエスト時の処理
  Wire.onRequest(send_count);

  // センサーのピンを指定
  pinMode(SENSOR_PIN, INPUT);
  Serial.println(sizeof(unsigned int));
}

// カウント
unsigned int count_duration = 0;

void loop()
{
  if (digitalRead(SENSOR_PIN) == 1) {
    count_duration = 0;
  } else {
    count_duration++;
  }
  delay(100);
}

// 送信済みBYTE数
byte count_byte = 0;
unsigned int count_duration_fix = 0;

// 記録回数の送信
void send_count () {
  if (count_byte == 0){
    count_duration_fix = count_duration;
    Serial.println(count_duration_fix);
  }
  Wire.write((count_duration_fix >> (8 * count_byte)) & 0xff);
  if (++count_byte == 4) count_byte = 0;
}
