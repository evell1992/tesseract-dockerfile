# tesseract-dockerfile

##### Dockerfile

- 准备基础镜像:ubuntu:22.04
- 安装 tesseract 编译所需环境
- 编译安装

##### Dockerfile1

- 因为编译安装时间太长,所以分成两个镜像操作
- 继承Dockerfile
- 安装python 三方库
- 准备app运行环境

##### traineddata

- 字体文件夹,训练的字体放到该文件夹

##### 启动

- docker-compose up -d