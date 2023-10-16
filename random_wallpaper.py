import ctypes
import requests
import os
import shutil
import pystray
from PIL import Image
from pystray import MenuItem
from icon_png import img
import base64

# 图片缓存路径
IMG_CACHE_DIR = os.getcwd()+'\\img_cache'
# 图片保存路径
IMG_SAVED_DIR = os.getcwd()+'\\img_saved'
# 当前壁纸路径
CURRENT_WALLPAPER_PATH = ''

def get_and_cache_img(raw_img_url = "https://www.loliapi.com/acg/pc/?tpye=img"):
    '获取并缓存图片'
    # 获取图片
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    }
    r = requests.get(raw_img_url,headers=headers)
    
    # 缓存图片
    try:
        if not os.path.exists(IMG_CACHE_DIR):
            print('文件夹',IMG_CACHE_DIR,'不存在，重新建立')
            os.makedirs(IMG_CACHE_DIR)
        img_url = r.url # 得到图片文件的网址
        #获得图片文件名，包括后缀
        basename = img_url.split('/')[-1]
        #拼接目录与文件名，得到图片路径
        filepath = os.path.join(IMG_CACHE_DIR, basename)
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
    global CURRENT_WALLPAPER_PATH
    CURRENT_WALLPAPER_PATH = filepath

def save_wallpaper():
    '保存当前壁纸'
    try:
        if not os.path.exists(IMG_SAVED_DIR):
            print('文件夹',IMG_SAVED_DIR,'不存在，重新建立')
            os.makedirs(IMG_SAVED_DIR)
        dst_dir = IMG_SAVED_DIR + '\\' + CURRENT_WALLPAPER_PATH.split('\\')[-1]
        shutil.move(CURRENT_WALLPAPER_PATH, dst_dir)
    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print('错误 ：',e)

def clear_wallpaper_cache():
    '清除所有壁纸缓存'
    for file in os.listdir(IMG_CACHE_DIR):
        if file.endswith(".jpg"):
            os.remove(os.path.join(IMG_CACHE_DIR, file))

def on_exit(icon):
    clear_wallpaper_cache()
    icon.stop()

def change_wallpaper():
    filepath = get_and_cache_img()
    set_wallpaper(filepath)

def main():
    change_wallpaper()
    menu = (MenuItem('保存当前壁纸', save_wallpaper),
            MenuItem('换一张', change_wallpaper),
            MenuItem('退出', on_exit))
    if not os.path.exists('icon.png'):
        tmp = open('icon.png', 'wb')        #创建临时的文件
        tmp.write(base64.b64decode(img))    ##把这个one图片解码出来，写入文件中去。
        tmp.close()
    image = Image.open('icon.png')
    icon = pystray.Icon("随机壁纸", image, "随机壁纸\n右键“换一张”\n等待五秒", menu)
    icon.run()

if __name__ == '__main__':
    main()