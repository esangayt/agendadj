from rest_framework import serializers, pagination

from .models import Person, Reunion


class PersonasSerializer(serializers.ModelSerializer):
    hobbies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Person
        fields = '__all__'


class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    # no es obligatorio
    # activo = serializers.BooleanField(default=False)
    activo = serializers.BooleanField(required=False)


# Model + atributos extras

class PersonasSerializer2(serializers.ModelSerializer):
    activo = serializers.BooleanField(required=False)

    class Meta:
        model = Person
        fields = '__all__'


class ReunionSerializer(serializers.ModelSerializer):
    # person_id = serializers.PrimaryKeyRelatedField(**get_person_id_field_options())
    person = PersonasSerializer(read_only=True)

    class Meta:
        model = Reunion
        fields = ['id', 'fecha', 'hora', 'asunto', 'person', 'person_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['person_id'] = serializers.PrimaryKeyRelatedField(**self.get_person_id_field_options())

    @staticmethod
    def get_person_id_field_options():
        return {
            'queryset': Person.objects.all(),
            'source': 'person',
            'write_only': True
        }


class ReunionSerializerNewAttribute(serializers.ModelSerializer):
    reunion = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = ['id', 'fecha', 'hora', 'asunto', 'person', 'reunion']

    def get_reunion(self, obj):
        return '{} - {}'.format(obj.fecha, obj.hora.strftime('%H:%M'))


class ReunionSerializerHyperLink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reunion
        fields = ['id', 'fecha', 'hora', 'asunto', 'person']
        extra_kwargs = {
            'person': {
                'view_name': 'persona_app:persona-detail',
                'lookup_field': 'pk',
                'read_only': True
            }
        }


class PersonPagination(pagination.PageNumberPagination):
    page_size = 5 #de cuantos
    max_page_size = 100 #maximo a guardar
    # page_size_query_param = 'page_size'
    # last_page_strings = ('last',
