import argparse

parser = argparse.ArgumentParser(
    prog='VoiceLaTeX',
    description='An automatic, configurable translator from voice to LaTeX.',
    epilog='This project is still at an extremely early stage.'
)

parser.add_argument('-device', type='str', default='cpu', required=False)

args = parser.parse_args()
