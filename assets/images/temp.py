from PIL import Image

def replace_color(icon_path, new_icon_path, target_color, replacement_color):
    # 打开 ICO 文件
    print("正在打开 ICO 文件...")
    icon = Image.open(icon_path)

    # 转换为 RGBA 模式，以便进行颜色替换
    print("转换为 RGBA 模式...")
    icon = icon.convert("RGBA")

    # 获取图像的像素数据
    print("获取图像的像素数据...")
    pixel_data = icon.load()

    # 遍历图像的每个像素
    print("遍历图像的每个像素...")
    for y in range(icon.size[1]):
        for x in range(icon.size[0]):
            # 打印当前像素的颜色
            print("当前像素的颜色：" + str(pixel_data[x, y]))
            
            # 如果当前像素的颜色接近目标颜色，则将其替换为替换颜色
            if pixel_data[x, y] == target_color:
                print("替换像素颜色为：" + str(replacement_color))
                pixel_data[x, y] = replacement_color

    # 保存修改后的 ICO 文件
    print("保存修改后的 ICO 文件...")
    icon.save(new_icon_path)

    print("颜色替换完成")

# 指定 ICO 文件路径和新图标保存路径
icon_path = "favicon3.ico"
new_icon_path = "favicon3_modified.ico"

# 定义黑色和紫色的 RGBA 颜色值
black_color = (51, 51, 51, 255)  # 黑色 (R, G, B, A)
purple_color = (128, 0, 128, 255)  # 紫色 (R, G, B, A)

# 调用函数进行颜色替换
replace_color(icon_path, new_icon_path, black_color, purple_color)
