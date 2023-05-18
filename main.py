import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'{self.token}'
        }

    def get_upload_link(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {
            'path' : file_path,
            "overwrite": "true"
        }
        responce = requests.get(url=url, headers=headers, params=params)
        return responce.json()['href']

    def upload(self, file_path):
        href = self.get_upload_link(file_path=file_path)
        responce = requests.put(href, data=open(file_path, 'rb'))
        if responce.status_code == 201:
            print('Загрузка прошла успешно!')
        else:
            print(responce)

if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу(название файла из корневого католога)')
    token = input('Введите токен')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)



