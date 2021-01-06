<template>
  <div id="app">
    <router-view/>
    <modal
      :message="modalMessage"/>
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
        modalMessage: {
          title: '支払いが完了しました',
          description: 'まもなくゲームを開始します'
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
          this.$router.push(message.link)
        }

        // 
      }
    },
    mounted() {
      const uri = 'ws://192.168.0.23:50000'
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  margin: 0;
}
</style>
