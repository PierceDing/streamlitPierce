import streamlit as st

def main():
    st.title("簡單的 Streamlit 網頁")
    st.write("這是一個基本的 Streamlit 網頁，包含 Checkbox 和送出按鈕。")
    
    # Checkbox
    agree = st.checkbox("我同意條款")
    
    # 送出按鈕
    if st.button("送出"):
        if agree:
            st.success("感謝您的同意！後端已收到您的回應。")
        else:
            st.warning("請勾選同意條款後再送出。")

if __name__ == "__main__":
    main()



