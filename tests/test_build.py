import unittest
from scripts.build import ROOT, build_site, parse_numbered_list


class TestProjectDataAndBuild(unittest.TestCase):

    def test_fructe_file_exists(self):
        self.assertTrue((ROOT / "fructe.txt").exists())

    def test_legume_file_exists(self):
        self.assertTrue((ROOT / "legume.txt").exists())

    def test_fructe_list_is_not_empty(self):
        fructe = parse_numbered_list(ROOT / "fructe.txt")
        self.assertGreaterEqual(len(fructe), 3)

    def test_legume_list_is_not_empty(self):
        legume = parse_numbered_list(ROOT / "legume.txt")
        self.assertGreaterEqual(len(legume), 3)

    def test_fructe_has_no_duplicates(self):
        fructe = parse_numbered_list(ROOT / "fructe.txt")
        normalized = [item.lower() for item in fructe]
        self.assertEqual(len(normalized), len(set(normalized)))

    def test_legume_has_no_duplicates(self):
        legume = parse_numbered_list(ROOT / "legume.txt")
        normalized = [item.lower() for item in legume]
        self.assertEqual(len(normalized), len(set(normalized)))

    def test_build_creates_index_html(self):
        output_file = build_site()
        self.assertTrue(output_file.exists())
        content = output_file.read_text(encoding="utf-8")
        self.assertIn("Fructe", content)
        self.assertIn("Legume", content)


if __name__ == "__main__":
    unittest.main()