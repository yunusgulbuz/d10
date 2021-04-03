from randomapp.models import DefaultDegerler


def main_processor(request):
    context = dict()
    context['default_degerler'] = DefaultDegerler.objects.last()
    return context
