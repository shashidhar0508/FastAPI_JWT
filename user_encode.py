# import jwt
# import datetime
#
# token_validity = datetime.datetime.now() + datetime.timedelta(minutes=2)
# str(token_validity)
# print("token_validity : ", token_validity)
#
# payload = {'name': 'shashi'}
# encoded = jwt.encode(payload, key='star1', algorithm='HS256').decode('utf-8')
# print("encoded : ", encoded)
#
# # decoded_user_name = jwt.decode(encoded, key='star1', algorithms='HS256')
# # print("decoded_user_name : ",decoded_user_name)
#
# def decode_token(encoded_token):
#     user_name = jwt.decode(encoded_token, key='EvO>|3_LND_SeC123t', algorithms=['HS512'])
#     print("user_name : ", user_name)
#     return user_name
#
#
# # h="""eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoic2hhc2hpIiwicGFzc3dvcmQiOiJzaGFzaGkxMjMiLCJleHAiOjE2MDgyODg0NjJ9.lrA_Kg5dcBx0Ri8-
# # maCYwiPbTV-j2PygcFdU3sne0fM"""
#
# # decode_token(h)