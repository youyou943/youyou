<template>
  <div class="home-container">
    <!-- <img :src="backgroundImage" alt="Background" class="background-image" /> -->
    <button class="train-button" @click="goToTrainPage">立即训练</button>
  </div>
</template>

<script>
export default {
  name: 'home',
  data() {
    return {
      //backgroundImage: '/public/img/homeimg.png', // 背景图片路径
    };
  },
  methods: {
    goToTrainPage() {
      this.$router.push('/train');
      console.log('wem');
    },
  },
};
</script>

<style scoped>
.home-container {
  position: relative;
  height: 100vh; /* 视口高度 */
  background-image: url('/public/img//homeimg.png');
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.background-image {
  position: absolute;
  width: 100%;
  object-fit: cover;
}

.train-button {
  padding: 20px 40px;
  font-size: 18px;
  color: white;
  background-color: #42b983;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.train-button:hover {
  background-color: #368b75;
}
</style>