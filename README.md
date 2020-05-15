# 欢迎使用 NER-BIO-Generator

**NER, bio-format-generator, bio-format-correction**


由于语料不够丰富或者模型不够先进，命名实体识别的结果有时不尽如人意。有些很显见的结果被识别错误，为了下游应用的数据保持高质量，不能缺少必要的人为纠查。比如：增加未识别词的语料、直接正则修改错误项等。该REPO主要目的是将文本文档直接生成标注为BIOES格式，并允许工程师进行动态修正。


## 用法

步骤一、安装必要包
`pip install requirements.txt`

步骤二、安装tensorflow.contrib
`git clone https://www.github.com/keras-team/keras-contrib.git`
`cd keras-contrib`
`python setup.py install`

步骤三、模型训练
`python ner.py`

步骤四、生成BIO文件
`python BIO/generator.py`

步骤五、查看BIO文件质量，添加JIEBA辞典、BIO替换字典，重新训练

###  模型实验结果
> 2020-05-15 17:59:46,413 - log/train.log - INFO - iteration:10 step:42/762, NER loss: 0.825400
> 2020-05-15 18:00:05,493 - log/train.log - INFO - iteration:10 step:142/762, NER loss: 0.727794
> 2020-05-15 18:00:25,318 - log/train.log - INFO - iteration:10 step:242/762, NER loss: 0.806955
> 2020-05-15 18:00:42,635 - log/train.log - INFO - iteration:10 step:342/762, NER loss: 0.758553
> 2020-05-15 18:01:03,367 - log/train.log - INFO - iteration:10 step:442/762, NER loss: 0.802380
> 2020-05-15 18:01:21,216 - log/train.log - INFO - iteration:10 step:542/762, NER loss: 0.766387
> 2020-05-15 18:01:37,297 - log/train.log - INFO - iteration:10 step:642/762, NER loss: 0.745498
> 2020-05-15 18:01:54,277 - log/train.log - INFO - iteration:10 step:742/762, NER loss: 0.819221
> 2020-05-15 18:01:57,615 - log/train.log - INFO - evaluate:dev
> 2020-05-15 18:02:02,834 - log/train.log - INFO - processed 109870 tokens with 3819 phrases; found: 3791 phrases; correct: 3518.
> 2020-05-15 18:02:02,835 - log/train.log - INFO - accuracy:  99.01%; precision:  92.80%; recall:  92.12%; FB1:  92.46
> 2020-05-15 18:02:02,835 - log/train.log - INFO -               LOC: precision:  92.38%; recall:  93.80%; FB1:  93.08  1981
> 2020-05-15 18:02:02,835 - log/train.log - INFO -               ORG: precision:  90.58%; recall:  86.99%; FB1:  88.75  945
> 2020-05-15 18:02:02,835 - log/train.log - INFO -               PER: precision:  96.18%; recall:  94.12%; FB1:  95.14  865
> 2020-05-15 18:02:02,897 - log/train.log - INFO - new best dev f1 score:92.460

###  BIOES语料产生实验结果
> 父 O
亲 O
为 O
三 B-LOC
峡 E-LOC
工 O
程 O
调 O
来 O
武 B-LOC
汉 E-LOC
方 B-PER
方 E-PER
两 O
岁 O
即 O
随 O
父 O
母 O
也 O
来 O
了 O
武 B-LOC
汉 E-LOC


### 重点参考文档和引用代码
[Information-Extraction-Chinese](https://github.com/crownpku/Information-Extraction-Chinese)



# [ner-bio-generator](https://github.com/jackyin68/ner-bio-generator)
NER, BIO, BIOES, generator, adapter, nlp, jieba, keras, idcnn, lstm
