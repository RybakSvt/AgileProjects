from rest_framework import serializers
from projects.models import Task, Project, Tag
from django.utils import timezone


class AllTasksSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    assignee = serializers.SlugRelatedField(
        slug_field='email',
        read_only=True
    )
    class Meta:
        model = Task
        fields = [
            'title',
            'status',
            'priority',
            'project',                #(название проекта)
            'assignee',               #(email сотрудника)
            'due_date',
        ]

class CreateTaskSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Project.objects.all(),
    )
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'priority',
            'project',        #(заполняется не по id, а по имени проекта)
            'tags',
            'due_date',
            ]


    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Минимальная длина задачи должна быть больше 10")
        return value


    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Минимальная длина описания должна быть больше 50")
        return value


    def validate_project_name(self, value):
        if not Project.objects.filter(name=value):
            raise serializers.ValidationError("Такого названия проекта не существует")
        return value


    def validate_tags(self, value):
        if not Tag.objects.filter(id__in=value):
            raise serializers.ValidationError("Такого названия тега не существует")
        return value

    def validate_due_date(self, value):
        time_date = timezone.make_aware(value, timezone.get_current_timezone())
        if time_date < timezone.now():
            raise serializers.ValidationError("Deadline не может существовать в прошлом")
        return time_date
