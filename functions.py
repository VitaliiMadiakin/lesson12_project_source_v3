import json
import logging

logger_error = logging.getLogger()
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("error.txt", 'w', 'utf-8')
logger_error.addHandler(console_handler)
logger_error.addHandler(file_handler)


def read_posts():
    try:
        with open("posts.json", "r", encoding="utf8") as file:
            posts = json.load(file)
            return posts
    except FileNotFoundError:
        return "Отсутствует файл posts.json"


def find_post(s):
    posts = read_posts()
    posts_found = []

    for post in posts:
        if s in post["content"].lower():
            posts_found.append(post)

    return posts_found


def post_upload(picture, content, filename):
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    extension = filename.split(".")[-1]
    if extension in allowed_extensions:
        picture.save(f"./uploads/images/{filename}")
        with open("posts.json", "r", encoding="utf8") as file:
            entry = {"pic": f"/uploads/images/{filename}", "content": content}
            data = json.load(file)
            data.append(entry)
            with open("posts.json", "w", encoding="utf8") as file:
                json.dump(data, file, ensure_ascii=False)
        return False
    elif extension not in allowed_extensions:
        result = "Загруженный файл - не картинка (расширение не jpeg и не png)"
        logger_error.warning(f"Попытка загрузки файла с расширением - {extension}")
        return result
    else:
        result = "Ошибка загрузки"
        logger_error.warning("Ошибка загрузки")
        return result
