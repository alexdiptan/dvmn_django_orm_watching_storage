from datacenter.models import Passcard, Visit, is_visit_long, get_duration, format_duration
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    # Программируем здесь
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits_by_passcard = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in all_visits_by_passcard:
        if visit.leaved_at is None:
            duration = format_duration(get_duration(visit))
        else:
            duration = format_duration(visit.leaved_at - visit.entered_at)

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_visit_long(visit)
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
