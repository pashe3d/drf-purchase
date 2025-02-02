from fancy.viewsets import FancyViewSet
from purchase.models import Product, Order, Payment, Price, Package
from purchase.serializers import (
    ProductSerializer,
    OrderSerializer,
    PaymentSerializer,
    PriceSerializer,
    PackageSerializer,
)


class ProductViewSet(FancyViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PriceViewSet(FancyViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PackageViewSet(FancyViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class OrderViewSet(FancyViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PaymentViewSet(FancyViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
