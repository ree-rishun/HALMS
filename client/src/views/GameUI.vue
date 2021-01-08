<template>
  <div id="game">
    <img
      id="title"
      src="../assets/img/sasori.png">
    <img
      id="scorpion"
      src="../assets/img/sasori_img.png">

    <div
      id="scorpion_life">
      <span :style="'width: ' + ((life - damage) / 100) + '%'"></span>
    </div>
  </div>
</template>

<script>
  import firebase from 'firebase'
  export default {
    name: 'GameUI',
    data () {
      return {
        life: 10000,
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
          console.log(this.life - this.damage)
          this.damage += (Number(message.damage) * 6)
          this.attackNum++

          // ライフが0以下になった場合にゲーム終了
          if (this.life - this.damage <= 0) {
            this.scorpionDead()
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
            attackNum: this.attackNum
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
            time: this.time.limit
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
    },
    beforeDestroy () {
      this.connection.close()
    }
  }
</script>

<style scoped lang="scss">
  #title {

  }
  #scorpion {
    width: 400px;
    height: auto;
    margin-top: -120px;
  }

  #scorpion_life {
    width: 80%;
    height: 40px;
    margin: 0 10%;
    border-radius: 10px;
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
</style>