# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox, tkSimpleDialog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
import SendKeys
import telnetlib
import logging

class m5(object):
    def telnet(self):
        global HOST, user, passwd, tn, default_tn,ret
        if default_tn == True:
            check_tn = False

            try:
                tn = telnetlib.Telnet(HOST)
                # tn.read_until("login: ")
                # tn.write(user + "\n")
                # if passwd:
                #     tn.read_until("Password: ")
                #     tn.write(passwd + "\n")
                # print 'Success' 
                tn.write('cd ' + sample_bin_path + '\n')
                time.sleep(1)
                # tn.write('./setup.sh restart\n')
                # time.sleep(25)
                logging.warning(tn.read_very_eager)  
                tn.write('cat /proc/ips_info\n')
                print 'Restart OK'
                ret = True  

            except WindowsError:
                tkMessageBox.showwarning(message='Can not connect telnet')  
                print 'Failed'  
                ret = False 
            else:
                if ret :
                    tkMessageBox.showwarning(message='Telnet IP is ' + HOST)
                    for x in range(11):
                        streamingMenu.entryconfig(x,state=NORMAL)
                    for x in range(9):
                        socialMenu.entryconfig(x, state=NORMAL)
                    for x in range(8):
                        transferMenu.entryconfig(x, state=NORMAL)
                    for i in range(4):
                        testMenu.entryconfig(i, state=NORMAL)
                    settingMenu.entryconfig(1, label="Disconnect Telnet Console", command=m5.disconnect_telnet)
                    menu.entryconfig(5, state=NORMAL)
                    check_tn = True  
                else:
                    print "Final"

        elif default_tn == False:
            try:
                tn.close()
                tn = telnetlib.Telnet(HOST)
            except WindowsError:
                tkMessageBox.showwarning(message='Can not connect' + HOST)    
            except ValueError:
                tkMessageBox.showwarning(message=user + "/"+ passwd + ' is Error!!')   

            else:
                for i in range(11):
                    streamingMenu.entryconfig(i , state=NORMAL)
                for i in range(9):
                    socialMenu.entryconfig(i ,state=NORMAL)
                for i in range(8):
                    transferMenu.entryconfig(i ,state=NORMAL)
                for i in range(4):
                    testMenu.entryconfig(i ,state=NORMAL)        
                settingMenu.entryconfig(1, label="Disconnect Telnet", command=m5.disconnect_telnet)
                menu.entryconfig(5, state=NORMAL)
                tkMessageBox.showinfo(message='Connect ' + HOST + ' Successfully!')    
        else:
            tkMessageBox.showinfo(message='Telnet was connected!!!')

        # tn.write("exit\n")
        # print tn.read_all()
    def disconnect_telnet(self):
        global tn, ret
        if ret:
            tn.write("exit\n")
            tn.close()
            
            for i in range(11):
                streamingMenu.entryconfig(i, state=DISABLED)
            for i in range(9):
                socialMenu.entryconfig(i, state=DISABLED)
            for i in range(8):
                transferMenu.entryconfig(i, state=DISABLED)
            for i in range(4):
                testMenu.entryconfig(i, state=DISABLED)
            tkMessageBox.showinfo(title='Telnet Status', message="Telnet is disconnected!!")
            settingMenu.entryconfig(1, label="Connect Telnet Console", command=m5.telnet) 
    def duration(self):
        def time_set():
            global duration, default_duration
            data = str(msgShow.get(1.0, END)).rstrip()
            if len(data) == 0:
                tkMessageBox.showwarning(title='Null!', message='Can not Empty!!')
                root.top.focus()
            else:
                duration = int(data)
                tkMessageBox.showinfo(title='Update Setting...', message='Updated Successfully!!!')
                default_duration = False
                root.top.destroy()

        global duration
        root.top = Toplevel(master=root, height=5, width=60)
        root.top.title("Test Duration Setting")
        Label(root.top, height=1, width=55, text="Unit: Second", fg="blue").pack()
        Label(root.top, height=1, width=55, text="Current Duration is: ").pack()
        Label(root.top, height=1, width=55, text=str(duration), fg="red").pack()
        msgShow = Text(root.top, height=1, width=55)
        msgShow.pack()
        Button(root.top, text="Confirm", command=time_set).pack()
        Button(root.top, text="Cancel", command=root.top.destroy).pack()
    def sample_BIN(self):
        def path_set():
            global sample_bin_path
            data = str(msgShow.get(1.0, END)).rstrip()
            if len(data) == 0:
                tkMessageBox.showwarning(title='Null!', message='Can not Empty!!')
                root.top.focus()
            else:
                sample_bin_path = data
                tkMessageBox.showinfo(title='Update Setting...', message='Updated Successfully!')
                root.top.destroy()

        global sample_bin_path
        root.top = Toplevel(master=root, height=5, width=60)
        root.top.title("Sample.bin Path Setting")
        Label(root.top, height=1, width=55, text="Sample.bin Full Path Name").pack()
        Label(root.top, height=1, width=55, text="Current Path is: ").pack()
        Label(root.top, height=1, width=55, text=sample_bin_path, fg="red").pack()
        msgShow = Text(root.top, height=1, width=55)
        msgShow.pack()
        Button(root.top, text="Confirm", command=path_set).pack()
        Button(root.top, text="Cancel", command=root.top.destroy).pack()   
    def smartDNS(self):
        driver = webdriver.Chrome()
        driver.get("https://smartdns.smartydns.com/index.php?smartkey=55bdd65658122819c46e2384d7dda7c7")
        time.sleep(1)
        driver.quit()
    def engine(self):
        global sample_bin_path, tn 
        tn.write('cd ' + sample_bin_path + '\n')
        tn.write('./setup.sh restart br-wan\n')
        time.sleep(10)
        # tn.write('./iqos.sh restart\n')
        # time.sleep(5)
        print("DPI restart done")
     
