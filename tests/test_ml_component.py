# tests/test_ml_component.py
import unittest
from dotenv import load_dotenv
from ml_component.model_builder import build_model

class MLComponentTest(unittest.TestCase):
    def test_build_model(self):
    	load_dotenv()
        # Modify below path and label when executed across platforms
    	csv_file_location = "C:\\Users\\Asus\\Desktop\\Assignment\\CSV\\data.csv"
    	target_column = "label"
    	model, score = build_model(csv_file_location, target_column)

    	self.assertIsNotNone(model)
    	self.assertIsInstance(score, float)

if __name__ == "__main__":
    unittest.main()
