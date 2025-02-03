from django.shortcuts import render
from rest_framework import generics
from .models import House, Booking, Review
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import HouseSerializer, BookingSerializer, ReviewSerializer

@permission_classes([IsAuthenticated])
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def api(request, id=None):
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'object not found'}, status=404)
            else:
                instances = model_class.objects.all()
                serializer = serializer_class(instances, many=True)
                return Response(serializer.data)
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=400)
                except model_class.DoesNotExist:
                    return JsonResponse({'message': 'object not found'}, status=404)
            return Response({'message': 'id is required for update'}, status=400)
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'}, status=204)
                except model_class.DoesNotExist:
                    return JsonResponse({'message': 'Object not found'}, status=404)
            return Response({'message': 'ID is required for deletion'}, status=400)

        return JsonResponse({'message': 'Invalid method'}, status=405)

    return api

manage_house = generic_api(House, HouseSerializer)
manage_booking = generic_api(Booking, BookingSerializer)
manage_review = generic_api(Review, ReviewSerializer)