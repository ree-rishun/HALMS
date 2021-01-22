<template>
  <div id="game">
    <img
      id="title"
      src="../assets/img/sasori.png">

    <div id="scorpion">
      <img
        src="../assets/img/sasori_img.png">

      <div
        id="scorpion_life">
        <span :style="'width: ' + ((scorpionLife - damage) / 100) + '%'"></span>
      </div>
    </div>

    <div id="user">
      <img
        src="../assets/img/rabit_attack.png">

      <div
        id="user_life">
        <span :style="'width: ' + ((userLife - userDamage) / 300) + '%'"></span>
      </div>
    </div>
  </div>
</template>

<script>
  import firebase from 'firebase'
  export default {
    name: 'GameUI',
    data () {
      return {
        scorpionLife: 10000,
        userLife: 30000,
        userDamage: 0,
        damage: 0,
        attackNum: 0,
        time: {
          limit: 60,
          count: 0,
          timer: null
        }
      }
    },
    methods: {
      onMessage (event) {
        console.log(event)
        const JSONmessage = event.data

        // JSONをパース
        const message = JSON.parse(JSONmessage)

        // ルーター処理の場合
        if (message.mode === 'damage') {
          console.log('user : ' + this.scorpionLife - this.damage)
          this.damage += (Number(message.damage) * 4)
          this.attackNum++

          // ライフが0以下になった場合にゲーム終了
          if (this.scorpionLife - this.damage <= 0) {
            this.scorpionDead()
          }
        } else if (message.mode === 'damage_user') {
          console.log(this.userLife - this.userDamage)
          this.userDamage += (Number(message.damage) * 3)

          // ライフが0以下になった場合にゲーム終了
          if (this.scorpionLife - this.userDamage <= 0) {
            this.userDead()
          }
        }
      },
      scorpionDead () {
        // タイマーの停止
        clearInterval(this.time.timer)

        // 結果画面に遷移
        this.$router.push({
          name: 'Result',
          query: {
            result: 'win',
            time: this.time.count,
            damage: this.damage,
            attackNum: this.attackNum,
            life: this.userDamage
          }
        })
      },
      userDead () {
        // タイマーの停止
        clearInterval(this.time.timer)

        // 結果画面に遷移
        this.$router.push({
          name: 'Result',
          query: {
            result: 'lose',
            time: this.time.count,
            damage: this.damage,
            attackNum: this.attackNum,
            life: this.userDamage
          }
        })
      },
      timeUp () {
        // タイマーの停止
        clearInterval(this.time.timer)

        // 結果画面に遷移
        this.$router.push({
          name: 'Result',
          query: {
            result: 'lose',
            time: this.time.limit,
            damage: this.damage,
            attackNum: this.attackNum
          }
        })
      }
    },
    mounted () {
      // IPアドレスの取得
      const deviceID = 'D0001'
      firebase.database().ref('/devices/' + deviceID).once('value').then((snapshot) => {
        const server = (snapshot.val() && snapshot.val().server) || 'Anonymous';
        const uri = 'ws://' + server + ':50000'

        // ソケットサーバへ接続
        this.connection = new WebSocket(uri)
        this.connection.onopen = this.onOpen
        this.connection.onmessage = this.onMessage
      })

      // タイムアップ時間を設定
      this.time.timer = setInterval(
        () => {
          // 時間を加算
          this.time.count += 0.01

          // タイムアップ時に終了
          if (this.time.count >= this.time.limit) {
            this.timeUp()
          }
        },
        10
      )

      // タイマーの停止
      // clearInterval(this.time.timer)
    },
    beforeDestroy () {
      // タイマーの停止
      clearInterval(this.time.timer)
      // サソリの停止
      this.connection.send('{"mode":"move","pattern":"stop"}')
      // ソケットのクローズ
      this.connection.close()
    }
  }
</script>

<style scoped lang="scss">
  #title {
    margin-bottom: 50px;
  }

  // サソリのスタイル
  #scorpion {
    display: inline-block;
    width: 45%;
    text-align: center;
    vertical-align: top;

    img {
      margin: -100px auto -50px;
      height: 450px;
    }

    #scorpion_life {
      display: block;
      width: 100%;
      height: 30px;
      margin: 0;
      border-radius: 10px 0 0 10px;
      background: #001021;
      overflow: hidden;
      border: solid 3px #b5b5bf;

      span {
        display: block;
        background: red;
        height: 100%;
        -webkit-transition: all 0.3s ease;
        -moz-transition: all 0.3s ease;
        -o-transition: all 0.3s ease;
        transition: all  0.3s ease;
      }
    }
  }

  // サソリのスタイル
  #user {
    display: inline-block;
    width: 45%;
    text-align: center;
    vertical-align: top;

    img {
      height: 300px;
    }

    #user_life {
      display: block;
      width: 100%;
      height: 30px;
      margin: 0;
      border-radius: 0 10px 10px 0;
      background: #001021;
      overflow: hidden;
      border: solid 3px #b5b5bf;
      text-align: right;

      span {
        display: inline-block;
        background: #007cff;
        height: 100%;
        -webkit-transition: all 0.3s ease;
        -moz-transition: all 0.3s ease;
        -o-transition: all 0.3s ease;
        transition: all  0.3s ease;
      }
    }
  }

</style>