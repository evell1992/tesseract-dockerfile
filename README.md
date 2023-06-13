# tesseract-dockerfile

##### Dockerfile

- 准备基础镜像:ubuntu:22.04
- 安装 tesseract 编译所需环境
- 编辑安装

##### Dockerfile1

- 因为编译安装时间太长,所以分成两个镜像操作
- 继承Dockerfile1
- 安装python 三方库
- 准备app运行环境