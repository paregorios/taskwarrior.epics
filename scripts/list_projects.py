#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
list taskwarrior projectts with additional information
"""

import better_exceptions
from airtight.cli import configure_commandline
import logging
from taskw import TaskWarrior

logger = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = logging.WARNING
OPTIONAL_ARGUMENTS = [
    ['-l', '--loglevel', 'NOTSET',
        'desired logging level (' +
        'case-insensitive string: DEBUG, INFO, WARNING, or ERROR',
        False],
    ['-v', '--verbose', False, 'verbose output (logging level == INFO)',
        False],
    ['-w', '--veryverbose', False,
        'very verbose output (logging level == DEBUG)', False],
]
POSITIONAL_ARGUMENTS = [
    # each row is a list with 3 elements: name, type, help
]


def main(**kwargs):
    """
    main function
    """
    tw = TaskWarrior()
    tasks = tw.load_tasks()
    pending = tasks['pending']
    loose_tasks = [t for t in pending if 'project' not in t.keys()]
    assigned_tasks = [t for t in pending if t not in loose_tasks]
    projects = [t['project'] for t in pending if 'project' in t.keys()]
    projects = sorted(set(projects))
    print('Taskwarrior Project Report')
    print('==========================')
    print('active projects: {}'.format(len(projects)))
    print('tasks without projects: {}'.format(len(loose_tasks)))
    projects_epics = {}
    for p in projects:
        project_tasks = [t for t in assigned_tasks if t['project'] == p]
        epics = []
        for t in project_tasks:
            try:
                t['tags']
            except KeyError:
                continue
            else:
                if 'epic' in t['tags']:
                    epics.append(t)
        ecount = len(epics)
        projects_epics[p] = {
            'ecount': ecount,
            'tasks': project_tasks,
            'epics': epics
        }
    proper = {k: v for k, v in projects_epics.items() if v['ecount'] == 1}
    print('projects with a single epic: {}'.format(len(proper)))
    marooned = {k: v for k, v in proper.items() if len(v['tasks']) == 1}
    print('projects that have an epic, but no other tasks: '.format(len(marooned)))
    for p, d in marooned.items():
        print('    {}'.format(p))
    without = {k: v for k, v in projects_epics.items() if v['ecount'] == 0}   
    print('projects without epics: {}'.format(len(without))) 
    for p, d in without.items():
        print('    {}'.format(p))
    excess = {k: v for k, v in projects_epics.items() if v['ecount'] > 1}   
    print('projects with too many epics: {}'.format(len(excess))) 
    for p, d in excess.items():
        print('    {} ({})'.format(p, d['ecount']))


if __name__ == "__main__":
    main(**configure_commandline(
            OPTIONAL_ARGUMENTS, POSITIONAL_ARGUMENTS, DEFAULT_LOG_LEVEL))
