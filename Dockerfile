FROM python:3.9-alpine3.13

# 设置工作目录
WORKDIR /app

# 复制项目文件到镜像中
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 5000

# 启动应用程序
CMD ["python", "app.py"]
