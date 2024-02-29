from rest_framework import serializers

class DataStatsSerilizers(serializers.Serializer):
    dataset = serializers.CharField()

    def validate_data(self, value):
        """
        check if the provided path ends with " .csv"

        """
        if not value.endswith(".csv"):
            raise serializers.ValidationError("Invalid file format. Only CSV files are allowed.")
        return value