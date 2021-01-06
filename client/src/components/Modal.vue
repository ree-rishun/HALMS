<template>
  <div id="modal">
    <h2>{{ message.title }}</h2>
    <p>{{ message.description }}</p>
  </div>
</template>

<script>
  export default {
    name: 'Modal',
    props: {
      message: {
        title: '',
        description: ''
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
      line-height: 7vh;
    }
    p {
      line-height: 3vh;
    }
  }
</style>