from frutipedia.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


class HasProfileMixin:
    extra_context = {
        'has_profile': get_profile(),
    }


class GetProfileObjectMixin:
    def get_object(self, queryset=None):
        return get_profile()