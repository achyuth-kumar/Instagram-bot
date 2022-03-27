from instabot import Bot
bot=Bot()
bot.login(username="demo",password="******")
bot.upload_photo("demo.jpg",caption="Ultimate photo")   
followers=bot.get_user_followers("demo")
for follower in followers:
    print(bot.get_user_info(follower))
