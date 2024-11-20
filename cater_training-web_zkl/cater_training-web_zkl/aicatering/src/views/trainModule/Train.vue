<template>
  <div class="scene-training">
    <h2>场景训练</h2>

    <!-- 场景展示 -->
    <el-row :gutter="20">
      <el-col :span="8" v-for="scene in scenes" :key="scene.id">
        <el-card class="scene-card" @click="selectScene(scene)">
          <h3>{{ scene.sceneName }}</h3>
          <p>{{ scene.sceneProfile }}</p>
        </el-card>
      </el-col>
    </el-row>

    <!-- 难度选择对话框 -->
    <el-dialog title="选择训练难度" v-model="isDifficultyDialogVisible">
      <el-form>
        <el-form-item label="难度选择">
          <el-radio-group v-model="trainLevel">
            <el-radio label="1">简单</el-radio>
            <el-radio label="2">中等</el-radio>
            <el-radio label="3">困难</el-radio>
          </el-radio-group>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="isDifficultyDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="startTraining">开始训练</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
import axios from 'axios';

export default {
   name: 'ChatWithAI',
  data() {
    return {
      scenes: [], // 场景数据
      isDifficultyDialogVisible: false, // 控制难度选择窗口的显示
      selectedScene: null, // 记录选中的场景
      trainLevel: '1', // 记录选择的难度
      userId: '2212190521',
    };
  },
  mounted() {
    // 请求展示现有场景
    this.showAllScenes();
     this.userId = localStorage.getItem('userId'); 
    console.log("this.userId", this.userId)
  },
  methods: {
    // 请求展示所有场景
    showAllScenes() {
      //http://10.21.30.30:8080/train/showAllScene
      axios.get('http://10.21.30.30:8080/train/showAllScene')
        .then(response => {
          this.scenes = response.data.scene;
        })
        .catch(error => {
          console.error('Error fetching scenes:', error);
        });
    },

    // 用户点击场景后，显示难度选择窗口
    selectScene(scene) {
      
      this.selectedScene = scene.sceneName;
      console.log("选择场景", this.selectedScene);
      this.isDifficultyDialogVisible = true;
    },

    // 用户选择难度并开始训练
    startTraining() {
      if (!this.selectedScene || !this.trainLevel) {
        alert('请选择场景和难度');
        return;
      }
      console.log(this.selectedScene);
      const payload = {
        sceneName: this.selectedScene,
        trainLevel: this.trainLevel,
        userID:this.userId,
      };
    //http://10.21.30.30:8080/train/selectTrain
      axios.get('http://10.21.30.30:8080/train/selectTrain', {
      params: {
         sceneName: this.selectedScene,
        trainLevel: this.trainLevel,
        userID:this.userId,
      }
    })
        .then(response => {
            // 获取服务器返回的所有数据
          console.log('响应数据:', response);
          //response.data.status === 'start training'
          if (response.status === 200) {
            alert('场景选择成功，开始训练');
            // 跳转到大模型对话界面
            this.$router.push({
              path: '/train/chatWithAI',
              query: {
                //sceneName: this.selectedScene.sceneName,
                trainLevel: this.trainLevel,
                //userId:this.userId,
              }
            });
          }
        })
        .catch(error => {
          console.error('Error starting training:', error);
        });

      this.isDifficultyDialogVisible = false; // 关闭窗口
    }
  }
};
</script>


<style scoped>
.scene-training {
  padding: 20px;
}

.scene-card {
  cursor: pointer;
  transition: all 0.3s ease;
}

.scene-card:hover {
  transform: scale(1.05);
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
}
</style>
