__author__ = 'perecullera'

from rest_framework import serializers
from .models import Apartment, Category, Owner

class CategoryListingSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ( 'id', 'name')

class AptSerializer(serializers.HyperlinkedModelSerializer):

    cats = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ('id_2', 'neighborhood', 'name', 'district','created','cats','address','postal_code','latitude','longitude')





class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = ('name')

