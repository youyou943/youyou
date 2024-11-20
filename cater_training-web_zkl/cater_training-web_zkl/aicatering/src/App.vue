<script setup>
import { RouterLink, RouterView } from 'vue-router'
import SideBar  from './components/SideBar.vue';
import ElementBar from './components/ElementBar.vue'
</script>

<template>
  <el-container>
      <el-header><ElementBar />  </el-header>
      <el-container>
        <el-aside ><SideBar/> </el-aside>
        <el-main><RouterView /></el-main>
      </el-container>
    </el-container>
</template>


