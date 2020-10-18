import math as m

def get_customers_within_distance(customers: list, location: tuple, distance_limit_in_km: int) -> list:
    
    def is_within_distance(location1: tuple, location2: tuple, distance_limit_in_km: int) -> bool:
        #https://en.wikipedia.org/wiki/Great-circle_distance
        #d = earth_radius*central_angle
        #central_angle = arccos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(abs(long1-long2)))
        #radians = degrees * (pi/180)

        def to_rad(degree: float):
            return degree * (m.pi / 180)

        earth_radius_km = 6371.009

        lat1 = to_rad(location1[0])
        lon1 = to_rad(location1[1])
        lat2 = to_rad(location2[0])
        lon2 = to_rad(location2[1])

        central_angle = m.acos((m.sin(lat1)*m.sin(lat2)) + (m.cos(lat1)*m.cos(lat2)*m.cos(abs(lon1-lon2))))

        actual_distance = earth_radius_km * central_angle

        return actual_distance < distance_limit_in_km
    
    customers_within_distance = list(filter(lambda customer: is_within_distance((customer.latitude, customer.longitude), location, distance_limit_in_km), customers))
    customers_within_distance.sort(key = lambda customer: customer.user_id)

    return customers_within_distance