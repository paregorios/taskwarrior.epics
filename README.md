# taskwarrior.epics

manage complex projects in taskwarrior using tasks tagged with epic

taskwarrior.epics is the work of Tom Elliott (tom.elliott@nyu.edu). Copyright (c) 2019 Tom Elliott. See LICENSE.txt file for complete license.

## definitions

<dl>
    <dt>programme</dt>
        <dd>an on-going, discrete domain or area or initiative of work of life, e.g., "health" or "pleiades"</dd>
    <dt>project</dt>
        <dd>a major, coherent activity within a particular programme domain that requires multiple tasks to complete</dd>
    <dt>epic</dt>
        <dd>a task/action that embodies the end/completion state of a project. One epic per project. Once the epic is done, the project is done.</dd>
    <dt>task</dt>
        <dd>a task as defined by task warrior (action in GTD): a discrete, atomic piece of work</dd>
</dl>

## dependencies

    - [Ralph Bean's Python Taskwarrior API](https://github.com/ralphbean/taskw)

## capabilities/desiderata/todo

    - get list of projects (```scripts/list_projects.py```) with:
        - [x] list of problems like no epic, too many epics, etc.
        - [ ] description (where to store this? maybe ```data/projects.txt```?)
        - [ ] epic task
        - [ ] first action for the epic
        - [ ] associated project folders, messages, online links
        - [ ] due dates

    - get taskwarrior orphans/incompletes; i.e., projects without:
        - [ ] description
        - [x] epic
        - [x] ~~tasks~~ (projects are defined by the project attribute on tasks, so they cannot exist without at least one task)
        - [ ] programme association (NB: ```data/programmes.txt```)

    - how to manage/make use of a list of active programmes a list of active projects, etc.
