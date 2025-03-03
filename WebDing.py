import streamlit as st

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
    st.markdown("<div class='title'>丁丁快遞服務中心</div>", unsafe_allow_html=True)
    
    # 內文
    st.markdown("<div class='subtitle'>請選擇商品配送方式，勾選完畢後記得送出</div>", unsafe_allow_html=True)
    
    # 商品配送選項
    products = {
        "精淬玫瑰四物飲": ["萬運", "青田街"],
        "天地合補含鐵四物飲盒裝6瓶": ["萬運", "青田街"],
        "加倍佳酸甜軟糖袋裝10包彩虹造型": ["萬運", "青田街"],
        "得意的一天玄米油": ["萬運", "青田街"],
        "得意的一天極選酪梨油": ["萬運", "青田街"]
    }
    
    selections = {}
    
    st.markdown("### 配送商品清單")
    st.markdown("<div class='table-container'>", unsafe_allow_html=True)
    for product, options in products.items():
        st.markdown(f"<div class='radio-box'><strong>{product}</strong></div>", unsafe_allow_html=True)
        selections[product] = st.radio("選擇配送方式", options, key=product, horizontal=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 文字說明
    st.markdown("<div class='subtitle'>起手無回大丈夫，確認無誤請送出</div>", unsafe_allow_html=True)
    
    # 送出按鈕
    if st.button("送出服務鈴", key="submit", help="確認後點擊送出"):
        st.success("丁丁飛踢！")
        for product, choice in selections.items():
            st.write(f"{product}: {choice}")
    
if __name__ == "__main__":
    main()
