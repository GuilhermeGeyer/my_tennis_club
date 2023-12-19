from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    mymembers = Member.objects.all()  # .values()
    firstnames = Member.objects.values_list('firstname')
    emil_data = Member.objects.filter(firstname='Emil').values()
    '''data_2 = Member.objects.filter(
        id=2) | Member.objects.filter(firstname='Emil')'''
    data_2 = Member.objects.filter(Q(id=2) | Q(
        lastname__iexact='refsnes')).order_by('lastname', '-firstname')
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
        'firstname': 'Linus',
        'mymembers': mymembers,
        'firstnames': firstnames,
        'emil_data': emil_data,
        'data_2': data_2,
        'greetings': 1,
    }
    return HttpResponse(template.render(context, request))
