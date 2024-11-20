import { createRouter, createWebHistory } from 'vue-router'
import login from '@/views/login.vue'
import home from '@/views/Home.vue'
import register from '@/views/register.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/register',  //注册
      name: 'register',
      component: register
    },
    {
      path: '/home',
      name: 'home',
      component: home //首页
    },
    {
      path: '/train',
      name: 'train',
      component: () => import('../views/trainModule/Train.vue'),//场景训练

    },
    {
      path: '/history',
      name: 'history',
      component: () => import('../views/trainModule/HistoryTrain.vue')//历史训练
    },
    {
      path: '/history/detialPage',
      name: 'detialPage',
      component: () => import('../views/trainModule/detialPage.vue'), // 与 AI 对话
    },
    {
      path: '/rank',
      name: 'rank',
      component: () => import('../views/messagesModule/Messages.vue')//排行榜
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/profileModule/Profile.vue'),//个人信息
    },
    {
      path: '/scores',
      name: 'scores',
      component: () => import('../views/profileModule/ScoresShow.vue')//学习记录
    },
    {
      path: '/train/chatWithAI',
      name: 'chatWithAI',
      component: () => import('../views/trainModule/chatWithAI.vue'), // 与 AI 对话
      props: (route) => ({
        sceneName: route.query.sceneName,
        difficulty: route.query.difficulty,
      }),
    },
    {
      path: '/train/chatWithAI/commentpage',
      name: 'commentpage',
      component: () => import('../views/trainModule/commentpage.vue'), // 与 AI 对话
    },

  ]
})

export default router
