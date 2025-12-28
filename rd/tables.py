from django_tables2 import Table, Column

from rd.models import SparePart

class PartsTable(Table):
    name = Column(linkify=True)
    
    class Meta:
        model = SparePart
        # template_name = "django_tables2/bootstrap.html"
        fields = ("name", "type", "dop", "owner", "location")
        attrs = {"class": "table table-striped table-bordered"}

