import unittest
import pkg_resources
import pathlib

_REQUIREMENTS_PATH = pathlib.Path(__file__).parent.with_name("requirements.txt")


class TestSetup(unittest.TestCase):
    """
    Test 1: Do all required files exist?
    """

    def test_check_directory(self):
        """Test that this is running from the ACE Labs directory"""
        pwd = pathlib.Path.cwd()
        self.assertTrue(pwd.name == "ACE Labs", True)

    def test_check_labs(self):
        """Test that 'Labs' folder exists"""
        pwd = pathlib.Path.cwd()
        lab_folder = pwd / 'Labs'
        self.assertTrue(lab_folder.is_dir(), True)

    def test_check_testdir(self):
        """Test that 'Tests' folder exists"""
        pwd = pathlib.Path.cwd()
        lab_folder = pwd / 'Tests'
        self.assertTrue(lab_folder.is_dir(), True)

    def test_check_gitignore(self):
        """Test that '.gitignore' file exists"""
        pwd = pathlib.Path.cwd()
        gitignore_file = pwd / '.gitignore'
        self.assertTrue(gitignore_file.is_file(), True)

    def test_check_readme(self):
        """Test that 'README.md' file exists"""
        pwd = pathlib.Path.cwd()
        readme_file = pwd / 'README.md'
        self.assertTrue(readme_file.is_file(), True)

    def test_check_requirements(self):
        """Test that 'requirements.txt' file exists"""
        pwd = pathlib.Path.cwd()
        req_file = pwd / 'requirements.txt'
        self.assertTrue(req_file.is_file(), True)

    def test_requirements(self):
        """Test that each required package is available."""
        # Ref: https://stackoverflow.com/a/45474387/
        requirements = pkg_resources.parse_requirements(_REQUIREMENTS_PATH.open())
        for requirement in requirements:
            requirement = str(requirement)
            with self.subTest(requirement=requirement):
                pkg_resources.require(requirement)


if __name__ == '__main__':
    unittest.main()
