<template>
  <el-row class="tac">
    <el-col>
      <el-menu
        :active-text-color="activeTextColor"
        :background-color="backgroundColor"
        class="el-menu-vertical-demo"
        :default-active="defaultActive"
        :text-color="textColor"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-menu-item v-for="item in menuItems" :key="item.index" :index="item.index" @click="handleMenuClick(item.route)">
          <el-icon><component :is="item.icon" /></el-icon>
          <span>{{ item.label }}</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'SidebarMenu',
  props: {
    menuItems: {
      type: Array,
      required: true
    },
    activeTextColor: {
      type: String,
      default: '#ffd04b'
    },
    backgroundColor: {
      type: String,
      default: '#36373E'
    },
    defaultActive: {
      type: String,
      default: '1'
    },
    textColor: {
      type: String,
      default: '#fff'
    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log('this is open',key, keyPath)
    },

    handleClose(key, keyPath){
      console.log('this is close',key, keyPath);
  },
    handleMenuClick(route) {
        this.$emit('menu-click', route);
      }
  }
};
</script>

<style scoped>
.tac {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>