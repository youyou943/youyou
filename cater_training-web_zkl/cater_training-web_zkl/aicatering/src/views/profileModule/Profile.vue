<template>
  <div>
     <section class="content">
			  <div class="row">			  
				  <div class="col-lg-6 col-12">
					  <div class="box">
						<div class="box-header with-border">
						  <h4 class="box-title">基本信息</h4>
						</div>
						<!-- /.box-header -->
						<el-form class="form" ref="elForm" :model="formData" :rules="rules" @submit.prevent="submitForm">
							<div class="box-body">
								<h4 class="box-title text-info"><i class="ti-user mr-15"></i> Personal Info</h4>
								<hr class="my-15">
								<div class="row">
								  <div class="col-md-6">
									<div class="form-group">
									  <label prop="field106">用户名</label>
									  <input type="text" class="form-control" placeholder="请输入用户名" v-model="formData.field106">
									</div>
								  </div>
								  <div class="col-md-6">
									<div class="form-group">
									  <label prop="field107">工号</label>
									  <input type="text" class="form-control" placeholder="请输入工号" v-model="formData.field107">
									</div>
								  </div>
								</div>
								<div class="row">
								  <div class="col-md-6">
									<div class="form-group">
									  <label prop="field105">邮箱</label>
									  <input type="text" class="form-control" placeholder="请输入邮箱">
									</div>
								  </div>
								  <div class="col-md-6">
									<div class="form-group">
									  <label prop="field110">联系电话</label>
									  <input type="text" class="form-control" placeholder="请输入联系电话">
									</div>
								  </div>
								</div>
								
								<div class="row">
								  <div class="col-md-6">
									<div class="form-group">
									  <label prop="field104">职位</label>
									  <select class="form-control" >
                    <option v-for="(item, index) in field104Options" :key="index" :label="item.label"
              :value="item.value" :disabled="item.disabled"></option>
									  </select>
									</div>
								  </div>
                  <div class="col-md-6">
									<div class="form-group" prop="field102">
									  <label prop="field102">性别</label>
									  <select class="form-control" > 
                    <option v-for="(item, index) in field102Options" :key="index" :label="item.label"
              :value="item.value" :disabled="item.disabled"></option>
									  </select>
									</div>
								  </div>
								</div>
							</div>
							<!-- /.box-body -->
							<div class="box-footer">
								<button type="button" class="btn btn-rounded btn-warning btn-outline mr-1" @click="resetForm">
								  <i class="ti-trash"></i> 重置
								</button>
								<button type="submit" class="btn btn-rounded btn-primary btn-outline" >
								  <i class="ti-save-alt"></i> 提交
								</button>
							</div>  
						</el-form>
					  </div>
					  <!-- /.box -->			
				</div>
          <div class="col-lg-6 col-12">
					  <div class="box">
						<div class="box-header with-border">
						  <h4 class="box-title">修改密码</h4>
						</div>
						<!-- /.box-header -->
						<form class="form" ref="elForm">
							<div class="box-body">
								<h4 class="box-title text-info"><i class="ti-save mr-15"></i> Password modification</h4>
								<hr class="my-15">
								<div class="row">
								  <div class="col-md-6">
									<div class="form-group">
									  <label >当前密码</label>
									  <div class="input-group mb-3">
											<div class="input-group-prepend">
												<span class="input-group-text bg-transparent"><i
														class="ti-lock"></i></span>
											</div>
											<input type="password" class="form-control pl-15 bg-transparent"
												placeholder="请输入当前密码">
										</div>
									</div>
								  </div>
								</div>
								<div class="row">
								  <div class="col-md-6">
									<div class="form-group">
									  <label >修改密码</label>
									  <div class="input-group mb-3">
											<div class="input-group-prepend">
												<span class="input-group-text bg-transparent"><i
														class="ti-lock"></i></span>
											</div>
											<input type="password" class="form-control pl-15 bg-transparent"
												placeholder="请输入修改密码" v-model="new_pwd">
										</div>
									</div>
								  </div>
								</div>
								
								<div class="row">
								  <div class="col-md-6">
									<div class="form-group">
									  <label >再次输入修改密码</label>
									  <div class="input-group mb-3">
											<div class="input-group-prepend">
												<span class="input-group-text bg-transparent"><i
														class="ti-lock"></i></span>
											</div>
											<input type="password" class="form-control pl-15 bg-transparent"
												placeholder="请再次输入修改后的密码" v-model="confirmPassword">
										</div>
									</div>
								  </div>
								</div>
							</div>
							<!-- /.box-body -->
							<div class="box-footer">
								<button type="submit" class="btn btn-rounded btn-primary btn-outline" @click="submitFormPwd">
								  <i class="ti-save-alt"></i> 提交
								</button>
							</div>  
						</form>
					  </div>
					  <!-- /.box -->			
				</div>
        </div>
    </section>
   
  </div>
