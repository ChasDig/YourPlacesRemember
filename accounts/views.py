from django.views.generic import TemplateView


# ------ User views ----- #

class UserLoginView(TemplateView):

    http_method_names = ('get', )
    template_name = 'places_memory/memory_list.html'
