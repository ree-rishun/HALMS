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
      <span :style="'width: ' + life + '%'"></span>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'GameUI',
    data () {
      return {
        life: 100
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
          this.life -= message.damage
        }
      }
    },
    mounted () {
      const uri = 'ws://172.20.10.7:50000'
      this.connection = new WebSocket(uri)
      this.connection.onopen = this.onOpen
      this.connection.onmessage = this.onMessage
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