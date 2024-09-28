import json

genre_list = ["이세계", "판타지", "전투", "SF"]

with open('animation.json', 'r', encoding='UTF-8') as f:
    animations = json.load(f)


new_list = []
for animation in animations:
    new_data = {"model": "articles.animation"}
    if animation["genre"]:
        genres = animation["genre"]
        genre_int_list = []
        for genre in genres:
            genre_int = genre_list.index(genre) + 1
            genre_int_list.append(genre_int)

        animation['genre'] = genre_int_list

    else:
        animation["genre"] = []
    
    new_data["fields"] = animation
    new_list.append(new_data)

with open('animations_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
