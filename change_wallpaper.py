import ctypes
import requests
import os

# 图片缓存路径
IMG_CACHE_DIR = os.getcwd()+'\\img_cache'

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

def save_wallpaper_path(filepath):
    '保存壁纸路径到文件'
    with open('wallpaper_path.txt','w',encoding='utf-8') as f:
        f.write(filepath)

def set_wallpaper(filepath):
    '设置壁纸为指定的图片'
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
    save_wallpaper_path(filepath)

def change_wallpaper():
    filepath = get_and_cache_img()
    set_wallpaper(filepath)

if __name__ == '__main__':
    change_wallpaper()