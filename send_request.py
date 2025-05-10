import requests

"""
请求
"""

# 用于发送get请求
requests.get()

# 用于发送post请求
requests.post()

# 用于发送delete请求
requests.delete()

# 用于发送put请求
requests.put()

requests.request()

"""
响应
"""

rep = requests.request()

# 请求返回字符串的数据
print(rep.text)


#请求返回字节格式的数据
print(rep.content)

#请求返回字典格式的数据
print(rep.json())

