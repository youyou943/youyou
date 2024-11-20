<template>
<div>
  <div class="historytitle">
    <el-icon :size="40">
      <ArrowRight />
    </el-icon>
    <el-icon :size="40">
      <User />
    </el-icon>
    <h2>训练详情</h2>
  </div>
  <div class="table-container">
    <h3>{{ userName }}</h3>
    <el-table :data="tableData" stripe style="width: 950px" class="mb-0">
      <el-table-column prop="time" label="日期" />
      <el-table-column prop="trainingScene" label="练习场景" />
      <el-table-column prop="score" label="分数" />
      <el-table-column label="操作">
     <template #default="scope">
      <el-button type="primary" round @click="viewDetails(scope.row.time)">查看详情</el-button>
    </template>
      </el-table-column>
    </el-table>
  </div>

  </div>
</template>

<script>
import axios from 'axios';
import { compileScript } from 'vue/compiler-sfc';
import { useStore } from 'vuex';
export default {
  data() {
    return {
      userName: '用户姓名', // 假设从其他地方获取用户名称
      tableData: [], // 用于存放从后端获取的数据
      userId: null,
     
    };
  },
  mounted() {
     this.userId = localStorage.getItem('userId'); 
    console.log("this.userId",this.userId)
    // 请求后端数据
    //http://10.21.30.30:8080/history/getAllTrainById
    axios.get('http://10.21.30.30:8080/history/getAllTrainById', {
      params: {
        userId: this.userId // 假设有 userId 需要传递
        //userId:'2212190521'
      }
    })
    .then(response => {
      // 将获取的数据赋值给 tableData
      this.tableData = response.data.history;
      console.log(response.data.history);
    })
    .catch(error => {
      console.error('数据获取失败:', error);
    });
  },
  methods:{
    viewDetails(time) {
      console.log("查看详情", time);
    // 将日期转换为时间戳
      const timestamp = new Date(time).getTime();
      console.log(timestamp);


    // 跳转到detialPage并传递 time 和 userId 参数
    this.$router.push({
      path: '/history/detialPage', 
      query: {
        time: timestamp,
      }
    });
   
    }



  },
};
</script>

<style scoped>
.table-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* background-image: url('/public/img/bc1.png'); */
  padding: 20px;
  padding-top: 30px;
}

.historytitle {
  padding: 20px;
  padding-left: 70px;
  padding-bottom: 0px;
  display: flex;
  align-items: center;
}

.el-table {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

th,
td {
  text-align: center;
  padding: 8px;
}

th {
  background-color: #d1bf7b;
  font-weight: 800;
}

.el-dialog {
  position: fixed; /* 使弹窗固定定位 */
  z-index: 9999 !important; /* 强制设置较高的 z-index */
}

</style>