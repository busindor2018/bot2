import telebot, cfg
import buttons as btn
import openai

openai.api_key = 'sk-proj-V3XzWTs0fzUJshN4S71rT3BlbkFJ1fZ42pWTxjaF3aLLpf5A'
bot = telebot.TeleBot(cfg.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Здарова", reply_markup=btn.func_btn)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Личный многофункциональный бот Ильи Александровича версия 0.1.4", reply_markup=btn.func_btn)

@bot.message_handler(func=lambda message: True)
def func(message):
    print('message polucheno')
    ask(message)

    '''
    if message.text == 'ChatGPT':
        bot.send_message(message.chat.id, "Введите ваш запрос:", reply_markup=btn.back_btn)
        bot.register_next_step_handler(message, ask)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, f'Выберите категорию: ', reply_markup=btn.func_btn)
    elif message.text != None:
        while message.text != None:
            ask(message)
            #bot.register_next_step_handler(message, ask)
            bot.send_message(message.chat.id, 'Запрос успешно обработан', reply_markup=btn.back_btn)
    else:
        bot.send_message(message.chat.id, f'Простите, я вас не понимаю.')'''


def ask(message):
    #while message.text != 'Назад':
    '''
    if message.text == 'Назад':
        bot.send_message(message.chat.id, f'Выберите категорию:', reply_markup=btn.func_btn)
        return 0
    elif message.text != None:'''
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            max_tokens=150
        )
        bot.send_message(message.chat.id, response.choices[0].text.strip(), reply_markup=btn.func_btn)


    except Exception as e:
        bot.send_message(message.chat.id, 'При выполенении запроса произошла ошибка', reply_markup=btn.func_btn)
        print(e)

if __name__ == "__main__":
    bot.polling()

    '''Exception as e:
            bot.send_message(message.chat.id, 'При выполенении запроса произошла ошибка', reply_markup=btn.func_btn)
            print(e)'''