from models import Client, ProductArea, Feature


def toDict(feature):
    return {'id': feature.id,
            'title': feature.title,
            'description': feature.description,
            'client': feature.client,
            'priority': feature.priority,
            'target_date': str(feature.target_date),
            'product_area': feature.product_area}


def updatePriority(client, priority):
    priority = int(priority)
    feature = Feature.query.filter_by(
        client=client).filter_by(priority=priority).first()
    update_list = []
    while (feature != None):
        update_list.append(feature)
        priority = priority + 1
        feature = Feature.query.filter_by(
            client=client).filter_by(priority=priority).first()

    for i in range(len(update_list)):
        update_list[i].priority = update_list[i].priority + 1
