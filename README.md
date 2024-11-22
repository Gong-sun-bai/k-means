# **K-Means 图像压缩**

本仓库展示了如何使用 **K-Means 聚类算法**对图像进行压缩。实验的目标是通过减少图像中的颜色种类来降低存储需求，同时尽量保留图像的主要视觉信息。该项目基于 Python 实现，使用了 `NumPy`、`scikit-learn` 和 `matplotlib` 等库。

---

## **功能介绍**

1. **基于 K-Means 的图像压缩**  
   - 根据像素的 RGB 值对其进行聚类，减少图像中的颜色种类。
   - 输出压缩后的图像，显著减少存储空间占用。

2. **自定义压缩参数**  
   - 用户可设置聚类数量 (`num_clusters`) 或通过每通道的位数 (`num_bits`) 控制压缩比例。

3. **图像可视化**  
   - 支持原始图像与压缩后图像的对比显示。
   - 计算并展示压缩率等关键信息。

---

## **项目结构**

- `compress_image.py`: 主脚本，用于图像压缩。
- `flower.jpg`: 示例输入图像。
- `output/`: 输出目录，用于存储压缩后的图像及相关结果。
- `README.md`: 项目文档（即本文件）。

---

## **快速开始**

### **环境依赖**

确保系统中已安装以下环境：

- Python（版本 >= 3.7）
- 必要的库：
  ```bash
  pip install numpy scikit-learn matplotlib
  ```

### **使用方法**

1. 克隆本仓库：
   ```bash
   git clone https://github.com/Gong-sun-bai/k-means.git
   cd k-means
   ```

2. 运行主脚本：
   ```bash
   python compress_image.py
   ```

3. 根据需求修改脚本参数：
   - `num_bits`: 设置每通道的颜色位数（例如 `2` 表示 4 种颜色）。
   - `input_file`: 指定输入图像的路径。

---

## **运行结果**

脚本会对输入图像进行压缩，并输出以下结果：

1. **原始图像**。
2. **压缩后图像**，保存在 `output/` 目录中。
3. 压缩细节（如压缩率和缩减因子）。

### 示例输出：

- 原始图像：  
  ![原始图像](output/original_image.png)

- 压缩图像：  
  ![压缩图像](output/compressed_image.png)

---

## **核心函数**

- **`compress_image(img, num_clusters)`**  
  - 将图像转换为适合聚类的数据结构。
  - 使用 K-Means 聚类对像素点进行聚类。
  - 使用聚类质心重建图像。

- **`plot_image(img, title)`**  
  - 可视化指定图像，并添加标题。

---

## **参数调整**

- 可通过调整 `num_bits` 控制压缩比例：  
  - 较低的位数会带来更高的压缩率，但可能损失更多细节。
  - 示例：  
    - `num_bits = 2`（4 种颜色，高压缩率）。  
    - `num_bits = 4`（16 种颜色，低压缩率）。

- 更改 `input_file` 参数，使用自己的图片进行测试。

---

## **未来改进**

- 支持其他聚类算法，例如 MiniBatch K-Means。
- 引入评价指标（如 PSNR 和 SSIM），对压缩质量进行量化评估。
- 实现基于空间相关性的算法，进一步提升压缩图像的细节保留能力。

---

## **许可证**

本项目基于 MIT 许可证开源，详见 `LICENSE` 文件。

---

## **贡献者**

- **Gong Sun Bai**  
  项目所有者及维护者。  
  欢迎通过 [issues](https://github.com/Gong-sun-bai/k-means/issues) 或 Pull Requests 提交建议与改进。

---

本项目适用于学习和实验 K-Means 聚类在图像处理中的应用，希望你能从中获得乐趣！🎨
