<template>
 <div class="container h-p100">
		<div class="row align-items-center justify-content-md-center h-p100">

			<div class="col-12">
				<div class="row justify-content-center no-gutters">
					<div class="col-lg-5 col-md-5 col-12">
						<div class="bg-white rounded30 shadow-lg">
							<div class="content-top-agile p-20 pb-0">
								<h2 class="text-primary">登录</h2>
								<p class="mb-0">欢迎使用</p>
							</div>
							<div class="p-40">
								<form action="index.html" method="post" @submit.prevent="login">
									<div class="form-group">
										<div class="input-group mb-3">
											<div class="input-group-prepend">
												<span class="input-group-text bg-transparent"><i
														class="ti-user"></i></span>
											</div>
											<input type="text" class="form-control pl-15 bg-transparent"
												placeholder="用户名" v-model="username">
										</div>
									</div>
									<div class="form-group">
										<div class="input-group mb-3">
											<div class="input-group-prepend">
												<span class="input-group-text bg-transparent"><i
														class="ti-user"></i></span>
											</div>
											<input type="text" class="form-control pl-15 bg-transparent"
												placeholder="工号" v-model="id">
										</div>
									</div>
									<div class="form-group">
										<div class="input-group mb-3">
											<div class="input-group-prepend">
												<span class="input-group-text  bg-transparent"><i
														class="ti-lock"></i></span>
											</div>
											<input type="password" class="form-control pl-15 bg-transparent"
												placeholder="密码" v-model="password">
										</div>
									</div>
									<div class="row">
										<div class="col-6">
											<div class="checkbox">
												<input type="checkbox" id="basic_checkbox_1">
												<label for="basic_checkbox_1">记住密码</label>
											</div>
										</div>
										<!-- /.col -->
										<div class="col-6">
											<div class="fog-pwd text-right">
												<a href="javascript:void(0)" class="hover-warning"><i
														class="ion ion-locked"></i> 忘记密码?</a><br>
											</div>
										</div>
										<!-- /.col -->
										<div class="col-12 text-center">
											<button type="submit" class="btn btn-danger mt-10">登录</button>
										</div>
										<!-- /.col -->
									</div>
								</form>
								<div class="text-center">
									<p class="mt-15 mb-0">没有账号?<router-link to="/register" class="text-warning ml-5">注册</router-link></p>
								</div>
							</div>
						</div>

					</div>
				</div>
			</div>
		</div>
	</div>

</template>

<script>
import axios from 'axios';
import { useStore } from 'vuex';
export default {
  name: 'login',
  data() {
	  return {
		id:'',
      username: '',
	  password: '',
	  socket: null, // 用于存储 WebSocket 连接
    };
	},
	mounted() {

    },
   methods: {
    login() {
      if (this.username === '' || this.password ===''||this.id==='') {
        alert('请完整输入用户名,工号和密码');
        return;
		   };
	   
		   const payload = {
			   //username: this.username,
			   password: this.password,
			   id:this.id,
		   };
		   console.log('发送的登录数据:', payload); // 打印发送的数据
		   //http://10.21.30.30:8080
		   axios.get('http://127.0.0.1:4523/m1/5289681-4958794-default/api/user/login', {
      params: {
               username: this.username,
			   password: this.password,
			   id:this.id,
      }
    })
			   .then(response => {
			   //根据返回的code处理逻辑
			   console.log("查看返回的结果",response);
			   if (response.status === 200) {
				   alert('登录成功！');
				   console.log("查看一下在localStorage里面的数据",this.id);
					// 使用 localStorage 存储 userId
				   localStorage.setItem('userId', this.id);
		
				   //登录成功后跳转到首页home
                  this.$router.push('/home'); 
			   }
			   else {
				alert(`登录失败: ${response.data.message}`);
			   }
		   })
		   .catch(error => {
                console.error('登录请求失败:', error);
                alert('发生错误，请稍后再试');
            });

	   },
	goToRegister() {
      this.$router.push('/register'); // 跳转到注册页面
    },
  },
};
</script>


<style>
@import './static/css/vendors_css.css';
@import './static/css/style.css';
@import './static/css/skin_color.css';

/* 其他自定义样式 */
</style>