<template>
  <div id="home" @click="$router.push('/rule')">
    <img
      id="logo"
      src="../assets/img/logo_wh.png">
    <p>- ICカードをタッチしてスタート -</p>
  </div>
</template>

<script>

export default {
  name: 'Home',
  mounted () {
    // サソリの再開
    this.connection.send('{"mode":"move","pattern":"play"}')
  }
}
</script>

<style scoped lang="scss">
  @keyframes blink{
    0% {opacity:0;}
    100% {opacity:1;}
  }
  #home {
    display: block;
    width: 100%;
    height: 100vh;
  }

  #logo {
    display: block;
    width: 100%;
    height: auto;
    padding: 60px 0 60px;
  }
  p {
    color: #b5b5bf;
    animation:blink 1s ease-in-out infinite alternate;
  }
</style>