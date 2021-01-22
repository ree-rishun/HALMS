#include <Wire.h>

//スレーブ受信時のdelay
#define delay_t 10

//スレーブからの受信データ　最後にセンサーが反応した時間
unsigned long recvSlave(byte);



//i2c 　スレーブからの受信
unsigned long now_t = 0;

//マスター制御用
int mode = 0;
unsigned long stop_t = 0;
unsigned long Master_t = 0;

//速度算出　最初に反応したn番目のセンサー　＋　２回目に反応したn番目のセンサー　/ 　2
byte farst_sensar        = -1;
byte farst_flg           = 0;
unsigned long farst_time = 0;
unsigned long last_time  = 0;
unsigned long spead = 0;
unsigned long spead_ = 0;



void setup() {
  Wire.begin();        
  Serial.begin(9600);
  Master_t = millis();  
}



void loop() {
  // 9個のスレーブを順に取得
  for (int i = 0; i < 9; i++)
  {
      now_t = recvSlave(i);
      //Serial.print(i); Serial.print("\t"); Serial.println(now_t);
      if(farst_flg && i == farst_sensar && now_t)        last_time = now_t;
      if(farst_flg && i == farst_sensar && now_t == 0)   spead     = last_time - farst_time;
      
      if(now_t && farst_flg == 0)
      {
        farst_sensar = i;
        farst_flg    = 1;
        farst_time   = now_t;
      }    
  }


  
  //stop_t = millis() - Master_t;
  //if(mode && stop_t < 2000)    spead = 0;
  //else    mode = 0;



  
  if(spead) 
  {
    if(spead < 1000)
    {
      Serial.print("spead = "); Serial.println(spead);
      delay(1000);
    }

    farst_sensar = -1;
    farst_flg    = 0;
    farst_time   = 0;
    last_time    = 0;
    spead_ = spead;
    spead        = 0;
    mode = 1;
    Master_t = millis();
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