<template>
  <div id="result">
    <h2 v-if="result.result === 'win'">勝利</h2>
    <h2 v-else>敗北</h2>

    <div>
      タイム：{{ result.time }}

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
          time: 0
        }
      }
    },
    methods: {

    },
    mounted () {
      // 勝利/敗北の判定
      if (this.$route.query.result === 'win') {
        // 勝利
      } else {
        // 敗北
      }

      // 表示終了時間
      setTimeout(
        () => {
          // ホーム画面へ戻る
          this.$router.push('/home')
        },
        15000
      )
    }
  }
</script>

<style scoped lang="scss">

</style>