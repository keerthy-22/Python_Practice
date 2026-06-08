class Movie:
    def __init__(self,mid,title,description,genere):
        self.mid=mid
        self.title=title
        self.description=description
        self.genere=genere
        self.is_watched=False
    def display(self):
        text = f"ID: {self.mid}\nTitle: {self.title}\nDecription: {self.description}\nGenere: {self.genere}\nIs Watched: {self.is_watched}"
        print(text)
    def display_partial(self):
        text = f"ID: {self.mid}\nTitle: {self.title}\nGenere: {self.genere}"
        print(text)
    def get_id(self):
        return self.mid
    def set_status(self,status):
        self.is_watched = status
mid=1
title="Darling"
description="It is my first prabhas movie that made me to become dhf of prabhas"
genere="romantic"
watch1=Movie(mid,title,description,genere)
print(watch1.get_id())
watch1.set_status(True)
watch1.display()
watch1.display_partial()
