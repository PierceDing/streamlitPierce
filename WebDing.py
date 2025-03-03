import streamlit as st
import pandas as pd
import yagmail

def save_data(selections):
    df = pd.DataFrame(list(selections.items()), columns=["商品名稱", "配送方式"])
    df.to_csv("order_data.csv", index=False, encoding="utf-8-sig")

def send_email():
    receiver = "ggy2354@gmail.com"
    subject = "丁丁快遞服務中心 - 訂單紀錄"
    body = "您好，這是您的訂單紀錄，請查收附件。\n\n感謝您的使用！"
    filename = "order_data.csv"
    
    try:
        yag = yagmail.SMTP("your_email@gmail.com", "your_app_password")
        yag.send(to=receiver, subject=subject, contents=body, attachments=filename)
        st.success("訂單已成功寄送至 ggy2354@gmail.com！")
    except Exception as e:
        st.error(f"郵件發送失敗: {e}")

def main():
    # 設定網頁標題與主題顏色
    st.markdown(
        """
        <style>
            .title {
                font-size: 36px;
                font-weight: bold;
                color: #FF5733;
                text-align: center;
            }
            .subtitle {
                font-size: 18px;
                color: red;
                text-align: center;
            }
            .radio-box {
                background-color: #F5F5F5;
                padding: 5px;
                border-radius: 10px;
                border: 1px solid #333;
                margin-bottom: 5px;
                color: blue;
            }
            .submit-button {
                background-color: #FF5733 !important;
                color: white !important;
                font-size: 20px !important;
                border-radius: 10px !important;
                width: 100%;
            }
            .table-container {
                border: 2px solid #333;
                padding: 10px;
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # 標題
    st.markdown("<div class='title'>丁丁快遞服務中心XD</div>", unsafe_allow_html=True)
    
    # 內文
    st.markdown("<div class='subtitle'>請選擇商品配送地點，勾選完畢後送出</div>", unsafe_allow_html=True)
    
    # 商品配送選項
    products = {
        "精淬玫瑰四物飲2盒": ["萬運", "青田街"],
        "天地合補含鐵四物飲盒裝6瓶4盒": ["萬運", "青田街"],
        "加倍佳酸甜軟糖袋裝10包彩虹造型1袋": ["萬運", "青田街"],
        "得意的一天玄米油1瓶": ["萬運", "青田街"],
        "得意的一天極選酪梨油1瓶": ["萬運", "青田街"]
    }
    
    selections = {}
    
    st.markdown("### 配送商品清單")
    st.markdown("<div class='table-container'>", unsafe_allow_html=True)
    for product, options in products.items():
        st.markdown(f"<div class='radio-box'><strong>{product}</strong></div>", unsafe_allow_html=True)
        selections[product] = st.radio("選擇配送方式", options, key=product, horizontal=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 文字說明
    st.markdown("<div class='subtitle'>起手無回大丈夫，確認無誤請按送出~</div>", unsafe_allow_html=True)
    
    # 送出按鈕
    if st.button("送出小牛服務鈴", key="submit", help="確認後點擊送出"):
        st.success("丁丁飛踢！！！")
        save_data(selections)
        send_email()
        for product, choice in selections.items():
            st.write(f"{product}: {choice}")
    
if __name__ == "__main__":
    main()
