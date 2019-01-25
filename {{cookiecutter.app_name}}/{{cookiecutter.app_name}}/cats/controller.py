# Practically, we'd probably use sqlalchemy here. Keeping scope
# small for flexibility with other things - dynamodb e.g. *shrugs*
CATS = [{"id": "1", "name": "Furball"}]


def list_cats():
    return CATS


def get_cat(cat_id):
    for cat in CATS:
        if cat["id"] == cat_id:
            return cat
