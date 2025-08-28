from message_formatter.Msg_decorater import formatter, add_emoji


@formatter
@add_emoji

def message():
    return "Hello"
if __name__ =="__main__":
    message()