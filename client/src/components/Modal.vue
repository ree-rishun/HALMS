<template>
  <div id="modal">
    <h2>{{ modalMessage[message].title }}</h2>
    <p>{{ modalMessage[message].description }}</p>
  </div>
</template>

<script>
  export default {
    name: 'Modal',
    props: {
      message: {
        constructor: ''
      }
    },
    data () {
      return {
        modalMessage: {
          payment: {
            title: '支払いが完了しました',
            description: 'まもなくゲームを開始します...',
            delay: 3000,
            router: {
              route: '/rule'
            }
          },
          error: {
            title: 'エラーが発生しました',
            description: '申し訳ございませんが店員までお声がけください',
            delay: 0
          }
        }
      }
    },
    methods: {
      finishModal () {
        // 画面遷移がある場合は遷移
        if ('router' in this.modalMessage[this.message]) {
          this.$router.push(this.modalMessage[this.message].router.route)
        }

        // 終了処理
        this.$emit('finish')
      }
    },
    mounted () {
      console.log(this.modalMessage[this.message].delay)
      console.log(this.message)
      console.log('------')

      if (this.modalMessage[this.message].delay !== 0) {
        setTimeout(
          () =>  {
            this.finishModal()
          },
          this.modalMessage[this.message].delay
        )
      }
    }
  }
</script>

<style scoped lang="scss">
  #modal {
    position: fixed;
    top: 40vh;
    left: 20vw;
    display: block;
    height: 20vh;
    width: 60vw;
    background: #b5b5bf;
    border-radius: 10px;
    color: #001021;
    text-align: center;

    h2 {
      font-size: 2rem;
      line-height: 6vh;
    }
    p {
      font-size: 1.5rem;
      line-height: 3vh;
    }
  }
</style>