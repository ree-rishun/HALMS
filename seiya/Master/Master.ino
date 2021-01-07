//作成者　くわはら
//機能　　i2c スレーブ
//作成日　12/22
//備考　　スレーブ側のソース　”Slave_num”を１～９の番号に変更する
//        上記についてマスター側調整済み
//        本番時はシリアルプリントをコメントアウトすること

#include <Wire.h>

//スレーブ受信時のdelay
#define delay_t 50

//スレーブからの受信データ　最後にセンサーが反応した時間
unsigned long recvSlave(byte);



//i2c 　スレーブからの受信
unsigned long now_t = 0;

//速度算出　最初に反応したn番目のセンサー　＋　２回目に反応したn番目のセンサー　/ 　2
byte farst_sensar        = -1;
byte farst_flg           = 0;
unsigned long farst_time = 0;
unsigned long last_time  = 0;
byte spead = 0;


void setup() {
  Wire.begin();        
  Serial.begin(9600);  
}



void loop() {
  for (int i = 1; i <= 9; i++)
  {
      now_t = recvSlave(i);
      Serial.print(i); Serial.print("\t"); Serial.println(now_t);
      if(farst_flg && i == farst_sensar && now_t)        last_time = now_t;
      if(farst_flg && i == farst_sensar && now_t == 0)   
      {
        spead     = last_time - farst_time;
        break;
      }
      
      if(now_t && farst_flg == 0)
      {
        farst_sensar = i;
        farst_flg    = 1;
        farst_time   = now_t;
      }
      
  }
  if(spead) 
  {
    Serial.print("spead = "); Serial.println(spead);
    delay(2000);
    farst_sensar = -1;
    farst_flg    = 0;
    farst_time   = 0;
    last_time    = 0;
    spead        = 0;
  }
}




//i2c 　スレーブからの受信
unsigned long recvSlave(byte slave)
{
  Wire.requestFrom(slave, 4);    
  unsigned long time_ = 0;
  int num = 0;
  while (Wire.available())
  {     
    unsigned long c = Wire.read();    
    for(int i = 0; i < num; i++) c = c << 8;
    time_ |= c;
    if(num == 3) break;
    num++;
  } 
  delay(delay_t);
  return time_;
}
