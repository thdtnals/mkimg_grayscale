def createFolder(directory: str) -> bool:
    '''
    createFolder는 directory이름을 입력받아서 폴더를 만드는 함수입니다.
    input: directory(str)
    output: True or False
    '''
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            return True
    except OSError:
        print('Error: Creating directory. ' + directory) 
        return False