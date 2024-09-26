from time import sleep

class User():
    users = []

    def __init__(self,nickname,password,age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video():
    videos = []

    def __init__(self,title = str(),duration = int(),time_now = 0,adult_mode = bool(0)):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube():

    def __init__(self,current_user = None):
        self.current_user = current_user

    def register(self,*args): #new_user добавляется как User в общий список
        global current_user
        new_user = User(*args)
        a = None
        for i in User.users:
            if new_user.nickname == i.nickname:
                print('Пользователь с таким именем уже существует.')
                a = 1
        if a is None:
            User.users.append(new_user)
            ur.current_user = new_user

    def log_in(self,nickname, password):
        global current_user
        exciting_user = {nickname:hash(password)}
        for i in User.users:
            if nickname == i[0] and hash(password) == i[1]:
                current_user = exciting_user
        if current_user is None:
            print('Вход не был выполнен')

    def log_out(self):
        global current_user
        current_user = None

    def add(self, *args):#видео добавляется как dict в общий список
        a = 0
        for i in args:
            Video.videos.append(i.__dict__)
            a+=1

    def get_videos(self,search = str()):
        a = 0
        b = []
        for video in Video.videos:
            if search.lower() in Video.videos[a]['title'].lower():
                b.append(Video.videos[a]['title'])
            a +=1
        return b


    def watch_video(self,search = str()):
        global current_user
        if self.current_user is None:
            print('Не зарегистрирован в системе')
        if self.current_user in User.users: # current_user берется в виде объекта User из списка users
            for video in Video.videos: # video берется в виде dict из списка videos
                if video['title'] == search:
                    if video['adult_mode']==True and self.current_user.age >= 18:
                        for x in range(1,video['duration']):
                            sleep(1)
                            print(x)
                        print('Конец видео')
                    elif video['adult_mode']==False:
                        for x in range(1,video['duration']):
                            sleep(1)
                            print(x)
                        print('Конец видео')
                    else:
                        print('Малышка, возвращайся взрослым :)')




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Эй,красивый, улыбнись (:',3)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')