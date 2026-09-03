from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     author = serializers.CharField(max_length=255)
#     title = serializers.CharField(max_length=255)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "image",
            "status",
            "content",
            "category",
            "created_date",
            "published_date",
        ]
        read_only_fields = ['author']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["category"] = CategorySerializer(instance.category).data
        request = self.context.get("request")
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("created_date", None)
            rep.pop("published_date", None)
        else:
            rep.pop("content", None)
            
        return rep
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
