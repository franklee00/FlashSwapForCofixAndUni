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
                    csvwriter = csv.writer(datacsv,dialect = ("excel"))
                    csvwriter.writerow(["unlucky", time.strftime("%Y-%m-%d %H:%M:%S", timeArray)])
            else:
                print("success")
                sendTransationWithMoreGas(tx_dic, "2")
                with open("runninglog.csv","w",newline="") as datacsv:
                    csvwriter = csv.writer(datacsv,dialect = ("excel"))
                    csvwriter.writerow(["success", time.strftime("%Y-%m-%d %H:%M:%S", timeArray)])
            time.sleep(20)
