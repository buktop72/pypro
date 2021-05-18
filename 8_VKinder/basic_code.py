from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = '10e60d8515fb7ef82c2fa4c947b64a87c19e6c0a8d5f7e31dd16e30452841ec0640af9684d615ff16a216'

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            elif request == "q":
                exit()
            else:
                write_msg(event.user_id, "Не понял вашего ответа...")

if __name__ == '__main__':
    pass