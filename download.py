import time
from datetime import datetime
import requests
from config import *

class getTengXunDoc:

    def __init__(self, document_url, document_pad_id, cookie_str):
        # 腾讯在线文档的地址
        self.document_url = document_url
        # 每个腾讯在线文档有一个唯一的值,需要手动获取
        self.document_pad_id = document_pad_id
        self.headers = {
            # "content-type": "application/x-www-form-urlencoded",
            "Cookie": cookie_str,
        }

    # 获取操作ID
    def getOperationId(self, export_excel_url):
        body = {"docId": self.document_pad_id, "version": "2"}

        res = requests.post(
            url=export_excel_url, headers=self.headers, data=body, verify=False
        )
        operation_id = res.json()["operationId"]
        return operation_id

    def ExcelDownload(self, check_progress_url, file_name):
        # 拿到下载excel文件的url
        start_time = time.time()
        file_url = ""
        while True:
            print(1)
            res = requests.get(
                url=check_progress_url, headers=self.headers, verify=False
            )
            progress = res.json()["progress"]
            if progress == 100:
                file_url = res.json()["file_url"]
                break
            elif time.time() - start_time > 3:
                print("准备超时,请排查")
                break
        if file_url:
            # self.headers["content-type"] = "application/octet-stream"
            dl = requests.get(url=file_url, headers=self.headers, verify=False)
            if False:
                with open(file_name, "wb") as f:
                    f.write(dl.content)
                print("下载成功,文件名: " + file_name)
            elif dl.status_code == 200:
                print("请求成功")
            else:
                print("下载失败")
                return None
            return dl.content
        else:
            print("下载文件地址获取失败, 下载excel文件不成功")
            return None


def main():
    # 数据准备步骤一获取文件url
    document_url = 'https://docs.qq.com/sheet/DTkFpU2VJV01IYUVG'
    # 数据准备步骤二获取文件id
    document_pad_id = '300000000$NAiSeIWMHaEF'
    # 数据准备步骤三获取cookie
    cookie_str = 'RK=VCFhy547ck; ptcz=01eb007d2762963ae07e6f53a3c5c3bfd3626a6d602e05a3bc5772e719112db7; traceid=d24a9e0645; TOK=d24a9e0645b35694; hashkey=d24a9e06; pgv_pvid=1744167417144504; pgv_info=ssid=s1974441161714504; fingerprint=8d8a2a70e82e4d6b907c007407322a7096; low_login_enable=0; uid=144115353973530477; uid_key=EOP1mMQHGixnSi9MNU1HWlc2aTd5MDlDNHUvN0JQdFl3L2NCT1U4UlJkcVMybjgxeFV3PSKBAmV5SmhiR2NpT2lKQlEwTkJURWNpTENKMGVYQWlPaUpLVjFRaWZRLmV5SlVhVzU1U1VRaU9pSXhORFF4TVRVek5UTTVOek0xTXpBME56Y2lMQ0pXWlhJaU9pSXhJaXdpUkc5dFlXbHVJam9pYzJGaGMxOTBiMk1pTENKU1ppSTZJa3AwV2tSWmRpSXNJbVY0Y0NJNk1UYzBOamMxTkRrNE1pd2lhV0YwSWpveE56UTBNVFl5T1RneUxDSnBjM01pT2lKVVpXNWpaVzUwSUVSdlkzTWlmUS5hd1dOWVdPS2g0Rk1vb2x0bno5RGlveGRCMkxVVlIyTGRhUzVkc1Vwc09vKKa79cAG; utype=wx; wx_appid=wx02b8ff0031cec148; openid=oy6SixItgOJIRad2z3AsyhrtmHeg; access_token=91_vfWHkcSupZOgJ2NSQgqpMhazRthK8wjw_Jc3HwDjv5q99LApmHDodLoyvB5eJVpb9MU6vOpz0hAFYQ4_Gvo6me2Cspr3OKaJm7h2FyhxG0U; refresh_token=91_E6_mq2RqnQMjyx-htgeULhIIZKGsFk8uMGPGtx385zJIPGae3ajLQvi25bWkHqnCGmy4FW2_Berq0ZDc0xEcnU9_cf9oMJVcXohFAM2H3Ws; env_id=gray-no4; gray_user=true; DOC_SID=4d2f309d6547408a81370777d2fc3205d42186dd7d5e4e4c92a9306895e4f464; DOC_SID_S=420b3c76db5c4935b34d8942c9042adc; SID=4d2f309d6547408a81370777d2fc3205d42186dd7d5e4e4c92a9306895e4f464; SID_S=420b3c76db5c4935b34d8942c9042adc; backup_cdn_domain=docs.gtimg.com; loginTime=1744163022805; optimal_cdn_domain=docs2.gtimg.com; adtag=toolbox; adtag=toolbox'

    # 创建类的实例化对象
    tx = getTengXunDoc(document_url, document_pad_id, cookie_str)
    # 获取导出任务的操作id，
    operation_id = tx.getOperationId(export_excel_url)
    check_progress_url = f'{check_progress_url_front}?operationId={operation_id}'

    current_datetime = datetime.strftime(datetime.now(), '%Y_%m_%d_%H_%M_%S')
    file_name = f'{current_datetime}腾讯在线文档.xlsx'
    # 下载文件
    excel_data = tx.ExcelDownload(check_progress_url, file_name)
    return excel_data


if __name__ == '__main__':
    main()

