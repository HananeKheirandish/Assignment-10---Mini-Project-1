import Media

class Film(Media.Media):
    def __init__(self, i, n, di, Is, u, du, c, ci):
        super().__init__(i, n, di, Is, u, du, c)
        self.cinema = ci
    
    def show_info(self):
        return super().show_info() , 'Cinema: %s' %self.cinema

# film = Film('asd' , 'erty' , 12 , 'http.ljkj' , 90 , 'lale' , 'afrigha')
# # print(film.show_info())
# list=[]
# print(list)
# list.append(film)
# print(list)
# for i in range(len(list)):
#     print(list[i].show_info())
#     print(list[i].name)

# ['', <Film.Film object at 0x0000014531A027B8>]