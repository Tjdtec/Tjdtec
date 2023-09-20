## 工程概论作业二

## 《论文查重程序设计》

### 作业要求

|                      |                                                              |
| -------------------- | :----------------------------------------------------------: |
| 这个作业属于哪个课程 | [工程概论](https://edu.cnblogs.com/campus/jmu/ComputerScience21) |
| 这个作业要求在哪里   | [作业要求](https://edu.cnblogs.com/campus/jmu/ComputerScience21/homework/13034) |
| 这个作业的目标       |               构建完整的项目流程，体验测试环节               |

### 需求分析

题目：**论文查重**

 设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重复率。

- 原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
- 抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。

要求输入输出采用文件输入输出，规范如下：

- 从**命令行参数**给出：论文原文的文件的**绝对路径**。
- 从**命令行参数**给出：抄袭版论文的文件的**绝对路径**。
- 从**命令行参数**给出：输出的答案文件的**绝对路径**。

注意：答案文件中输出的答案为浮点型，精确到小数点后两位

### 算法设计

查重的本质实际上就是比较两份文章的相似度，可以套用在立体几何里常用的余弦公式：

$$cos\theta = \frac{\vec{V_1} ·\vec{V_2}}{||V_1||^2·||V_2||^2}$$

关键思路就是把文章转化为对应的词向量，如对于原文章，则转化为词向量 $\vec{V_1}$ , 也就是说，对于一篇文章，我们可以使用一个独一的向量表示，同理对于抄袭文章也可以用一个向量 $\vec{V_2}$ 单独表示。那么如果两个向量是一样的，类比于平面几何，两个向量应该是重合的，夹角  $\theta$ 应该为0,则对应的 $cos\theta$ 值应该为1，也就是$100$%，可以想见，两篇文章越相似，则夹角余弦值应该是越接近于1。

#### 模块设计

- 读取文本文件模块

- 文本预处理模块

  使用 `jieba` 依赖库和正则表达式 `^\u4e00-\u9fa5` 对文章进行分词操作，将文章拆分成为由系列词和短句组成的结构

- 余弦相似度计算模块

  使用 `collections.Counter` 类对预处理后的文章词频（词语频率）进行统计，结合 `numpy` 和 `pandas` 库构建两篇文章的词向量，最后带入余弦公式计算，将计算结果返回

- main 模块

### 开发环境

- 操作系统：Windows 10 专业版
- 处理器：Intel(R) Core(TM) i5-10200H CPU @ 2.40GHz   2.40 GHz
- 内存：16 GB
- IDE：PyCharm 2023.2.1
- Python：3.10

### 项目结构

![](https://github.com/Tjdtec/Tjdtec/blob/main/ImageOnComputer/20230920.png)

其中, 文件夹\data用来存放数据，也就是需要比较的文本文件，tests作为测试模块，来检测功能代码能否达到测试要求, main函数中则存放主要运行的代码。

### 异常处理

- 文件路径错误

- 参数传递错误

- 余弦相似角的除0错误

  ![]((https://github.com/Tjdtec/Tjdtec/blob/main/ImageOnComputer/20230920_1.png)

### 测试结果

- 对余弦相似度计算模块进行测试

![](https://github.com/Tjdtec/Tjdtec/blob/main/ImageOnComputer/20230920test.png)

- 对主程序运行测试

![](https://github.com/Tjdtec/Tjdtec/blob/main/ImageOnComputer/20230920main.png)

保存结果如下：

![](https://github.com/Tjdtec/Tjdtec/blob/main/ImageOnComputer/20230920result.png)

### 性能分析

使用pycharm分析对应的统计表:

![](https://github.com/Tjdtec/Tjdtec/blob/main/ImageOnComputer/%E4%BF%A1%E6%81%AF%E8%B0%83%E7%94%A8%E5%9B%BE.png)

使用pycharm作出对应的调用图：

<img src="https://github.com/Tjdtec/Tjdtec/blob/main/ImageOnComputer/PaperCheck.png" style="zoom:50%;" />

### PSP 表格记录

|                PSP2.1                 | Personal Software Process Stages | 预估耗时（min） | 实际耗时（min） |
| :-----------------------------------: | :------------------------------: | :-------------: | :-------------: |
|               Planning                |               计划               |       20        |       10        |
|               Estimate                |     估计这个任务需要多少时间     |        5        |        5        |
|              Development              |               开发               |       30        |       40        |
|               Analysis                |    需求分析 (包括学习新技术)     |       10        |        8        |
|              Design Spec              |           生成设计文档           |       10        |       10        |
|             Design Review             |             设计复审             |       20        |       20        |
|            Coding Standard            |             代码规范             |        1        |        1        |
|                Design                 |             具体设计             |       15        |       13        |
|                Coding                 |             具体编码             |       20        |       17        |
|              Code Review              |             代码复审             |       10        |        8        |
|                 Test                  |               测试               |       50        |       60        |
|               Reporting               |               报告               |       30        |       30        |
|              Test Repor               |             测试报告             |       30        |       20        |
|           Size Measurement            |            计算工作量            |        5        |        5        |
| Postmortem & Process Improvement Plan |   事后总结, 并提出过程改进计划   |       10        |        3        |
|                                       |               合计               |       206       |       175       |



