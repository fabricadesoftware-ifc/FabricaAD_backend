from core.models import Function
from core.models import Avaliation
from core.serializers import (
    FunctionCreateSerializer,
    FunctionSerializer,
    AvaliationSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from filters import FunctionFilter


class FunctionViewSet(ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.action == "create":
            return FunctionCreateSerializer
        return FunctionSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticatedOrReadOnly], authentication_classes=[JWTAuthentication],)
    def subordinates(self, request):
        user = request.user
        qs = Function.objects.filter(supervisor=user)

        filterset = FunctionFilter(request.GET, queryset=qs)
        if filterset.is_valid():
            qs = filterset.qs

        avaliation_qs = Avaliation.objects.filter(evaluator=user)
        avaliation_serializer = AvaliationSerializer(avaliation_qs, many=True)
        avaliation_list = [
            item["avaliation_is_in_day"] for item in avaliation_serializer.data
        ]

        serializer = FunctionSerializer(qs, many=True)

        for idx, i in enumerate(serializer.data):
            if idx < len(avaliation_list):
                i["avaliation_is_in_day"] = avaliation_list[idx]

        page = self.paginate_queryset(serializer.data)
        data_source = page if page is not None else serializer.data

        data = [
            {
                "email": item["employer"]["email"],
                "name": f"{item['employer']['first_name']} {item['employer']['last_name']}",
                "registration": item["employer"]["registration"],
                "media": (
                    float(item["employer"]["media"])
                    if item["employer"]["media"]
                    else None
                ),
                "sector": item["sector"]["name"],
                "avaliation": item.get("avaliation_is_in_day"),
            }
            for item in data_source
        ]

        if page is not None:
            return self.get_paginated_response(data)
        return Response({"data": data}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticatedOrReadOnly], authentication_classes=[JWTAuthentication])
    def myteam(self, request):
        user = request.user
        my_function = Function.objects.filter(employer=user)
        my_team = Function.objects.filter(supervisor=my_function.supervisor)
        serializer = FunctionSerializer(my_team, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
