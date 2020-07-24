import Chatbot

if __name__ == '__main__':
    tokenTelegram='1255840202:AAESK__tlVGY63FVPJOJufa70DLej8UfXrI'
    ibm_apiKey='VZHzvjelK9YsjuYtBGOkXhFLhoDGruweoDcYIfKhE7hT'
    ibm_url='https://api.us-east.assistant.watson.cloud.ibm.com/instances/1b62e879-1f7e-4e0b-9d72-5ab9c1d9328b'
    ibm_assitantId='a8817251-2b48-47d0-a208-09f7fde9b369'

    chatbot=Chatbot.Chatbot(tokenTelegram, ibm_apiKey, ibm_url, ibm_assitantId)