<template>
  <div>
    <div v-if="isTrainPage || isHistoryPage" class="sidebar">
      <sidebar-menu
        :menu-items="trainMenuItems"
        :active-text-color="activeTextColor"
        :background-color="backgroundColor"
        :text-color="textColor"
        @menu-click="handleMenuClick"
      />
    </div>
    <div v-if="isProfilePage || isScoresPage" class="sidebar">
      <sidebar-menu
        :menu-items="profileMenuItems"
        :active-text-color="activeTextColor"
        :background-color="backgroundColor"
        :text-color="textColor"
        @menu-click="handleMenuClick"
      />
    </div>
  </div>
</template>

<script>
import { computed, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import SidebarMenu from '@/util/SidebarMenu.vue';
import { Document, Menu, Setting } from '@element-plus/icons-vue';

export default {
  components: {
    SidebarMenu
  },
  setup() {
    const route = useRoute();
    const router = useRouter();

    const activeTextColor = ref('#ffd04b');
    const backgroundColor = ref('#36373E');
    const textColor = ref('#fff');

    const isTrainPage = computed(() => {
      return route.path.startsWith('/train');
    });

     const isHistoryPage = computed(() => {
      return route.path.startsWith('/history');
    });

    const isProfilePage = computed(() => {
      return route.path.startsWith('/profile');
    });
    const isScoresPage = computed(() => {
      return route.path.startsWith('/scores');
    });

    const handleMenuClick = (route) => {
      router.push(route);
    };

    const trainMenuItems = ref([
      { index: '1', icon: Menu, label: '场景训练', route: '/train' },
      { index: '2', icon: Document, label: '历史记录', route: 'history' }
    ]);

    const profileMenuItems = ref([
      { index: '1', icon: Setting, label: '基本信息', route: '/profile' },
      { index: '2', icon: Document, label: '成绩曲线', route: 'scores' }
    ]);

    return {
      activeTextColor,
      backgroundColor,
      textColor,
      isTrainPage,
      isProfilePage,
      isHistoryPage,
      isScoresPage,
      handleMenuClick,
      trainMenuItems,
      profileMenuItems
    };
  }
};
</script>

<style scoped>
.sidebar {
  position: fixed; /* 固定在左侧 */
  top: 68px;
  left: 0;
  width: 180px; /* 侧边栏宽度 */
  height: 100%; 
  background-color: rgb(54, 55, 62); /* 背景颜色 */
  box-shadow: 2px 0 5px rgba(0,0,0,0.1); /* 阴影效果 */
  padding: 20px; /* 内边距 */
  font-size: 20px;
}

.sidebar-item {
  margin: 10px 0; /* 项目间距 */
}

.router-link {
  text-decoration: none; /* 移除下划线 */
  color: #333; /* 文字颜色 */
  font-size: 1rem; /* 字体大小 */
  padding: 10px; /* 内边距 */
  display: block; /* 块级显示 */
  border-radius: 5px; /* 圆角 */
}

.router-link:hover {
  background-color: #ddd; /* 悬停背景颜色 */
}
</style>
