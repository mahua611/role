import time

import cv2
import numpy as np
import pyautogui


# //改为传入两个值一个是图片一个是对比度
def ver_picture(img, percentage, threshold_percent):
    flag = True
    num = 1
    judge_num = 1
    percentage = 0.8
    while flag and num <= 3:
        try:
            # 查找图片
            jump_location = pyautogui.locateOnScreen(img, confidence=percentage)
            # 拆解坐标位置
            screen_width, screen_height, wide, height = jump_location
            # 确定一个范围用于截图
            region = (int(screen_width + wide - 150), int(screen_height + height) - 150, 100, 100)
            screenshot1 = pyautogui.screenshot(region=region)
            if jump_location:
                # 图片中心
                jump_x, jump_y = pyautogui.center(jump_location)
                # 移动鼠标
                pyautogui.moveTo(jump_x, jump_y + 10, 1)
                # 控制鼠标点击事件
                pyautogui.click()
                # 到这里说明已经匹配成功令flag=False可以使循环停止
                flag = False
                time.sleep(1)
                screenshot2 = pyautogui.screenshot(region=region)
                while not compare_screenshots(screenshot1, screenshot2, threshold_percent) and judge_num < 3:
                    num += 1
                    time.sleep(2)
                    pyautogui.click()
            else:
                print('未找到按钮图像')
        except pyautogui.ImageNotFoundException:
            percentage -= 0.1
            print("没有匹配到图片将数值下降0.1当前值为:" + str(percentage))
            num += 1
            time.sleep(1)
            # 如果没有匹配成功的话使confidence值自减0.1


# pyautogui包规定的坐标原点位于左上角向下y值增大向右x值增大
def picture(img, percentage, threshold_percent):
    ver_picture(img, percentage, threshold_percent)


# 这是一个特殊的图片匹配方法如果点击前后两个图片的变化不大不能使用openCV来比较两张图片
def special_picture(img):
    flag = True
    num = 1
    percentage = 0.7
    while flag and num <= 4:
        try:
            jump_location = pyautogui.locateOnScreen(img, confidence=percentage)
            jump_x, jump_y = pyautogui.center(jump_location)
            if jump_location:
                # 图片中心
                jump_x, jump_y = pyautogui.center(jump_location)
                # 移动鼠标
                pyautogui.moveTo(jump_x, jump_y + 10, 1)
                # 控制鼠标点击事件
                pyautogui.click()
                # 到这里说明已经匹配成功令flag=False可以使循环停止
                flag = False
        except pyautogui.ImageNotFoundException:
            percentage -= 0.1
            print("没有匹配到图片将数值下降0.1当前值为:" + str(percentage))
            num += 1
            time.sleep(1)
            # 如果没有匹配成功的话使confidence值自减0.1


def cai_picture(img):
    screen_width, screen_height = pyautogui.size()
    search_region = (screen_width - 300, 0, 300, 500)
    flag = True
    num = 1
    percentage = 0.9
    while flag and num <= 3:
        try:
            jump_location = pyautogui.locateOnScreen(img, region=search_region, confidence=percentage)
            jump_x, jump_y = pyautogui.center(jump_location)
            if jump_location:
                # 图片中心
                jump_x, jump_y = pyautogui.center(jump_location)
                # 移动鼠标
                pyautogui.moveTo(jump_x, jump_y, 1)
                # 控制鼠标点击事件
                pyautogui.click()
                # 到这里说明已经匹配成功令flag=False可以使循环停止
                flag = False
        except pyautogui.ImageNotFoundException:
            percentage -= 0.1
            print("没有匹配到图片将数值下降0.1当前值为:" + str(percentage))
            num += 1
            time.sleep(1)
            # 如果没有匹配成功的话使confidence值自减0.1


# 这是一个判断函数判断是否还有新内容判断是否自动弹出下载剧情
def judge_picture(img):
    percentage = 0.8
    flag = True
    num = 1
    while flag and num < 4:
        try:
            location = pyautogui.locateOnScreen(img, confidence=percentage)
            if location:
                print("存在需要判断的按钮")
                # 返回True和False如果返回了True说明还有新内容可以继续进行循环操作
                # 如果返回的是False的话则需要进行返回找寻新的剧情
                return True
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            percentage -= 0.1
            print("没有匹配到图片将数值下降0.1当前值为:" + str(percentage))
            num += 1
    print("不存在需要的按钮")
    return False


# 对比函数通过比较操作后两个图片的差异来判断是否操作成功
def compare_screenshots(screenshot1, screenshot2, threshold_percent):
    # 将截图转换为 NumPy 数组
    frame1 = np.array(screenshot1)
    frame2 = np.array(screenshot2)

    # 将截图转换为灰度图（为了简化比较）
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # 计算两张图片之间的绝对差异
    diff = cv2.absdiff(gray1, gray2)

    # 计算差异图像中非零像素的数量
    num_diff_pixels = np.sum(diff != 0)

    # 计算截图的总像素数量
    total_pixels = gray1.shape[0] * gray1.shape[1]

    # 计算差异比例
    diff_percent = (num_diff_pixels / total_pixels) * 100

    # 打印差异比例
    print(f'Difference percentage: {diff_percent:.2f}%')

    # 根据差异比例判断并返回结果
    if diff_percent > threshold_percent:
        print("成功")
        return True
    else:
        print("没有成功")
        return False


# 添加一个函数判断是否有菜单如果没有的话说明正在播放剧情 这个函数只起到了判断的作用
def judge_menu(img):
    screen_width, screen_height = pyautogui.size()
    search_region = (screen_width - 300, 0, 300, 500)
    flag = True
    num = 1
    percentage = 0.7
    while flag and num <= 2:
        try:
            jump_location = pyautogui.locateOnScreen(img, region=search_region, confidence=percentage)
            jump_x, jump_y = pyautogui.center(jump_location)
            if jump_location:
                # 这里是匹配到了菜单说明这里不是在播放视频可以返回一个bool类型的数据继续进行后续过程
                return True
        except pyautogui.ImageNotFoundException:
            # 这里没有匹配到图片的话实行B操作执行点击跳过函数
            percentage -= 0.1
            print("没有匹配到图片将数值下降0.1当前值为:" + str(percentage))
            num += 1
            time.sleep(1)
            # 如果没有匹配成功的话使confidence值自减0.1
    # 这里显示没有存在菜单按钮
    return False


# 这是一个判断是否是幕间的函数
def judge_interlude(img, percentage):
    pyautogui.click()
    time.sleep(1)
    try:
        location = pyautogui.locateOnScreen(img, confidence=percentage)
        if location:
            print("通过点击事件出现跳过说明是剧情视频")
            return True
    except:
        print("没有识别到跳过按键说明是幕间无法跳过")
        return False


# 这是个查看是否在加载中的函数
def await_picture(img):
    flag = True
    percentage = 0.9
    while flag:
        time.sleep(2)
        try:
            jump_location = pyautogui.locateOnScreen(img, confidence=percentage)
            if jump_location:
                print("仍在加载中")
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            flag = False
