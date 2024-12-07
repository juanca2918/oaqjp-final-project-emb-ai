import unittest
from emotion_detection from emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['emociones_dominantes'], 'joy')

    def test_anger(self):
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['emociones_dominantes'],'anger')

    def test_disgust(self):
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['emociones_dominantes'],'disgust')

    def test_sadness(self):
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['emociones_dominantes'],'sadness')
    
    def test_fear(self):
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['emociones_dominantes'],'fear')

if __name__ == '__main__'
    unittest.main()
