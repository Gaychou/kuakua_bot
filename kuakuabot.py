import requests
from wxpy import *

bot = Bot()
kuakua_url = "https://chp.shadiao.app/api.php"

# 打印所有*群聊*对象中的*文本*消息
@bot.register(Group, TEXT)
def print_group_msg(msg):
	# 如果是群聊，但没有被 @，则不回复
	if isinstance(msg.chat, Group) and not msg.is_at:
		return
	else:
		kuakua = requests.get(kuakua_url)
		print(msg.raw['ActualNickName'])
		return '@{} {}'.format(msg.raw['ActualNickName'], kuakua.text)
		
# 堵塞线程，并进入 Python 命令行
embed()