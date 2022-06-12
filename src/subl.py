import sys
import os
from workflow import Workflow
from plistlib import readPlist

info = readPlist('info.plist')

def main(wf):
	projects = info['variables']['PROJECTS_PATH']
	for dir in os.listdir(projects):
		if dir == '.DS_Store':
			continue
		if exists(projects + '/' + dir + '/' + dir + '.sublime-project'):
			wf.add_item(title=dir, arg=projects + '/' + dir + '/' + dir + '.sublime-project', valid=True, icon='icon/iu.png')
		else:
			wf.add_item(title=dir, arg=projects + '/' + dir, valid=True, icon='icon/iu.png')
	wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))