import zipfile,os

def zip_dir(dir_path, zip_path):
    """
    压缩文件夹
    :param dir_path: 文件夹路径
    :param zip_path: 压缩文件路径
    :return:
    """
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(dir_path):
            print(root, dirs, files)
            for file in files:
                zf.write(os.path.join(root, file))
    print(f"打包完成,文件路径为：{zip_path}")
    
if __name__ == '__main__':
    zip_dir('./Report','./Tools.zip')