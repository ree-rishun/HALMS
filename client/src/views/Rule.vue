<template>
  <div id="rule">
    <img
      id="title"
      src="../assets/img/rule.png">

    <div
      v-if="state === 0"
      class="description">
      <img
        src="../assets/img/rabit_attack.png">
      <p>
        コントローラの上で手をスライドさせると手裏剣が飛びます。<br>
        手裏剣を沢山投げて敵を倒しましょう。
      </p>
    </div>
    <div
      v-if="state === 1"
      class="description">
      <img
        src="../assets/img/rabit_jump.png">
      <p>
        足場が黄色に点滅した場合、そこは敵の攻撃範囲です。<br>
        足場が赤色に変化する前に他の足場に移りましょう。
      </p>
    </div>
    <div
      v-if="state === 2"
      class="description">
      <img
        src="../assets/img/rabit_read.png">
      <p>
        制限時間以内に倒しましょう。<br>
        制限時間を超える、自身の体力を失った場合は負けになります。
      </p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Rule',
    data () {
      return {
        time: {
          timer: null,
          interval: 5000
        },
        state: 0
      }
    },
    methods: {
      startGame () {
        clearInterval(this.time.timer)
        this.$router.push('/game')
      },
      changeState () {
        this.state++
        if (this.state === 3) {
          this.startGame()
        }
      }
    },
    mounted () {
      this.time.timer = setInterval(
        () => {
          this.changeState()
        },
        this.time.interval
      )
    },
    destroyed () {
      clearInterval(this.time.timer)
    }
  }
</script>

<style scoped lang="scss">
  .description {
    img {
      height: 50vh;
    }
    p {
      margin-top: 40px;
      font-size: 2rem;
      font-family: "HG行書体", monospace;
    }
  }
</style>