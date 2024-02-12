from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Tag, Item
from .serializers import CategorySerializer, TagSerializer, ItemSerializer, UserSerializer, ItemCreateSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class CategoryList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer
    
    def get_queryset(self):
        queryset = Item.objects.all()

        # Retrieve query parameters
        sku = self.request.query_params.get('sku', None)
        name = self.request.query_params.get('name', None)
        category = self.request.query_params.get('category', None)
        tags = self.request.query_params.getlist('tags', None)  # Get list of tags
        stock_status = self.request.query_params.get('stock_status', None)
        available_stock = self.request.query_params.get('available_stock', None)

        # Filter queryset based on provided parameters
        if sku:
            queryset = queryset.filter(sku__icontains=sku)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        if tags:
            queryset = queryset.filter(tags__name__in=tags)
        if stock_status:
            queryset = queryset.filter(stock_status__icontains=stock_status)
        if available_stock:
            queryset = queryset.filter(available_stock__exact=available_stock)

        return queryset

class ItemList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ItemCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ItemCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TagCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)