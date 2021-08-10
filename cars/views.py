from django.shortcuts import render
from rest_framework import generics
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from cars.models import Car
from cars.serializer import CarDetailSerializer ,CarsListSerializer
from rest_framework.authentication import TokenAuthentication

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser, )

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )