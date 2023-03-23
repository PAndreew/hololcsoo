import requests

headers = {
    'Authorization': 'DeepL-Auth-Key c850eb6d-2bbb-b4ba-dd52-30d6faeadcab',
}

files = {
    'target_lang': (None, 'HU'),
    'file': open('C:\\Users\\uif56391\\Documents\\Own\\Translation\\document - 2023-02-02T100841.464.docx', 'rb'),
}

response = requests.post('https://api.deepl.com/v2/document', headers=headers, files=files)
print(response)