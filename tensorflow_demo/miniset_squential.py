import tensorflow as tf
from matplotlib import pyplot as plt
# from tensorflow.keras.layers import Dense, Flatten
# from tensorflow.keras import Model

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 对神经网络的输入特征进行归一化，归一到0-1，把输入特征的数值变小更适合神经网络吸收
x_train, y_train = x_train / 255.0, y_train / 255.0

# 可视化训练集输入
plt.imshow(x_train[0],cmap='gray')
plt.show()

# 打印出训练集输入的第一个元素
print('x_train[0]:\n', x_train[0])
# 打印出标签集的第一个元素
print('y_train[0]:\n', y_train[0])

# 打印出整个训练集输入特征形状
print("x_train.shape:\n", x_train.shape)
# 打印出整个训练集标签的形状
print("y_train.shape:\n", y_train.shape)
# 直接API
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),# 把28*28的输入特征拉直为一维数组
    tf.keras.layers.Dense(128, activation='relu'), # 定义第一层又128(经验值)个神经元 relu激活函数
    tf.keras.layers.Dense(10, activation='softmax') # 定义第二层有10个神经元 softmax激活函数 使输出符合概率分布
])


# class
# class MnistModel(Model):
#     def __init__(self):
#         super(MnistModel, self).__init__()
#         self.flatten = Flatten()
#         self.d1 = Dense(128, activation='relu')
#         self.d2 = Dense(10, activation='softmax')
#
#     def call(self, x):
#         x = self.flatten(x),
#         x = self.d1(x),
#         y = self.d2(x)
#         return y
#
#  model = MnistModel()

model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),# 如果输出不满足概率分布 要写true
    metrics=['sparse_categorical_accuracy'] # 因为数据集标签是数值，输出是概率分布
)

model.fit(
    x_train,
    y_train,
    batch_size=32,
    epochs=5,
    validation_data=(x_test, y_test),
    validation_freq=1
)
model.summary()
# 准确率是使用测试集计算出来的准确率
# 准确率看的是 val_sparse_categorical_accuracy: 0.0980