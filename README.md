# 基于轻量型模型的垃圾桶满溢识别检测

项目成员：任乐山，于丁怡，杜海欣，宫晨峰，牟仕鼎

## 项目简介：

本项目共分为三大部分：轻量型检测模型的对比实验，基于生成模型的数据增强，在摄像头芯片上的模型部署及应用。

**轻量型检测模型的对比实验**包含两部分内容：（Part1/Part2）

**Part1**：对论文“**基于轻量型卷积神经网络的垃圾桶满溢识别及应用**”进行研读并对相关代码进行解析，同时对所分析的内容录制讲解视频并上传至B站；

**Part2**：基于Part1的相关数据及模型，完成以下内容。

- 在百度飞桨的模型库中，选择若干最新的轻量级目标检测模型。
- 基于论文中提供的数据，参考《 better_deep_learning 》一书，对选择的模型进行优化、调参和训练，并完成对垃圾桶状态的检测，并将结果与论文中的进行比较，尽可能在各项指标上超过论文中的结果；
- 对所选择的若干轻量级目标检测模型之间进行对比，分析其参数、性能及相关指标，比较其优劣并对产生这些结果的原因进行分析；
- 完成项目的实验报告，包括所选模型的相关基础知识，模型训练及调参的相关流程，以及所选择模型之间的对比分析结果，相关的分析以及比较的结果需以图表的形式给出；
- 对上述内容录制讲解视频并上传至B站。

**基于生成模型的数据增强**包含以下内容：

- 选择合适的生成式深度学习模型对论文中提供的的垃圾桶数据集数据集进行扩充和数据增强；
- 基于原始数据集使用生成式深度学习模型生成更多天气状态和光影状态下的数据，包括：不同程度的下雨下雪天气，不同程度的夜晚状态（较暗、傍晚、路灯等）；
- 使用基于百度飞桨的EasyDL平台对新扩充的数据进行标注，标注的类别主要分三类：分别是未满溢的垃圾桶、满溢的垃圾桶和垃圾；
- 完成项目的实验报告；
- 对上述内容录制讲解视频并上传至B站。

**垃圾桶目标检测模型的云部署**包含以下内容：

- 选择一个效果较好的目标检测模型并使用垃圾桶数据集进行训练；
- 将模型制作成标准Rest API，并使用flask将模型部署到云服务器上；
- 使用本地笔记本python上传一张垃圾桶图片，使用云主机进行推理，最终返回json检测结果；
- 对上述内容录制讲解视频并上传至B站。

### 轻量型检测模型的对比实验

#### Part1:

项目组成员研读了论文“**基于轻量型卷积神经网络的垃圾桶满溢识别及应用**”，并对相关代码进行了解析。对论文和代码的研读笔记在文件`轻量型检测模型的对比实验 ——> Part1 ——> 笔记`中。数据集链接：https://aistudio.baidu.com/aistudio/datasetdetail/228648

#### Part2:

上一部分项目组成员对《基于轻量型卷积神经网络的垃圾桶满溢识别及应用》进行了解读和分析，对其所使用的轻量级模型进行了介绍，并复现了相关的代码。在Part2中，项目组各成员从百度飞桨paddle的模型库选取了YOLOv3_mobilenetv3、RT-DETR_HGNetV2、PP-YOLOE+_crn_l_80e、PP-PicoDet_LCNet、PP-ShiTuV2-det和yolov8这六个模型进行解读，学习其模型原理和架构，并使用论文“**基于轻量型卷积神经网络的垃圾桶满溢识别及应用**”的数据集进行训练和评估。其中，YOLOv3_mobilenetv3使用了PaddleDetection框架进行训练，其余模型则是使用飞桨的AI套件paddlex进行训练和优化，详细结果可以查看`轻量型检测模型的对比实验 ——> Part2`中的相关笔记以及百度AiStudio项目[山东大学威海数据科学与人工智能实验班大三上大作业第一部分Part2](https://aistudio.baidu.com/projectdetail/7158182?contributionType=1&sUid=989685&shared=1&ts=1701358853657)。

### 基于生成模型的数据增强

首先，项目组成员使用了DDMP-去噪扩散概率模型对原始数据进行扩充。随后，在为了生成不同天气的及光影状况下的图片数据，项目组成员学习了CycleGAN以及stable diffusion的相关原理与方法，最终生成了雪天、雨天以及夜晚的垃圾桶图片数据。同时，项目组成员还采用了一种基于opencv的雨天模拟算法，在原始数据集上生成了雨天特效。最后，项目组成员使用百度EasyDL来对上述生成的数据集进行标注。详细内容可以查看百度AiStudio项目[基于生成式模型的数据增强实验报告](https://aistudio.baidu.com/projectdetail/7405954?contributionType=1)

### 垃圾桶目标检测模型的云部署


