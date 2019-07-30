class Song(object):#(object) not necessary.Used to pass arguments to self var in __init__
    def __init__(self, lyrics): #init not necessary either
        self.lyrics = lyrics #self is empty object which can have attributes

    def sing_me_a_song(self): #self.functname not posssible [syntax error]
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthfay to you", 'I dont want to get suded',
    "So i'll stop right there"])

bulls_on_parade = Song(["They rally aorunf that famuly",
"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

song = ['High up in the hills', 'In days of old', 'Jenny was dancing with her ghosts']

got_song = Song(song)
got_song.sing_me_a_song()
