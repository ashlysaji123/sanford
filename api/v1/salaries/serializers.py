from rest_framework import serializers

from documents.models import ( 
    EmployeeDocuments,
    EmployeeDocumentsItems
)



class CreateEmployeeDocumentsItemsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = EmployeeDocumentsItems
        fields = ("id","title", "image",)
        read_only_fields = ("document",)



class CreateEmployeeDocumentsSerializer(serializers.ModelSerializer):
    doc_items = CreateEmployeeDocumentsItemsSerializer(many=True)

    class Meta:
        model = EmployeeDocuments
        fields = ("doc_items",)

    def create(self, validated_data):
        doc_items_data = validated_data.pop("doc_items")
        doc = EmployeeDocuments.objects.create(**validated_data)
        for item in doc_items_data:
            title = item["title"]
            # image = item["image"]
            EmployeeDocumentsItems.objects.create(
                document=doc,
                title=title,
                # image=image,
                creator=doc.user,
                **item
            )
        return doc

    def update(self, instance, validated_data):
        print("update view")
        doc_items_data = validated_data.pop("doc_items")
        doc = instance
        keep_items = []
        existing_items = EmployeeDocumentsItems.objects.filter(document=doc)
        for item in doc_items_data:
            # any Item item logic here
            title = item["title"]
            # image = item["image"]
            doc_item = EmployeeDocumentsItems.objects.create(
                document=doc,
                title=title,
                # image=image,
                creator=doc.user,
                **item
            )
            keep_items.append(item.id)
        for i in existing_items:
            if i.id not in keep_items:
                i.delete()
        return instance


class EmployeeDocumentsItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeDocumentsItems
        fields = ("title", "image")


class EmployeeDocumentsSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    doc_items = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeDocuments
        fields = (
            "user",
            "is_approved",
            "is_rejected",
            "doc_items",
            "pk",
        )

    def get_user_name(self, obj):
        if obj.user:
            return obj.user.username

    def get_doc_items(self, obj):
        doc_items = EmployeeDocumentsItems.objects.filter(sale=obj)
        return EmployeeDocumentsItemsSerializer(doc_items, many=True).data


