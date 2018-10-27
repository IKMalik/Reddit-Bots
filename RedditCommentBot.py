import praw

bot = praw.Reddit(user_agent='ASimplePlanetCommentBot',
                  client_id='AbCdEfGhI01234567',
                  client_secret='934829340231-_',
                  username='Bot_demo_usertest',
                  password='Bot_password')

subreddit = bot.subreddit('space')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Get body of text
    author = comment.author # Get comment author
    if 'mars' in text.lower():
        message = "Greetings from planet Earth, u/{0} ?".format(author) # Generate a message
 
        comment.reply(message) # Send message

