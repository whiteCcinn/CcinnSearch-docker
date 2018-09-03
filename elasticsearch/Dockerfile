FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.0.0

LABEL author = "ccinn<471113744@qq.com>"

# 提交配置　包括新的elasticsearch.yml 和　keystore.jks文件
COPY --chown=elasticsearch:elasticsearch conf/ /usr/share/elasticsearch/config/

# 安装ik
RUN ./bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.0.0/elasticsearch-analysis-ik-6.0.0.zip

# 安装readonlyrest
RUN ./bin/elasticsearch-plugin install https://github.com/HYY-yu/BezierCurveDemo/raw/master/readonlyrest-1.16.14_es6.0.0.zip

USER elasticsearch
CMD ./bin/elasticsearch