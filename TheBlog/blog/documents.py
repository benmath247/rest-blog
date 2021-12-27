from django_elasticsearch_dsl import Document, Text
from django_elasticsearch_dsl.registries import registry
from blog.models import Post


@registry.register_document
class PostDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = "posts"

    class Django:
        model = Post  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = ["title", "content", "id"]
