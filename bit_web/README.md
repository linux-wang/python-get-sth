### BIT_web登录注销脚本

#### 使用说明

1. 在account_conf.py中写入用户名，密码
2. 运行命令```python bit_web.py```
3. 会显示登录/注销结果

#### 示例

```
➜  bit_web git:(master) ✗ python bit_web.py
登录成功
```

#### 说明

如果当前在线，执行注销操作；反之执行登录操作

没有什么多余的功能

系统环境中需要有Python环境，未执行兼容性测试

#### 文件说明

```bit_web.html```和```bit_web.js```是学校网关的源码(分析过程可以直接抓包，也可以直接看源码)

```account_conf.py```是配置文件

```bit_web.py```是执行脚本
