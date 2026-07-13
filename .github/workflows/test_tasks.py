import unittest
from Projectpedro import Task

class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task("Testar")
        self.assertEqual(task.title, "Testar")
        self.assertFalse(task.completed)
    
    def test_task_priority(self):
        task = Task("Alta", priority="alta")
        self.assertEqual(task.priority, "alta")
    
    def test_task_to_dict(self):
        task = Task("Comprar", "Comprar pão", "baixa")
        dados = task.to_dict()
        self.assertEqual(dados['title'], "Comprar")
        self.assertEqual(dados['description'], "Comprar pão")
        self.assertEqual(dados['priority'], "baixa")

if __name__ == '__main__':
    unittest.main()