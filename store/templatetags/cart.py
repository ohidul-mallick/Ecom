from django import template

register = template.Library()



@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==product.id:
            return True
    return False

@register.filter()
def equal(product,key):
    if product.id ==int(key):
        return True
    else:
        return False


@register.filter()
def cartTotal(product,cart):
    Sum=0
    for key,value in cart.items():
        Sum=Sum+(value['quantity']*float(value['price']))

    return Sum

