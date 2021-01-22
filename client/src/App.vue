<template>
  <div id="app">
    <router-view/>
    <modal
      v-if="modal.display"
      :message="modal.mode"
      @finish="modal.display = false"/>
  </div>
</template>

<script>
  import Modal from '@/components/Modal'
  import firebase from 'firebase'

  export default {
    name: 'room',
    components: {Modal},
    data() {
      return {
        messages: [],
        connection: null,
        modal: {
          display: false,
          mode: ''
        }
      }
    },
    methods: {
      onOpen () {
        console.log('open!')
      },
      onMessage (event) {
        console.log(event)
        const JSONmessage = event.data

        // JSONをパース
        const message = JSON.parse(JSONmessage)

        // ルーター処理の場合
        if (message.mode === 'router') {
          this.$router.push(message.route)
        }

        // モーダル表示の場合
        if (message.mode === 'modal') {
          this.modal.display = true
          this.modal.mode = message.modal
        }
      }
    },
    mounted() {
      // IPアドレスの取得
      const deviceID = 'D0001'
      firebase.database().ref('/devices/' + deviceID).once('value').then((snapshot) => {
        const server = (snapshot.val() && snapshot.val().server) || 'Anonymous';

        const uri = 'ws://' + server + ':50000'
        console.log(uri)
        this.connection = new WebSocket(uri)
        this.connection.onopen = this.onOpen
        this.connection.onmessage = this.onMessage
      });
    },
    updated () {
      console.log(this.$route)
      if (this.$route.name === 'Home') {
        this.connection.send('{"mode":"music","music":"home"}')
        // サソリの再開
        this.connection.send('{"mode":"move","pattern":"play"}')
      }
      else if (this.$route.name === 'Game') {
        this.connection.send('{"mode":"music","music":"battle"}')
      }
      else if (this.$route.name === 'Result') {
        // 勝利/敗北の判定
        if (this.$route.query.result === 'win') {
          // 勝利
          this.connection.send('{"mode":"music","music":"win"}')
        } else {
          // 敗北
          this.connection.send('{"mode":"music","music":"lose"}')
        }
      }
      else if (this.$route.name === 'Rule') {
        this.connection.send('{"mode":"music","music":"rule"}')
      }
    }
  }
</script>

<style lang="scss">
  body, html {
    background: #001021;
  }
#app {
  display: block;
  height: 100vh;
  width: 100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  margin: 0;
  background-image: url("./assets/img/background.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100vw auto;
  background-color: #001021;
  background-blend-mode:lighten;
}
</style>
