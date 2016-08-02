import mystuff

class MyStuff(object):
    
    def __init__(self):
        self.tangerine = "And now a thousand years between."
    
    #def apple(self):
        #print "I AM CLASSY APPLES!"


mystuff = {'apple': "I AM APPLES!"}
#print mystuff['apple']

#mystuff.apple()
#print mystuff.tangerine

thing = MyStuff()
#thing.apple()
#print thing.tangerine

######## EXERCISE #########

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.chorus = False
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    
    def chorus1(self):
        if self.chorus == True:
            for i in range(4):
                self.sing_me_a_song()

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get suid",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

battle_scars = ["These battle scars", "don't look like they\'re fading"]

b_s = Song(battle_scars)

b_s.chorus = True

b_s.chorus1()
















