<template>
	<div class="container h-p100">
		<div class="row align-items-center justify-content-md-center h-p100">

			<div class="col-12">
				<div class="row justify-content-center no-gutters">
					<div class="col-lg-5 col-md-5 col-12">
						<div class="bg-white rounded30 shadow-lg">
							<div class="content-top-agile p-20 pb-0">
								<h2 class="text-primary">注册</h2>
								<p class="mb-0">注册一个新身份</p>
							</div>
							<div class="p-40">
								<form action="index.html" method="get" @submit.prevent="register">
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
												placeholder="工号" v-model="employeeId">
										</div>
									</div>

									<div class="form-group">
										<div class="input-group mb-3">
											<div class="input-group-prepend">
												<span class="input-group-text bg-transparent"><i
														class="ti-lock"></i></span>
											</div>
											<input type="password" class="form-control pl-15 bg-transparent"
												placeholder="密码" v-model="password">
										</div>
									</div>
									<div class="form-group">
										<div class="input-group mb-3">
											<div class="input-group-prepend">
												<span class="input-group-text bg-transparent"><i
														class="ti-lock"></i></span>
											</div>
											<input type="password" class="form-control pl-15 bg-transparent"
												placeholder="再次输入密码" v-model="confirmPassword">
										</div>
									</div>
									<div class="row">
										<div class="col-12">
											<div class="checkbox">
												<input type="checkbox" id="basic_checkbox_1">
												<label for="basic_checkbox_1">I agree to the <a href="#"
														class="text-warning"><b>Terms</b></a></label>
											</div>
										</div>
										<!-- /.col -->
										<div class="col-12 text-center">
											<button type="button" class="btn btn-info margin-top-10"
												@click="register">提交</button>
										</div>
										<!-- /.col -->
									</div>
								</form>
								<div class="text-center">
									<p class="mt-15 mb-0">已经有个账户?<router-link to="/" class="text-danger ml-5">
											登录</router-link></p>
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
export default {
    data() {
        return {
            username: '',
            employeeId: '',
            password: '',
			confirmPassword: '',
			socket:null,
        };
	},
	mounted() {
		
	},
   methods: {
    register() {
        const password = this.password; // 假设你有一个绑定到密码输入框的变量
        const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$/;
		   console.log('注册方法被调用');
        if (!passwordPattern.test(password)) {
            alert('密码必须包含字母和数字，并且长度至少为6位');
            return;
        }

         if (this.password !== this.confirmPassword) {
                alert('两次输入的密码不一致');
                return;
		 }

		   //发送http请求到后端注册接口
		   //http://10.21.30.30:8080
		   axios.post('http://127.0.0.1:4523/m1/5289681-4958794-default/api/user/register', {
			   id: this.employeeId,
			   userName: this.username,
			  password:this.password
		   }).then(response => {
			   //根据返回的code处理逻辑
			   console.log("查看返回的结果",response.request.status);
			   if (response.request.status === 200) {
				   alert('注册成功！');

			   }
			   else {
				alert(`注册失败: ${response.data.message}`);
			   }
		   })
		   .catch(error => {
                console.error('注册请求失败:', error);
                alert('发生错误，请稍后再试');
            });
		   
    }
  },
};
</script>
<style>
@import './static/css/vendors_css.css';
@import './static/css/style.css';
@import './static/css/skin_color.css';

/* 其他自定义样式 */
</style>