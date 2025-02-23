
# список покупок
purchases: list[dict] = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# total_revenue(purchases): Рассчитайте и верните общую выручку (цена * количество для всех записей).
# items_by_category(purchases): Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
# expensive_purchases(purchases, min_price): Выведите все покупки, где цена товара больше или равна min_price.
# average_price_by_category(purchases): Рассчитайте среднюю цену товаров по каждой категории.
# most_frequent_category(purchases): Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).

''' Функция, формирующая необходимые структуры и показатели '''
def get_result(purchases: list[dict], min_price: float = None) -> tuple:
    # общая выручка
    total_revenue: float = sum([i['price']*i['quantity'] for i in purchases])
    # товары по категориям
    categories: list[str] = [i['category'] for i in purchases]
    items_by_categories: dict[str, list] = {c: [i['item'] for i in purchases if i['category'] == c] for c in set(categories)}
    # покупки дороже 1.0
    expensive_purchases: list[dict] = [i for i in purchases if i['price'] > min_price]
    # средние цены по категориям
    cats_count: dict[str, float] = {c: categories.count(c) for c in categories}
    average_price_by_categories: dict[str, float] = {c: sum([i['price'] for i in purchases if i['category'] == c]) / cnt for c, cnt in
                      cats_count.items()}
    # наиболее продаваемая категория
    most_common_category: dict[str, int] = {c: sum([i['quantity'] for i in purchases if i['category'] == c]) for c in set(categories)}

    return (
        total_revenue,
        items_by_categories,
        expensive_purchases,
        average_price_by_categories,
        most_common_category
    )

variables: tuple = (
    'Общая выручка',
    'Товары по категориям',
    'Покупки дороже 1.0',
    'Средняя цена по категориям',
    'Категория с наибольшим количеством проданных товаров'
)

for var, res in tuple(zip(variables, get_result(purchases, min_price=1.0))):
    print(f'{var}: {res}')