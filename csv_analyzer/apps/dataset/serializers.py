# Rest Framework
from rest_framework import serializers

# Models
from csv_analyzer.apps.dataset.models import DataSet, DataSetFiles


class CreateDataSetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = (
            'id',
            'name',
            'is_analyzed',
            'owner',
        )
        read_only_fields = ('id',)


class FileDataSetModelSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%Y-%m-%d", required=True)

    class Meta:
        model = DataSetFiles
        fields = ('id', 'file', 'data_set', 'created', 'is_analyzed', 'start_date')
        read_only_fields = ('id',)


class DataSetModelSerializer(serializers.ModelSerializer):
    files = FileDataSetModelSerializer(many=True)

    class Meta:
        model = DataSet
        fields = (
            'id',
            'name',
            'is_analyzed',
            'owner',
            'files',
            'created',
        )
        read_only_fields = fields
