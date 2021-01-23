#include <Wire.h>

#define SLAVE_NUM     3   // スレーブ数
#define REQUEST_DELAY 1   // リクエスト間隔

// セットアップ
void setup()
{
    Serial.begin(9600);
    Wire.begin(); // マスターに設定
}

// メイン処理
void loop()
{
  unsigned int duration[256];

  // 初期化
  for (int i = 0; i < 256; ++i) duration[i];

  // スレーブから値を取得
  for (byte slaveID = 0; slaveID < SLAVE_NUM; slaveID++) {
    Wire.requestFrom(slaveID + 1, 1);
    
    // 値を受信
    for (int i = 0; i < sizeof(int); ++i) {
      byte one_byte = Wire.read();  // 1byte受信
      duration[slaveID] += one_byte << (8 * i);                // 結合
    }
    
    // 値を表示
    for (int i = 0; i < sizeof(int); ++i) {
      Serial.print(slaveID);
      Serial.print("\t:\t");
      Serial.println(duration[slaveID]);
    }
  }

  Serial.println("===========");
}
