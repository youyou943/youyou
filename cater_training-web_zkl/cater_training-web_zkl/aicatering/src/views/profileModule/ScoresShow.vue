<template>
  <el-container class="scores-page">
    <el-header>
      <el-select v-model="selectedScene" placeholder="选择场景" @change="fetchChatScores">
        <el-option
          v-for="(scene, index) in scenes"
          :key="index"
          :label="scene.sceneName"
          :value="scene.sceneName">
        </el-option>
      </el-select>
    </el-header>

    <el-main>
      <div class="charts-container">
         <div class="chart-row">
    <div id="chartL" style="width: 48%; height: 300px;"></div>
    <div id="chartA" style="width: 48%; height: 300px;"></div>
  </div>
  <div class="chart-row">
    <div id="chartS" style="width: 48%; height: 300px;"></div>
    <div id="chartT" style="width: 48%; height: 300px;"></div>
  </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts'

export default {
   name: 'echart',
  data() {
    return {
      scenes:[], // 场景数据
      selectedScene: '', // 当前选择的场景
      userId: '',
      chartOptionsArray: [], // 存储每个折线图的配置
      chatL:null,
      chatA:null ,
      chatS:null,
      chatT:null,
    };
  },
  mounted() {
    // 页面加载时获取场景类别
    this.fetchScenes();
    this.userId = localStorage.getItem('userId'); 
    console.log("this.userId", this.userId);
  },
  methods: {
    // 获取场景类别
    fetchScenes() {
      axios.get('http://127.0.0.1:4523/m1/5289681-4958794-default/train/showAllScene')
        .then(response => {
          this.scenes = response.data.scene;
          console.log(this.scenes);
        })
        .catch(error => {
          console.error('Error fetching scenes:', error);
        });
    },
    async fetchChatScores() {
      if (this.selectedScene) {
        try {
          const response = await axios.get('http://127.0.0.1:4523/m1/5289681-4958794-default/train/getTrainCurve', {
            params: {
              userId:this.userId,
              scen_name: this.selectedScene,  // 传递场景名称              
            }
          });
          // 假设返回的数据是包含分数的对象
          this.chatScores = response.data;
          console.log('获取到成绩曲线:', this.chatScores["1stTime"].L);
          this.chatL =[this.chatScores["1stTime"].L,this.chatScores["2ndTime"].L,this.chatScores["3rdTime"].L,this.chatScores["4thTime"].L];
          this.chatA= [this.chatScores["1stTime"].A, this.chatScores["2ndTime"].A, this.chatScores["3rdTime"].A, this.chatScores["4thTime"].A];
          this.chatS = [this.chatScores["1stTime"].S, this.chatScores["2ndTime"].S, this.chatScores["3rdTime"].S, this.chatScores["4thTime"].S];
          this.chatT =[this.chatScores["1stTime"].T,this.chatScores["2ndTime"].T,this.chatScores["3rdTime"].T,this.chatScores["4thTime"].T];
      // 为每个维度生成图表
      this.getChartOptions(this.chatL, 'chartL', 'L维度');
      this.getChartOptions(this.chatA, 'chartA', 'A维度');
      this.getChartOptions(this.chatS, 'chartS', 'S维度');
      this.getChartOptions(this.chatT, 'chartT', 'T维度');
        } catch (error) {
          console.error('获取成绩失败:', error);
        }
      }
    },
    getChartOptions(dataScore, chartId, title) {
       // 初始化实例
      let myChart = echarts.init(document.getElementById(chartId));
 // 绘制图表，定义数据
      let option = {
        // 设置背景为白色
        backgroundColor: 'white',
        // 定义表的标题
        title: {
          text: title
        },
        // 定义类别
        legend: {
          data: ["柱状","折线"]
        },
        // 定义提示类型
        tooltip: {
          trigger: 'axis',  // axis显示每一列的所有类别数据, item只显示单个类别
        },
        // 定义横坐标标签
        xAxis: {
          name: '训练时间',
          data: ['1stTime', '2edTime', '3thTime', '4thTime'],
          axisLabel: {
            show: true,
            textStyle: {
              color: 'black',  //更改X坐标轴文字颜色
              fontSize : 16      //更改坐标轴文字大小
            }
          }
        },
        // 定义纵坐标尺度，一般会自己变化
        yAxis: {
          name: '分',
          axisLabel: {
            show: true,
            textStyle: {
              color: 'black',  //更改Y坐标轴文字颜色
              fontSize : 16      //更改坐标轴文字大小
            }
          }
        },
        // 定义每个标签对应类别的数值
        series: [
          {
          name: '柱状',
          type: 'bar', // bar为条状图
          color: ['#dee1e6'], // 设置背景颜色
          data: dataScore
          },
          {
            name: '折线',
            type: 'line', // line为折线图
            color: ['#1f1f1f'],
            data: dataScore
          },
        ]
      }
 
      // 渲染数据
      myChart.setOption(option, true)
    },

  }
};
</script>

<style scoped>
.scores-page {
  padding: 20px;
}


.line-chart {
  width: 100%;
  height: 400px; /* 调整高度 */
}



.charts-container {
  padding: 20px; /* 可选的内边距 */
}

.image-grid {
  display: flex;          /* 使用 Flexbox 布局 */
  flex-wrap: wrap;       /* 允许换行 */
  gap: 20px;             /* 图片之间的间距 */
}

.chart-image {
  width: calc(50% - 10px);  /* 每个图片宽度为50%减去间距 */
  height: auto;              /* 高度自适应 */
}

.chart-container {
  display: flex;
  flex-direction: column; /* 垂直排列 */
  gap: 20px; /* 每行之间的间距 */
}

.chart-row {
  display: flex;
  justify-content: space-between; /* 水平排列并分配空间 */
  gap: 20px; /* 每个图表之间的间距 */
}

.chart-row div {
  flex: 1; /* 每个图表容器宽度均分 */
}

</style>
