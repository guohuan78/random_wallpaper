# 软件使用

随机更换二次元壁纸

## 使用姿势

1. 将“随机壁纸.exe”添加至开机自启动，每次开机随机更换壁纸，系统托盘处可进行“更换壁纸”、“保存壁纸”等操作。
2. 将“更换壁纸.exe”添加至桌面鼠标右键菜单，右键桌面背景点击“更换壁纸”即可进行更换，更加方便快捷高效。

## 设置方法

一、设置软件开机自启动：[在 Windows 10 中添加在启动时自动运行的应用 - Microsoft 支持](https://support.microsoft.com/zh-cn/windows/%E5%9C%A8-windows-10-%E4%B8%AD%E6%B7%BB%E5%8A%A0%E5%9C%A8%E5%90%AF%E5%8A%A8%E6%97%B6%E8%87%AA%E5%8A%A8%E8%BF%90%E8%A1%8C%E7%9A%84%E5%BA%94%E7%94%A8-150da165-dcd9-7230-517b-cf3c295d89dd)

1. 按 Windows 徽标键+  **R** ，键入“ **shell:startup** ”，然后选择“ **确定** ”。这将打开“ **启动** ”文件夹。
2. 右键该应用，选择“创建快捷方式”，并粘贴到 **“启动”** 文件夹中。

二、添加到桌面鼠标右键时的菜单：[Python：一键更换桌面壁纸_python修改桌面壁纸-CSDN博客](https://blog.csdn.net/kingjeewhy8023/article/details/112980736)

1. 开始 + R打开运行框，输入regedit打开注册，进入 `HKEY_CLASSES_ROOT\Directory\Background\shell\`，右键点击shell，选择新建>项（K），命名为更换壁纸。
2. 点击刚刚创建好的项，双击默认，数值数据填入 `更换壁纸`。
3. 再次选择刚刚创建好的项新建>项（K），命名为command，数据填为“更换壁纸”软件的EXE文件地址。

# 依赖的API

[主页 | LoliAPI](https://loliapi.com/)

# 打包命令

```bash
pyinstaller -F -w -i icon.png random_wallpaper.py
```

```bash
pyinstaller -F -w -i icon.png change_wallpaper.py --hidden-import plyer.platforms.win.notification
```
