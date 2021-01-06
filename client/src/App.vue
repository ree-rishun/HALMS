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
      const uri = 'ws://172.20.10.7:50000'
      this.connection = new WebSocket(uri)
      this.connection.onopen = this.onOpen
      this.connection.onmessage = this.onMessage
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
