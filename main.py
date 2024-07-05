import streamlit as st
import datetime as dt
st.title("⏲️中国理论时间计算器")
h=int(dt.datetime.utcnow().strftime("%H"))
m=int(dt.datetime.utcnow().strftime("%M"))
s=int(dt.datetime.utcnow().strftime("%S"))
if h < 10:
    h = "0" + str(h)
if m < 10:
    m = "0" + str(m)
if s < 10:
    s = "0" + str(s)
st.write("当前UTC时间：",str(h),":",str(m),":",str(s))
st.write("当前北京时间：",str(int(h)+8),":",str(m),":",str(s))
h=int(h)
m=int(m)
st.markdown("---")
a=st.text_input("请输入您所在地区的经度：")

b=0

if a!="":
    try:
        a=int(a)
    except ValueError:
        st.error("请输入-180~180之间的整数！")
    try:
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
        res="当地理论时间  "+str(ansh)+":"+str(ansm)+":"+str(s)
        st.info(res)
    except TypeError:
        st.error("请输入正确的数字！")





