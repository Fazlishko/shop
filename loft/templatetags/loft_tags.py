from django import template
from loft.models import Category, Product, FavoriteProduct

register = template.Library()


@register.simple_tag()
def get_categories():  # Функция для получения Категорий у которых нет родителей
    return Category.objects.filter(parent=None)


@register.simple_tag()
def get_normal_price(price):
    return f'{price:_}'.replace('_', ' ')


# Функция для получения цветов товара
@register.simple_tag()
def get_colors_product(model, category):
    products = Product.objects.filter(model=model, category=category)
    return products

# Функция для сбора запроса фильрации
@register.simple_tag(takes_context=True)
def query_params(context, **kwargs):
    query = context['request'].GET.copy()
    for key, value in kwargs.items():
        query[key] = value

    return query.urlencode()


@register.simple_tag()
def get_favorites(user):
    favorites = FavoriteProduct.objects.filter(user=user)
    favorites = [i.product for i in favorites]
    return favorites

@register.simple_tag()
def get_discount_price(price, discount):
    procent = (price * discount) / 100
    price = price - procent
    return f'{price:_}'.replace('_', ' ')






