FROM python:3.6-jessie

LABEL author = "ccinn<471113744@qq.com>"

ENV WORKSPACE /usr/src/myapp
ARG PROJECT=ccinnSearch

WORKDIR ${WORKSPACE}

COPY . .

# 更换了源必须update
# libnss3 用于谷歌驱动
# ldd ${WORKSPACE}/chromedriver 可以查看缺少的动态库
# apt-cache search lib

RUN ln -s ${WORKSPACE}/source /etc/apt/sources.list.d/cn.source.list && \
    apt-get update && \
    wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    apt-get install -y apt-transport-https && \
    apt-get update && \
    apt-get install -y \
            vim \
            wget \
            zip \
            libnss3 \
            libgconf2-4 \
            fonts-liberation \
            libappindicator3-1 \
            libasound2 \
            libatk-bridge2.0-0 \
            libatk1.0-0 \
            libcups2 \
            libgtk-3-0 \
            libx11-xcb1 \
            libxcomposite1 \
            lsb-release \
            xdg-utils

RUN cd /usr/local/src/ && \
    wget https://github.com/whiteCcinn/resource/releases/download/v68.0/chromedriver_linux64.zip && \
    unzip -o chromedriver_linux64.zip && \
    mv -f chromedriver ${WORKSPACE}/ && \
    wget https://github.com/whiteCcinn/resource/releases/download/v68.0/google-chrome-stable_68.0.3440.106-1_amd64.deb && \
    dpkg -i google-chrome-stable_68.0.3440.106-1_amd64.deb

#RUN dpkg -i google-chrome-stable_68.0.3440.106-1_amd64.deb

RUN mkdir -p  ~/.pip/ && \
    ln -s ${WORKSPACE}/pip.conf ~/.pip/pip.conf && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR ${WORKSPACE}/${PROJECT}

CMD ["scrapy"]
