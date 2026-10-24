import unittest
from mc6_grimoire.engineer import validate, build_prompt

class EngineerTests(unittest.TestCase):
    def setUp(self):
        self.packet={"version":"0.1","language":"en","vocabulary":"BEW","platform":"unix","provider":"none","question":"Explain a node.","evidence_status":"synthetic_example","sources":[],"continuity":[True,False,True],"human_review":"pending"}
    def test_valid(self): self.assertEqual(validate(self.packet),self.packet)
    def test_gap_score(self): self.assertAlmostEqual(build_prompt(self.packet)['continuity']['Q'],2/3)
    def test_no_connection(self):
        self.packet['provider']='qwen';self.assertEqual(build_prompt(self.packet)['connection_status'],'not_connected')
    def test_empty_checklist(self):
        self.packet['continuity']=[];self.assertIsNone(build_prompt(self.packet)['continuity']['Q'])
    def test_extra_field(self):
        self.packet['command']='run'
        with self.assertRaises(ValueError):validate(self.packet)
    def test_unknown_provider(self):
        self.packet['provider']='unknown'
        with self.assertRaises(ValueError):validate(self.packet)
    def test_numeric_not_bool(self):
        self.packet['continuity']=[1]
        with self.assertRaises(ValueError):validate(self.packet)
    def test_empty_question(self):
        self.packet['question']=' '
        with self.assertRaises(ValueError):validate(self.packet)
