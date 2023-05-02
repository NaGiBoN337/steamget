import uuid
import hashlib
from bs4 import BeautifulSoup
import httpx
class QiwiForm():
    def __init__(self,summ):
        self.data = {
            'orderId': str(uuid.uuid4()),
            'amount': summ,
            'comment': 'Оплата',
            'formId': '700433',   #// Укажите номер формы, который начинается с 7.
            'cardGuid': '',       #// Передается, если при создании формы вы не указали "Номер карты получателя".
            'backUrl': 'https://steamget.ru/results',
            'language': 'RU',

        }
        self.bearerToken = 'be9ade5a89ca499e98f520f18689656f'
        self.signKey = '2558010caabe40a8a74bede9199d4ebe'
        self.formSecretKey = 'Qwerty123'
        self.formId = '700433'

    def createSignHash(self):
        # orderId::amount::formId::cardGuid::comment::backUrl::language
        signStringToBeHashed = "::".join([self.data['orderId'], self.data['amount'], self.data['formId'],self.data['cardGuid'], self.data['comment'], self.data['backUrl'], self.data['language'],self.signKey])
        self.data["signHashedString"] = hashlib.sha256(signStringToBeHashed.encode()).hexdigest()

    def qiwi_request(self):
        headers = {
            'Authorization': 'Bearer ' + self.bearerToken,
            'Sign': self.data["signHashedString"]
        }
       # headers = {f"Authorization": f"Bearer {self.bearerToken}", 'Sign': self.data["signHashedString"]}

        stringToBeHashed = '::'.join([str(self.data['orderId']), self.data['amount'], self.data['formId'], self.data['cardGuid'], self.data['comment'], self.data['backUrl'], self.data['language'], self.formSecretKey])
        hashedString = hashlib.sha1(stringToBeHashed.encode()).hexdigest()
        self.data['hash'] = hashedString

        url = 'https://api.intellectmoney.ru/p2p/GetFormUrl'
        response = httpx.post(url, headers=headers,  data=self.data)
        #print(response.text)
        #print(response.status_code)
        #print(response.text)
        page = BeautifulSoup(response.text, 'xml')
        OperId = page.OperationId.text

        return page.Url.text, OperId
