import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt
import imageio

### STEP1 ###
# compress_image 函数实现图片压缩功能。
def compress_image(img, num_clusters):
    """
    该函数的目标是通过 KMeans 聚类算法压缩图片的颜色种类。
    
    参数:
        img (ndarray): 输入图片，形状为 (height, width, 3)。
        num_clusters (int): 聚类的类别数。
    
    返回:
        input_image_compressed (ndarray): 压缩后的图片，形状与输入图片相同。
    """
    # 问题一：将 img 转换为适合聚类输入的结构，即将每个像素作为一个样本。
    # KMeans 需要输入二维数组，每一行是一个样本（像素），每列是特征（R, G, B）。
    img_data = img.reshape((-1, 3))  # 转换为 (height × width, 3)
    
    # 创建 KMeans 模型并训练
    # 使用 `n_init=10` 代替错误的 `n_iniat` 参数。
    kmeans = cluster.KMeans(n_clusters=num_clusters, n_init=10, random_state=5)
    kmeans.fit(img_data)  # 训练模型

    # 问题二：获取聚类标签和质心
    labels = kmeans.labels_  # 每个像素点对应的类别标签
    cluster_centers = kmeans.cluster_centers_  # 聚类的质心 (num_clusters, 3)

    # 问题三：使用质心值代替原数据的 label 值
    # 替换每个像素的值为其对应类别的质心值
    compressed_img_data = cluster_centers[labels]
    
    # 恢复原图片的形状
    input_image_compressed = compressed_img_data.reshape(img.shape)
    return input_image_compressed


### STEP2 ###
# plot_image 函数打印图片
def plot_image(img, title):
    """
    打印图片并保存为 PNG 文件。
    
    参数:
        img (ndarray): 要打印的图片，形状为 (height, width, 3)。
        title (str): 图片标题，用于保存图片时的文件名。
    """
    plt.figure()
    plt.title(title)
    plt.imshow(img.astype(np.uint8))  # 显示图片时确保类型为 uint8
    plt.axis('off')  # 不显示坐标轴
    plt.savefig(f'./{title}.png')  # 保存图片


### STEP3 ###
# 读取图片，设置压缩率，实现压缩
if __name__ == '__main__':
    # 设置图片路径和压缩参数
    input_file = "/home/gdut_students/lwb/k-means/数据源/flower.jpg"
    num_bits = 3  # 压缩到 2^2 = 4 种颜色
    if not 1 <= num_bits <= 8:
        raise ValueError('Number of bits should be between 1 and 8')
    
    num_clusters = 2 ** num_bits  # 计算聚类类别数
    compression_rate = round(100 * (8.0 - num_bits) / 8.0, 2)  # 计算压缩率
    print(f"\nThe size of the image will be reduced by a factor of {8.0 / num_bits}")
    print(f"\nCompression rate = {compression_rate}%")
    
    # 读取图片并转换为 NumPy 数组
    input_image = imageio.imread(input_file)
    
    # 原始图像的输出
    plot_image(input_image, 'Original image')
    
    # 压缩图片
    input_image_compressed = compress_image(input_image, num_clusters)
    plot_image(input_image_compressed, f'Compressed image; compression rate = {compression_rate}%')
    
    # 显示所有图片
    plt.show()