</template>
<script>
import axios from 'axios';
export default {
  components: {},
  props: [],
  data() {
	  return {
		  formData: {
			  field107: undefined,//工号
			  field106: undefined,//用户名
			  field104: 2,//职位
			  field102: 1,//性别
			  field110: undefined,//联系电话
			  field105: undefined,//邮箱
		  },
		  rules: {
			  field107: [{
				  required: true,
				  message: '请输入工号',
				  trigger: 'blur'
			  }],
			  field106: [{
				  required: true,
				  message: '请输入用户名',
				  trigger: 'blur'
			  }],
			  field104: [{
				  required: true,
				  message: '请选择职位',
				  trigger: 'change'
			  }],
			  field102: [{
				  required: true,
				  message: '性别不能为空',
				  trigger: 'change'
			  }],
			  field109: [{
				  required: true,
				  message: '请输入密码',
				  trigger: 'blur'
			  }],
		  },
		  field104Options: [{
			  "label": "普通员工",
			  "value": 1
		  }, {
			  "label": "经理",
			  "value": 2
		  }],
		  field102Options: [{
			  "label": "男",
			  "value": 1
		  }, {
			  "label": "女",
			  "value": 2
		  }],
		  socket: null,
		  password: '',
		  new_pwd:'',
		  confirmPassword: '',
	  };
  },
  computed: {},
  watch: {},
  created() {},
  mounted() {
  },
  methods: {
    submitForm() {
          // 确保 `elForm` 引用存在并且包含 `validate` 方法
    if (!this.$refs.elForm || typeof this.$refs.elForm.validate !== 'function') {
        console.error('elForm 引用无效或 validate 方法不存在');
        return;
    }
        
        
		  this.$refs['elForm'].validate(valid => {
			console.log("Validation completed", valid);
			  if (!valid) return;

			  //准备数据
			  const payload = {
				  id: this.formData.field107,
				  username: this.formData.field106,
				  tel: this.formData.field110,
				  email: this.formData.field105,
				  postion: this.formData.field104,
				  
			  };
             
			  console.log('发送的修改的数据:', payload); // 打印发送的数据

			  //在 axios.post 请求中，params通常用于 GET 请求，而对于 POST 请求，数据应该直接放在请求体里。可以将 params 替换为数据对象 data
             axios.post('http://127.0.0.1:4523/m1/5289681-4958794-default/api/user/updateInfoById', {          
                  id: this.formData.field107,
				  userName: this.formData.field106,
				  tel: this.formData.field110,
				  email: this.formData.field105,
				  postion: this.formData.field104,
              })
			   .then(response => {
			   //根据返回的code处理逻辑
			   console.log("查看返回的结果",response);
			   if (response.status === 200) {
				   alert('个人信息提交成功！');
				   console.log("查看一下在localStorage里面的数据",this.formData.field107);
					// 使用 localStorage 存储 userId
				   localStorage.setItem('userId', this.formData.field107);
			   }
			   else {
				alert(`个人信息提交失败: ${response.data.message}`);
			   }
		   })
		   .catch(error => {
                console.error('个人信息提交请求失败:', error);
                alert('发生错误，请稍后再试');
            });

		  });

	},
	submitFormPwd() {
		const password = this.new_pwd; // 假设你有一个绑定到密码输入框的变量
        const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$/;
		   console.log('注册方法被调用');
        if (!passwordPattern.test(password)) {
            alert('密码必须包含字母和数字，并且长度至少为6位');
            return;
        }

         if (this.new_pwd !== this.confirmPassword) {
                alert('两次输入的密码不一致');
                return;
		}
		
		   const payload = {
			   id: this.formData.field107,
			   password: this.password,
			   newPassword:this.new_pwd,
		   };
		console.log('发送的修改密码数据:', payload); // 打印发送的数据

		 axios.post('http://127.0.0.1:4523/m1/5289681-4958794-default/api/user/updatePwdById', {
                 id: this.formData.field107,
			   password: this.password,
			   newPassword:this.new_pwd,
              })
			   .then(response => {
			   //根据返回的code处理逻辑
			   console.log("查看返回的结果",response);
			   if (response.status === 200) {
				   alert('密码修改成功！');
			   }
			   else {
				alert(`密码修改失败: ${response.data.message}`);
			   }
		   })
		   .catch(error => {
                console.error('密码修改请求失败:', error);
                alert('发生错误，请稍后再试');
            });
		   
	},
    resetForm() {
      alert('重置成功！');
      this.$refs['elForm'].resetFields()
    },
  }
}

</script>
<style>
</style>
