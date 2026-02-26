from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 


# 共通で使用するLLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# タイトルと見出し
st.title("LLM回答Webアプリ")
st.write("##### LLMに振る舞わせる専門家の種類を選択できます")
st.write("専門家を選択し、質問を入力して実行ボタンを押すことで回答が得られます")

# LLMに振る舞わせたい専門家をラジオボタンで選択させる
selected_item = st.radio(
    "LLMに振る舞わせる専門家を選択してください。",
    ["AIエンジニア", "キャリアコンサルタント"]
)

# ユーザ入力
user_input = st.text_input("質問してください")

st.divider()

# ラジオボタンの選択値とユーザ入力を受け取り、LLMからの回答を返す関数
def chain_run(selected_item, user_input):
    # ラジオボタンの選択値によってシステムメッセージ切り替え
    if selected_item == "AIエンジニア":
        system_message = "あなたは優秀なAIエンジニアです。専門的かつ分かりやすく回答してください。"
    else:
        system_message = "あなたは優秀なキャリアコンサルタントです。相談者に寄り添って回答してください。"

    # LLMに渡すプロンプトを定義
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", "{input}")
    ])
    # promptとllmをもとにchain作成
    chain = prompt | llm

    # ユーザ入力値を入れてchain実行
    res = chain.invoke({"input": user_input})
    # レスポンスの内容を返す
    return res.content

# ユーザが実行ボタンを押したらchain_run関数実行
if st.button("実行"):
    st.divider()
    reesult = chain_run(selected_item, user_input)
    st.write(reesult)