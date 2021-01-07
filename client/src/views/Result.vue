<template>
  <div id="result">
    <img
      v-if="this.$route.query.result === 'win'"
      src="../assets/img/win.png">
    <img
      v-else
      src="../assets/img/lose.png">

    <table>
      <tr>
        <td>タイム</td>
        <td>{{ result.time }}</td>
      </tr>
      <tr>
        <td>スコア</td>
        <td>{{ result.time }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'Result',
    data () {
      return {
        result: {
          result: '',
          time: 0
        }
      }
    },
    methods: {

    },
    mounted () {
      // 勝利/敗北の判定
      this.result = this.$route.query
      if (this.$route.query.result === 'win') {
        // 勝利
      } else {
        // 敗北
      }

      // 表示終了時間
      const timer = setTimeout(
        () => {
          // ホーム画面へ戻る
          this.$router.push('/')
        },
        15000
      )

      // デバッグ用
      clearTimeout(timer)
    }
  }
</script>

<style scoped lang="scss">

</style>