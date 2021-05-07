from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import (
    SAFE_METHODS,
    DjangoModelPermissions,
    BasePermission,
    IsAuthenticated)

from .models import Institution

from .performance_scheduling import schedule_performances_for_each_theatre
from .serializers import InstitutionSerializer


class IsOwnerOrReadOnly(BasePermission):
    """Custom permission"""
    message = 'Updating of institution details and deregistration' \
              ' restricted to Head of Institution Only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.head_of_institution == request.user


class RegisterInstitutions(generics.RetrieveUpdateAPIView):
    """
    Update institution details once  heads of institutions are registered into the system
    """
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'id'
    lookup_url_kwarg = 'institution_pk'


def schedule_performances(request):
    return render(request, 'time_table.html', {})
