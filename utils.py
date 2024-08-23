# from langchain.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_community.utilities import WikipediaAPIWrapper
# from dotenv import load_dotenv
# from openai import OpenAI
# import os
#
#
# load_dotenv()
# api_key = os.getenv("PROXY_API_KEY")
# api_url = os.getenv("PROXY_SERVER_URL")
# def generate_script(video_subject, title, video_length, creativity, api_key):
#     title_template = ChatPromptTemplate.from_messages(
#         [
#             ("human", f"please give this video a title, which is about '{video_subject}'")
#         ]
#     )
#     script_template = ChatPromptTemplate.from_messages(
#         [
#             ("human",
#              """You are a vlogger, now you got following messages.
#              Please write a script for this video.
#              The title of the video is '{title}', it is
#              about '{duration}' minutes long. The script you generate should follow
#              the instructions strictly. The beginning should be the most craziest part of all
#              and the story should be filled with madness and enthusiasm. And the ending
#              must be a unearthly question.
#              The whole script should be separated by beginning, middle part and ending clearly.
#              You can refer to the content of '''{Wikipedia_search}''', but only a small part.
#              """)
#         ]
#
#     )
#
#     # model = ChatOpenAI(openai_api_key=api_key, temperature=creativity)
#     client = OpenAI(api_key=api_key, base_url=api_url)
#     model = ChatOpenAI(openai_api_key=api_key, openai_api_base=api_url, client=client, temperature=creativity)
#
#     title_chain = title_template | model
#     script_chain = script_template | model
#
#     title = title_chain.invoke({"subject": video_subject}).content
#
#     search = WikipediaAPIWrapper(lang="zh")
#     search_result = search.run(video_subject)
#
#     script = script_chain.invoke({"video_title": title, "duration": video_length,
#                                   "Wikipedia_search": search_result}).content
#
#     return search_result, title, script
#
#
# api_key = os.getenv("PROXY_API_KEY")
# print(f"API Key: {api_key}")
#
# # Run the function with the API key
# print(generate_script("sora的妙用", "sora", 1, 1, api_key))
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("PROXY_API_KEY")
api_url = os.getenv("PROXY_SERVER_URL")

def generate_script(video_subject, video_length, creativity, api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", f"please give this video a title, which is about '{video_subject}'")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """You are a vlogger, now you got following messages.
             Please write a script for this video.
             The title of the video is '{title}', it is
             about '{duration}' minutes long. The script you generate should follow
             the instructions strictly. The beginning should be the most craziest part of all
             and the story should be filled with madness and enthusiasm. And the ending
             must be a unearthly question.
             The whole script should be separated by beginning, middle part and ending clearly.
             You can refer to the content of '''{Wikipedia_search}''', but only a small part.
             """)
        ]
    )

    client = OpenAI(api_key=api_key, base_url=api_url)
    model = ChatOpenAI(openai_api_key=api_key, openai_api_base=api_url, temperature=creativity)

    title_chain = title_template | model
    script_chain = script_template | model

    title_response = title_chain.invoke({"subject": video_subject})
    title = title_response.content if hasattr(title_response, 'content') else str(title_response)

    search = WikipediaAPIWrapper(lang="zh")
    search_result = search.run(video_subject)

    script_response = script_chain.invoke({"title": title, "duration": video_length, "Wikipedia_search": search_result})
    script = script_response.content
    # if hasattr(script_response, 'content') else str(script_response)
    return search_result, title, script

# print(generate_script("sora的妙用", 1, 1, api_key))


#     try:
#         title_response = title_chain.invoke({"subject": video_subject})
#         title = title_response.content if hasattr(title_response, 'content') else str(title_response)
#
#         search = WikipediaAPIWrapper(lang="zh")
#         search_result = search.run(video_subject)
#
#         script_response = script_chain.invoke({"title": title, "duration": video_length, "Wikipedia_search": search_result})
#         script = script_response.content if hasattr(script_response, 'content') else str(script_response)
#
#         return search_result, title, script
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#         return None, None, None
#
# # 测试代码
# if __name__ == "__main__":
#     print(f"API Key: {api_key}")
#     print(f"API URL: {api_url}")
#     result = generate_script("sora的妙用", "sora", 1, 1, api_key)
#     if result[0] is not None:
#         print(result)
#     else:
#         print("Script generation failed.")
