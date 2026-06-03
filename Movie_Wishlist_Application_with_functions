name = "Movie_Wishlist: "
options = """1. Add movie 
2. List all movies 
3. display single movie 
4. Mark movie as watched 
5. Close the application"""
watches = []
mid = 1
def add_movie(mid,title,description,genere,watches):
    watch = {"id":mid,"title":title,"description":description,"genere":genere,"is_watched":False}
    watches.append(watch)
def list_movie(mid,title,watches):
    for watch in watches:
            print(f"ID: {watch["id"]}")
            print(f"Title: {watch["title"]}")
            print()
def get_movie(mid,watches):
    for watch in watches:
        if watch["id"] == mid:
           return watch
    return None
def display_movie(mid,watches):
    watch = get_movie(mid,watches) 
    if watch == None: 
        print("Movie Not found")
    else:
        print("Movie Details: ")
        print(f"ID: {watch["id"]}")
        print(f"Title: {watch["title"]}")
        print(f"Description: {watch["description"]}")
        print(f"Genere: {watch["genere"]}")
        print(f"is_watched: {watch["is_watched"]}")
def mark_movie(mid,watches):
    watch = get_movie(mid,watches)
    if watch == None: 
        print("Movie not found")
    else: 
        watch["is_watched"] = True 
while True: 
    print(name)
    print(options)
    choice = int(input("Enter your choice ( 1 - 5 ): "))
    match choice: 
        case 1: 
            print("Adding a Movie: ")
            title = input("Enter Title: ")
            description = input("Enter description: ")
            genere = input("Enter genere: ")
            add_movie(mid,title,description,genere,watches)
            mid += 1
        case 2:
            print("List all movies: ")
            list_movie(mid,title,watches)
        case 3:
            m_id = int(input("Enter the ID of Movie: "))
            display_movie(m_id,watches)
            
        case 4: 
            print("Mark movie as watched: ")
            m_id = int(input("Enter the ID of the Movie: "))
            mark_movie(m_id,watches)
        case 5:
            print("Closing the application....")
            break
        case _: 
            print("Invalid choice! Try again")
    print("-"*15)
    choice = input("Do you want to continue (y/n)?: ")
    if choice == "y":
        continue
    else:
        break 
                
