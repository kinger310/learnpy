from Crypto.Cipher import AES
import base64


class AESEncrypt:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC
        self.length = AES.block_size

    def encrypt(self, text):
        crypt = AES.new(self.key, self.mode, self.iv)
        text_pad = self.padding(text)
        cipher_text = crypt.encrypt(text_pad)
        cipher_str = str(base64.b64encode(cipher_text), encoding='utf-8')
        return cipher_str

    def padding(self, text):
        count = len(text.encode('utf-8'))
        if count % self.length != 0:
            add = self.length - (count % self.length)
        else:
            add = 0
        text1 = text + ('\0' * add)
        return text1

    def decrypt(self, text):
        base_text = base64.b64decode(text)
        crypt = AES.new(self.key, self.mode, self.iv)
        plain_text = crypt.decrypt(base_text)
        ne = plain_text.decode('utf-8').rstrip('\0')
        return ne


if __name__ == '__main__':
    aes_encrypt = AESEncrypt(key='keyskeyskeyskeys', iv="keyskeyskeyskeys")  # 初始化key和IV
    txt = '{"mobilePhone": "137771XXXXX"}'
    sign_data = aes_encrypt.encrypt(txt)
    print(sign_data)
    # sign_data = "7e6PN5O7/YHmMIkH4QbJ6vqxt5daOftn2jzf6bVpV2c="
    sign_data = "7PWFMEZ4epXe3tKTYBAjjQ=="
    data = aes_encrypt.decrypt(sign_data)
    import json
    dd = json.loads(data)
    print(data)
