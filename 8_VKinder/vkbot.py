from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

def main() -> None:
    vk_session = VkApi(token='10e60d8515fb7ef82c2fa4c947b64a87c19e6c0a8d5f7e31dd16e30452841ec0640af9684d615ff16a216')
    long_poll = VkBotLongPoll(vk_session, '204606128')
    vk = vk_session.get_api()
    print('start bot!')

    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('event!')
            peer_id = event.obj['peer_id']
            message = event.obj['text'].lower()

            if message == 'hi':
                print('message!')
                vk.messages.send(
                    peer_id=peer_id,
                    message='Привет!',
                    random_id=get_random_id(),
                )


if __name__ == '__main__':
    main()