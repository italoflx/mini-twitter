from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'created_at', 'updated_at', 'likes']
        read_only_fields = ['likes']  

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("O conteúdo não pode estar vazio.")
        if len(value) > 500:
            raise serializers.ValidationError("O conteúdo não pode ter mais de 500 caracteres.")
        return value

    def validate_image(self, value):
        if value:
            if not value.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                raise serializers.ValidationError("O arquivo deve ser uma imagem válida (PNG, JPG, JPEG, GIF).")
        return value
