'''我的主页'''
import streamlit as st
import pandas as pd
from PIL import Image

d = {
    'pass':['pass','pass','pass'],
    'pass':['pass','pass','pass']
}

d = pd.DataFrame(d)

page = st.sidebar.radio('首页',['我的兴趣推荐','图片处理','我的智慧词典','我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    with open('永不放弃.mp3','rb')as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('20240608.jpg')
    st.write('pass')
    st.write('-----------------------')
    st.write('pass')
    st.write('-----------------------')
    st.write('pass')
    st.write('-----------------------')
    st.write(d)

def page_2():
    '''图片处理'''
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片',type = ['png','jpeg','jpg','gif'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img))

def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')
    with open('words_space.txt','r',encoding='utf-8')as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8')as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8')as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数:',times_dict[n])
        
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8')as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌎'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🌖'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是...',['阿短','编程猫'])
    new_message = st.text_input('想要说的话...')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt','w',encoding='utf-8')as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' +i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
            

def img_change(img):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][0]
            g = img_array[x,y][1]
            b = img_array[x,y][2]
            img_array[x,y] = (b,g,r)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '图片处理':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()