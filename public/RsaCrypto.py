from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

class RsaCrypto(object):
    """负责 RSA 加密

    Args:
        object (_type_): _description_
    """
    def __init__(self) -> None:
        self.privateKey = """-----BEGIN RSA PRIVATE KEY-----
MIICeQIBADANBgkqhkiG9w0BAQEFAASCAmMwggJfAgEAAoGBALFkKSL8ABW2stte
y0vcmZIpPb1ZENILV6c13/1lOrg009fVxiNbwJs+1H8qdkKmNaEZ0QP2vNr0WRvH
ot9gsSg/7T7mqBQbKgOu8+sbv0auZcon+Vse1VqAqlRI0cMqbOFieyuPER+/D7tg
ksVIBlTMoDWroxiPjXGU6acl1mCjAgMBAAECgYEAoOpVDrE+enQDB1CUZjq07IuQ
wATdZ0x2tO4ARGLhw1vYl8AKPuTqcWmrZbflE0ym9X7vxgK7CnwBoVuVecDCslek
29Rai8p2lnsRghrMqr6DkYKVeLHEIF5g+q4fWagMD7/TaiyK4hX2GISMwSVgvSSQ
AxnAHQGahgPeXlSDDsECQQDZt5FkqphMF/cnTKaIyES/qF38DPTNoLd6R/MOY7tN
QySmzXWH5rbxl1e/nujtfDKsAEglQFM+Df292PHfYkfTAkEA0JVYYPgVRnyax8fM
zUIQxmp4Dk00bfeTPry8Or1eNGF8QxfQd8Z4REI3Q5tyytpR64Q007gHcdST8eqs
6K1R8QJBAKb8bt3BItKqRvyzg7/Bq0k8/+kEnvbgYBm/+aJ9x/k4mHH/gDfeM08V
f04PuiP8cHkQNkWsEqyz2ny0Wr+1B9UCQQCZy/Tdky8EyS3LbxwooLUDyE97pBur
leghU0KrQSQsFVFtmyqgllvpYLWlCQKsZiwPL21QSxpaKXdo4jPaYKnRAkEAlnT/
CusBA7Bexax/fCgFVIjG9w1EblS2IB2k7omUOpD2qib/qUIYgDYCLiwRwgnhxxTx
nGOAFWbN0EhoH8RvIg==
-----END RSA PRIVATE KEY-----"""

    def decryptData(self, input_data):
        try:
            # 分组解密默认长度 128
            default_length = 128

            # 创建私钥对象
            pri_key = RSA.importKey(self.privateKey.encode('utf-8'))
            cipher = PKCS1_v1_5.new(pri_key)

            # 现将base64编码格式的数据解码，然后解密，并用decode转成str
            input_data_b64 = base64.b64decode(input_data.encode('utf-8'))

            # 获取密文长度
            length = len(input_data_b64)

            if length < default_length:
                # 直接解密
                output_data = cipher.decrypt(input_data_b64, sentinel='error').decode('utf-8')
            else:
                # 分组解密
                offset = 0
                res = []
                while length - offset > 0:
                    if length - offset > default_length:
                        res.append(cipher.decrypt(input_data_b64[offset: offset + default_length], sentinel='error'))
                    else:
                        res.append(cipher.decrypt(input_data_b64[offset:], 'error'))
                    offset += default_length
                output_data = b''.join(res)
                output_data = output_data.decode('utf-8')

            return output_data

        except Exception as e:
            return e