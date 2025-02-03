# 和角色剧情不同的是有可能会有视频面对视频这种点击屏幕并且选择跳过选项
# 如何判断这个页面是视频
# 1.一种是使用对比两张图片的差异如果差异较大的话就进行点击屏幕跳过
# 2.还可以通过判断无语音下载的大小但是这个不准确
# 3.在屏幕中找元素如果没有菜单说明是视频实行点击跳过视频（可行）
# 幕间和结尾的不能跳过的联播图画
import time

import pyautogui

from service import IdenPicture
from img import mast_img1, mast_img2, mast_img3, mast_img4, mast_img5, mast_img6, mast_img7, mast_img8, await_img


def mast_process():
    # 进入主线剧情界面
    IdenPicture.picture(mast_img1, 0.8, 60)
    # 查找新内容
    sel_process()
    cir_process()
    judge_process()
    # 判断菜单如果有菜单的话正常进行没有的话开始等待
    # if IdenPicture.judge_menu(mast_img4):
    #     cir_process()
    #     judge_process()


# 接下来是循环过程
def judge_process():
    flag = True
    while flag:
        # 这里第一个本页没有新内容判断的是没有无语音下载
        if IdenPicture.judge_picture(mast_img3):
            cir_process()
        else:
            # 返回然后选择新内容
            IdenPicture.special_picture(mast_img8)
            # 中间间隔3秒点击下一个新剧情
            time.sleep(3)
            # 加一个if语句如果说看到还有new就继续进行循环否则则停止
            if IdenPicture.judge_picture(mast_img2):
                flag = True
                sel_process()
                cir_process()
            else:
                flag = False
                print("剧情已经全部过完")


def cir_process():
    # 选择无语音下载
    IdenPicture.picture(mast_img3, 0.8, 60)
    # 等待下载结束后点击菜单
    # 添加等待函数判断是否已经下载完成
    time.sleep(2)
    IdenPicture.await_picture(await_img)
    # 这里开始判断是否存在菜单不存在的话返回False说明进入了幕间或者是视频
    # 点击屏幕弹出跳过的话就是剧情视频没有出现的话是幕间(幕间不能跳过静静等待菜单的出现)
    if IdenPicture.judge_menu(mast_img4):
        var_jump()
        # 后续开始循环查看是否存在关闭
    judge_close()
    IdenPicture.picture(mast_img7, 0.8, 60)


# 这个方法的作用是判断是否已经过完了这段剧情
def judge_close():
    flag = True
    while flag:
        # 页面内是否存在关闭
        if IdenPicture.judge_picture(mast_img7):
            print("一次跳过全部的剧情")
            # 这里是存在说明本次剧情已经过完
            flag = False
        else:
            # 没有提示关闭开始查看是否有菜单判断是否是剧情
            # 调用小循环函数点击菜单并点击跳过
            if IdenPicture.judge_menu(mast_img4):
                print("这里有菜单执行点击菜单并选择跳过的流程")
                var_jump()
            else:
                # 判断是否是幕间
                if IdenPicture.judge_interlude(mast_img6, 0.8):
                    print("这里是个视频点击鼠标并选择跳过剧情的环节")
                    # 点击跳过
                    click()
                else:
                    # 等待10s
                    print("这里是个幕间等待幕间结束")
                    time.sleep(10)


def var_jump():
    # 点击菜单进行跳过操作
    IdenPicture.cai_picture(mast_img4)
    # 选择跳过
    IdenPicture.picture(mast_img5, 0.8, 50)
    IdenPicture.picture(mast_img6, 0.8, 50)

    # 这是一个点击函数


def click():
    # 判断已经点击了屏幕会出现跳过按钮
    IdenPicture.picture(mast_img6, 0.8, 55)


def sel_process():
    # 这里的内容是看一个剧情的重复阶段
    # 点击没有看过的剧情
    IdenPicture.picture(mast_img2, 0.7, 60)
    # 中间间隔3秒点击下一个新剧情
    time.sleep(3)
    IdenPicture.picture(mast_img2, 0.7, 60)
