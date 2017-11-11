from elasticsearch_dsl import DocType, Object, Date, GeoPoint, Keyword, Nested


class Trip(DocType):
    departure = Object(
        properties={
            'date_time': Date(),
            'location': Object(
                properties={
                    'name': Keyword(),
                    'geo_point': GeoPoint()
                }
            )
        }
    )
    arrival = Object(
        properties={
            'date_time': Date(),
            'location': Object(
                properties={
                    'name': Keyword(),
                    'geo_point': GeoPoint()
                }
            )
        }
    )
    checkpoints = Nested(
        properties={
            'action': Keyword(), # pick up / drop off
            'location': Object(
                properties={
                    'name': Keyword(),
                    'geo_point': GeoPoint()
                }
            )
        }
    )
