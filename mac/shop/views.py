from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
# fetch data from database in display in html templates


# Create your views here.
def index(request):
    products = Product.objects.all()
    # products_len = len(products)
    # nSlides = products_len//4 + ceil((products_len/4)-products_len//4)
    # params = {'no_of_slides':nSlides,'range': range(1,nSlides),'product': products}
    # all_products = [[products, range(1, nSlides), nSlides],
    #                 [products, range(1, nSlides), nSlides],
    # ]
    all_products = []
    # fetch all product categories in quersyset
    product_categories = Product.objects.values('category')
    # save product categories in a list using set comprihension
    categories = {item['category'] for item in product_categories}
    for category in categories:
        product = Product.objects.filter(category=category)
        product_len = len(product)
        nSlides = product_len//4 + ceil((product_len/4)-product_len//4)
        all_products.append([product, range(1, nSlides), nSlides])
    params = {'all_products': all_products}
    print(params)
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone')
        description = request.POST.get('description', '')
        user = Contact(name=name, email=email, phone=phone,
                       description=description)
        user.save()
    return render(request, 'shop/contact.html')


def search(request):
    return HttpResponse("This is the search section")


def product(request, productid):
    product_details = Product.objects.filter(id=productid)
    context = {'product': product_details[0]}
    return render(request, 'shop/productview.html', context)


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = f"{request.POST.get('address1', '')} {request.POST.get('address2', '')}"
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        zip_code = request.POST.get('zip_code', '')
        customer_order = Orders(items_json=items_json, name=name, email=email,
                                address=address, city=city, state=state, phone=phone, zip_code=zip_code)
        customer_order.save()

        update = OrderUpdate(order_id=customer_order.order_id,
                             update_desc="The order has been placed")
        update.save()
        order_id = customer_order.order_id
        thanks = True
        return render(request, 'shop/checkout.html', {'thanks': thanks, 'id': order_id})

    return render(request, 'shop/checkout.html')


def tracker(request):

    if request.method == "POST":
        order_id = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            check_order = Orders.objects.filter(order_id=order_id, email=email)
            if len(check_order) > 0:
                update = []
                order_update = OrderUpdate.objects.filter(order_id=order_id)
                for item in order_update:
                    update.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                # response store python dict to string data for sending to js
                response = json.dumps([update, check_order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')
