import streamlit as st
import time

st.title('Streamlit 学習用')

st.write('ブログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!'

#for文が実行されている間表示されない。
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ１')
expander.write('問い合わせ１の回答')
expander = st.expander('問い合わせ２')
expander.write('問い合わせ２の回答')
expander = st.expander('問い合わせ３')
expander.write('問い合わせ３の回答')



