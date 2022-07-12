from datetime import datetime
from django.shortcuts import render
from django.views import generic

# from product.models import Variant
from ..models import Variant, Product, ProductVariant


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductsListView(generic.ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 2
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        variants = Variant.objects.all()
        context['variants'] = list(variants.all())
        # print(context['variants'])
        return context

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        drop_variant = request.POST.get('drop_variant')
        price_from = request.POST.get('price_from')
        price_to = request.POST.get('price_to')
        date = request.POST.get('date')

        products = Product.objects.filter(
            title__icontains=title,
            created_at__date=date if date else datetime.now(),
            product_variant_price__price__range=(price_from, price_to),
            product_variant__variant_title__icontains=drop_variant
        )
        context = {
            'products': products
        }
        #
        # print(f"====== {context['products']}")
        # # print(f"**********{context['product']}")

        return render(request, self.template_name, context)
