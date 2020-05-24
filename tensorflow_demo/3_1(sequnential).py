import tensorflow as tf
from sklearn import datasets
import numpy as np

x_train = datasets.load_iris().data
y_train = datasets.load_iris().target
# 实现数据集的乱序
np.random.seed(116)
np.random.shuffle(x_train)
np.random.seed(116)
np.random.shuffle(y_train)
tf.random.set_seed(116)
# 搭建神经网络结构
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(3, # 神经元个数
                          activation='softmax', # 计划函数
                          kernel_regularizer=tf.keras.regularizers.l2() #正则化方法
                          )
])
# 配置训练方法
model.compile(
    optimizer=tf.keras.optimizers.SGD(lr=0.1), # 优化器 学习率设置为 0.1
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False), # 选择损失函数，由于神经网络末端使用了softmax函数，使得输出是概率分布而不是原始输出，所以from_logits=False
    metrics=['sparse_categorical_accuracy'] # 由于标签是数值，神经网络前向输出是概率分布<所以选这个评测指标
)
# 执行训练过程
model.fit(
    x_train,
    y_train,
    batch_size=32,# 训练时，一次喂入神经网络多少组数据batch_size
    epochs=500,# 数据集迭代循环多少次
    validation_split=0.2, # 从训练集中选择20%的数据作为测试集
    validation_freq=20 # 每迭代20次训练集，要在测试集中验证一次准确率
)
# 打印出网络结构和参数统计
model.summary()