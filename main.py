import streamlit as st
from utils import generate_script

# Title for the application
st.title("🎬 视频脚本生成器")

# API Key Input
api_key = st.sidebar.text_input("请输入OpenAI API密钥：", type="password")
api_url = st.sidebar.text_input("请输入中转url：", type="password")
st.sidebar.markdown("[获取OpenAI API密钥](https://platform.openai.com/signup)")

# Subject Input
subject = st.text_input("💡 请输入视频的主题", "Sora模型")

# Video Length Input (in minutes)
video_length = st.number_input("⏰ 请输入视频的大致时长（单位：分钟）", min_value=0.0, step=0.5, value=1.0)

# Creativity Slider
creativity = st.slider(
    "✨ 请输入视频脚本的创造力（数字小说更严谨，数字大说明更多样）",
    min_value=0.0, max_value=1.0, value=0.2
)

# Submit button to generate script
if st.button("生成脚本"):
    with st.spinner("AI正在思考中, 请稍等..."):
        # Dummy function to simulate script generation
        # Replace with your actual API call
        search_result, title, script = generate_script(subject, video_length, creativity, api_key, api_url)

        st.success("视频脚本已生成!")
        st.subheader("🔥 视频标题:")
        st.write(title)
        st.subheader("📝 视频脚本:")
        st.write(script)

        with st.expander("👀 维基百科搜索结果"):
            st.write(search_result)
