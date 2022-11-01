from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render


def storage_information_view(request):
    serialized_visits = []
    not_leaved_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in not_leaved_visits:
        duration = get_duration(visit)
        serialized_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(duration)
            }
        )

    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
