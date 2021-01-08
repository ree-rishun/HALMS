<template>
  <div id="result">
    <img
      v-if="this.$route.query.result === 'win'"
      src="../assets/img/win.png">
    <img
      v-else
      src="../assets/img/lose.png">

    <div id="result_score">
      <h3>討伐時間</h3>
      <p>{{ Math.round(result.time * 100) / 100 }}秒</p>

      <h3>投げた手裏剣の数</h3>
      <p>{{ result.attackNum }}回</p>

      <h3>与えたダメージ</h3>
      <p>{{ result.damage }}</p>

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
        score: 0
      }
    },
    methods: {
      calcScore () {
        // タイムを加算
        this.score += Math.round((60 - this.result.time) * 1000)

        console.log(this.score)

        // 攻撃回数を加算
        this.score += (this.result.attackNum / 20) * 10000

        console.log(this.score)

        // ダメージを加算
        this.score += Number(this.result.damage)

        console.log(this.score)
      }
    },
    mounted () {
      // 勝利/敗北の判定
      this.result = this.$route.query
      if (this.$route.query.result === 'win') {
        // 勝利
        this.bgm = new Audio('../assets/music/win.mp3')
      } else {
        // 敗北
        this.bgm = new Audio('../assets/music/win.mp3')
      }

      this.calcScore()

      setTimeout(
        () => {
          this.bgm.play()
        },
        10
      )

      // 表示終了時間
      const timer = setTimeout(
        () => {
          // ホーム画面へ戻る
          this.$router.push('/')
        },
        15000
      )

      // デバッグ用
      // clearTimeout(timer)
    },
    destroyed () {
      this.bgm.pause()
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
</style>