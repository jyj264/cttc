import streamlit as st
import datetime as dt

st.title("⏲️中国理论时间计算器")
h = int(dt.datetime.utcnow().strftime("%H"))
m = int(dt.datetime.utcnow().strftime("%M"))
s = int(dt.datetime.utcnow().strftime("%S"))
<<<<<<< HEAD
hs = "0" + str(h) if h < 10 else str(h)
ms = "0" + str(m) if m < 10 else str(m)
ss = "0" + str(s) if s < 10 else str(s)
hbs = "0" + str((int(h) + 8) % 24) if (int(h) + 8) % 24 < 10 else str((int(h) + 8) % 24)
st.write("当前UTC时间：", hs, ":", ms, ":", ss)
st.write("当前北京时间：", hbs, ":", ms, ":", ss)
=======
if h < 10: h = "0" + str(h)
if m < 10: m = "0" + str(m)
if s < 10: s = "0" + str(s)
st.write("当前UTC时间：", str(h), ":", str(m), ":", str(s))
st.write("当前北京时间：", str((int(h) + 8) % 24), ":", str(m), ":", str(s))
h = int(h)
m = int(m)
>>>>>>> c900a6e0e170a88b773c34f25d2517fb8f406898
st.markdown("---")
a = st.text_input("请输入您所在地区的经度：")
b = 0

if a != "":
    try:
        a = int(a)
        if a < -180 or a > 180: raise ValueError
        jl = a - b
        flag = True if a >= b else False
        jlsj = jl * 4
        jlh = int(jlsj / 60)
        jlm = int(abs(jlsj) % 60)
        ansh = h + jlh if flag else h - jlh
<<<<<<< HEAD
        ansm = m + jlm if flag else m - jlm
        while ansm < 0:
            ansh -= 1
            ansm += 60
        while ansm >= 60:
            ansh += 1
            ansm -= 60
        ansh = "0" + str(ansh % 24) if ansh % 24 < 10 else str(ansh % 24)
=======
        ansm = (m + jlm) % 60
        ansh = "0" + str(ansh % 24) if ansh < 10 else str(ansh % 24)
>>>>>>> c900a6e0e170a88b773c34f25d2517fb8f406898
        ansm = "0" + str(ansm) if ansm < 10 else str(ansm)
        res = "当地理论时间  " + str(ansh) + ":" + str(ansm) + ":" + ss
        st.info(res)
    except ValueError:
        st.error("请输入-180~180之间的整数！")
    except TypeError:
        st.error("请输入正确的数字！")
