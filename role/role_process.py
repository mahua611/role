# 这个文件的作用是确定该脚本的流程   确定识别图片的顺序
# 对中途下载或称长短和中间夹杂视频等情况的处理
import time

from service import IdenPicture
from img import role_img1, role_img2, role_img3, role_img4, role_img5, role_img6, role_img7, role_img8, await_img


def cir_process():
    # 选择无语音下载
    IdenPicture.picture(role_img3, 0.8, 60)
    # 等待下载结束后点击菜单
    # 添加等待函数判断是否已经下载完成
    time.sleep(2)
    IdenPicture.await_picture(await_img)
    IdenPicture.cai_picture(role_img4)
    # 选择跳过
    IdenPicture.picture(role_img5, 0.8, 55)
    # 选择跳过
    IdenPicture.picture(role_img6, 0.8, 60)
    # 点击关闭
    IdenPicture.picture(role_img7, 0.8, 60)


def sel_process():
    # 这里的内容是看一个剧情的重复阶段
    # 点击没有看过的剧情
    IdenPicture.picture(role_img2, 0.7, 60)
    # 中间间隔3秒点击下一个新剧情
    time.sleep(3)
    IdenPicture.picture(role_img2, 0.7, 60)


def judge_process():
    flag = True
    while flag:
        # 这里第一个本页没有新内容判断的是没有无语音下载
        if IdenPicture.judge_picture(role_img3):
            cir_process()
        else:
            # 返回然后选择新内容
            IdenPicture.special_picture(role_img8)
            # 中间间隔3秒点击下一个新剧情
            time.sleep(3)
            # 加一个if语句如果说看到还有new就继续进行循环否则则停止
            if IdenPicture.judge_picture(role_img2):
                flag = True
                sel_process()
                cir_process()
            else:
                flag = False
                print("剧情已经全部过完")


# 角色剧情
def role_process():
    # 进入角色剧情界面
    IdenPicture.picture(role_img1, 0.8, 60)
    # 这里是进行选择角色是否还有没有看过的剧情
    sel_process()
    # 这里是看一个角色剧情时的循环操作
    cir_process()
    # 这里是判断返回值如果是True的话进行重复操作
    judge_process()
