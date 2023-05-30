# import os
#
#
# # INFO RAM
# def get_ram_info():
#     p = os.popen("free -h")
#     i = 0
#     while 1:
#         i += 1
#         line = p.readline()
#         if i == 2:
#             return line.split()[1:4]
#
#
# def ip_route(chat_id):
#     bot.send_message(chat_id, "Result:")
#     result = os.popen("ip route").read()
#     splitted_text = util.split_string(result, 3000)
#     for text in splitted_text:
#         bot.send_message(chat_id, text)
#
#
# def inf_serv(chat_id):
#     bot.send_message(chat_id, "Information available:", reply_markup=info_menu)
#     userStep[chat_id] = 1
#
#
# def ip_public(chat_id):
#     bot.send_message(chat_id, "Your Public IP Address is:")
#     public_ip = os.popen(r"curl https://ifconfig.me").read()
#     bot.send_message(chat_id, public_ip)
#
#
# def who_is_logged(chat_id):
#     bot.send_message(chat_id, "Who are logged in:")
#     bot.send_message(chat_id, os.popen("who | grep -Eo '^[^ ]+'").read())
#
#
# def active_processes(chat_id):
#     bot.send_message(chat_id, "Active processes:")
#     active_process = os.popen("ps -e").read()
#     splitted_text = util.split_string(active_process, 3000)
#     for text in splitted_text:
#         bot.send_message(chat_id, text)
#
#
# def netstat(chat_id):
#     bot.send_message(chat_id, "Netstat by services:")
#     net = os.popen("netstat -tp").read()
#     splitted_text = util.split_string(net, 3000)
#     for text in splitted_text:
#         bot.send_message(chat_id, text)
#
#
# optionsMainMenu = {
#     "info serv": inf_serv,
#     "ip route": ip_route,
#     "public ip": ip_public,
#     "active processes": active_processes,
#     "netstat": netstat,
#     "who": who_is_logged,
# }
