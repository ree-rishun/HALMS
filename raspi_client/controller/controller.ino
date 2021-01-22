// ヘッダ読み込み
#include <WiFi.h>
#include <HTTPClient.h>

// Wi-Fi関係
const char WIFI_SSID[] = "ReE_Device";
// "Buffalo-G-4870",

const char WIFI_PASS[] = "1223334444";
// "cdcjv6f7cpd7c",

// GET先
const char URL[] = "http://172.20.10.2:5000/api/";

// プロトタイプ宣言
void connectWiFi(char* ssid, char* passwd);
void getWebLink(char*);

// セットアップ
void setup() {
  // ボーレート設定
  Serial.begin(115200);

  // Wi-Fi接続
  connectWiFi(WIFI_SSID, WIFI_PASS);

  // 必要があれば（機種判別とか）
  // uint64_t chipid = ESP.getEfuseMac(); //  Macアドレス取得
  // IPAddress ipAddress = WiFi.localIP();//  ローカルのIPアドレス取得
}

// メイン処理
void loop() {
  // 接続失敗時に再接続
  if ( WiFi.status() == WL_DISCONNECTED) {
    connectWiFi(WIFI_SSID, WIFI_PASS);
  }
  
  // GET
  getWebLink(URL);

  delay(5000);
}


// --------------------
//  自作関数
// --------------------

// Wi-Fi接続関数
void connectWiFi(const char* ssid, const char* passwd)
{
    // 接続開始
    WiFi.begin(ssid, passwd);
    Serial.print("WiFi connecting...");

    // 接続成功までループ
    while(WiFi.status() != WL_CONNECTED) {
      Serial.print(".");
      delay(100);
    }
    Serial.println(".");
    
    // 接続完了
    Serial.print("connected : ");
    Serial.println(WiFi.localIP());
}


// GET関数
void getWebLink(const char* API_URL){
  // HTTPのインスタンス作成
  HTTPClient http;
  
  // GET
  http.begin(API_URL);
  int httpCode = http.GET();

  // 結果表示
  Serial.printf("Response: %d", httpCode);
  Serial.println();
  if (httpCode == HTTP_CODE_OK) {
    String body = http.getString();
    Serial.print("Response Body: ");
    Serial.println(body);
  }
}
