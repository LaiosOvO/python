



#### 文档



[Welcome to Flask — Flask Documentation (3.1.x)](https://flask.palletsprojects.com/en/stable/)





#### 视频



[Full Flask Course For Python - From Basics To Deployment](https://www.youtube.com/watch?v=oQ5UfJqW5Jo)



# syntax



#### Route & urls

![image-20241215200616300](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215200616300.png)



#### tempaltes & html



先定义路由。

![image-20241215203543950](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215203543950.png)



![image-20241215202234036](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215202234036.png)

页面内对字符串进行处理。可以定义过滤器。

![image-20241215202254630](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215202254630.png)



#### forms file post

表单中拿数据

![image-20241215210725553](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215210725553.png)



##### 文件上传

![image-20241215210749646](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215210749646.png)



##### 返回文件流

![image-20241215210801839](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215210801839.png)

##### 返回服务端目录下文件

![image-20241215210824488](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215210824488.png)

![image-20241215210837827](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215210837827.png)



![image-20241215210830486](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215210830486.png)



![image-20241215211253978](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215211253978.png)



#### static file

![image-20241215212045004](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215212045004.png)



#### session & cookie



![image-20241215222645097](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215222645097.png)



![image-20241215222658705](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215222658705.png)



#### database & sql alchemy

```
pip3 install flask-sqlalchemy flask-migrate

# 创建数据库和迁移数据库
flask db init
flask db migrate
flask db upgrade
```



##### 装配数据库

![image-20241215225325230](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215225325230.png)

![image-20241215225153452](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215225153452.png)

##### 模型类定义

![image-20241215225205772](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215225205772.png)



##### 路由定义

![image-20241215225236766](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215225236766.png)

#### crud

![image-20241215225309279](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215225309279.png)



#### 用户认证



![image-20241215235704031](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215235704031.png)

flask的用户认证封装的方法

![image-20241215235712055](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215235712055.png)

认证才能访问的修饰器

![image-20241215235731507](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241215235731507.png)





#### blueprint

注册模块路由

![image-20241216000554221](C:\Users\16915\AppData\Roaming\Typora\typora-user-images\image-20241216000554221.png)















