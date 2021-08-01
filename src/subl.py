import sys
import os
from workflow import Workflow
from plistlib import readPlist

info = readPlist('info.plist')

def main(wf):
	for dir in os.listdir(info['variables']['PROJECTS_PATH']):
		if dir != '.DS_Store': 
			wf.add_item(title=dir, arg=info['variables']['PROJECTS_PATH'] + '/' + dir, valid=True, icon='icon/iu.png')
	wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))