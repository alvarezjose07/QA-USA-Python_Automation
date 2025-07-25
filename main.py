import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # This method runs once before all tests
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print(" Server is ON. Proceeding with tests...")
        else:
            print(" Server is OFF. Please update URBAN_ROUTES_URL in data.py")

    def test_set_route(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("Function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("Function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("Function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("Function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created for ordering blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Add in S8
        for i in range(2):
            # Add in S8
            pass

        print("Function created for ordering 2 ice creams")
        pass


    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created for car search model appears")
        pass
