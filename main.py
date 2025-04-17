from io import BytesIO
import tempfile
import pandas as pd
import numpy as np
import os
import chardet
from download import main as download_main
from conn_mysql import main as conn_mysql_main


def main():
    # 获取二进制数据
    binary_data = download_main()

    # print(binary_data)
    binary_data = binary_data.decode('latin-1')
    print(binary_data)
    df = pd.read_excel(binary_data)
    print(df)
        
  

if __name__ == '__main__':
    main()

