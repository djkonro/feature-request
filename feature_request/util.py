from models import Client, ProductArea, Feature


def toDict(feature):
    return {'id': feature.id,
            'title': feature.title,
            'description': feature.description,
            'client': feature.client,
            'priority': feature.priority,
            'target_date': str(feature.target_date),
            'product_area': feature.product_area}
