import unittest
from mc6_grimoire.medical_words import load_record, lookup

class MedicalWordTests(unittest.TestCase):
    def test_bengali_unicode(self):self.assertEqual(lookup('signal','bn')['text'],'সংকেত')
    def test_punjabi_unicode(self):self.assertEqual(lookup('signal','pa-Guru')['text'],'ਸੰਕੇਤ')
    def test_draft_not_verified(self):self.assertEqual(lookup('consent','bn')['status'],'machine_draft')
    def test_missing_shahmukhi(self):self.assertIsNone(lookup('consent','pa-Arab')['text'])
    def test_script_direction(self):self.assertEqual(lookup('signal','pa-Arab')['script']['direction'],'rtl')
    def test_distinct_medicine_senses(self):self.assertNotEqual(lookup('medical_care','bn')['text'],lookup('medicine_drug','bn')['text'])
    def test_unknown_language(self):
        with self.assertRaises(ValueError):lookup('signal','pa')
    def test_foundation_separate(self):self.assertEqual(load_record()['foundation']['classification'],'spiritual_project_foundation_not_medical_guidance')
