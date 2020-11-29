#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 10:34
# @Author  : Chris.Ma
#对不同浏览器的支持,浏览器常用操作
from selenium import webdriver
from time import sleep

if __name__ == "__main__":
    #浏览器初始化
    #1,python selenium 代码与Remote Server通过ChromeDrvier建立http通讯通道
    #2,Remote Server通过浏览器内核api去启动浏览器
    #3，启动浏览器操作返回调用结果给Remote Server
    #4，Remote Server返回http response给到python selenium代码
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()
    # driver = webdriver.Edge()
    #浏览器最大化
    driver.maximize_window()
    #浏览器URL导航操作
    driver.get("http://www.baidu.com")
    sleep(2)
    #最小化
    driver.minimize_window()
    sleep(2)
    #浏览器大小设置
    driver.set_window_size(800,600)
    driver.get("https://cn.bing.com/")
    sleep(2)
    driver.back()
    #当前页面标题
    print(driver.title)
    #当前页面url
    print(driver.current_url)
    sleep(2)
    driver.forward()
    #页面刷新
    driver.refresh()
    #当前页面源码
    print(driver.page_source)
    sleep(2)
    #浏览器关闭
    #关闭当前页面
    # driver.close()
    #关闭当前driver打开的所有浏览器
    driver.quit()
