# import requests
#
# # Flask 应用程序的地址
#
# # url = 'http://120.53.244.183:808//'  # 替换为你的 Flask 应用程序的地址
# url =  'http:/120.53.244.183:808/uploadimg' # 替换为你的 Flask 应用程序的地址
# # 上传的图像文件
# image_path = '1.jpg'  # 替换为你要上传的图像文件的路径
#
# # 发送 POST 请求
# with open(image_path, 'rb') as file:
#     files = {'image': file}
#     response = requests.post(url, files=files)
#     print("服务器响应：", response.json())
import requests

url = 'http://120.53.244.183:5000/uploadimg'
files = {'imgFile': open('1.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())

# 获取并打印响应结果
# print(response.json())
# import requests
#
# # Flask 应用程序的地址
# flask_app_url = 'http://192.168.0.102:80//upload'  # 替换为你的 Flask 应用程序的地址
#
# # 上传的图像文件路径
# image_path = '1.jpg'  # 替换为你要上传的图像文件的路径
#
# # 创建一个文件对象
# with open(image_path, 'rb') as file:
#     # 构造上传文件的字典
#     files = {'file': file}
#
#     # 发送 POST 请求
#     try:
#         response = requests.post(flask_app_url, files=files)
#
#         # 检查响应状态码
#         if response.status_code == 200:
#             print("上传成功！")
#             print("服务器响应：", response.json())
#         else:
#             print("上传失败！")
#             print("服务器响应：", response.text)
#     except requests.exceptions.RequestException as e:
#         print("请求异常：", e)
