from django.urls import path
from .category_views import categoryView,categoryCreate,categoryDetail,categoryUpdate,categoryDelete
from .product_views import productView,productCreate,productDetail,productUpdate,productDelete
from .order_views import orderView,orderCreate,orderDetail,orderUpdate,orderDelete
from .invoice_views import invoiceView,invoiceCreate,invoiceDetail,invoiceUpdate,invoiceDelete

urlpatterns = [
    # category
    path('category/',categoryView),
    path('category/create/',categoryCreate),
    path('category/detail/<int:cate_id>',categoryDetail),
    path('category/update/<int:cate_id>',categoryUpdate),
    path('category/delete/<int:cate_id>',categoryDelete),

    # product
    path('product/',productView),
    path('product/create',productCreate),
    path('product/detail/<int:pro_id>',productDetail),
    path('product/update/<int:pro_id>',productUpdate),
    path('product/delete/<int:pro_id>',productDelete),

    # order
    path('order/',orderView),
    path('order/create',orderCreate),
    path('order/detail/<int:order_id>',orderDetail),
    path('order/update/<int:order_id>',orderUpdate),
    path('order/delete/<int:order_id>',orderDelete),

    # invoice
    path('invoice/',invoiceView),
    path('invoice/create',invoiceCreate),
    path('invoice/detail/<int:in_id>',invoiceDetail),
    path('invoice/update/<int:in_id>',invoiceUpdate),
    path('invoice/delete/<int:in_id>',invoiceDelete),


]