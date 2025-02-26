import random

class RouteGenerator:
    def __init__(self, center_lat, center_lon, num_routes=3, waypoints_per_route=5, max_offset=0.01, altitude_variation=50):
        """
        Generate random routes around a centralized point.

        :param center_lat: Central latitude coordinate.
        :param center_lon: Central longitude coordinate.
        :param num_routes: Number of different routes to generate.
        :param waypoints_per_route: Number of waypoints per route.
        :param max_offset: Maximum latitude/longitude variation (~0.01 = ~1km).
        :param altitude_variation: Maximum altitude variation for waypoints.
        """
        self.center_lat = center_lat
        self.center_lon = center_lon
        self.num_routes = num_routes
        self.waypoints_per_route = waypoints_per_route
        self.max_offset = max_offset
        self.altitude_variation = altitude_variation

    def generate_routes(self):
        """
        Create multiple routes with randomized waypoints.
        
        :return: List of routes (each route is a list of (lat, lon, alt)).
        """
        routes = []
        for _ in range(self.num_routes):
            route = []
            base_altitude = random.randint(80, 150)  # Base altitude between 80m-150m

            for _ in range(self.waypoints_per_route):
                lat_offset = random.uniform(-self.max_offset, self.max_offset)
                lon_offset = random.uniform(-self.max_offset, self.max_offset)
                altitude = base_altitude + random.randint(0, self.altitude_variation)  # Dynamic altitude variation
                
                lat = self.center_lat + lat_offset
                lon = self.center_lon + lon_offset
                route.append((lat, lon, altitude))

            routes.append(route)

        return routes
