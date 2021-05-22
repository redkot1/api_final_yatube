import django_filters

from .models import Post


class PostFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='group')

    class Meta:
        model = Post
        fields = ['group', ]
