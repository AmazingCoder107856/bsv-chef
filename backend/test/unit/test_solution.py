import pytest
import unittest.mock as mock
from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet

@pytest.fixture
def controller():
    return RecipeController()

def test_get_recipe_optimal_vegan(controller):
    with mock.patch.object(controller, 'get_readiness_of_recipes', return_value={'Vegan Recipe': 0.5}):
        recipe = controller.get_recipe(Diet.VEGAN, True)
        assert recipe == 'Vegan Recipe'

def test_get_recipe_random_vegan(controller):
    with mock.patch.object(controller, 'get_readiness_of_recipes', return_value={'Vegan Recipe': 0.5, 'Another Vegan Recipe': 0.3}):
        recipe = controller.get_recipe(Diet.VEGAN, False)
        assert recipe in ['Vegan Recipe', 'Another Vegan Recipe']

def test_get_recipe_optimal_none(controller):
    with mock.patch.object(controller, 'get_readiness_of_recipes', return_value={'Any Recipe': 0.5}):
        recipe = controller.get_recipe(Diet.NONE, True)
        assert recipe == 'Any Recipe'

def test_get_recipe_random_none(controller):
    with mock.patch.object(controller, 'get_readiness_of_recipes', return_value={'Any Recipe': 0.5, 'Another Recipe': 0.3}):
        recipe = controller.get_recipe(Diet.NONE, False)
        assert recipe in ['Any Recipe', 'Another Recipe']

def test_get_recipe_no_suitable_recipe(controller):
    with mock.patch.object(controller, 'get_readiness_of_recipes', return_value={}):
        recipe = controller.get_recipe(Diet.VEGAN, True)
        assert recipe is None
