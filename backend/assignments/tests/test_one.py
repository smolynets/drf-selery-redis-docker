import pytest
from django.urls import reverse
from django.db import transaction

from assignments.models import Assignment


@pytest.mark.django_db
def test_assignments_detail(client):
    with transaction.atomic():
        assignment = Assignment.objects.create(first_term=1, second_term=2)
    url = reverse('assignments-detail', args=(assignment.id,))
    response = client.get(url)
    assert response.status_code == 200
    assert Assignment.objects.count() == 1
    assert Assignment.objects.filter(id=assignment.id).exists()
