from classes.restaurant import RestaurantDTO
import pandas as pd


class RestaurantDTOExporter:    
    def to_excel(path: str, restaurant_list: list[RestaurantDTO]):
        df = pd.DataFrame([rest.model_dump() for rest in restaurant_list])

        df.to_excel(path)