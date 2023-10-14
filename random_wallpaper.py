import ctypes
import requests
import os
import pystray
from PIL import Image
from pystray import MenuItem

# 图片缓存路径
img_cache_dir = os.getcwd()+'\\img_cache'

def get_and_cache_img(raw_img_url = "https://www.loliapi.com/acg/pc/?tpye=img"):
    '获取并缓存图片'
    # 获取图片
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    }
    r = requests.get(raw_img_url,headers=headers)
    
    # 缓存图片
    try:
        if not os.path.exists(img_cache_dir):
            print('文件夹',img_cache_dir,'不存在，重新建立')
            os.makedirs(img_cache_dir)
        img_url = r.url # 得到图片文件的网址
        #获得图片文件名，包括后缀
        basename = img_url.split('/')[-1]
        #拼接目录与文件名，得到图片路径
        filepath = os.path.join(img_cache_dir, basename)
        #下载图片，并保存到文件夹中
        with open(filepath, 'wb') as f:  # 图片信息是二进制形式，所以要用wb写入
            f.write(r.content)
    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print('错误 ：',e)
    
    return filepath

def set_wallpaper(filepath):
    '设置壁纸为指定的图片'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)

def clear_wallpaper_cache():
    '清除所有壁纸缓存'
    for file in os.listdir(img_cache_dir):
        if file.endswith(".jpg"):
            os.remove(os.path.join(img_cache_dir, file))

def on_exit(icon):
    icon.stop()

def change_wallpaper():
    filepath = get_and_cache_img()
    set_wallpaper(filepath)

def main():
    change_wallpaper()
    menu = (MenuItem('清空壁纸缓存', clear_wallpaper_cache),
            MenuItem('换一张', change_wallpaper),
            MenuItem('退出', on_exit))
    image = Image.open("icon.png")
    icon = pystray.Icon("随机壁纸", image, "随机壁纸\n右键“换一张”\n等待五秒", menu)
    icon.run()

if __name__ == '__main__':
    main()