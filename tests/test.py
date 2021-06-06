import pandas

#file=pandas.read_csv('E:\\DATN_2020\\Chatbot_v1\\tests\\dao-tao-thac-si-khmt-sau-dai-hoc.txt')

#print(file)
#print(file[['link-name', 'name-gv', 'chuc-vu','mail-gv', 'huong-nghien-cuu-link-href', 'content']])
#print(file[['link-name', 'name-gv', 'chuc-vu']])

file =open('E:\\DATN_2020\\Chatbot_v1\\tests\\dao-tao-thac-si-khmt-sau-dai-hoc.txt', 'r')
data= file.read()

print(data)