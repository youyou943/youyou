<template>
  <el-container class="comment-page">
    <!-- 第一行：训练得分 -->
    <el-header class="score-section">
      <el-card class="score-card">
        <div class="score-content">
          <h2>训练得分</h2>
          <p class="score">{{ score }}</p>
        </div>
      </el-card>
    </el-header>

    <!-- 第二行：三个板块 -->
    <div class="analysis-section">
      <el-tabs v-model="activeTab">
        <!-- 能力分析（雷达图） -->
        <el-tab-pane label="能力分析" name="ability">
          <div id="main" style="width: 800px;height:600px;"></div>
        </el-tab-pane>

        <el-tab-pane label="AI 点评" name="comment">
          <div class="tab-content">
            <div class="comment-container">
              <p class="highlight">{{ aiComment }}</p>
            </div>
          </div>
        </el-tab-pane>

       <el-tab-pane label="参考答案" name="reference">
  <div class="tab-content">
    <div class="chat-container">
      <!-- 对话列表 -->
      <div class="message" v-for="(dialogue, index) in dialogues" :key="index" :class="['message-item', dialogue.role]">
        <!-- 头像 -->
        <div class="avatar" :class="{'customer-avatar': dialogue.role === 'customer', 'user-avatar': dialogue.role === 'user'}">
          <img
            :src="dialogue.role === 'customer' ? 'https://img2.baidu.com/it/u=1181520836,3159211372&fm=253&fmt=auto&app=138&f=PNG?w=332&h=332' : 'https://img1.baidu.com/it/u=2489377995,2650947137&fm=253&fmt=auto&app=138&f=JPEG?w=475&h=475'"
            alt="头像">
        </div>
        <!-- 对话气泡 -->
        <div class="bubble" :class="{'customer-bubble': dialogue.role === 'customer', 'user-bubble': dialogue.role === 'user'}">
          <p>{{ dialogue.text }}</p>
          <!--<span class="anger-level">当前怒气值：{{ dialogue.angerLevel }}</span>-->
        </div>
      </div>
    </div>
  </div>
</el-tab-pane>

      </el-tabs>
    </div>
  </el-container>
</template>

<script>
import axios from 'axios';
import { useStore } from 'vuex';
export default {
  data() {
    return {
      dialogues: [],
      score: null,
      aiComment: '',
      referenceVersion: '',
      userId: null,
      trainingTime: null,
      aspects: null, // 存储从后端获取的分项分数
    };
  },
  mounted() {
    const time = this.$route.query.time;
    console.log('Time:', time);
    this.trainingTime = time;
   this.userId = localStorage.getItem('userId'); 
    console.log("this.userId", this.userId)
    
    // 先请求训练分数，再获取雷达图
    this.fetchTrainingScores().then(() => {
      this.fetchRadar();
    });
    this.fetchReferenceVersion();
  },
  methods: {
    // 请求训练分数
    fetchTrainingScores() {
      //http://10.21.30.30:8080
      return axios.get('http://127.0.0.1:4523/m1/5289681-4958794-default/train/getChatScores', {
        params: {
          userid: this.userId,
          time: this.trainingTime
        }
      })
        .then(response => {
          this.score = response.data.score;
          console.log("获取到了训练的总分", this.score);
          this.aspects = response.data.aspects;
          console.log("获取分项", this.aspects);
        })
        .catch(error => {
          console.error('Error fetching training scores:', error);
        });
    },

    // 获取参考答案和ai点评
    fetchReferenceVersion() {
      //http://10.21.30.30:8080
      axios.get('http://127.0.0.1:4523/m1/5289681-4958794-default/train/getChatInfo', {
        params: {
          userid: this.userId,
          time: this.trainingTime
        }
      })
        .then(response => {      
          let chat = response.data;
          
          const chat2 = chat["chat"];
          console.log("chat", chat2);
          chat2.forEach((round, index) => {
            console.log("数组循环",round);
            if (round.round === -1) {
               this.aiComment = round.message;
            }
            else {
              if (round.sender === 'customer') {
              const customerMessage = round.message;
               const roundData = {
                role: 'customer',
                text: customerMessage,
              };
              this.dialogues.push(roundData);
              }
            if (round.sender === 'specialist') {
              const bestanswer = round.bestanswer;
              console.log(bestanswer);
              const roundData = {
                role: 'user',
                text: bestanswer,
              };
              this.dialogues.push(roundData);
            }
            }
          });
        })
        .catch(error => {
          console.error('Error fetching history:', error);
        });
    },
    // 绘制雷达图
    fetchRadar() {
      const myChart = echarts.init(document.getElementById('main'));
      console.log("在雷达图中", this.aspects);

      // 将 `this.aspects` 转换为数组
      const aspectValues = [
        this.aspects?.L || 0,
        this.aspects?.A || 0,
        this.aspects?.S || 0,
        this.aspects?.T || 0
      ];

      const option = {
        title: { text: '' },
        tooltip: {},
        legend: { data: ['训练分数分项细节'] },
        radar: {
          shape: 'circle',
          radius: '60%', 
          name: {
            textStyle: {
              color: '#fff',
              backgroundColor: '#999',
              borderRadius: 1,
              padding: [3, 5]
            }
          },
          indicator: [
            { name: '仔细聆听（Listen）', max: 100 },
            { name: '真诚道歉（Apology）', max: 100 },
            { name: '满足顾客需求（Satisfaction）', max: 100 },
            { name: '表示感谢（Thanks）', max: 100 }
          ]
        },
        series: [{
          name: '训练分数分项细节',
          type: 'radar',
          data: [{
            value: aspectValues,
            name: '训练分数分项细节',
            label: {
              show: true,
              color: 'darkblue',
              fontSize: 12,
              formatter: (params) => params.value
            }
          }],
          areaStyle: {
            opacity: 0.1
          },
          emphasis: {
            label: {
              show: true,
              color: 'darkblue',
              fontSize: 12
            }
          }
        }]
      };

      myChart.setOption(option);
    }
  }
}

