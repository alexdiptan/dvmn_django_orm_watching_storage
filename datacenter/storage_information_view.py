from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь
    not_closed_visits = []
    not_leaved_visits = Visit.objects.filter(leaved_at__isnull=True)
    for some_visit in not_leaved_visits:
        duration = get_duration(some_visit)
        print(f'{format_duration(duration)=}')
        print(f'{some_visit.leaved_at}')
        not_closed_visits.append(
            {
                'who_entered': some_visit.passcard,
                'entered_at': some_visit.entered_at,
                'duration': format_duration(duration)
            }
        )

    context = {
        'non_closed_visits': not_closed_visits,
    }
    return render(request, 'storage_information.html', context)
