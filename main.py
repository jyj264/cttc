import streamlit as st
st.title("⏲️中国理论时间计算器")
a=st.text_input("请输入您所在地区的经度：")
k= st.time_input('请输入当前的北京时间：', value=None)
k=str(k)
if a!="":
    try:
        a=int(a)
    except ValueError:
        st.error("请输入-180~180之间的整数！")

if k!="None":
    c=k.split(":")
    h=int(c[0])
    m=int(c[1])

b=116

if st.button("转换"):
    if a>=b:
        jl=a-b
        flag=True
    else:
        jl=b-a
        flag=False
    jlsj=jl*4
    jlh=int(jlsj/60)
    jlm=int(jlsj%60)
    if flag:
        ansh=h+jlh
    else:
        ansh = h-jlh
    if flag:
        ansm=m+jlm
    else:
        ansm=m-jlm
    if ansm>=60:
        ansm-=60
        ansh+=1
    if ansm<0:
        ansm+=60
        ansh-=1
    if ansh>=24:
        ansh-=24
    if ansh<0:
        ansh+=24
    if ansh<10:
        ansh="0"+str(ansh)
    if ansm < 10:
        ansm = "0" + str(ansm)
    res="当地理论时间  "+str(ansh)+":"+str(ansm)
    st.info(res)





