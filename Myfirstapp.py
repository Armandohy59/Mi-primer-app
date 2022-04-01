import streamlit as st
st.title("Mi primer App")



with st.sidebar:
  num1 = st.slider('Elige el numero 1', 0.0, 100.0, 25.0)
  num2 = st.slider('Elige el numero 2', 0.0, 100.0, 25.0)
Click=st.button("Dale click")
st.write("El valor de Click es: ", Click)

if Click==True:
  st.image("perro.jpg")

#st.button("Dale click x2")
import pandas as pd

#Las siguientes lineas de código eran para visualizar
#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')

#st.write(df)
                 
#st.map(df)
#INTEGRAL
#st.text("Hola Mundo")

#st.text("La siguiente es una integral")
#st.latex("\int_1^6 sin[x]dx")
#st.markdown("Esta es una viñeta")

num1 = st.slider('Elige el numero 1', 0.0, 100.0, 25.0)
num2 = st.slider('Elige el numero 2', 0.0, 100.0, 25.0)
suma = num1+num2
st.write("La suma de", num1," y ", num1, "es :",suma)

st.write("Ahora multipliquemos")
nn1 = st.number_input("Dame n1")
nn2 = st.number_input("Dame n2")

mult=nn1*nn2
st.write("la multiplicación de",nn1," y ",nn2,"es :",mult)