class streaming:
    def youtube(self):
        global logFile, tn, duration, sample_bin, g_driver
        print ("Youtube test start")
        serSet()
        tn.write('echo YouTube Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://www.youtube.com/watch?v=HmZKgaHa3Fg")
        driver.implicitly_wait(10)
        try:
            if driver.find_element_by_xpath("//div[@class='videoAdUiSkipContainer html5-stop-propagation']"):
                print ("ad")
                time.sleep(10)
                driver.find_element_by_xpath("//div[@class='videoAdUiSkipContainer html5-stop-propagation']").click()
                print ("ad skip")
                pass 
        except:
            print ("No ad")   
        time.sleep(duration + 60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()
    def netflix(self):
    	global logFile, tn, duration, email, password, sample_bin, g_driver
        print ("Netfilx test start")
        serSet()
        tn.write('echo Netflix Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        profile = webdriver.ChromeOptions()
        profile.add_experimental_option('excludeSwitches', ['disable-component-update'])
        driver = webdriver.Chrome(executable_path=g_driver, chrome_options=profile)
        driver.get("chrome://components/")
        components = driver.find_elements_by_class_name('button-check-update')
        for c in components:
                try:
                    c.click()
                except:
                    pass
        time.sleep(3)
        driver.get("https://www.netflix.com/Login")
        time.sleep(1)
        emailKey = driver.find_element_by_name('email')
        emailKey.send_keys(email)
        time.sleep(1)
        nextstep = "//button[@class='btn login-button btn-submit btn-small']"
        driver.find_element_by_xpath(nextstep).click()
        time.sleep(1)
        password = driver.find_element_by_name('password')
        password.send_keys('Vro16100web')
        time.sleep(1)
        nextstep = "//button[@class='btn login-button btn-submit btn-small']"
        driver.find_element_by_xpath(nextstep).click()
        time.sleep(1)
        while driver.find_element_by_css_selector('.profile-icon') == False:
                    SendKeys.SendKeys("{F5}")
        if driver.find_element_by_css_selector('.profile-icon'):
            driver.find_element_by_css_selector('.profile-icon').click()
        driver.get("https://www.netflix.com/watch/70296528?trackId=14170082&tctx=1%2C1%2C5fd2de46-16ae-4bfc-a28e-421d619190af-158205054")
        time.sleep(duration + 60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('pwd\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('pwd', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()        
    def dailymotion(self):
    	global logFile, tn, duration, sample_bin, g_driver
        print ("Dailymotion test start")
        serSet()
        tn.write('echo Dailymotion Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("http://www.dailymotion.com/video/x5xi9b4")
        time.sleep(duration + 60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close() 
    def hulu(self):
    	global logFile,  tn, duration, email, password, sample_bin, g_driver
        print ("Hulu test start")
        serSet()
        tn.write('echo Hulu Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://secure.hulu.com/account")
        time.sleep(5)

        """
        If html can't find id or name,can use xpath search need function place
        """
        emailKey = driver.find_element_by_xpath("//input[@placeholder='email']")
        emailKey.send_keys(email)
        time.sleep(2)
        passwordKey = driver.find_element_by_xpath("//input[@placeholder='password']")
        passwordKey.send_keys(password)
        time.sleep(2)
        
        driver.find_element_by_xpath("//button[@class='hulu-login-btn']").click()
        time.sleep(10)
        driver.get("https://www.hulu.com/watch/1105805")		
        time.sleep(duration + 60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()    
    def amazon(self):
        global logFile, tn, duration, email, password, sample_bin, g_driver
        print ("Amazon test start")
        serSet()
        tn.write('echo Amazon Instant Video Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        profile = webdriver.ChromeOptions()
        profile.add_experimental_option('excludeSwitches', ['disable-component-update'])
        driver = webdriver.Chrome(executable_path=g_driver, chrome_options=profile)
        driver.get("chrome://components/")
        components = driver.find_elements_by_class_name('button-check-update')
        for c in components:
                try:
                    c.click()
                except:
                    pass
        driver.get("https://www.primevideo.com/region/fe/auth-redirect/ref=av_auth_ubid/358-5756486-5855621?_encoding=UTF8&returnUrl=%2Fregion%2Ffe%2Fref%3Datv_primeLPsignin%2F358-5756486-5855621")
        driver.implicitly_wait(5)
        driver.find_element_by_name("email").send_keys(email)
        time.sleep(1)
        driver.find_element_by_name("password").send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(2)
        driver.get("https://www.primevideo.com/region/fe/detail/0HX3CC57M63NWXIHBE5NH2SJ5F/ref=pd_cbs_318_9")
        driver.implicitly_wait(10)
        try:
            if driver.find_element_by_class_name("av-play-icon js-deeplinkable"):
                driver.find_element_by_class_name("av-play-icon js-deeplinkable").click()
                time.sleep(duration + 60)	
        except:
            print("log in fail")
            driver.get("https://www.amazon.com/gp/video/detail/B072FNHS9P/ref=atv_hm_hom_1_c_tmpopa_brws_11_1?ie=UTF8&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=3258029442&pf_rd_r=5R8Z2XGSF25G7T3554BC&pf_rd_s=center-17&pf_rd_t=12401")
            driver.implicitly_wait(5)
            driver.find_element_by_xpath("//div[@class='dv-trailer js-trailer-button js-hide-on-play-left deeplinkable']").click()
            time.sleep(120)
            driver.get("https://www.amazon.com/gp/video/detail/B0711Y5YZ8/ref=atv_hm_hom_1_c_tmpopa_brws_11_2?ie=UTF8&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=3258029442&pf_rd_r=5R8Z2XGSF25G7T3554BC&pf_rd_s=center-17&pf_rd_t=12401")
            driver.implicitly_wait(5)
            driver.find_element_by_xpath("//div[@class='dv-trailer js-trailer-button js-hide-on-play-left deeplinkable']").click()
            time.sleep(120)
            driver.get("https://www.amazon.com/gp/video/detail/B07215NWRL/ref=atv_hm_hom_1_c_tmpopa_brws_11_3?ie=UTF8&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=3258029442&pf_rd_r=5R8Z2XGSF25G7T3554BC&pf_rd_s=center-17&pf_rd_t=12401")
            driver.implicitly_wait(5)
            driver.find_element_by_xpath("//div[@class='dv-trailer js-trailer-button js-hide-on-play-left deeplinkable']").click()
            time.sleep(120)
        driver.delete_all_cookies()    
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()
    def vevo(self):
    	global logFile, tn, duration, sample_bin, g_driver
        print ("Vevo test start")
        serSet()
        tn.write('echo Vevo Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://www.vevo.com/watch/logic/1-800-273-8255/USUV71703560")
        time.sleep(duration + 60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()
    def vimeo(self):
    	global logFile, tn, duration, sample_bin, g_driver
        print ("Vimeo test start")
        serSet()
        tn.write('echo Vimeo Test\n')		
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://vimeo.com/170955105")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@data-title-play='Play']").click()
        time.sleep(duration+60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()	
    def vudu(self):
        global logFile, tn, duration, sample_bin, g_driver
        print ("Vudu test start")
        serSet()
        tn.write('echo Vudu Test\n')
        time.sleep(1)
        tn.write('./sample.bin -a get_qos_user_info -i ' + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://www.vudu.com/movies/#!content/850532/Transformers-The-Last-Knight-Digital")
        time.sleep(3)
        play = driver.find_element_by_xpath("//div[@class='trailer']")
        play.click()
        time.sleep(180)
        play.click()
        time.sleep(duration + 60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()	
    def pandora(self):
        global logFile, tn, duration, sample_bin
        print ("Pandora test start")
        serSet()
        tn.write('echo Pandora Test\n')
        time.sleep(1)
        tn.write('./sample.bin -a get_qos_user_info -i ' + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome()
        driver.get("https://www.pandora.com/station/play/3832432596176838023")
        time.sleep(60)
        play = driver.find_element_by_xpath("//button[@class='TunerControl SkipButton Tuner__Control__Button Tuner__Control__Skip__Button']")
        play.click()
        time.sleep(60)
        play.click()
        time.sleep(60)
        play.click()
        time.sleep(60)
        play.click()
        time.sleep(60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()	    
    def streamingTest(self):
        streaming.hulu()
        time.sleep(10)
        streaming.amazon()
        time.sleep(10)
        streaming.youtube()
        time.sleep(10)
        streaming.netflix()
        time.sleep(10)
        streaming.dailymotion()
        time.sleep(10)
        streaming.pandora()
        time.sleep(10)
        streaming.vevo()
        time.sleep(10)
        streaming.vimeo()
        time.sleep(10)
        m5.engine()
        time.sleep(20)

class socialSoftware:
    def facebook(self):
        global logFile, sample_bin, tn, duration, g_driver
        print ("Facebook test start")
        serSet()
        tn.write('echo Facebook Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://www.facebook.com/login/")
        username = driver.find_element_by_name('email')
        username.send_keys('XXXXX')
        password = driver.find_element_by_name('pass')
        password.send_keys('XXXXX')
        time.sleep(5)
        try:
            driver.find_element_by_id('loginbutton').click()
        except:
            driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _52e0 _4jy6 _4jy1 selected _51sy']").click()
            
        time.sleep(5)
        SendKeys.SendKeys("{ESC}")
        time.sleep(1)
        for i in range(1, duration*2):
            if i % 200 == 0:
                SendKeys.SendKeys("{F5}")
            SendKeys.SendKeys("{PGDN}")
            time.sleep(0.5)
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                        
        f.close()        
    def google_Plus(self):
    	global logFile, sample_bin, tn, duration, g_driver
        print ("Google+ test start")
        serSet()
        tn.write('echo Google-Plus Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://plus.google.com/")
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_xpath("//input[@type='email']").send_keys("XXXXX")
        driver.find_element_by_id("identifierNext").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[@type='password']").send_keys("XXXXX")
        driver.find_element_by_id("passwordNext").click()
        time.sleep(1)
        for i in range(1, duration*2):
            if i % 100 == 0:
                SendKeys.SendKeys("{F5}")
            SendKeys.SendKeys("{PGDN}")
            time.sleep(0.5)
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break     
        f.close()
    def instagram(self):
        global logFile, sample_bin, tn, duration, g_driver
        print ("Instagram test start")
        serSet()
        tn.write('echo Instagram Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        # driver.get("https://www.instagram.com/")
        driver.get("https://www.instagram.com/accounts/login/")
        # driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_name("username").send_keys("XXXXX")
        driver.find_element_by_name("password").send_keys("XXXXX")
        driver.find_element_by_xpath("//button[@class='_qv64e _gexxb _4tgw8 _njrw0']").click()
        time.sleep(2)
        SendKeys.SendKeys("{ESC}")
        time.sleep(1)
        for i in range(1, duration*2):
            if i % 100 == 0:
                SendKeys.SendKeys("{F5}")
                time.sleep(2)
                SendKeys.SendKeys("{ESC}")
            SendKeys.SendKeys("{PGDN}")
            time.sleep(0.5)
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break        
        f.close()
    def linkedIn(self):
        global logFile, sample_bin, tn, duration, g_driver
        print ("LinkedIn test start")
        serSet()
        tn.write('echo LinkedIn Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://www.linkedin.com/")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//input[@id='login-email']").send_keys("XXXXX")
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='login-password']").send_keys("XXXXX")
        time.sleep(3)
        driver.find_element_by_xpath("//input[@id='login-submit']").click()
        driver.implicitly_wait(5)
        for i in range(1, duration*2):
            if i % 100 == 0:
                SendKeys.SendKeys("{F5}")
            SendKeys.SendKeys("{PGDN}")
            time.sleep(0.5)
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                       
        f.close()
    def flickr(self):
        global logFile, sample_bin, tn, duration, g_driver
        print ("Flickr test start")
        serSet()
        tn.write('echo Flickr Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://www.flickr.com/")
        driver.find_element_by_link_text("Log In").click()
        time.sleep(1)
        driver.find_element_by_name("username").send_keys("XXXXX")
        time.sleep(1)
        driver.find_element_by_id("login-signin").click()
        time.sleep(1)
        driver.find_element_by_name("password").send_keys("XXXXX")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)
        for i in range(1, duration*2):
            if i % 100 == 0:
                SendKeys.SendKeys("{F5}")
            SendKeys.SendKeys("{PGDN}")
            time.sleep(0.5)
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()
    def twitter(self):
        global logfile, tn, duration, sample_bin, g_driver
        print("Twitter test start")
        serSet()
        tn.write('echo Twitter Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver) 
        driver.get("https://twitter.com/login")
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//input[@class='js-username-field email-input js-initial-focus']").send_keys("XXXXX")
        time.sleep(3)
        driver.find_element_by_class_name("js-password-field").send_keys("XXXXX")
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        for i in range(1, duration*2):
            if i % 100 == 0:
                SendKeys.SendKeys("{F5}")
            SendKeys.SendKeys("{PGDN}")
            time.sleep(1)    
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                
        f.close()      
    def socialTest(self):
    	socialSoftware.facebook()
        time.sleep(10)
        socialSoftware.google_Plus()
        time.sleep(10)
        socialSoftware.instagram()
        time.sleep(10)
        socialSoftware.linkedIn()
        time.sleep(10)
        socialSoftware.flickr()
        time.sleep(10)
        socialSoftware.twitter()
        time.sleep(10)
        m5.engine()
        time.sleep(20)

class fileBox:
    def dropbox(self):
    	global logFile, sample_bin, tn, duration, g_driver
        print ("Dropbox test start")
        serSet()
        tn.write('echo Dropbox Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.maximize_window()
        # driver.get("https://www.dropbox.com/")
        driver.get("https://www.dropbox.com/login?src=logout")
        driver.implicitly_wait(10)
        # driver.find_element_by_link_text('Sign in').click()
        # driver.find_element_by_xpath("//button[@class='RebrandNavigation-nav--links-item RebrandNavigation-nav--links-item__sign-up ob-button ob-button--link']").click()
        # time.sleep(3)
        driver.find_element_by_xpath("//input[@class='text-input-input autofocus']").send_keys("XXXXX")
        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//input[@class='password-input text-input-input']").send_keys("XXXXX")
        driver.implicitly_wait(2)
        # driver.find_element_by_xpath("//button[@class='login-button signin-button button-primary']").click()
        driver.find_element_by_xpath("//button[@class='login-button button-primary']").click()
        time.sleep(10)
        driver.get("https://www.dropbox.com/home?preview=TestVideo.mp4")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//button[@class='c-btn control__button button-secondary c-btn--secondary open-button__download']").click()
        time.sleep(10)
        driver.find_element_by_xpath("//button[@class='vjs-big-play-button']").click()
        time.sleep(duration + 60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                      
        f.close()
    def google_Driver(self):
        global logFile, sample_bin, tn, duration, g_driver
        print ("Google Driver test start")
        serSet()
        tn.write('echo Google-Driver Test\n')
        time.sleep(1)
        tn.write('./sample.bin -a get_qos_user_info -i ' + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://drive.google.com/?tab=wo")
        driver.find_element_by_link_text("Go to Google Drive").click()
        main_window = driver.current_window_handle
        driver.find_element_by_xpath("//input[@type='email']").send_keys("XXXXX")
        driver.find_element_by_id("identifierNext").click()
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='password']").send_keys("XXXXX")
        time.sleep(3)
        driver.find_element_by_id("passwordNext").click()
        time.sleep(3)
        driver.get("https://drive.google.com/file/d/0B-4n115M_MLPaXBmcTNoZ2FXSlE/view?usp=sharing")
        time.sleep(3)
        driver.find_element_by_xpath("//div[@class='drive-viewer-content-download-button-text']").click()
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])
        time.sleep(1)
        driver.find_element_by_link_text("仍要下載").click()
        time.sleep(duration + 60)
        driver.switch_to_window(main_window)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
                       
        f.close()
    def oneDrive(self):
        global logFile, sample_bin, tn, duration, g_driver
        print ("OneDrive test start")
        serSet()
        tn.write('echo OneDrive Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get("https://onedrive.live.com/about/zh-tw/")
        time.sleep(1)
        driver.find_element_by_link_text("登入").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//input[@class='SignInDialog-input SignInDialog-input--email']").send_keys("XXXXX")
        time.sleep(1)
        driver.find_element_by_link_text("下一步").click()
        driver.implicitly_wait(5)
        driver.find_element_by_name("passwd").send_keys("XXXXX")
        time.sleep(1)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@data-key='id=C3436CE4AFB24B1D%21497&cid=C3436CE4AFB24B1D']").click()
        time.sleep(duration + 60)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break   
                
        f.close()
    def box(self):
        global logFile, sample_bin, tn, duration, g_driver
        print ("Box test start")
        serSet()
        tn.write('echo Box Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver)
        driver.get('https://account.box.com/login')
        driver.implicitly_wait(2)
        driver.find_element_by_name("login").send_keys("XXXXX")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.implicitly_wait(3)
        driver.find_element_by_name("password").send_keys("XXXXX")
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.implicitly_wait(3)
        driver.get('https://app.box.com/file/227682859107')
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//button[@class='bp-btn bp-btn-primary']").click()
        time.sleep(10)
        driver.get('https://app.box.com/file/227658249407')
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//button[@class='bp-btn bp-btn-primary']").click()
        time.sleep(10)
        driver.get('https://app.box.com/file/227664450751')
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//button[@class='bp-btn bp-btn-primary']").click()
        time.sleep(10)
        driver.get('https://app.box.com/file/227678629841')
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//button[@class='bp-btn bp-btn-primary']").click()
        time.sleep(duration)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break      
                
        f.close()
    def mediaFire(self):
        global logfile, tn, duration, sample_bin, g_driver
        print("MediaFire test start")
        serSet()
        tn.write('echo MediaFire Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver) 
        driver.get("http://www.mediafire.com/file/cy6mm4bbs1kmq4d/Doraemon%2BStand%2Bby%2BMe%2BEng%2BIndo%2B480p-1.mp4")
        time.sleep(10)
        driver.find_element_by_class_name("download_link").click()
        time.sleep(10)
        driver.get("http://www.mediafire.com/file/mfy6rdlhsf9ob9g/Doraemon%2BStand%2Bby%2BMe%2BEng%2BIndo%2B480p.mp4")
        time.sleep(10)
        driver.find_element_by_class_name("download_link").click()
        time.sleep(50)
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
        f.close()    
    def four_shared(self):
        global logFile, tn, duration, sample_bin, g_driver
        print("4Shared test start")
        serSet()
        tn.write('echo 4Shared Test\n')
        time.sleep(1)
        tn.write(sample_bin + str(duration) + '\n')
        time.sleep(1)
        driver = webdriver.Chrome(g_driver) 
        driver.get("https://www.4shared.com/video/VJUF0Uqlca/hd_1nf3rn0_n0_f4r03st3_2_dub.html")
        driver.implicitly_wait(5)
        if driver.find_element_by_xpath("//div[@class='guideTipOk jsHideTip floatRight']"):
            try:
                driver.find_element_by_xpath("//div[@class='guideTipOk jsHideTip floatRight']").click()
            except:
                print "None"
        # driver.find_element_by_xpath("//button[@class='head-elem small-button hidden-xs']").click()
        # driver.implicitly_wait(5)
        # driver.find_element_by_name('login').send_keys('broadweb_a@hotmail.com.tw')
        # driver.implicitly_wait(5)
        # driver.find_element_by_name('password').send_keys('2wsx1qaz')
        # driver.implicitly_wait(5)
        # driver.find_element_by_xpath("//button[@class='big-button b-w jsLogIn']").click()
        # driver.implicitly_wait(10)
        # driver.find_element_by_xpath("//button[@class='btn-download jsDownloadButton']").click()
        # driver.implicitly_wait(5)
        # driver.find_element_by_class_name("//button[@class='freeDownloadButton round4 alignCenter floatLeft']").click()
        time.sleep(duration + 60)
        tn.write(sample_bin + '\n')
        time.sleep(3)
        driver.delete_all_cookies()
        driver.quit()
        time.sleep(1)
        tn.write('uptime\n')
        tn.write('\n')
        time.sleep(2)
        while True:
            x = tn.read_until('\n', timeout=20)
            if x:	
                f = open('C:\\log\\' + logFile, 'a+')
                try:
                    f.write(x + '\n')
                    time.sleep(1)
                    f.flush()
                except EOFError as e:
                    logging.warning (e)       
            elif not x:
                break
        f.close() 
    def fileTransferTest(self):
        fileBox.dropbox()
        time.sleep(15)
        fileBox.google_Driver()
        time.sleep(10)
        fileBox.oneDrive()
        time.sleep(10)
        fileBox.four_shared()
        time.sleep(10)
        fileBox.box()
        time.sleep(10)
        fileBox.mediaFire()
        time.sleep(10)
        m5.engine()
        time.sleep(20)

def skype_msg():
    print("Skype test start")
    serSet()
    tn.write('echo Skype Test\n')
    time.sleep(1)
    tn.write(sample_bin + str(duration) + '\n')
    time.sleep(1)
    print("Loading...")
    driver = webdriver.Chrome()
    driver.get('https://web.skype.com/')
    print("Loaded Skype!")
    print("Signing in...")
    userNameField = driver.find_element_by_id("username")
    userNameField.clear()
    userNameField.send_keys("XXXXX" )
    driver.find_element_by_xpath("//button[@class='btn primaryCta']").click()
    time.sleep(5)
    passwordField = driver.find_element_by_name("passwd")
    passwordField.clear()
    passwordField.send_keys("XXXXX")
    passwordField.submit()
    driver.implicitly_wait(5)
    SendKeys.SendKeys("{ESC}")
    driver.implicitly_wait(5)
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.TAG_NAME,'swx-textarea')))
    element = element.find_element_by_tag_name("textarea")
    element.click()
    element.clear()

    for i in range(1, duration*2):
        if i % 1 == 0:
            element.send_keys("Hello test")
            element.send_keys(Keys.ENTER)
        time.sleep(1)
    tn.write(sample_bin + '\n') 
    time.sleep(5)         
    driver.quit()
    time.sleep(1)
    tn.write('uptime\n')
    tn.write('\n')
    time.sleep(2)
    while True:
        x = tn.read_until('\n', timeout=20)
        if x:	
            f = open('C:\\log\\' + logFile, 'a+')
            try:
                f.write(x + '\n')
                time.sleep(1)
                f.flush()
            except EOFError as e:
                logging.warning (e)       
        elif not x:
            break     
            
    f.close()           
def skype_af():
    print("Skype test start")
    serSet()
    tn.write('echo Skype Test\n')
    time.sleep(1)
    tn.write(sample_bin + str(duration) + '\n')
    time.sleep(1)
    print("Loading...")
    driver = webdriver.Chrome()
    driver.get('https://web.skype.com/')
    print("Loaded Skype!")
    print("Signing in...")
    userNameField = driver.find_element_by_id("username")
    userNameField.clear()
    userNameField.send_keys("broadweb_a" )
    driver.find_element_by_xpath("//button[@class='btn primaryCta']").click()
    time.sleep(5)
    passwordField = driver.find_element_by_name("passwd")
    passwordField.clear()
    passwordField.send_keys("2wsx1qaz")
    passwordField.submit()
    driver.implicitly_wait(5)
    SendKeys.SendKeys("{ESC}")
    driver.implicitly_wait(20)
    element = driver.find_element_by_xpath("//div[@class='swx-file-picker-btn filePicker']")

    for i in range(1, duration*2):
        if i % 1 == 0:
            element.click()
            element.send_keys("C:\Users\Python-Auto\Downloads\steaming.mp4")
            # element.send_keys(Keys.ENTER)
        time.sleep(1)
    tn.write(sample_bin + '\n') 
    time.sleep(5)         
    driver.quit()
    time.sleep(1)
    tn.write('uptime\n')
    tn.write('\n')
    time.sleep(2)
    while True:
        x = tn.read_until('\n', timeout=20)
        if x:	
            f = open('C:\\log\\' + logFile, 'a+')
            try:
                f.write(x + '\n')
                time.sleep(1)
                f.flush()
            except EOFError as e:
                logging.warning (e)       
        elif not x:
            break     
            
    f.close()           
def serSet():
    global logFile, sample_bin_path, tn, duration, ret, HOST
    if ret == False:
        tn = telnetlib.Telnet(host=HOST, port="23", timeout=socket._GLOBAL_DEFAULT_TIMEOUT )
    f = open('C:\\log\\' + logFile, 'a+')
    if ret == False:    
        tn.open()
    tn.write('\x03')
    tn.write('\x03')
    tn.write('\n')
    time.sleep(1)
    tn.write('echo ==========================================================================\n')
def quit():
    global tn
    try:
        # tn.write("exit\n")
        # time.sleep(2)
        tn.close()
        root.destroy()
    except NameError:
        root.destroy()   
def all_test():
    streaming.streamingTest()
    time.sleep(10)
    socialSoftware.socialTest()
    time.sleep(10)
    fileBox.fileTransferTest()
    time.sleep(10)          

# ======Environment Parameter Setting======
email = "XXXXX"
password = "XXXXX"
sample_bin = "./sample.bin -a get_qos_user_info -i "
set_qos_off = "./iqos-setup.sh stop\n"
set_qos_on = "./iqos-setup.sh restart\n"
logDate = time.strftime("%Y-%m-%d_%H%M%S")
logFile = 'App-Test Report_' + logDate + '_M5.txt'
sample_bin_path = '/tmp/tm-shn'
g_driver = 'C:\Users\Python-Auto\Documents\chromedriver.exe'
duration = 300
default_duration = True

HOST = "192.168.0.1"
user = "admin"
passwd = "admin1"
default_tn = True

m5 = m5()
streaming = streaming()
socialSoftware = socialSoftware()
fileBox = fileBox()
#======Wedget Setting======  
root = Tk()
root.title("App Weekly Release Auto Test!!!")
root.geometry('550x300')
Label(root,text="SHN Application Auto Test", padx=300, pady=300, fg='blue', font='12').pack()
menu = Menu(root)
root.config(menu=menu)
streamingMenu = Menu(menu)
socialMenu = Menu(menu)
transferMenu = Menu(menu)
testMenu = Menu(menu)
settingMenu = Menu(menu)

menu.add_cascade(label="Streaming Video", menu=streamingMenu)
streamingMenu.add_command(label="Amazon Instant Video", command=streaming.amazon, state=DISABLED)
streamingMenu.add_command(label="Hulu+", command=streaming.hulu, state=DISABLED)
streamingMenu.add_command(label="Netflix", command=streaming.netflix, state=DISABLED)
streamingMenu.add_command(label="YouTube", command=streaming.youtube, state=DISABLED)
streamingMenu.add_command(label="Dailymotion", command=streaming.dailymotion, state=DISABLED)
streamingMenu.add_command(label="Vevo", command=streaming.vevo, state=DISABLED)
streamingMenu.add_command(label="Vudu", command=streaming.vudu, state=DISABLED)
streamingMenu.add_command(label="Vimeo", command=streaming.vimeo, state=DISABLED)
streamingMenu.add_command(label="Pandora", command=streaming.pandora, state=DISABLED)
streamingMenu.add_command(label="Test All Streaming", command=streaming.streamingTest, state=DISABLED)

menu.add_cascade(label="Social Network", menu=socialMenu)
socialMenu.add_command(label="Facebook", command=socialSoftware.facebook, state=DISABLED)
socialMenu.add_command(label="Google+", command=socialSoftware.google_Plus, state=DISABLED)
socialMenu.add_command(label="Instagram", command=socialSoftware.instagram, state=DISABLED)
socialMenu.add_command(label="LinkedIn", command=socialSoftware.linkedIn, state=DISABLED)
socialMenu.add_command(label="Flickr", command=socialSoftware.flickr, state=DISABLED)
socialMenu.add_command(label="Twitter", command=socialSoftware.twitter, state=DISABLED)
socialMenu.add_command(label="Test All SocialNetwork", command=socialSoftware.socialTest, state=DISABLED)

menu.add_cascade(label="File Transfer", menu=transferMenu)
transferMenu.add_command(label="Dropbox", command=fileBox.dropbox, state=DISABLED)
transferMenu.add_command(label="Google-Driver", command=fileBox.google_Driver, state=DISABLED)
transferMenu.add_command(label="OneDrive", command=fileBox.oneDrive, stat=DISABLED)
transferMenu.add_command(label="Box", command=fileBox.box, stat=DISABLED)
transferMenu.add_command(label="MediaFire", command=fileBox.mediaFire, stat=DISABLED)
transferMenu.add_command(label="4Shared", command=fileBox.four_shared, stat=DISABLED)
transferMenu.add_command(label="Test All FileTransfer", command=fileBox.fileTransferTest, state=DISABLED)

menu.add_cascade(label="Test All App!!", menu = testMenu)
testMenu.add_command(label="Type test for all", command=all_test, state=DISABLED)
testMenu.add_command(label="Skype meassage", command=skype_msg, state=DISABLED)
# testMenu.add_command(label="Skype Attach File", command=skype_af, state=DISABLED)

menu.add_cascade(label="Setting", menu=settingMenu)
settingMenu.add_command(label="Connect Telnet", command=m5.telnet)
settingMenu.add_command(label="Set up Test Duration", command=m5.duration)
settingMenu.add_command(label="Set up sample.bin Path", command=m5.sample_BIN)
settingMenu.add_command(label="Enable SmartDNS", command=m5.smartDNS)

menu.add_cascade(label="Exit", command=quit)
root.protocol("WM_DELETE_WINDOW", quit)
root.mainloop() 