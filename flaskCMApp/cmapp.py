import click
import os
from app import create_app

app = create_app()

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    '''
    Runs the named test, or if no arguments find tests and runs them
    '''
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)