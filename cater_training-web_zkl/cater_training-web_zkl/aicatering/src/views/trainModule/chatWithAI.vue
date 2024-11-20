<template>
  <el-container class="chat-page">
    <!-- 怒气值显示区域 -->
    <div class="anger-bar-container">
      <el-progress :percentage="angerLevel" :status="angerLevel > 20 ? 'exception' : 'success'" show-text
        stroke-width="18">
        <!-- 显示当前怒气值 -->
        <div class="anger-level-text">
          当前怒气值: {{ angerLevel }}
        </div>
      </el-progress>
    </div>

    <!-- 主聊天区域 -->
    <el-main class="chat-container">
      <div class="messages">
        <div
      v-for="(msg, index) in messages"
      :key="index"
      :class="['message-row', msg.sender === 'user' ? 'user-row' : 'ai-row']"
    >
      <el-avatar :src="msg.sender === 'user' ? userAvatar : aiAvatar" size="40" class="avatar"></el-avatar>

      <!-- AI 消息显示 -->
    <div v-if="msg.sender === 'ai'" :class="['message-bubble', 'ai-bubble']">
      
      <!-- 图标容器 -->
  <div class="ai-bubble-icons" style="display: flex; align-items: center; justify-content: flex-start;">
    
    <!-- 语音播放图标，使用 flex-grow 让其宽度更大 -->
    <div class="icon-container" style="flex-grow: 1; display: flex; justify-content: flex-start;">
      <svg t="1731662797244" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6877" width="40" height="40" @click="speak(msg.text)">
        <path d="M670.72 159.168a48 48 0 1 0-67.84 67.84 398.592 398.592 0 0 1 117.12 282.88 398.592 398.592 0 0 1-117.12 282.88 48 48 0 1 0 67.84 67.84 494.592 494.592 0 0 0 145.28-350.72c0-136.96-55.552-260.992-145.28-350.72z" p-id="6878" fill="#cdcdcd"></path>
        <path d="M444.48 317.44a48 48 0 0 1 67.84 0A271.36 271.36 0 0 1 592 509.76a271.36 271.36 0 0 1-79.68 192.32 48 48 0 0 1-67.84-67.84 175.296 175.296 0 0 0 51.52-124.48c0-48.64-19.648-92.544-51.52-124.416a48 48 0 0 1 0-67.904zM320 573.888a64 64 0 1 0 0-128 64 64 0 0 0 0 128z" p-id="6879" fill="#cdcdcd"></path>
      </svg>
    </div>
    
    <!-- 显示文字按钮 -->
    <div class="icon-container" style="flex-shrink: 0;">
      <svg t="1731412105417" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4422" width="30" height="30" @click="toggleText(msg)" style="transform: translateY(-6px);">
        <path d="M464.213333 87.637333h-1.024a200.405333 200.405333 0 0 0 1.024 0z m203.306667 199.722667c0-110.421333-89.6-200.746667-199.765333-201.984L465.493333 85.333333a202.538667 202.538667 0 0 0-202.069333 202.026667v189.44a202.538667 202.538667 0 0 0 202.069333 202.026667l4.864-0.042667c109.397333-2.858667 197.162667-92.757333 197.162667-201.984v-189.44z m-234.837333 622.976l0.085333 2.389333v0.085334a32.725333 32.725333 0 0 0 65.450667-2.474667v-96.768a349.013333 349.013333 0 0 0 78.549333-16.512c-8.533333-15.786667-13.354667-33.664-13.354667-53.418667 0-3.968 0.085333-7.765333 0.256-11.392a284.8 284.8 0 0 1-98.176 17.322667c-150.016 0-271.957333-115.456-271.957333-255.232a32.768 32.768 0 0 0-65.536 0c0 166.4 134.656 303.445333 304.682667 319.232v96.768z m65.536 0l-2.304 0.085333v-0.085333h2.304z m-32.725334-759.466667c75.008 0 136.533333 61.482667 136.533334 136.533334v189.397333a137.045333 137.045333 0 0 1-132.992 136.490667H465.066667c-74.581333 0-136.106667-61.44-136.106667-136.490667v-189.44c0-75.008 61.525333-136.533333 136.533333-136.533333z m134.784 521.728h113.877334a216.192 216.192 0 0 0-21.589334-28.928l-5.802666-6.570666 43.733333-15.786667 2.645333 3.413333c10.410667 13.653333 19.968 29.610667 28.629334 47.872h115.072v43.008h-46.72c-13.781333 41.386667-33.194667 76.501333-58.368 105.514667 29.269333 22.314667 65.237333 41.045333 107.733333 56.746667l7.04 2.56-24.021333 36.906666-4.48-1.706666c-46.336-17.365333-85.333333-38.698667-116.949334-64.085334-33.493333 28.544-74.24 49.621333-121.856 63.061334l-4.352 1.237333-23.296-38.229333 7.808-2.005334c44.288-11.434667 81.237333-28.885333 110.677334-52.394666a271.530667 271.530667 0 0 1-62.848-107.605334h-46.933334v-43.008z m140.373334 121.173334a244.352 244.352 0 0 0 44.544-78.165334h-95.146667c11.349333 29.141333 28.16 55.082667 50.645333 78.208z" p-id="4423" fill="#bfbfbf"></path>
      </svg>
    </div>
    
  </div>
      
        <!-- 动态显示的消息文字 -->
         <div v-if="msg.showText" class="message-text">{{ msg.text }}</div>
      

    </div>

    <!-- 用户消息显示 -->
    <div v-if="msg.sender === 'user'" :class="['message-bubble', 'user-bubble']">
       <div v-if="msg.type === 'audio'" >
             <!-- 音频播放控件 -->
            <audio :src="msg.content" controls ></audio> 
              <!-- "显示文字"按钮和消息文字 -->
              <svg t="1731412105417" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4422" width="30" height="30" @click=toggleText(msg) style="transform: translateY(-8px);"><path d="M464.213333 87.637333h-1.024a200.405333 200.405333 0 0 0 1.024 0z m203.306667 199.722667c0-110.421333-89.6-200.746667-199.765333-201.984L465.493333 85.333333a202.538667 202.538667 0 0 0-202.069333 202.026667v189.44a202.538667 202.538667 0 0 0 202.069333 202.026667l4.864-0.042667c109.397333-2.858667 197.162667-92.757333 197.162667-201.984v-189.44z m-234.837333 622.976l0.085333 2.389333v0.085334a32.725333 32.725333 0 0 0 65.450667-2.474667v-96.768a349.013333 349.013333 0 0 0 78.549333-16.512c-8.533333-15.786667-13.354667-33.664-13.354667-53.418667 0-3.968 0.085333-7.765333 0.256-11.392a284.8 284.8 0 0 1-98.176 17.322667c-150.016 0-271.957333-115.456-271.957333-255.232a32.768 32.768 0 0 0-65.536 0c0 166.4 134.656 303.445333 304.682667 319.232v96.768z m65.536 0l-2.304 0.085333v-0.085333h2.304z m-32.725334-759.466667c75.008 0 136.533333 61.482667 136.533334 136.533334v189.397333a137.045333 137.045333 0 0 1-132.992 136.490667H465.066667c-74.581333 0-136.106667-61.44-136.106667-136.490667v-189.44c0-75.008 61.525333-136.533333 136.533333-136.533333z m134.784 521.728h113.877334a216.192 216.192 0 0 0-21.589334-28.928l-5.802666-6.570666 43.733333-15.786667 2.645333 3.413333c10.410667 13.653333 19.968 29.610667 28.629334 47.872h115.072v43.008h-46.72c-13.781333 41.386667-33.194667 76.501333-58.368 105.514667 29.269333 22.314667 65.237333 41.045333 107.733333 56.746667l7.04 2.56-24.021333 36.906666-4.48-1.706666c-46.336-17.365333-85.333333-38.698667-116.949334-64.085334-33.493333 28.544-74.24 49.621333-121.856 63.061334l-4.352 1.237333-23.296-38.229333 7.808-2.005334c44.288-11.434667 81.237333-28.885333 110.677334-52.394666a271.530667 271.530667 0 0 1-62.848-107.605334h-46.933334v-43.008z m140.373334 121.173334a244.352 244.352 0 0 0 44.544-78.165334h-95.146667c11.349333 29.141333 28.16 55.082667 50.645333 78.208z" p-id="4423" fill="#bfbfbf"></path></svg>
        </div>

        <!-- 动态显示的消息文字 -->
         <div v-if="msg.showText" class="message-text">{{ msg.text }}</div>
    </div>
    </div>
      </div>
    </el-main>

    <!-- 输入区域 -->
    <el-footer class="input-area">
      <div v-if="!isVoiceInputActive" class="input-container">
        <svg t="1731248682086" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5563" width="45" height="45" @click="activateVoiceInput"><path d="M512 64c247.424 0 448 200.576 448 448S759.424 960 512 960 64 759.424 64 512 264.576 64 512 64z m0 68c-209.868 0-380 170.132-380 380s170.132 380 380 380 380-170.132 380-380-170.132-380-380-380z m52.766 130.24c12.33-12.32 32.298-12.32 44.625-0.005l0.018 0.019 4.026 4.133c131.545 137.211 131.4 354.035-0.317 491.07l-4.073 4.17-0.342 0.348c-5.74 5.758-13.6 9.025-21.802 9.025a30.85 30.85 0 0 1-22.19-9.419c-11.208-11.926-11.208-30.444-0.044-42.324l0.097-0.1 3.343-3.404c109.19-113.003 109.2-292.426 0.033-405.442l-3.376-3.438-0.365-0.372c-11.943-12.356-11.821-32.055 0.367-44.261z m-115.333 89.643c11.818-10.51 29.644-10.51 41.463-0.003l0.462 0.418 0.096 0.1 2.53 2.652c82.68 88.053 82.688 225.361 0.026 313.424l-2.672 2.799-0.124 0.11-0.358 0.316c-11.864 10.301-29.51 10.302-41.376 0.003l-0.533-0.472-0.157-0.171-0.325-0.36c-10.61-11.942-10.502-30.015 0.325-41.832l0.132-0.138 1.892-1.933c61.805-64.168 61.812-165.846 0.019-230.022l-1.998-2.04-0.083-0.092-0.318-0.361c-10.4-11.99-10.294-29.879 0.318-41.747l0.154-0.172 0.17-0.157z m-128.057 125.89c13.666-13.46 34.104-17.488 51.906-10.157C391.264 475.02 403 492.549 403 512c0 19.452-11.736 36.98-29.718 44.385a47.973 47.973 0 0 1-51.93-10.182l-0.413-0.412-0.425-0.427A47.64 47.64 0 0 1 306.889 512a47.658 47.658 0 0 1 13.675-33.413l0.4-0.403z" fill="#cdcdcd" p-id="5564"></path></svg>
        <el-input v-model="userInput" placeholder="请输入您的消息" class="input-box" @keyup.enter="sendMessage"></el-input>
        <el-button type="primary" @click="sendMessage">发送</el-button>
        <!--<el-button type="success" @click="activateVoiceInput">语音输入</el-button>-->
        <el-button type="danger" @click="finishTraining">结束训练</el-button>
      </div>

      <div v-else class="voice-input-container" >
        <svg t="1731248623141" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4460" width="35" height="35" @click="deactivateVoiceInput"><path d="M512 64A448 448 0 1 0 960 512 448.5 448.5 0 0 0 512 64z m0 832a384 384 0 1 1 384-384 384.5 384.5 0 0 1-384 384z" fill="#bfbfbf" p-id="4461"></path><path d="M320 400m-48 0a48 48 0 1 0 96 0 48 48 0 1 0-96 0Z" fill="#bfbfbf" p-id="4462"></path><path d="M448 448A48 48 0 1 0 400 400a48 48 0 0 0 48 48zM576 352a48 48 0 1 0 48 48 48 48 0 0 0-48-48zM704 352a48 48 0 1 0 48 48 48 48 0 0 0-48-48z" fill="#bfbfbf" p-id="4463"></path><path d="M320 528m-48 0a48 48 0 1 0 96 0 48 48 0 1 0-96 0Z" fill="#bfbfbf" p-id="4464"></path><path d="M448 576a48 48 0 1 0-48-48 48 48 0 0 0 48 48zM576 640H448a48 48 0 0 0 0 96h128a48 48 0 1 0 0-96zM576 480a48 48 0 1 0 48 48 48 48 0 0 0-48-48zM704 480a48 48 0 1 0 48 48 48 48 0 0 0-48-48z" fill="#bfbfbf" p-id="4465"></path></svg>
          
        <!--<voiceTotext></voiceTotext>-->
          <!-- 麦克风图标 -->
        <img src="/public/img/mico.gif" alt="" style="width: 150px; height: auto;" @click="translationStart">
       
        <el-button type="warning" @click="translationEnd">取消</el-button>
        
      </div>
    </el-footer>
  </el-container>
