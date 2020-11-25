from swapContract import initiateFlashLoan
from config import *
import time
import csv

if __name__ == '__main__':
    while 1:
        for num in SETTING["ETH_SPAN"]:
            now = int(time.time())
            timeArray = time.localtime(now)

            tx_dic = initiateFlashLoan(w3.toWei(num, "ether"))
            try:
                tx_dic_gas = w3.eth.estimateGas(tx_dic)
            except ValueError:
                print("unlucky", time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
                with open("runninglog.csv","w",newline="") as datacsv:
                    #dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔
                    csvwriter = csv.writer(datacsv,dialect = ("excel"))
                    #csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
                    csvwriter.writerow(["unlucky", time.strftime("%Y-%m-%d %H:%M:%S", timeArray)])
            else:
                print("success")
                sendTransationWithMoreGas(tx_dic, "2")
            time.sleep(20)
