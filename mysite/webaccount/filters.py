from .models import Client_Personal_Info, RMReport, clientInvoice, RMInvoice, PackageModel
import django_filters

class Client_Personal_InfoFilter(django_filters.FilterSet):
    Name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Client_Personal_Info
        fields = [
            'Name',
            'status'
        ]

class RMReportFilter(django_filters.FilterSet):
    # uploadFile = django_filters.CharFilter(lookup_expr='icontains')
    # Name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = RMReport
        fields = [
            # 'client__Name',
            'id',
            'reportType',
            'dateYear',
            'month_quarterType',
            'status',
            # 'uploadFile'
        ]

class Client_Invoice_Filter(django_filters.FilterSet):
    client__Name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = clientInvoice
        fields = [
            'id',
            'client__Name',
            'client__status',
            'statusType',
            
        ]

# class RMInvoice_Filter(django_filters.FilterSet):
#     class Meta:
#         model = RMInvoice,
#         fields = [
#             'id',
#             'statusType',
#         ]

class RMInvoice_Filter(django_filters.FilterSet):
    class Meta:
        model = RMInvoice
        fields = [
            'id',
            'statusType'
        ]


class PackageModelFilter(django_filters.FilterSet):
    class Meta:
        model = PackageModel
        fields = [
            'id',
        ]