</template>

<script>
import IatRecorder from '@/assets/js/IatRecorder.js'
const iatRecorder = new IatRecorder('en_us', 'mandarin', '5f27b6a9');
export default {
  /*props: {
    sceneName: String,
    trainLevel: String,
    userId: String,
  },*/
  data() {
    
    return {
      userInput: '',
      messages: [],
      angerLevel: this.getInitialAngerLevel(),
      userAvatar: 'https://img1.baidu.com/it/u=2489377995,2650947137&fm=253&fmt=auto&app=138&f=JPEG?w=475&h=475', // 用户头像
      aiAvatar: 'https://img2.baidu.com/it/u=1181520836,3159211372&fm=253&fmt=auto&app=138&f=PNG?w=332&h=332', // AI 头像
      socket: null,
      trainingFinished: false, // 标记训练是否结束
      isVoiceInputActive: false,//是否激活语音输入
      sceneName: '',
      trainLevel: '',
      userId: '',
      textToSpeech: '',
      speechToText: '',
      errorMsg: '',
      speech: null,
      recognition: null,   
      mediaRecorder: null,    // MediaRecorder 实例
      audioChunks: [],        // 存储音频数据块
      audioURL: null,         // 音频 URL，用于播放
      resultText: '',  // 用于显示识别结果的响应式数据
    };
  },
  mounted() {
     const trainLevel = this.$route.query.trainLevel;
    console.log('trainLevel:', trainLevel);
    this.trainLevel = trainLevel;
   // Initialize SpeechSynthesis and SpeechRecognition
        this.speech = new SpeechSynthesisUtterance();
        try {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
          this.recognition = new SpeechRecognition();
            this.recognition.lang = 'zh-CN';
        } catch (e) {
            this.errorMsg = "This device does not support the Web Speech API";
        }

    this.userId = localStorage.getItem('userId'); 
    console.log("this.userId", this.userId)

    // 初始化 WebSocket 连接
    this.socket = new WebSocket(`ws://10.21.30.30:8080/train/startChat?userId=${this.userId}`);
    //this.socket = new WebSocket(`ws://10.234.0.132:8080/train/startChat?userId=2212190521`);
    this.socket.onopen = () => {
      console.log('WebSocket connection established');
      // 第一次发送默认文字给后端
      this.socket.send(
        '开始对话'
     );
    };

    //获取到AI说的话
    this.socket.onmessage = (event) => {
      const response = JSON.parse(event.data);
      console.log("获取后端的返回结果",response);
      const chatData = response.message;
      console.log("chatData", chatData);
          // AI 回复消息
          this.messages.push({
            sender: 'ai',
            text: chatData,
            showText: false
          });
          console.log("消息被推入messages",this.messages); // 确认消息是否成功推入
          if (response.AngerLevel) {
            // 更新怒气值
            this.angerLevel = Math.floor(this.angerLevel) + Math.floor(response.AngerLevel);
            console.log(this.angerLevel);
          }
      

      // 检查怒气值是否小于等于20，结束对话
      if (this.angerLevel <= 0||this.angerLevel >= 60) {
        this.trainingFinished = true;
        //向后端发送结束训练的信号
         this.socket.send(
           'end training'
        );

        const time = response.endtime;
        console.log(time);
        const message = response.message.trim(); // 去掉前后的空白字符
        
        if (message === "get your message") {
           alert('训练结束，进入点评界面');
        this.$router.push({ path: '/train/chatWithAI/commentpage', query: {
        time: time,
      } },);
        }
       
      }
    };
  },
  methods: {
     //控制是否显示文本
     toggleText(msg) {
      msg.showText = !msg.showText; // 切换当前消息的显示状态
    },

    // 根据难度返回不同的初始怒气值
    getInitialAngerLevel() {      
      switch (this.trainLevel) {
        case '1':
          return 45;
        case '2':
          return 65;
        case '3':
          return 85;
        default:
          return 50;
      }
    },

    //把user在输入框里的文字送到后端，并且显示到聊天框
    sendMessage() {
      if (this.userInput.trim()) {
        // 发送用户的回答
        console.log("发送消息:", this.userInput); // 打印发送的消息
        this.socket.send(
         this.userInput        
        );

        // 将用户输入的消息添加到聊天框
        this.messages.push({
          sender: 'user',
          text: this.userInput,
          showText: true,
        });
        this.userInput = '';  // 清空输入框
      }
    },

    finishTraining() {
      this.trainingFinished = true; // 标记训练结束
      this.socket.close(); // 关闭WebSocket连接
      this.$router.push({ name: 'commentpage' }); // 跳转到点评页面
    },

     activateVoiceInput() {
      this.isVoiceInputActive = true; // 激活语音输入
    },
    deactivateVoiceInput() {
      this.isVoiceInputActive = false; // 取消语音输入
      this.userInput = ''; // 清空输入框      
      // 取消语音输入
      if (this.recognition) {
        this.recognition.stop();
      }
      if (this.mediaRecorder) this.mediaRecorder.stop();
    },

    //文字转语音
    speak(text) {
      if (window.speechSynthesis) {
        const speech = new SpeechSynthesisUtterance();
        speech.text = text;
        speech.volume = 1;
        speech.rate = 1;
        speech.pitch = 1;
        window.speechSynthesis.speak(speech);
      } else {
        console.error("Speech synthesis is not supported in this browser.");
      }
    },
    //语音转文字
  async translationStart() {
  // 请求麦克风权限并启动录音
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  this.mediaRecorder = new MediaRecorder(stream);
  this.audioChunks = [];  // 清空音频数据

  // 录音数据
  this.mediaRecorder.ondataavailable = (event) => {
    this.audioChunks.push(event.data);
  };

  // 录音结束时生成音频文件
  this.mediaRecorder.onstop = () => {
    const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
    this.audioURL = URL.createObjectURL(audioBlob);  // 生成音频文件URL

    // 将音频消息添加到聊天框
    this.messages.push({
      sender: 'user',
      text: this.resultText,
      type: 'audio',
      content: this.audioURL,
      showText: false
    });
     // 发送用户语音识别后的回答
                  this.socket.send(
                      this.resultText     
                  );
    // 自动播放录音
    const audio = new Audio(this.audioURL);
    audio.play();
  };

  // 开始录音
  this.mediaRecorder.start();
  iatRecorder.start();
},
translationEnd() {
  iatRecorder.stop();
  let finalResultCaptured = false;
  iatRecorder.onTextChange = (text) => {
    if (finalResultCaptured) return;
    this.resultText = text;
    finalResultCaptured = true;

    // 停止录音，触发 onstop 回调生成音频文件并播放
    this.mediaRecorder.stop();
  };
},



  },
  beforeDestroy() {

    // 组件销毁前关闭WebSocket连接
    if (this.socket) {
      this.socket.close();
    }
  }
};
</script>

