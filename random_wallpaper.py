import os
import shutil
import pystray
from PIL import Image
from pystray import MenuItem
from icon_png import img
import base64

from change_wallpaper import change_wallpaper

# 图片缓存路径
from change_wallpaper import IMG_CACHE_DIR
# 图片保存路径
IMG_SAVED_DIR = os.getcwd()+'\\img_saved'

def get_wallpaper_path():
    '获取壁纸路径'
    if not os.path.exists('wallpaper_path.txt'):
        return None
    with open('wallpaper_path.txt','r',encoding='utf-8') as f:
        filepath = f.read()
    return filepath

def save_wallpaper(icon):
    '保存当前壁纸'
    try:
        src_dir = get_wallpaper_path()
        if src_dir is not None:
            if not os.path.exists(IMG_SAVED_DIR):
                print('文件夹',IMG_SAVED_DIR,'不存在，重新建立')
                os.makedirs(IMG_SAVED_DIR)
            dst_dir = IMG_SAVED_DIR + '\\' + src_dir.split('\\')[-1]
            shutil.move(src_dir, dst_dir)
    except IOError as e:
        print('保存失败',e)
        icon.notify("图片缓存可能已被清理：" + str(e), "随机壁纸保存失败")
    except Exception as e:
        print('错误 ：',e)

def clear_wallpaper_cache():
    '清除所有壁纸缓存'
    if os.path.exists(IMG_CACHE_DIR):
        for file in os.listdir(IMG_CACHE_DIR):
            if file.endswith(".jpg"):
                os.remove(os.path.join(IMG_CACHE_DIR, file))

def on_exit(icon):
    clear_wallpaper_cache()
    icon.stop()

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