</script>

<style scoped>
.comment-page {
  padding: 20px;
}

.score-section {
  margin-bottom: 20px;
}

.score-card {
  text-align: center;
  background-color: #f0f9ff;
}

.score-content {
  padding: 10px;
}

.score {
  font-size: 32px;
  color: #409eff;
}

.analysis-section {
  display: flex;
  justify-content: center;
  /* 水平居中 */
  align-items: center;
  /* 垂直居中 */
  background-color: #ffffff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  margin-top: 100px;
}

.radar-chart {
  width: 100%;
  height: 600px;
  /* 或根据需要调整 */
  max-width: 800px;
  /* 设置最大宽度 */
  margin: 0 auto;
  /* 居中 */
  display: block;
  /* 确保是块级元素 */
  position: relative;
  /* 可以帮助调整定位 */
}

.tab-content {
  padding: 20px;
}







.chat-container {
  display: flex;
  flex-direction: column;
  padding: 10px;
}

.message {
  display: flex;
  align-items: flex-start;
  margin-bottom: 10px;
}

.message.user {
  flex-direction: row-reverse;  /* 用户的消息气泡右侧显示 */
  justify-content: flex-end;    /* 确保用户的气泡居右 */
  margin-left: 700px; 
}

.message.customer {
  flex-direction: row;          /* 顾客的消息气泡左侧显示 */
  justify-content: flex-start;  /* 确保顾客的气泡居左 */
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 10px;
}

.avatar img {
  width: 100%;
  height: 100%;
}

.bubble {
  max-width: 60%;
  padding: 10px;
  border-radius: 15px;
  position: relative;
  background-color: #f0f0f0;
}

.message.customer .bubble {
  background-color: #f1c40f;
   align-self: flex-start;
}

.message.user .bubble {
  background-color: #3498db;  /* 用户消息气泡背景色 */
  color: white;  /* 用户气泡文字颜色 */
  align-self: flex-end;  /* 用户气泡居右 */
  margin-right: 10px;  /* 给右边添加一定的间距，避免气泡紧贴右边缘 */
  padding: 10px;  /* 可以调整气泡内部的间距 */
  border-radius: 15px;  /* 圆角 */
  max-width: 75%;  /* 限制气泡最大宽度，不会占满整个宽度 */
}


.anger-level {
  display: block;
  font-size: 12px;
  color: gray;
  margin-top: 5px;
}




.tab-content {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  border: 1px solid #dcdcdc;
}

.comment-container {
  font-size: 16px;
  line-height: 1.8;
  color: #333;
  text-align: justify;
}

.highlight {
  font-weight: bold;
  color: #2c3e50;
}

p {
  margin-bottom: 15px;
}


</style>