<style scoped>
.chat-page {
  height: 90vh;
  display: flex;
  flex-direction: column;
}

.anger-bar-container {
  padding: 10px;
  background-color: #f5f5f5;
  margin-bottom: 10px;
}

.chat-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding: 20px;
  background-color: #e9e9eb;
}

.messages {
  display: flex;
  flex-direction: column;
  gap: 10px;
  overflow-y: auto;
}

.message-row {
  display: flex;
  align-items: flex-end;
  margin-bottom: 10px;
}

.user-row {
  justify-content: flex-end;
}

.ai-row {
  justify-content: flex-start;
}

.avatar {
  margin-right: 10px;
}

.user-row .avatar {
  order: 2;
  margin-left: 10px;
  margin-right: 0;
}

.message-bubble {
  max-width: 60%;
  padding: 10px;
  border-radius: 20px;
  word-wrap: break-word;
  position: relative;
}

.user-bubble {
  background-color: #dcf8c6;
  /* 用户消息气泡颜色 */
  color: black;
}

.ai-bubble {
  background-color: #f1f0f0;
  /* AI 消息气泡颜色 */
  color: black;
}

.input-area {
  display: flex;
  padding: 10px;
}

.input-container {
  display: flex;
  /* 使用 Flexbox 布局 */
  align-items: center;
  /* 垂直居中对齐 */
  flex-grow: 1;
  /* 使输入容器占据可用空间 */
}

.input-box {
  flex-grow: 1;
  /* 输入框占据剩余空间 */
  margin-right: 10px;
  /* 与按钮之间的间距 */
}

.voice-input-container {
  display: flex;
  align-items: center;
  /* 垂直居中对齐 */
}

.microphone-button {
  display: flex;
  align-items: center;
  /* 垂直居中对齐 */
}

.microphone-button svg {
  margin-right: 5px;
  /* 图标与文本之间的间距 */
}

.icon-container {
  display: flex;
  justify-content: center;
  margin-bottom: 5px;
}

.icon {
  cursor: pointer;
  fill: #006064;
  transition: transform 0.2s;
}

.icon:hover {
  transform: scale(1.1);
}

.message-bubble {
  max-width: 70%;
  padding: 10px 15px;
  border-radius: 15px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  background-color: #e0f7fa;
  color: #006064;
}

.toggle-text-btn {
  background: transparent;
  border: none;
  color: #006064;
  cursor: pointer;
  font-size: 14px;
  margin-top: 5px;
  padding: 0;
  text-decoration: underline;
}

.message-text {
  font-size: 16px;
  line-height: 1.5;
  margin-top: 8px;
}

</style>
