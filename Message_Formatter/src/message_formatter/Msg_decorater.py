def formatter(func):
    def starter():
        print("💫💫✨🌟🌟🎉🌟🎉🌟🎉🌟🌟✨💫💫")
        print(func())
        print("💫💫✨🌟🌟🎉🌟🎉🌟🎉🌟🌟✨💫💫")
    return starter

def add_emoji(func):
    def decorate():
        return "⭐>>       "+ func()+"       <<⭐"
    return decorate