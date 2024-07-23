from courses.models import Course


def get_all_courses():
    return Course.objects.all()
