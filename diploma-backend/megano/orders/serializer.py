from rest_framework import serializers

from .models import Order
from products.serializers import ImageSerializer, TagsSerializer, SpecificationsSerializer
from products.models import Product





class ProductFullSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description',
                  'freeDelivery', 'images', 'tags', 'rating', 'reviews'
                  ]

    def get_reviews(self, obj):
        return obj.reviews.count()




class OrderSerializer(serializers.ModelSerializer):
    products = ProductFullSerializer(many=True, read_only=True)

    fullName = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()


    class Meta:
        model = Order
        fields = [
            'id', 'products', 'deliveryType', 'paymentType', 'status',
             'address', 'city', 'createdAt', 'fullName', 'phone', 'email', 'totalCost',
        ]

    def get_fullName(self, obj):
        return obj.profile.fullName


    def get_phone(self, obj):
        return obj.profile.phone


    def get_email(self, obj):
        return obj.profile.email


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = (
            'id',
            'user',
            'profile',
            'products',
            'totalCost',
            'createdAt',
        )