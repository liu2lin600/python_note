import paramiko

''' 方法1：基于用户名和密码的 sshclient 方式登录 '''

# 建立一个sshclient对象
ssh = paramiko.SSHClient()

# 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 调用connect方法连接服务器
ssh.connect(hostname='10.10.195.180', port=22, username='root', password='xx')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df -hl')

# 打印输出
print(stdout.read().decode())

# 关闭连接
ssh.close()

''' 方法2：基于用户名和密码的 transport 方式登录 '''

# 实例化一个transport对象
trans = paramiko.Transport(('192.168.2.129', 22))
# 建立连接
trans.connect(username='super', password='super')

# 将sshclient的对象的transport指定为以上的trans
ssh = paramiko.SSHClient()
ssh._transport = trans

# 执行命令，和传统方法一样
stdin, stdout, stderr = ssh.exec_command('df -hl')
print(stdout.read().decode())
trans.close()


'''方法3：基于公钥密钥的 SSHClient 方式登录'''
# 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，password为设定的密码，如无不用指定password参数
pkey = paramiko.RSAKey.from_private_key_file('/home/super/.ssh/id_rsa', password='12345')

# 建立连接
ssh = paramiko.SSHClient()
ssh.connect(hostname='192.168.2.129',
            port=22,
            username='super',
            pkey=pkey)
# 执行命令
stdin, stdout, stderr = ssh.exec_command('hostname -f')
print(stdout.read().decode())
ssh.close()






















