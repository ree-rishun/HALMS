<template>
  <div id="rule">
    <h1>あそびかた</h1>

  </div>
</template>

<script>
  export default {
    name: 'Rule',
    methods: {
      startGame () {
        this.$router.push('/game')
      }
    },
    mounted () {
      setTimeout(
        () => {
          this.startGame()
        },
        3000
      )
    }
  }
</script>

<style scoped lang="scss">

</style>