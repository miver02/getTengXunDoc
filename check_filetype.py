import chardet

def detect_encoding(file_path):
    # 读取文件的一部分来检测编码
    with open(file_path, 'rb') as f:
        # 读取前4096字节用于检测
        raw_data = f.read(4096)
    
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    confidence = result['confidence']
    
    print(f"检测到的编码: {encoding}, 置信度: {confidence}")
    return encoding

# 使用示例
file_path = '2025_04_10_14_37_46腾讯在线文档.csv'
encoding = detect_encoding(file_path)
print(encoding)