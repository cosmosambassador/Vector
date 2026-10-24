import unittest
from mc6_grimoire.bridge import load_record, lookup, prompt

class BridgeTests(unittest.TestCase):
    def test_languages(self): self.assertEqual(set(load_record()['language_tags']), {'cop','en','grc','he','la','bn'})
    def test_coptic_cube_unknown(self): self.assertIsNone(lookup('geometric_cube','cop')['text'])
    def test_oube_not_cube(self): self.assertNotEqual(lookup('coptic_oube','en')['text'],lookup('geometric_cube','en')['text'])
    def test_draft_retained(self): self.assertEqual(lookup('coptic_oube','bn')['status'],'machine_draft')
    def test_source_url(self): self.assertEqual(lookup('geometric_cube','la')['source']['url'],'https://logeion.org/cubus')
    def test_no_approval(self): self.assertEqual(lookup('geometric_cube','he')['review']['status'],'working_revision_awaiting_TJ_approval')
    def test_no_global_number(self): self.assertIsNone(load_record()['review']['registry_number'])
    def test_unknown_language(self):
        with self.assertRaises(ValueError): lookup('geometric_cube','xx')
    def test_unknown_concept(self):
        with self.assertRaises(ValueError): lookup('made_up','en')
    def test_prompt_preserves_unicode_and_status(self):
        value=prompt('coptic_oube','bn');self.assertIn('বিপরীতে',value);self.assertIn('machine_draft',value)
