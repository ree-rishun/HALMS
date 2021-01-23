<template>
  <div id="result">
    <img
      v-if="this.$route.query.result === 'win'"
      src="../assets/img/win.png">
    <img
      v-else
      src="../assets/img/lose.png">

    <img
      class="result_image"
      v-if="this.$route.query.result === 'win'"
      src="../assets/img/rabit_win.png">
    <img
      class="result_image"
      v-else
      src="../assets/img/rabit_dead.png">

    <div id="result_score">
      <h3>討伐時間</h3>
      <p>{{ Math.round(result.time * 100) / 100 }}秒</p>

      <h3>投げた手裏剣の数</h3>
      <p>{{ result.attackNum !== 0 ? result.attackNum : 0 }}回</p>

      <h3>与えたダメージ</h3>
      <p>{{ result.damage !== 0 ? result.damage : 0 }}</p>

      <h3>受けたダメージ</h3>
      <p>{{ result.life !== 0 ? result.life : 0 }}</p>

      <div id="result_score__score">
        <h3>合計得点</h3>
        <p>{{ score }}</p>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Result',
    data () {
      return {
        result: {
          result: '',
          time: 0,
          damage: 0,
          attackNum: 1
        },
        bgm: null,
        score: 0,
        time: {
          timer: null,
          duration: 14000
        }
      }
    },
    methods: {
      calcScore () {
        console.log('score')
        console.log(this.result)
        // タイムを加算
        this.score += Math.round((60 - this.result.time) * 1000)

        // 攻撃回数を加算
        this.score += (this.result.attackNum / 20) * 10000

        // ダメージを加算
        this.score += Number(this.result.damage)
      }
    },
    mounted () {
      // 勝利/敗北の判定
      this.result = this.$route.query
      if (this.$route.query.result === 'win') {
        // 勝利
      } else {
        // 敗北
      }

      this.calcScore()

      setTimeout(
        () => {
          this.bgm.play()
        },
        10
      )

      // 表示終了時間
      this.time.timer = setTimeout(
        () => {
          // ホーム画面へ戻る
          this.$router.push('/')
        },
        this.time.duration
      )

      // デバッグ用
      // clearTimeout(this.time.timer)
    },
    destroyed () {
      clearTimeout(this.time.timer)
    }
  }
</script>

<style scoped lang="scss">
  #result_score {
    margin-right: 40px;
    h3, p {
      text-align: right;
    }
    h3 {
      font-size: 1rem;
      line-height: 1rem;
      height: 1rem;
      margin-top: 20px;
    }
    p {
      font-size: 3.5rem;
      line-height: 3.5rem;
      height: 3.5rem;
    }

    #result_score__score {
      h3 {
        font-size: 2rem;
        line-height: 2rem;
        height: 2rem;
      }
      p {
        font-size: 7rem;
        line-height: 7rem;
      }
    }
  }

  .result_image {
    position: fixed;
    bottom: 10vh;
    left: 50px;
  }
</style>