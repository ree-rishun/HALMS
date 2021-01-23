#include <Wire.h>

// 定数定義
#define UNDETECTED  0  // 未検知
#define PHOTO_MICRO 5   // センサーピン
#define DETECTED    1   //　検知

// 最後にセンサで検知してからの経過時間
unsigned int duration = UNDETECTED;

// プロトタイプ宣言
void send_duration();


// セットアップ
void setup()
{
  // 自身のアドレスを指定
  Wire.begin(0x01);
  
  // マスターからのリクエスト時の処理
  Wire.onRequest(send_duration);

  // センサーピンの設定
  pinMode(PHOTO_MICRO, INPUT);
}


// メイン処理
void loop()
{
  // 値を検知したか取得
  if (digitalRead(PHOTO_MICRO) === DETECTED) {
    // 検知した場合は値をリセット
    duration = UNDETECTED;
  } else {
    // 検知していない場合はカウント
    duration++;
  }
  delay(1);
}


// 経過時間の送信
void send_duration()
{
  // 経過時間をマスタへ送信
  Wire.write(duration, sizeof(duration));

  // 経過時間のリセット
  duration = UNDETECTED;
}
