import os


def get_upload_path(instance, filename: str) -> str:
    file_path = []
    category = instance.course.category
    category_level = category.level
    if category_level != 0:
        category = category.parent
    for _ in range(category_level + (category_level == 0)):
        file_path.append(category.name)
        category = category.parent
    file_path = [str(instance.course.id)] + file_path
    file_path = os.path.join(*reversed(file_path), filename)
    return file_path
