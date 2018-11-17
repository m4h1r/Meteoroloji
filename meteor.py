#Gerekli kütüphaneleri yükle.
from selenium import webdriver
import csv
import datetime
from datetime import date, timedelta
chrome_path = r"C:\Python36\chromedriver.exe" #Chrome sürücüsünün konumunu bilgisayarına göre ayarla.
driver = webdriver.Chrome(chrome_path)
bilgiler=[]
gun=datetime.datetime(2008, 7, 31) #Verileri çekmek istediğimiz tarihin 1 gün öncesini giriyoruz.
for x in range(1,11): #Kaç günlük veri çekmek isteniyorsa o kapsam belirler.
	gun=gun+timedelta(1)
	ara= gun.strftime("%Y")+"-"+gun.strftime("%m")+"-"+gun.strftime("%d")
	url = "https://tr.freemeteo.com/havadurumu/kocaeli/history/daily-history/?gid=745028&date="+ara+"&station=5408&language=turkish&country=turkey"
	driver.get(url)
	bilgiler.append((driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[2]/div[1]/a[2]""")).text)
	A1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[1]""")).text
	B1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[2]""")).text
	C1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[3]""")).text
	D1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[4]""")).text
	E1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[5]""")).text
	F1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[6]""")).text
	G1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[7]""")).text
	H1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[8]""")).text
	I1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[9]""")).text
	J1 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/thead/tr/th[10]""")).text
	satir=[A1, B1, C1, D1, E1, F1, G1, H1, I1, J1]
	bilgiler.append(satir)
	for y in range(1,31):
		try: #Boş satırlar yüzünden hataya düşmemek için.
			A2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[1]""")).text
			if A2!="":
				B2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[2]""")).text
				C2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[3]""")).text
				D2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[4]""")).text
				E2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[5]""")).text
				F2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[6]""")).text
				G2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[7]""")).text
				H2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[8]""")).text
				I2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[9]""")).text
				J2 = (driver.find_element_by_xpath("""//*[@id="content"]/div[3]/div[1]/div[3]/div/table/tbody/tr["""+str(y)+"""]/td[10]""")).text
				satir=[A2, B2, C2, D2, E2, F2, G2, H2, I2, J2]
				bilgiler.append(satir)
				pass #if sorgusunu kapat.
			pass #try bloğunu kapat.
		except : pass
		pass
with open('KocaeliBilgiler.csv', 'a', newline='', encoding='utf-8') as f:
	w = csv.writer(f, delimiter='\n')
	w.writerow(bilgiler) #Bilgileri CVS formatında yazdır.
pass
driver.close() #Otomatik Chrome'u kapat.